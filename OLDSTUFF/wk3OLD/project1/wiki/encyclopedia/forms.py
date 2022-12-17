import re
from .util import list_entries

from django import forms


class searchForm(forms.Form):

    query = forms.charField(label='', required=True, widget=forms.TextInput(attrs={'placeholder': 'Search Encyclopedia'}))


