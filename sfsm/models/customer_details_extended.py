from odoo import models, fields

class Partner(models.Model):

    _inherit = "res.partner"

    customer_id = fields.Integer(string="DH ID",readonly=True)
    first_name = fields.Char(string="First Name")
    middle_name = fields.Char(string="Middle Name")
    last_name = fields.Char(string="Last Name")
    nearest_landmark = fields.Char(string="Nearest Landmark")

    documents = fields.One2many('fs.isp.files', 'rel_partner_id', string="Documents")
    owned_devices = fields.One2many('customer.device.data', 'rel_partner_id', string="Owned Device")
