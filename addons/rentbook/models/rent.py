# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date,time,datetime,timedelta
from dateutil.relativedelta import relativedelta


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
    begin_rent = fields.Date(string="Ngày mượn")
    end_rent = fields.Date(string="Ngày trả",
    compute='_compute_end'
    )
    expired = fields.Boolean(string="Hết hạn",default=False)
    
    @api.multi
    @api.depends('begin_rent')
    def _compute_end(self):
        for record in self:
            record.begin_rent = date.today()
            record.end_rent = record.begin_rent + relativedelta(days=1)

    @api.onchange('end_rent')
    def _check_expired(self):
        self.date_now = date.today()
        if self.end_rent < self.date_now:
            self.expired = True
        else:
            self.expired = False
    

    