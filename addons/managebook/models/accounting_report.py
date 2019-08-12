from odoo import api,fields,models
from odoo.osv import osv

class accounting_report(osv.AbcstractModel):

    _name = 'report.FullAccountingReport'
    _description = 'It is full account'

    name_report = fields.Char(string="Name Report")
    n