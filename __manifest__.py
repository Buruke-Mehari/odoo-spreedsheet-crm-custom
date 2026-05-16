# -*- coding: utf-8 -*-
{
    'name': 'Spreadsheet CRM Custom',
    'version': '1.0',
    'category': 'Productivity/Dashboard',
    'summary': 'Integrate a functional CRM Pipeline view into the Dashboards sidebar panel.',
    'depends': ['base', 'web', 'crm','spreadsheet_dashboard'],
    'data': [
        'data/dashboard_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}