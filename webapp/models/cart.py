from django.db import models


class Cart(models.Model):
    product = models.ForeignKey(verbose_name="Product", to="webapp.Product", related_name="cart", on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name="Quantity", null=False, blank=False)

    def __str__(self):
        return f'{self.product.name}, {self.quantity}, {self.product.price}'