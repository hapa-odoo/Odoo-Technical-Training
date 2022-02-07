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

    # @http.route(['/welcome/<model("property.type"):property Type>', '/course/<string:is_static>'], auth="public", website=True)
    # def course_details(self, course=False, **kw):
    #     if course:
    #         return request.render('open_academy.course_details', {
    #             'course': course,
    #         })
