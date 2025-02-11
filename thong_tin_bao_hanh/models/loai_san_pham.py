from odoo import api, fields, models

class LoaiSanPham(models.Model):
    _name = 'loai.san.pham'

    _rec_name = 'ten_loai_san_pham'
    ma_loai_san_pham = fields.Char(string="Mã loại sản phẩm")
    ten_loai_san_pham = fields.Text(string="Tên loại sản phẩm")