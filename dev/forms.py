from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label='',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Email Address'})
    )
    first_name = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'First name'})
    )
    last_name = forms.CharField(
        label='',
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Last name'})
    )
    username = forms.CharField(
        label='',
        max_length=150,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Username'}),
        help_text='<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
    )
    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'}),
        help_text='<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'
    )
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        help_text='<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                field.widget.attrs.update({'class': 'form-control'})
                field.label = ''

        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'


class RecordAddForm(forms.ModelForm):
    first_name = forms.CharField(required=True,
                                 max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True,
                                max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(required=True, max_length=150, widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    phone = forms.CharField(required=True, max_length=150, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    address = forms.CharField(required=True, max_length=150, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    city = forms.CharField(required=True, max_length=150, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    state = forms.CharField(required=True, max_length=150, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    zipcode = forms.CharField(required=True, max_length=150, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = Record
        exclude = ('slug',)
