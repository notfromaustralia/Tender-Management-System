from django import forms
from .models import Tender

class TenderForm(forms.ModelForm):
    class Meta:
        model = Tender
        fields = ['tender_no' , 'title' , 'description' , 'category' , 'location', 'document' , 'due_date']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),  # Use HTML5 date input type
        }

    def __init__(self, *args, **kwargs):
        super(TenderForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'