# -*- coding: utf-8 -*-
from odoo import models,fields

class Tacgia(models.Model):
    _name = "managebook.author"
    _rec_name = "name"

    name = fields.Char("Tên tác giả")
    date_birth = fields.Date(string="Ngày sinh")
    mybook = fields.One2many(comodel_name="managebook.mybook",inverse_name="author_main",readonly= True, string="Sách")
    image =  fields.Binary("Hình ảnh")