from odoo import models, fields


class LibraryBook(models.Model):
    _name = "library.book"
    _description = "database book in library"
    _order = "name desc"

    name = fields.Char(string="Name Book", required=True)
    author_id = fields.Many2one("library.author.book", string="Author Book", ondelete="cascade")
    category_id = fields.Many2one("library.category.book", string="Category Book", ondelete="cascade")
    publisher_id = fields.Many2one("library.publisher.book", string="Publisher Book", ondelete="cascade")
    release = fields.Date(string="Release book")
    summary = fields.Text(string="Summary Book")
    status = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('publish', 'Publish'),
        ],
        string='Status Book',
        default='draft'
    )
    thumbnail = fields.Image(string="Thumbnail Book", width=100, height=100)
    total = fields.Integer(string="Total Book", default=5)
