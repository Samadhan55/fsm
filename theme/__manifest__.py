{
    'name': 'Dish Home Theme',
    'description': '1. Change odoo enterprise default colour to red',
    'version': '0.01',
    'author': 'Samadhan Sharma',
    'category': 'Theme/Creative',

    'depends': ['base'],
    'data': [
    ],
    'assets': {
        'web._assets_primary_variables': [
             'theme/static/src/scss/theme_style.scss'
        ]
    },
    'images': [
        'static/description/banner.png',
        'static/src/img/dishhome.png',
    ],
    'license': 'LGPL-3',
}