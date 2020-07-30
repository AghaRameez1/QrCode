from django import forms
from django.contrib.auth.models import User

from api.models import Products


class productAddForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['barcode', 'product_brand', 'product_image', 'product_description', 'product_name', 'product_score']
    def __init__(self, *args, **kwargs):
        super(productAddForm, self).__init__(*args, **kwargs)
        self.fields['barcode'].required = True
        self.fields['barcode'].widget.attrs['class']= "form-control"
        self.fields['product_score'].required = True
        self.fields['product_score'].widget.attrs['class']= "form-control"
        self.fields['product_image'].required = False
        self.fields['product_image'].widget.attrs['class']= "form-control-file"
        self.fields['product_image'].widget.attrs['accept']="image/*"

        self.fields['product_brand'].required = True
        self.fields['product_brand'].widget.attrs['class'] = "form-control"
        self.fields['product_description'].required = True
        self.fields['product_description'].widget.attrs['class'] = "form-control"
        self.fields['product_name'].required = True
        self.fields['product_name'].widget.attrs['class'] = "form-control"


class loginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(error_messages={'required': 'Enter your password'}, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}), required=True)
    def __init__(self, *args, **kwargs):
        super(loginForm, self).__init__(*args, **kwargs)
        self.fields['username'].required = True
        self.fields['username'].widget.attrs['class'] = "form-control"
        self.fields['password'].required = True
        self.fields['password'].widget.attrs['class'] = "form-control"
