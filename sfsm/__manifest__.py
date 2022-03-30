# -*- coding: utf-8 -*-
{
    'name': "FS-ISP",

    'summary': """
        1.Create necessary projects and stages (data) for managing different type of tasks.
        3.Adding fields(in res.partner, project.task) and models()
        3.flow automation and customization for each type of project.""",

    'description': """
        Flow, automation, constraint checking is based on given 3 projects uniquely.
            """,

    'author': "Smarten Technology",
    'license': 'LGPL-3',
    'sequence':'-10',
    'website': "https://www.smarten.com.np",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','industry_fsm'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
