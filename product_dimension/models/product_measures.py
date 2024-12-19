from odoo import api, fields, models


class ProductMeasures(models.Model):
    _name = "product.measures"
    _description = "Medidas del producto"

    product_measures_length = fields.Many2one(
        "product.measures",
        "Largo",
        readonly=False,
        store=True
    )
    product_measures_width = fields.Many2one(
        "product.measures",
        "Ancho",
        readonly=False,
        store=True
    )
    product_measures_thickness = fields.Many2one(
        "product.measures",
        "Grueso",
        readonly=False,
        store=True
    )
    product_template_id = fields.One2many(
        "product.template",
        "product_measures_id",
        "ID de Producto",
        readonly=False
    )
    product_category_id = fields.Many2one(
        "product.category",
        "ID de categoría del producto",
        readonly=False
    )
