{
    'name': 'Odoo Maintenance Mode',
    'version': '15.0.1.0.0',
    'author': 'Titus',
    'maintainer': 'Ecosoft',
    'category': 'Tools',
    'summary': 'Enable maintenance mode in Odoo and assign access rights.',
   'depends': [
    'base',
    'web',
],

  'data': [
        'security/user_maintenance_mode_security.xml',
        'views/res_users_view.xml',
        'wizards/change_maintenance_mode_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,
}
