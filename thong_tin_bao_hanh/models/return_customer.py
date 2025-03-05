from odoo import api, fields, models

class ReturnCustomer(models.Model):
    _name = 'return.customer'

    number_receipts = fields.Char(string="Số phiếu nhập")
    sap_document = fields.Char(string="XNGH/CT SAP")
    customer_name = fields.Char(string="Họ và tên")
    phone_number = fields.Char(string="Điện thoại")
    address = fields.Text(string="Địa chỉ")
    product_code = fields.Char(string="Mã sản phẩm")
    product_name = fields.Char(string="Tên sản phẩm")
    unit = fields.Char(string="ĐVT")
    request_amount = fields.Integer(string="Số lượng yêu cầu")
    import_amount = fields.Integer(string="Số lượng thực nhập")
    export_warehouse = fields.Char(string="Kho xuất")
    import_warehouse = fields.Char(string="Kho nhập")
    plant = fields.Char(string="Plant")
    note = fields.Text(string="Ghi chú")
    warranty_code = fields.Many2one('warranty.information', string="ID")
    branch = fields.Many2one('bh.branch', string="Chi nhánh")
