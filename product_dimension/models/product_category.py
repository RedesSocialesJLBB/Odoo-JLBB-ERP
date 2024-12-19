from odoo import fields, models


class ProductCategory(models.Model):
    _inherit = "product.category"

    product_measures_id = fields.One2many(
        "product.measures",
        "product_category_id",
        "ID de medidas del producto",
        readonly=False
    )
