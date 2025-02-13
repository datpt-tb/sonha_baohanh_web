from odoo import api, fields, models

class Nam(models.Model):
    _name = 'nam'

    nam = fields.Char(string="Năm")