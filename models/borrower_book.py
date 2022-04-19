from odoo import models, fields, api
import random
from odoo.exceptions import UserError


class BorrowerBook(models.Model):
    _name = "library.borrower.book"
    _description = "Database Borrower Book"
    _sql_constraints = [
        ("name_unique", "unique(name)", "Code Have Problem, Please Create Again")
    ]

    name = fields.Char(string="Number Invoice", unique=True, default="LIB/" + str(fields.datetime.now().year) + "/" + str(random.randint(1, 9999999)), readonly=True, required=True)
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
        res = super(BorrowerBook, self).create(vals)
        if res.total > 0:
            res.state = "in"
        else:
            raise UserError("Borrower must have book")
        return res
