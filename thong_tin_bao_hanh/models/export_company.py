from odoo import api, fields, models

class ExportCompany(models.Model):
    _name = 'export.company'

    export_date = fields.Date(string="Ngày xuất")
    delivery_note = fields.Char(string="Phếu xuất")
    request_emp = fields.Char(string="Họ và tên")
    warranty_code = fields.Many2one('warranty.information', string="ID")
    product_code = fields.Char(string="Mã sản phẩm")
    product_name = fields.Char(string="Tên sản phẩm")
    export_warehouse = fields.Char(string="Mã kho xuất")
    unit = fields.Char(string="ĐVT")
    request_amount = fields.Integer(string="Số lượng yêu cầu")
    export_amount = fields.Integer(string="Số lượng thực xuất")
    note = fields.Text(string="Ghi chú")