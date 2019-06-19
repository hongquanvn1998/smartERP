# -*- coding: utf-8 -*-

from odoo import models, fields, api

class employee_car2(models.Model):
    _name = 'db.employee_car2'
    _inherit = ['mail.thread']
    _description = "Can Request"
    
    name = fields.Char(string="Add Request",required=True,)
    date_begin = fields.Datetime(string="Starting Date",fields.Datetime().now)
    date_end = fields.Datetime(string="Date End",required=False)
    employee_id = fields.Many2one(comodel_name="hr.employee",string="Employee",required=True,)
    car_id = fields.Many2one(comodel_name="fleet.vehicle",string="Car",required=True,)
    state = fields.Selection(string="Status",selection=[('draft','Draft'),('confirm','Confirm'),
                                                        ('validate','Validate'),('refuse','Refuse'),
                                                        ('approved','Approved'),],default="draft",track_visibility='onchange')
    email = fields.Char(string="Email",required=False,)
    website = fields.Char(string="Website",required=False,)

    @api.onchange('email')
    def _onchange_email(self):
        """
        Email:YOURNAME@YOURCOMPANY.COM
        Website: https://WWW.YOURCOMPANY.COM
        :return:
        """
        result={}
        if self.email:
            result.update({
                'value':{
                    'website':'https://www.%s ' %(self.email.split('@')[1])            
                }
                'warning':{
                    'title':'Congrates!',
                    'massage':'You added your email!'
                }
                'domain':{
                    'employess_id':[('id','!=',20)]
                }
            })
        return result
    _sql_constraints=[
        ('unique_email'),('unique(email)'),('The email should be unique!'),
        ]
    @api.constrains
    def _check_email(self):
        """
        Constraints will check / triggered for the listed field only creation and updating 
        @api.constraints will work on the application level
        :return:
        """
        if self.email.endswith('gmail.com'):
            raise "It's not defined"
        if self.email.endswith('yahoo.com'):
            raise "It's not defined"