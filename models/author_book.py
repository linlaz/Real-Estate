from odoo import models, fields


class AuthorBook(models.Model):
    _name = "library.author.book"
    _description = "author book in library"
    _order = "name desc"

    name = fields.Char(string="Name Author Book", required=True)
    address = fields.Text(string="Address Author Book")
    biography = fields.Text(string="Biography Author Book")
    photo = fields.Image(string="Photo Author Book")
