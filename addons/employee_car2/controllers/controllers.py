# -*- coding: utf-8 -*-
from odoo import http

# class EmployeeCar2(http.Controller):
#     @http.route('/employee_car2/employee_car2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/employee_car2/employee_car2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('employee_car2.listing', {
#             'root': '/employee_car2/employee_car2',
#             'objects': http.request.env['employee_car2.employee_car2'].search([]),
#         })

#     @http.route('/employee_car2/employee_car2/objects/<model("employee_car2.employee_car2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('employee_car2.object', {
#             'object': obj
#         })