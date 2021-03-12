from django import forms


class URLForm(forms.Form):
    MainURL = forms.URLField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Example: https://github.com/rojinebrahimi'})
    )
    CustomURL = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Example: simplify'}), required=False
    )