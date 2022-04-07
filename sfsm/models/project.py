from odoo import models, fields

class Project(models.Model):
    _inherit="project.project"
    is_fsm_isp = fields.Boolean(string="FSM ISP",default=False)