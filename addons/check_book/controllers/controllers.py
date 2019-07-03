# -*- coding: utf-8 -*-
from odoo import http

# class CheckBook(http.Controller):
#     @http.route('/check_book/check_book/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/check_book/check_book/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('check_book.listing', {
#             'root': '/check_book/check_book',
#             'objects': http.request.env['check_book.check_book'].search([]),
#         })

#     @http.route('/check_book/check_book/objects/<model("check_book.check_book"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('check_book.object', {
#             'object': obj
#         })