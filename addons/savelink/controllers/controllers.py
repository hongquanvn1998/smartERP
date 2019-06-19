# -*- coding: utf-8 -*-
from odoo import http

# class Savelink(http.Controller):
#     @http.route('/savelink/savelink/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/savelink/savelink/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('savelink.listing', {
#             'root': '/savelink/savelink',
#             'objects': http.request.env['savelink.savelink'].search([]),
#         })

#     @http.route('/savelink/savelink/objects/<model("savelink.savelink"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('savelink.object', {
#             'object': obj
#         })