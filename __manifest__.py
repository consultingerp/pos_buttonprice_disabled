# -*- coding: utf-8 -*-
{
    'name': "POS deshabilitar boton Precio",

    'summary': "",

    'description': "",

    'author': "Javier Hilario",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale'],

    # always loaded
    'data': [
    ],
    'installable': True,
    'application': True,
    'qweb': [
        'static/src/xml/pos.xml'
    ],
}
