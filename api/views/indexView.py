from django.shortcuts import render
from django.views.generic.base import View

from api.models import Products


class indexView(View):

    def dispatch(self, request, *args, **kwargs):
        return super(indexView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args,**kwargs):
        product_obj = Products.objects.all()
        context = {
            'product': product_obj
        }
        return render(request, 'index.html', context)
