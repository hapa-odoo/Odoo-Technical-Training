from email.policy import default
from odoo import models,fields

class test(models.Model):
    _name = 'my.test'
    _description = 'my test'
    
    name = fields.Char()
    address = fields.Char()
    pincode = fields.Integer()

class S1(models.Model):
    _inherit = 'my.test'
    _description = 's1'
    city = fields.Char()
    country = fields.Char()
    
class S2(models.Model):
    _name = 's2.test'
    _description = 's2'
    _inherit = 'my.test'
    
    pan_number = fields.Integer()
    
class bankDetails(models.Model):
    _inherit = 'estate.property'
    _description = 'Bank Details'
    bankname = fields.Char(string='Bank Name')
    bankIntrest = fields.Float(string='Bank Intrest', readonly=True)
    