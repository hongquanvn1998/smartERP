# -*- coding: utf-8 -*-
from odoo import models,fields,api

class check_store(models.Model):
    _name="managebook.checkstore"
    _description="Check số lượng sách trong kho"

    
    name_book = fields.Many2one(string=u'name_book', comodel_name='managebook.mybook')
    # status = fields.One2many(
    #     string=u'status',
    #     comodel_name='managebook.mybook',
    #     inverse_name='status',
    # )
    


    
