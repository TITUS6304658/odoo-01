from odoo import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    maintenance_mode = fields.Boolean(string='Maintenance Mode')
