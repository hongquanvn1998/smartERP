# -*- coding: utf-8 -*-
from odoo import http

# class Save(http.Controller):
#     @http.route('/save/save/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/save/save/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('save.listing', {
#             'root': '/save/save',
#             'objects': http.request.env['save.save'].search([]),
#         })

#     @http.route('/save/save/objects/<model("save.save"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('save.object', {
#             'object': obj
#         })