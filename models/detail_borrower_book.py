from dateutil.relativedelta import relativedelta
from odoo import models, fields, api


class DetailBorrowerBook(models.Model):
    _name = "library.detail.borrower.book"
    _description = "Database detail Borrower Book"

    borrower_id = fields.Many2one("library.borrower.book", string="unique code invoice")
    validity = fields.Integer(string="Validity (days)", default=7, required=True)
    start_borrow = fields.Date(string="Start Borrow Book", default=lambda self: fields.datetime.now())
    finish_borrow = fields.Date(string="Finish Borrow Book", compute="_compute_date_finish_borrow", inverse="_inverse_date_finish_borrow")
    book_id = fields.Many2one("library.book", string="Name Book", required=True)
    state = fields.Selection(
        string="Status Loan",
        selection=[
            ("in", "Book In User"),
            ("due", "Due Date"),
            ("back", "Book Back"),
        ],
        default="in"
    )

    @api.depends('validity', 'start_borrow')
    def _compute_date_finish_borrow(self):
        for rec in self:
            rec.finish_borrow = rec.start_borrow + relativedelta(days=+rec.validity)

    def _inverse_date_finish_borrow(self):
        for rec in self:
            different = rec.finish_borrow - rec.start_borrow
            rec.validity = different.days
