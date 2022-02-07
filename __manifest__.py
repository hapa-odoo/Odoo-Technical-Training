# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Real Estate',
    'version': '15.1.0',
    'category': 'Sales',
    'author': 'Harshkumar Patel',
     'depends': ['website'],
#     'summary': '',
    'description':"E-Real Estate",
#     'website': 'https://www.odoo.com/estate',
    'installable': True,
    'application': True,
    'auto_install': False,
    'data' : [
        'security/ir.model.access.csv',
        'security/estate_security.xml',
        'views/estate.menus.xml',
        'views/estate.property.views.xml',
        'wizard/estate_wizard_views.xml',
        'views/estate_templates.xml',
        'data/estate_data.xml'
    ],
}
