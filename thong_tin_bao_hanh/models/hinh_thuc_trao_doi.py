from odoo import api, fields, models


class HinhThucTraoDoi(models.Model):
    _name = 'hinh.thuc.trao.doi'

    ma_trao_doi = fields.Char(string="Mã trao đổi")
    ten_trao_doi = fields.Text(string="Tên trao đổi")