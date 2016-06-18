from django import forms
from shortner import models
from django.utils.translation import ugettext_lazy as _

class UrlShortnerForm(forms.Form):
    weburl = forms.URLField(widget=forms.TextInput(attrs=dict(required=True, max_length=200)), label=_("Long link"),
                                error_messages={ 'invalid': _("You must enter a proper URL") })
    shortened_link = forms.CharField(widget = forms.TextInput(attrs = dict(max_length=2)), label = _('Custom URL'),
                                error_messages = {'Invalid': _('Length should be less than 20')})
