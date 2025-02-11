from odoo import api, fields, models


class TrangThaiBaoHanh(models.Model):
    _name = 'trang.thai.bao.hanh'

    ma_trang_thai = fields.Char(string="Mã trạng thái")
    ten_trang_thai = fields.Text(string="Tên trạng thái")
    # thong_tin_bao_hanh_ids = fields.One2many('thong.tin.bao.hanh', 'trang_thai_id', string="Thông tin bảo hành")