from django import forms

LIST_DISPLAY_CHOICES = (
    ('list', 'List'),
    ('grid', 'Grid'),
)
class CollectionFilterForm(forms.Form):
    
    type = forms.ChoiceField(label='type', choices=LIST_DISPLAY_CHOICES, initial="list")
    per_page = forms.IntegerField(label='per page', initial=10)
    page_number = forms.IntegerField(label='page number', initial=1)
