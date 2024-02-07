# creation of a movie review form
from django.forms import ModelForm, Textarea
from .models import Review

class ReviewForm(ModelForm):
    # default for extending ModelForm features
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'form-control'})
        self.fields['watchAgain'].widget.attrs.update({'class': 'form-check-input'})

    # specifying which model the form is for and the fields we want in it
    class Meta:
        model = Review
        fields = ['text', 'watchAgain']
        # labelling model headers to be more reader friendly
        labels = {
            'watchAgain': 'Watch Again'
        }
        # by default, CharFields will display an input tag thus change it to a textarea tag
        widgets = {
            'text': Textarea(attrs={'rows': 4}),
        }
