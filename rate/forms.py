from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name')

# class RateForm(forms.ModelForm):
#     # CHOICES = (('1', '1',), ('2', '2',),('3','3'),('4','4'),('5','5'))
#     # rating = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
#     #rating = forms.IntegerField(widget=forms.HiddenInput(attrs={'id':'ratingvalue'}), min_value=1, max_value=5, initial=1)
#     comment = forms.CharField(widget=forms.Textarea(attrs={'rows':'10', 'maxlength':'1024'}))
#
#     class Meta:
#         model = Rate
#         fields = ('rate', 'comment',)