from django.core.handlers.wsgi import WSGIRequest
from django.db.models import Q
from django.shortcuts import render
from django.utils.http import urlencode
from django.views.generic import ListView

from webapp.form import SearchForm
from webapp.models import Product


class IndexView(ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = 'product'
    queryset = Product.objects.filter(leftover__gte=1)
    paginate_by = 5
    paginate_orphans = 1
    ordering = ('name', 'category')

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get('search_value')
        return None

    def get_queryset(self):
        queryset = super().get_queryset().all()
        if self.search_value:
            query = Q(name__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context