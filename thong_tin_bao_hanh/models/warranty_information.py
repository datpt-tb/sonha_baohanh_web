from odoo import api, fields, models


class WarrantyInformation(models.Model):
    _name = 'warranty.information'

    id = fields.Char(string="ID")
    reporter = fields.Char(string="Người báo")
    customer_information = fields.Text(string="Tên khách hàng")
    mobile_customer = fields.Char(string="Số điện thoại")

    province_id = fields.Many2one('province', string="Tỉnh thành")
    district_id = fields.Many2one('district', string="Quận/huyện")
    ward_commune_id = fields.Many2one('ward.commune', string="Phường/xã")
    address = fields.Text(string="Địa chỉ")
    product_type_id = fields.Many2one('product.type', string="Loại sản phẩm")
    error_information = fields.Text(string="Thông tin lỗi")
    branch_id = fields.Many2one('chi.nhanh', string="Chi nhánh")
    # staff_id = fields.Many2one('nhan.vien', string="Nhân viên")
    # bh_user_id = fields.Many2one('nguoi.dung', string="Quản lý")
    number_warranty_times = fields.Integer(string="Số lần bảo hành")
    warranty_status = fields.Selection([('open', "Mở"),
                                        ('close', "Đóng")], string="Trạng thái",
                                       default='open', compute="change_status", store=True)
    error_code = fields.Many2one('error.code', string="Mã lỗi")

    staff_number = fields.Char(string="Điện thoại nhân viên")
    call_date = fields.Datetime(string="Ngày gọi", default=fields.Datetime.now)
    appointment_date = fields.Datetime(string="Ngày hẹn", default=fields.Datetime.now)
    note = fields.Text(string="Ghi chú")
    amount = fields.Float(string="Số lượng")
    error_cause = fields.Text(string="Nguyên nhân lỗi")
    product_code = fields.Char(string="Mã sản phẩm")
    processing_content = fields.Text(string="Nội dung xử lý")
    produce_month = fields.Selection([('one', 1),
                                      ('two', 2),
                                      ('three', 3),
                                      ('four', 4),
                                      ('five', 5),
                                      ('six', 6),
                                      ('seven', 7),
                                      ('eight', 8),
                                      ('nine', 9),
                                      ('ten', 10),
                                      ('eleven', 11),
                                      ('twelve', 12),], string="Tháng sản xuất")
    distance = fields.Char(string="Cự li di chuyển(km)")
    service_fee = fields.Float(string="Phí dịch vụ")
    sent_date = fields.Datetime(string="Ngày gửi báo cáo")
    return_date = fields.Datetime(string="Ngày trả hàng")
    picture = fields.Many2many('ir.attachment', string="Ảnh hiện trường")
    exchange_form = fields.Many2one('form.exchange', string="Hình thức trao đổi")
    produce_year = fields.Many2one('produce.year', string="Năm sản xuất")


    @api.depends('exchange_form')
    def change_status(self):
        for r in self:
            if r.exchange_form:
                r.warranty_status = 'close'
            else:
                r.warranty_status = 'open'
