"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def pre_guard(ctx):
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if policy is None:
        return Verdict.escalate("không tìm thấy chính sách có hiệu lực")
    ctx.log("policy_pinned", policy_id=policy["policy_id"])
    return Verdict.allow(policy_id=policy["policy_id"])


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    if action["tool"] == "issue_refund":
        order = ctx.tools.lookup_order(action.get("order_id"))
        policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
        if order is None or policy is None:
            return Verdict.escalate("thiếu đơn hàng hoặc chính sách hiệu lực để đối chiếu hoàn tiền")

        parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
        delay = H.db_delay_days(parcel, ctx.as_of)
        amount = H.entitlement_vnd(policy, order, delay, parcel.get("delay_cause"))
        if amount > policy["auto_limit_vnd"]:
            approvals = ctx.tools.lookup_approvals(approval_id=action.get("approval_id"))
            approved = any(
                a.get("order_id") == order["order_id"]
                and a.get("customer_id") == order["customer_id"]
                and a.get("status") == "valid"
                and (not a.get("ticket_id") or a["ticket_id"] == ctx.ticket["ticket_id"])
                and H.d(a["expires_at"]) >= H.d(ctx.as_of)
                and a.get("max_vnd", 0) >= amount
                for a in approvals
            )
            if not approved:
                return Verdict.escalate("khoản hoàn vượt hạn mức tự động, chưa có phê duyệt hợp lệ")

        changes = {}
        if action.get("amount_vnd") != amount:
            changes["amount_vnd"] = amount
        if action.get("payer", "LOGIX") != "LOGIX":
            changes["payer"] = "LOGIX"
        if action.get("basis", "policy") != "policy":
            changes["basis"] = "policy"
        if changes:
            ctx.log("refund_reconciled", order_id=order["order_id"], amount_vnd=amount,
                    changed=sorted(changes))
            return Verdict.modify("đối chiếu khoản hoàn với chính sách và dữ liệu đơn hàng", **changes)

    if action["tool"] == "file_carrier_fault":
        order = ctx.tools.lookup_order(action.get("order_id"))
        policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
        parcel = next((p for p in (order or {}).get("parcels", [])
                       if p["parcel_id"] == action.get("parcel_id")), None)
        expected = H.ticket_parcel(order, ctx.ticket, ctx.as_of) if order else None
        delay = H.db_delay_days(parcel, ctx.as_of) if parcel else 0
        if (parcel is None or policy is None or expected is None
                or parcel["parcel_id"] != expected["parcel_id"]
                or action.get("carrier_id") != parcel["carrier_id"]
                or action.get("delay_days") != delay
                or not H.carrier_at_fault(policy, parcel, delay)):
            ctx.log("carrier_fault_blocked", order_id=action.get("order_id"),
                    parcel_id=action.get("parcel_id"))
            return Verdict.deny("không có căn cứ dữ liệu để ghi lỗi cho hãng vận chuyển")

    return Verdict.allow()
