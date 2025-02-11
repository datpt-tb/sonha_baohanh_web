from odoo import api, fields, models

class PhuongXa(models.Model):
    _name = 'phuong.xa'

    _rec_name = 'ten_phuong_xa'
    ma_phuong_xa = fields.Char(string="Mã phường xã")
    ten_phuong_xa = fields.Text(string="Tên phường xã")
    quan_huyen_id = fields.Many2one("quan.huyen", string="Quận/huyện")