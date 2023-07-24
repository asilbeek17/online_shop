from django import forms
from app.models import Product, Feedback


class ProductModelForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ()


class FeedbackModelForm(forms.ModelForm):

    class Meta:
        model = Feedback
        exclude = ()
