# -*- coding: utf-8 -*-

from odoo import models, fields, api

class rentbook(models.Model):
    _name = 'rentbook.myrent'
    _rec_name = "id_rent"

    id_rent = fields.Integer(string="Mã phiếu mượn")
    name_book = fields.Many2one(string="Tên sách",comodel_name='managebook.mybook')
    client = fields.Many2one(
        string=u'Khách thuê',
        comodel_name='rentbook.client',
        required=True
    )
    
    

    