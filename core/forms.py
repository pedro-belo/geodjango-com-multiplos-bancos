from django import forms

from core import models


class FormMixin:
    widget_extra_attrs = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for extra_attr in self.widget_extra_attrs:
            field, attr_name, attr_value = extra_attr
            self.set_widget_attrs(field, attr_name, attr_value)

    def set_widget_attrs(self, field, attr, value):
        self.fields[field].widget.attrs[attr] = value


class FormSelectProduct(FormMixin, forms.Form):

    widget_extra_attrs = [
        ('product', 'class', 'form-control')
    ]

    product = forms.ModelChoiceField(queryset=models.Product.objects.all())


class MarketplaceForm(FormMixin, forms.ModelForm):

    widget_extra_attrs = [
        ('product', 'class', 'form-control col-md-7 col-xs-12'),
        ('quantity', 'class', 'form-control')
    ]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['product'].queryset = self.get_queryset_products()

    def get_queryset_products(self):
        return models.Product.objects.exclude(
            marketplace__seller__user=self.user)

    class Meta:
        model = models.Marketplace
        fields = ('product', 'quantity')
