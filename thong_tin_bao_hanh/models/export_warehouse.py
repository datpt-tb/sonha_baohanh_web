from odoo import api, fields, models

class ExportWarehouse(models.Model):
    _name = 'export.warehouse'

    delivery_note = fields.Char(string="Phếu xuất")
    number_receipts = fields.Char(string="Số phiếu nhập chờ trả khách")
    return_customer_id = fields.Many2one('return.customer', string="Key nhập chờ trả khách")
    phone_number = fields.Char(string="Điện thoại")
    address = fields.Text(string="Địa chỉ")
    product_code = fields.Char(string="Mã sản phẩm")
    product_name = fields.Char(string="Tên sản phẩm")
    unit = fields.Char(string="ĐVT")
    export_warehouse = fields.Char(string="Kho xuất")
    plant = fields.Char(string="Plant")
    request_amount = fields.Integer(string="Số lượng yêu cầu")
    export_amount = fields.Integer(string="Số lượng thực xuất")
    note = fields.Text(string="Ghi chú")
    delivery_confirmation = fields.Char(string="Phiếu XNGH")
    export_date = fields.Date(string="Ngày xuất kho")
    driver = fields.Char(string="Người lái xe")
    warranty_code = fields.Many2one('warranty.information', string="ID bảo hành")