from odoo import models, fields


class CategoryBook(models.Model):
    _name = "library.category.book"
    _description = "category book in library"
    _order = "name asc"

    name = fields.Char(string="Name Category Book", required=True)
    sequence = fields.Integer(string="Sequence Category", default=1)
