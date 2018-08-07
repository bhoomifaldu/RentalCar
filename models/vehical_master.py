# -*- encoding: utf-8 -*-
from odoo import api, fields, models, _

class Vehical(models.Model):
    _name = 'vehical.master'

    name = fields.Char('Model No')
    registration_no = fields.Char(string='Registration No')
    color = fields.Char(string='Color')
    value = fields.Float(string='Value',help='Vehical Price')
    purchase_date = fields.Date(string='Purchase Date')
    mileage = fields.Float(string='Mileage', help='Vehical Mileage')
    meter_reading = fields.Float(string='Meter Reading', help='Last Meter Reading')
    capacity = fields.Float(string='Passenger Capacity')
    type = fields.Selection([('ac','AC'),('non_ac','NON AC')],'Type',default='ac')
    fuel = fields.Float(string='Fuel Reading', help='Current Fuel Reading')
    rate = fields.Float(string='Rate Per KM.')
    state = fields.Selection([
        ('maintenance', 'Maintenance'),
        ('active', 'Active'),
		('inactive', 'Inactive')
        ], string='Status', readonly=True, default='inactive')

    @api.multi
    def action_active(self):
        return self.write({'state': 'active'})

    @api.multi
    def action_inactive(self):
        return self.write({'state': 'inactive'})

    @api.multi
    def action_maintenance(self):
        return self.write({'state': 'maintenance'})