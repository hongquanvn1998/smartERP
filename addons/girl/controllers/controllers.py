# -*- coding: utf-8 -*-
from odoo import http

# class Girl(http.Controller):
#     @http.route('/girl/girl/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/girl/girl/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('girl.listing', {
#             'root': '/girl/girl',
#             'objects': http.request.env['girl.girl'].search([]),
#         })

#     @http.route('/girl/girl/objects/<model("girl.girl"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('girl.object', {
#             'object': obj
#         })