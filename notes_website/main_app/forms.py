from django import forms

class AddNewNote(forms.Form):
    title = forms.CharField(min_length=1,max_length=100)
    describe = forms.CharField(widget=forms.Textarea(attrs = {"cols": "20", "rows": "3"}),min_length=1,max_length=1000) 