from odoo import api, fields, models

class ChiNhanh(models.Model):
    _name = 'chi.nhanh'
    _rec_name ='ten_chi_nhanh'

    ma_chi_nhanh= fields.Char(string="Mã chi nhánh")
    ten_chi_nhanh = fields.Text(string="Tên chi nhánh")
    # thong_tin_bao_hanh_ids = fields.One2many('thong.tin.bao.hanh', 'chi_nhanh_id', string="Thông tin bảo hành")