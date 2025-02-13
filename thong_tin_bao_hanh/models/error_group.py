from odoo import api, fields, models


class ErrorGroup(models.Model):
    _name = 'error.group'

    error_group_code = fields.Char(string="Mã nhóm lỗi")
    error_group_name = fields.Text(string="Tên nhóm lỗi")
