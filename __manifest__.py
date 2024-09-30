# -*- coding: utf-8 -*-
{
    'name': "Urgent Receipts",

    'summary': "Mark the receipts to be urgent",

    'description': """
In this module i have inherit the 3 modeule name as purchase.order.line and stock.move nad stock.move.line 
All the fields maded in this model is of type boolean . If i marked an field in any product in the purchase.order.line 
than automatically in stock.move and stock.move.line that product field is marked .

The cron will be call at every 1 minute .If any field is marked in the stock.move than the the cron will be called and the 
the priority of that product will be done. 
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'account', 'sale', 'purchase', 'stock', 'product','mrp_workorder'],

    # always loaded
    'data': [

        'Data/ir_cron.xml',
        'views/purchase_order_views.xml',
        'views/stock_move_views.xml',
        'views/stock_move_line_views.xml',
        'views/purchase_res_config_setting.xml',
        'views/stock_routes.xml',
        'report/sale_order_report_template_inherit.xml',

    ],

    'assets': {
        'web.assets_backend': [
            'urgent_receipts/static/src/**/*.xml',

        ],
    },
    'installable': True,
    'application': True,
}
