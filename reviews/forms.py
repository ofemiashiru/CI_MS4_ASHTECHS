from django import forms
from reviews.models import Review


class ReviewForm(forms.ModelForm):
    review_content = forms.CharField(widget=forms.Textarea)
    rating = forms.IntegerField(
        widget=forms.TextInput(
            attrs={'min': 0, 'max': 100, 'value': 0, 'type': 'number'}
        )
    )

    class Meta:
        model = Review
        fields = (
            'title', 'review_content', 'rating',
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'review_content': 'Write your review',
            'rating': 'Rating out of 100',
        }

        self.fields['title'].widget.attrs['autofocus'] = True

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
