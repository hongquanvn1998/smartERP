# -*- coding: utf-8 -*-
{
    'name': "Quản lý sách",

    'summary': """
        Ứng dụng quản lý sách.
        Một addon nhỏ trên odoo""",

    'description': """
        Quản lý toàn bộ sách của bạn trên odoo
    """,

    'author': "Hoàng Hồng Quân",
    'website': "http://www.fb.com/hh.quan98",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Manage',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
    ],

    # always loaded
    'data': [
        'security/group.xml',
        'security/ir.model.access.csv',
        'views/book.xml',
        'security/rule_group.xml',
        'views/mainpage.xml',
        # 'views/check.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable':True,
    'application':True,
    'auto_install':False,
    'qweb':[],
}