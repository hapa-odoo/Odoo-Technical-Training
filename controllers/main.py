from pickle import FALSE
from odoo import http
from odoo.http import request

class RealEstate(http.Controller):

    @http.route('/hello', auth="public")
    def hello(self, **kw):
        return "Hello World"
    

    @http.route('/hello_user', auth="user")
    def hello_user(self, **kw):
        return "Hello %s" %(request.env.user.name)

    @http.route('/hello_template_user',website=True)
    def hello_template_user(self, **kw):
        properties = request.env['estate.property'].search([('state', '=', 'new')])
        print ("Properties ::: ", properties)
        return request.render('estate.properties_list', { 'user': request.env.user, 'properties': properties })

    @http.route(['/hello_template_user/<model("estate.property"):Properties_c>'], auth="public", website=True)
    def property_details(self,Properties_c=False, **kw):
       if Properties_c:
            return request.render('estate.property_details', { 'Property': Properties_c})
