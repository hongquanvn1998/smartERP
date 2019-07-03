# -*- coding: utf-8 -*-
from odoo import http

class Managebook(http.Controller):
    @http.route('/managebook/sale/', auth='public')
    def index(self, **kw):
        books = http.request.env['managebook.mybook'].search([])

        return http.request.render('managebook.mainpage',{'books':books})

#     @http.route('/managebook/managebook/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('managebook.listing', {
#             'root': '/managebook/managebook',
#             'objects': http.request.env['managebook.managebook'].search([]),
#         })

#     @http.route('/managebook/managebook/objects/<model("managebook.managebook"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('managebook.object', {
#             'object': obj
#         })