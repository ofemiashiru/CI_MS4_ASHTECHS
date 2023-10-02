from django import forms
from checkout.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'f_name', 'l_name', 'email', 'phone_number', 'address_line_1',
            'address_line_2', 'city', 'post_code', 'country',
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'f_name': 'First Name',
            'l_name': 'Last Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'post_code': 'Postal Code',
            'city': 'City',
            'address_line_1': 'Address Line 1',
            'address_line_2': 'Address Line 2',
        }

        self.fields['f_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
