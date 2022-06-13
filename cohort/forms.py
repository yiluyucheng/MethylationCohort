from django import forms

ARRAY_CHOICES = (('450k', '450k'), ('epic', 'EPIC array (850k)'))

class CohortForm(forms.Form):
    ids = forms.CharField(label='Cohort ID', max_length=100)
    array = forms.CharField(label="Array", widget=forms.RadioSelect(choices=ARRAY_CHOICES), required=False)
    annotation = forms.CharField(label="annotation", max_length=100, required=False)
    count = forms.IntegerField(label='Count', required=False)
    tissue = forms.CharField(label='Source Tissue', max_length=100, required=False)
    note = forms.CharField(label='Note', max_length=100, required=False)
    project = forms.CharField(label='Project', max_length=100, required=False)
    

class DelForm(forms.Form):
    ids = forms.CharField(label='Cohort ID', max_length=100)    
