# -*- coding: utf-8 -*-

from odoo import models,fields,api

class client(models.Model):
    _name = "rentbook.client"
    _rec_name = "name_client"
    
    id_client = fields.Char(string="ID người thuê",
    required=True
    )
    name_client = fields.Char(
    string='Tên khách hàng',
    required=True
    )
    num_phone = fields.Integer(
        string=u'Số điện thoại',
        required=True
    )
    email_client = fields.Char(
        string=u'Email'
    )
    id_rent = fields.One2many(
        string=u'Mã mượn',
        comodel_name='rentbook.myrent',
        inverse_name='id_rent'
    )
    

    