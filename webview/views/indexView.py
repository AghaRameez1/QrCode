from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views.generic.base import View
from django.contrib.auth import logout, login
from django.contrib.auth import authenticate
from api.models import Products
from webview.forms.productForm import productAddForm, loginForm


class indexView(View):

    def dispatch(self, request, *args, **kwargs):
        return super(indexView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        product_obj = Products.objects.all()
        context = {
            'product': product_obj
        }
        return render(request, 'index.html', context)


class deleteView(View):
    def dispatch(self, request, *args, **kwargs):
        return super(deleteView, self).dispatch(request, *args, **kwargs)
    def delete(self, request, id, *args, **kwargs):
        if request.user.is_authenticated:
            Products.objects.filter(id= id).delete()
            product_obj = Products.objects.all()
            context = {
                'product': product_obj
            }
            string = render(request,'_partial/_table.html',context)
            return HttpResponse(string)


class loginView(View):
    def dispatch(self, request, *args, **kwargs):
        return super(loginView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = loginForm
        context = {
            'form': form
        }
        return render(request, 'login.html', context)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = loginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            password = data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse('success')

        else:
            print(form.errors)
            return HttpResponse('error')


class logoutView(View):
    def dispatch(self, request, *args, **kwargs):
        return super(logoutView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
            return redirect('index')


class productAdd(View):
    def dispatch(self, request, *args, **kwargs):
        return super(productAdd, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        # print(request.user)
        if request.user.is_authenticated:
            form = productAddForm
            context = {
                'form': form
            }
            return render(request, 'productAdd.html', context)
        else:
            string = render_to_string('404.html')
            return HttpResponse(string)

    def post(self, request, *args, **kwargs):
        form = productAddForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data
            barcode = data['barcode']
            name = data['product_name']
            description = data['product_description']
            brand = data['product_brand']
            score = data['product_score']
            image = request.FILES['product_image']
            Products.objects.create(
                barcode=barcode,
                product_name=name,
                product_description=description,
                product_brand=brand,
                product_score=score,
                product_image=image
            )
            return HttpResponse('success')
        else:
            print(form.errors)
            return HttpResponse('error')
