from odoo import api, fields, models


class FormExchange(models.Model):
    _name = 'form.exchange'
    _rec_name = 'form_exchange_code'

    form_exchange_code = fields.Char(string="Mã trao đổi")
    form_exchange_name = fields.Text(string="Tên trao đổi")