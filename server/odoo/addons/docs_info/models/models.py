# -*- coding: utf-8 -*-

from odoo import models, fields, api


class docs_info(models.Model):
    _name = "docs_info.docs_info"

    document_title = fields.Char(required=True, string="Document Title")
    document_description = fields.Text(string="Document Description")
    document_company = fields.Many2one("res.company", ondelete="set null", string="Company")

