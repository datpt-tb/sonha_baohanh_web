from odoo import api, fields, models


class TinhThanh(models.Model):
    _name = 'tinh.thanh'
    _rec_name='ten_tinh_thanh'
    ma_tinh_thanh = fields.Char(string="Mã tỉnh thành")
    ten_tinh_thanh = fields.Text(string="Tên tỉnh thành")
    # quan_huyen_ids = fields.One2many('quan.huyen', 'tinh_thanh_id', string='Quận/huyện')