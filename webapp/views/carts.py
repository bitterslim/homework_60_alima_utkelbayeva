from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DeleteView, CreateView

from webapp.models import Product, Cart


class CreateCartView(View):
    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        if product_id:
            try:
                products = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                messages.error(request, 'This product does not exist.')
                return products
            else:
                cart = request.session.get('cart', {})
                cart[product_id] = cart.get(product_id, 0) + 1
                request.session['cart'] = cart
                messages.success(request, 'Product has been added to your cart.')
        else:
            messages.error(request, 'Invalid request.')
        return redirect(reverse('cart'))

class CartView(ListView):
    template_name = 'cart.html'
    model = Cart

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['product'] = Cart.objects.all()
        return context

class CartDeleteView(DeleteView):
    model = Cart

    def post(self, request, *args, **kwargs):
        product = Cart.objects.filter(pk=kwargs['pk'])
        product.delete()
        return redirect('index')

