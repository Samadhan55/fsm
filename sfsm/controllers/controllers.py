# -*- coding: utf-8 -*-
# from odoo import http


# class Smarten/sfsm(http.Controller):
#     @http.route('/smarten/sfsm/smarten/sfsm', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/smarten/sfsm/smarten/sfsm/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('smarten/sfsm.listing', {
#             'root': '/smarten/sfsm/smarten/sfsm',
#             'objects': http.request.env['smarten/sfsm.smarten/sfsm'].search([]),
#         })

#     @http.route('/smarten/sfsm/smarten/sfsm/objects/<model("smarten/sfsm.smarten/sfsm"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('smarten/sfsm.object', {
#             'object': obj
#         })
