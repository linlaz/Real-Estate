from odoo import models, fields


class PublisherBook(models.Model):
    _name = "library.publisher.book"
    _description = "Publisher Book In Library"

    name = fields.Char(string="Name Publisher Book", required=True)
    address = fields.Text(string="Address Publisher Book", required=True)
    biography = fields.Text(string="Biography Publisher Book", required=True)
    photo = fields.Image(string="Logo Publisher Book")
