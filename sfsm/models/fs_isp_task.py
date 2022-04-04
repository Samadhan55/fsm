from odoo import api, fields, models, _
from odoo.exceptions import UserError
from datetime import timedelta, datetime

class ProjectTask(models.Model):
    _inherit = "project.task"


    name = fields.Char(string="Ticket Id", required=True)
    pod = fields.Char(string='POD')#change it to many to one later.
    pon=fields.Char(string='PON')

    cancel_note = fields.Text(string="Cancellation Note:")
    reschedule_note = fields.Text(string="Reschedule Note:")
    completion_note = fields.Text(string="Completion Note:")
    scheduled_date_start=fields.Datetime(string="Scheduled Date",default=fields.datetime.now())
    sla_time=fields.Float(string="SLA Time",default=48)
    scheduled_date_end=fields.Datetime(compute='_scheduled_end')


    @api.depends('sla_time','scheduled_date_start')
    def _scheduled_end(self):
        self.scheduled_date_end=self.scheduled_date_start+timedelta(hours=self.sla_time)
