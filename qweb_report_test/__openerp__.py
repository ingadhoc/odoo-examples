# -*- coding: utf-8 -*-
{
    'name': "qweb_report_test",

    'summary': """
        Simple module to test some functionalities and make some examples related to the
        QWeb reporting facilities of Odoo V8""",

    'description': """
        Simple module to test some functionalities and make some examples related to the
        QWeb reporting facilities of Odoo V8
    """,

    'author': "Ingenieria ADHOC",
    'website': "http://www.ingadhoc.com",

    # Categories can be used to filter modules in modules listing
    # Check <odoo>/addons/base/module/module_data.xml of the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website','sale'],
    'data': [
        'test_report.xml',
        'views/test_report_view.xml',
    ],

    'demo': [
    ],

    'tests': [
    ],
}
