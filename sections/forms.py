from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'form-control'},
        ),
        required=True,
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control'},
        ),
        required=True,
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control'},
        ),
        required=True,
    )
