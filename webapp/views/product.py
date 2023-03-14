from django.urls import reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from webapp.form import ProductForm
from webapp.models import Product


class ProductCreateView(CreateView):
    template_name = 'product_add.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})

class ProductDetailView(DetailView):
    template_name = 'product.html'
    model = Product

class ProductUpdateView(UpdateView):
    template_name = 'product_update.html'
    form_class = ProductForm
    model = Product
    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    def get_success_url(self):
        return reverse('index')