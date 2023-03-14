from django.shortcuts import get_object_or_404

from webapp.models import Product, Cart


def add_basket_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket_product = Cart.objects.filter(product=product.pk)
    if len(basket_product) == 0 and product.leftover != 0:
        data = {
            'product': product,
            'count': 1
        }
        Cart.objects.create(**data)
    elif len(basket_product) != 0:
          if basket_product[0].count < product.balance:
            basket_product = get_object_or_404(Basket, pk=basket_product[0].pk)
            basket_product.count += 1
            basket_product.save()
    return redirect('index')
