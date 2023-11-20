# -*- coding: utf-8 -*-
# from odoo import http


# class DocsInfo(http.Controller):
#     @http.route('/docs_info/docs_info/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/docs_info/docs_info/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('docs_info.listing', {
#             'root': '/docs_info/docs_info',
#             'objects': http.request.env['docs_info.docs_info'].search([]),
#         })

#     @http.route('/docs_info/docs_info/objects/<model("docs_info.docs_info"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('docs_info.object', {
#             'object': obj
#         })
