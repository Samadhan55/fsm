from odoo import api, fields, models, _
from odoo.exceptions import UserError
from datetime import timedelta, datetime

class ProjectTask(models.Model):
    _inherit = "project.task"


    name = fields.Char(string="Ticket Id", required=True)
    pod = fields.Char(string='POD')#change it to many to one later.
    pon=fields.Char(string='PON')

    cancellation_note = fields.Text(string="Cancellation Note:")
    reschedule_note = fields.Text(string="Reschedule Note:")
    completion_note = fields.Text(string="Completion Note:")
    scheduled_date_start=fields.Datetime(string="Scheduled Date",default=fields.datetime.now())
    sla_time=fields.Float(string="SLA Time",default=48)
    scheduled_date_end=fields.Datetime(compute='_scheduled_end')

    images = fields.One2many('fs.isp.files', 'rel_task_id', string="Documents")
    customer_signature = fields.Binary(string="Customer's Signature")

    stage_name = fields.Char(default=lambda self: self.stage_id.name)
    #is_fsm_isp = fields.Boolean(default=lambda self: self.project_id.is_fsm_isp,readonly=True)
    is_fsm_isp = fields.Boolean(related="project_id.is_fsm_isp")


    @api.depends('sla_time','scheduled_date_start')
    def _scheduled_end(self):
        self.scheduled_date_end=self.scheduled_date_start+timedelta(hours=self.sla_time)

    @api.constrains('scheduled_date_start')
    def _change_state_to_rescheduled(self):
        if self.reschedule_note:
            self.stage_id=self.env['project.task.type'].search([('name','=','Rescheduled'), \
                                                                ('project_ids','=',self.project_id.id)])
    @api.onchange('stage_id')
    def _t(self):
        print(self.stage_id)
        print(self.env['project.task.type'].browse(self.stage_id.id+1).name)

    @api.onchange('planned_date_begin','planned_date_end')
    @api.constrains('planned_date_begin','planned_date_end')
    def _change_state_to_scheduled(self):
        if self.planned_date_begin and self.planned_date_end:

            if self.planned_date_begin<self.scheduled_date_start-timedelta(hours=24) or self.planned_date_end>self.scheduled_date_end+timedelta(hours=24):
                raise UserError(_("Planned date must be between scheduled date"))
            if self.stage_id.name=='New':
                self.stage_id = self.env['project.task.type'].browse(self.stage_id.id+1).id
        else:
            self.stage_id = self.env['project.task.type'].search([('name', '=', 'New'), \
                                                             ('project_ids', '=', self.project_id.id)])

    @api.onchange('user_ids')
    def _onchange_uid(self):
        if self.stage_id.name == "Scheduled" and self.user_ids:
            self.stage_id = self.env['project.task.type'].browse(self.stage_id.id+1).id

