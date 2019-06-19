# -*- coding: utf-8 -*-

from odoo import models, fields, api

class savelink(models.Model):
    _name = 'savelink.savelink'
    name = fields.Char()
    images = fields.Binary("Hình ảnh")
    id = fields.Char(
        string='id',
    )
    link = fields.Text(
        string='Link',
    )
    description = fields.Text(
        string='Description',
    )
    types = fields.Selection(
        string='Format',
        selection=[('0','Mặn'),('1','Nhạt')]
    )
    status = fields.Selection(
        string= 'Status',
        selection=[('0','Live'),('1','Die')]
    )
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
