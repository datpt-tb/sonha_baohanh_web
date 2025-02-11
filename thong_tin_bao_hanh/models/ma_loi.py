from odoo import api, fields, models


class MaLoi(models.Model):
    _name = 'ma.loi'

    ma_loi = fields.Char(string="Mã lỗi")
    ten_loi = fields.Text(string="Tên lỗi")
    nhom_loi_id = fields.Many2one("nhom.loi", string="Nhóm lỗi")
    loai_sp_id = fields.Many2one("loai.san.pham", string="Loại sản phẩm")
