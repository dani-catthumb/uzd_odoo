# -*- coding: utf-8 -*-

from odoo import models, fields, api


class docs_info(models.Model):
    _name = "docs_info.docs_info"

    document_title = fields.Char(required=True, string="Document Title")
    document_description = fields.Text(string="Document Description")
    document_company = fields.Many2one("res.company", ondelete="set null", string="Company")

class wizard(models.TransientModel):
    _name = "docs_info.wizard"

    start_date = fields.Date(string="From")
    end_date = fields.Date(string="To")


    def list_selected(self):
        # comparison with docs_info create_date field, need datetime object
        # for correct results
        date_from = fields.Datetime.to_datetime(self.read(["start_date"])[0]["start_date"])
        # end_of used because i intend date_to to be inclusive
        date_to = fields.Datetime.end_of(fields.Datetime.to_datetime(self.read(["end_date"])[0]["end_date"]), 'day')

        # form empty or inverted dates
        if (
            date_from == None or date_to == None
            or
            date_to < date_from
            ):
            return True
        

        # used in the returned action dict
        view_id = self.env["ir.model.data"].xmlid_to_object("docs_info.Books_tree_view_by_date").read(["id"])[0]["id"]
        
        return {
            "name": f"Filtered Docs/Books view",
            "type": "ir.actions.act_window",
            "res_model": "docs_info.docs_info",
            "views": [(view_id , "tree")],
            "domain": [["create_date", ">=", date_from], ["create_date", "<=", date_to]],
            "target": "main",
        }