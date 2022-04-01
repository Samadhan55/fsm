from odoo import models, fields, _

class CustomerDevice(models.Model):
    _name='customer.device.data'
    _description='Device details and status information'

    name=fields.Char(string='ONT Serial No',required=True)
    db_port=fields.Integer(string='DB Port Number', required=True)
    power_level=fields.Char(string='Power Level')
    dropwire_length=fields.Float(string='Dropwire Length',required=True)
    olt_name=fields.Char(string='OLT Name')
    db_number=fields.Char(string='DB Box Number')
    rel_partner_id = fields.Many2one('res.partner',string='Owner')
