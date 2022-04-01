from odoo import api, fields, models

class FsFiles(models.Model):
    _name='fs.isp.files'
    _description="To store Binary files uploaded by field service worker"

    description=fields.Char(string='Description')
    file_img=fields.Binary(string='Image')
    rel_task_id=fields.Many2one('project.task')
    rel_partner_id=fields.Many2one('res.partner')

    @api.model
    def create(self,values):
        values['rel_partner_id']=self.env['project.task'].browse(values['rel_task_id']).partner_id.id
        return super(FsFiles, self).create(values)

