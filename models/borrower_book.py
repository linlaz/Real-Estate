from odoo import models, fields, api
import random
from odoo.exceptions import UserError


class BorrowerBook(models.Model):
    _name = "library.borrower.book"
    _description = "Database Borrower Book"

    name = fields.Char(string="Number Invoice", unique=True, default="Lib/" + str(fields.datetime.now().year) + "/" + str(random.randint(1, 9999999)), readonly=True, required=True)
    user_id = fields.Many2one("res.users", string="Borrower", default=lambda self: self.env.user)
    state = fields.Selection(
        string="Status Loan",
        selection=[
            ("draft", "Draft"),
            ("in", "In Progress"),
            ("due", "Due Date"),
            ("block", "Block User"),
        ],
        default="draft"
    )
    detail_borrower_ids = fields.One2many("library.detail.borrower.book", "borrower_id", string="detail Borrower Pick Up")
    total = fields.Integer(string="total book", compute="_compute_total_borrower")

    @api.depends("detail_borrower_ids")
    def _compute_total_borrower(self):
        for rec in self:
            rec.total = len(rec.detail_borrower_ids)

    @api.model
    def create(self, vals):
        self.state = "In Progress"
        # if self.total < 1:
        #     raise UserError("Invoice can't create because is null borrower book")
        return super(BorrowerBook, self).create(vals)
