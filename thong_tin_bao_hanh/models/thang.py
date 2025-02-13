from odoo import api, fields, models

class Thang(models.Model):
    _name = 'thang'

    thang = fields.Char(string="Tháng")