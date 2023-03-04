
from django.forms import ModelForm
from .models import *
from django import forms


class LeadModelForm(ModelForm):
    class Meta:
        model = Lead
        fields = "__all__"
        exclude = ('agent',)
  


    def __init__(self, *args, **kwargs ):
        super(LeadModelForm,self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'mt-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"',})
        
        #self.fields['title'].widget.attrs.update({'class':'input','placeholder':'Add Project Title here ..'})