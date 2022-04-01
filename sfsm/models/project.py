from odoo import models, fields

class Project(models.Model):
    _inherit="project.project"
    is_fsm_isp = fields.Boolean(default=False)