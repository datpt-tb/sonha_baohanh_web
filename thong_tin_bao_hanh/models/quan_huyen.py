from odoo import api, fields, models


class QuanHuyen(models.Model):
    _name = 'quan.huyen'
    _rec_name = 'ten_quan_huyen'
    ma_quan_huyen = fields.Char(string="Mã quận huyện")
    ten_quan_huyen = fields.Text(string="Tên quận huyện")
    tinh_thanh_id = fields.Many2one("tinh.thanh", string="Tỉnh thành")
