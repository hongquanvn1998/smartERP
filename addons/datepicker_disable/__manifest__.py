# -*- coding: utf-8 -*-
{
    'name': "Datepicker Disable AutoComplete",
    'description': """
        It's addons for everyone
    """,
	'price': 0,    
    'author': "Hoang Hong Quan",
    'website': "http://www.fb.com/hh.quan98",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra tool',
    'version': '0.1',
    'images':['views/description/logo_banner.png'],
    # any module necessary for this one to work correctly
    'depends': [
        'web'
    ],
    # always loaded
    'init_xml': [
    ],
    'data': [
    ],
    'test': [
    ],
    # only loaded in demonstration mode
    'demo_xml': [
    ],
    'qweb': ['views/src/xml/templates.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}