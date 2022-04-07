from odoo import models, fields, _


class RescheduleData(models.TransientModel):
    _name = "reschedule.data"
    _description = 'Need to fill this wizard to reschedule the task'

    r_desc = fields.Char(string="Description", required=True)
    start_time = fields.Datetime(string="New Start Time", required=True)
    SLA_time = fields.Float(string="SLA Time (Hours)", required=True)

    def action_reschedule(self):
        """Update from wizard button"""
        self.ensure_one()
        values_dict = {'sla_time': self.SLA_time, 'scheduled_date_start': self.start_time,
                       'reschedule_note': self.r_desc}
        self.env['project.task'].browse(self.env.context.get('active_ids')).write(values_dict)


class CancelData(models.TransientModel):
    _name = "cancel.data"
    _description = 'Need to fill this wizard to cancel the task'

    c_desc = fields.Char(string="Description", required=True)
    partner_id = fields.Many2one('res.partner', default=lambda self: self.env['project.task'].browse(
        self.env.context.get('active_ids')).partner_id)

    def action_cancel(self):
        """Update from wizard button"""
        self.ensure_one()
        current_task_obj = self.env['project.task'].browse(self.env.context.get('active_ids'))

        # find id of canceled stage
        canceled_stage_id = self.env['project.task.type'].search([('project_ids', '=', current_task_obj.project_id.id), \
                                                                  ('name', '=', 'Cancelled')]).id
        values_dict = {'cancellation_note': self.c_desc, 'stage_id': canceled_stage_id}
        # change update task (to cancelled)
        current_task_obj.write(values_dict)

class CompleteData(models.TransientModel):
    _name = "complete.data"
    _description = 'Need to fill this wizard to before the task'

    c_desc = fields.Char(string="Description", required=True)
    task_id = fields.Many2one('project.task',
                              default=lambda self: self.env['project.task'].browse(self.env.context.get('active_ids')))
    # task_id = fields.Many2one('res.partner', default=lambda self:self.env['project.task'].browse(self.env.context.get('active_ids')))
    r_docs = fields.One2many(related='task_id.images', string="Documents", readonly=False)
    ont_sn = fields.Char(string='ONT Serial No')
    db_port = fields.Integer(string='DB Port')
    power_level = fields.Char(string='Power Level')
    dropwire_length = fields.Float(string='Dropwire Length')
    olt_name = fields.Char(string='OLT Name')
    db_number = fields.Char(string='DB Number')
    customer_signature=fields.Binary(string="Customer's Signature")

    def action_complete(self):
        """Update from wizard button"""
        self.ensure_one()
        current_task_obj = self.env['project.task'].browse(self.env.context.get('active_ids'))
        print(current_task_obj)
        print(self.task_id)
        if self.ont_sn:
            device_dict = {'name': self.ont_sn,
                           'db_port': self.db_port,
                           'power_level': self.power_level,
                           'dropwire_length': self.dropwire_length,
                           'olt_name': self.olt_name,
                           'db_number': self.db_number,
                           'rel_partner_id': current_task_obj.partner_id.id}
            # create a new device and relate to the customer of current task
            self.env['customer.device.data'].create(device_dict)

        # find id of canceled stage
        completed_stage_id = self.env['project.task.type'].search([('project_ids', '=', current_task_obj.project_id.id), \
                                                                  ('name', '=', 'Completed')]).id
        #prepare changes for current task(ticket)
        values_dict = {'completion_note': self.c_desc, 'stage_id': completed_stage_id,
                       "customer_signature":self.customer_signature}
        current_task_obj.write(values_dict)
