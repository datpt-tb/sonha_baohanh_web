from odoo import api, fields, models

class NhomLoi(models.Model):
    _name = 'nhom.loi'

    ma_nhom_loi = fields.Char(string="Mã nhóm lỗi")
    ten_nhom_loi = fields.Text(string="Tên nhóm lỗi")