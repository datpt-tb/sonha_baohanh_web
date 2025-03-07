from odoo import api, fields, models

class FormExportCompany(models.Model):
    _name = 'form.export.company'

    delivery_note_number = fields.Char(string="Số phiếu xuất")
    warranty_code = fields.Many2one('warranty.information', string="ID bảo hành", domain="[('transfer_warehouse', '!=', True)]")
    import_before_repair_id = fields.One2many('import.before.repair', 'warranty_code', compute="_onchange_warranty_code", inverse="_inverse_data")
    export_date = fields.Datetime(string="Ngày xuất", default=fields.Datetime.now)

    @api.depends('warranty_code')
    def _onchange_warranty_code(self):
        for record in self:
            if record.warranty_code:
                record.import_before_repair_id = self.env['import.before.repair'].search([('warranty_code', '=', record.warranty_code.id)])
            else:
                record.import_before_repair_id = False

    def _inverse_data(self):
        for r in self:
            if r.import_before_repair_id:
                for record in r.import_before_repair_id:
                    record.write({'product_code': record.product_code})
