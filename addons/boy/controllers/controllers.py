# -*- coding: utf-8 -*-
from odoo import http

# class Boy(http.Controller):
#     @http.route('/boy/boy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/boy/boy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('boy.listing', {
#             'root': '/boy/boy',
#             'objects': http.request.env['boy.boy'].search([]),
#         })

#     @http.route('/boy/boy/objects/<model("boy.boy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('boy.object', {
#             'object': obj
#         })