# -*- coding: utf-8 -*-

from odoo import models, fields, api

class save(models.Model):
    _name = 'save.save'

    name = fields.Char(string="Nhập tên", required=True)
    value = fields.Integer(string="Số thứ tự", required=True)
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100