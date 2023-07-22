from django import forms

# TODO quantity of product!!!
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):

    def __init__(self, *args, default_quantity_product=1, **kwargs):
        self.default_quantity_product = default_quantity_product
        self.quantity_product_choices = [(i, str(i)) for i in range(1, default_quantity_product)]
        return super().__init__(*args, **kwargs)


    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int)
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)