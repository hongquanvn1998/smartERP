# -*- coding: utf-8 -*-

from odoo import models, fields, api

class boy(models.Model):
    _name = 'boy.boy'


    name = fields.Char()

    id = fields.Char(
        string='id',
    )
  
    description = fields.Text(
        string='Mô tả',
    )
    
    old = fields.Integer(
        string='Tuổi',
    )
    
    adress = fields.Char(
        string='Địa chỉ',
    )
    
    types = fields.Selection(
        string='Loại hàng',
        selection=[('0', 'Máy bay'), ('1', 'Teen')]
    )
    size = fields.Char(
        string='Kích thước',
    )
    status = fields.Selection(
        string='Trạng thái',
        selection=[('0', 'Còn hàng'), ('1', 'Hết hàng')]
    )
    image = fields.Binary("Hình ảnh")

    tall = fields.Integer(
        string='Chiều cao',
    )
    phone = fields.Char(
        string='Điện thoại',
    )