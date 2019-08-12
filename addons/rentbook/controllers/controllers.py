# -*- coding: utf-8 -*-
from odoo import http

# class Rentbook(http.Controller):
#     @http.route('/rentbook/rentbook/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rentbook/rentbook/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rentbook.listing', {
#             'root': '/rentbook/rentbook',
#             'objects': http.request.env['rentbook.rentbook'].search([]),
#         })

#     @http.route('/rentbook/rentbook/objects/<model("rentbook.rentbook"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rentbook.object', {
#             'object': obj
#         })