# -*- coding: utf-8 -*-
{
    'name': "Thuê sách",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Hoàng Quân",
    'website': "http://www.fb.com/hh.quan98",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Rent',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'managebook'
    ],

    # always loaded
    'data': [
        'security/group.xml',
        'security/ir.model.access.csv',
        'security/record_rule.xml',
        'views/rent.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable':True,
    'application':True,
}