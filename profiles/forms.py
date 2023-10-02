from django import forms
from profiles.models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'd_phone_number': 'Phone Number',
            'd_address_line_1': 'Address Line 1',
            'd_address_line_2': 'Address Line 2',
            'd_city': 'City',
            'd_post_code': 'Postal Code',
        }

        self.fields['d_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'd_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'profile-form-input'
            self.fields[field].label = False
