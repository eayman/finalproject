from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.forms import AuthenticationForm

class clientModelForm(ModelForm):
    class Meta:
        model = Client
        fields = "__all__"
        
        exclude = ('user',)



    def __init__(self, *args, **kwargs ):
        super(clientModelForm,self).__init__(*args, **kwargs)
        
        for label, field in self.fields.items():
            field.widget.attrs.update({'class':'mt-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"',})
        

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            
        )
        def save(self, commit = True):
            user = super(CustomUserCreationForm, self).save(commit= False)
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.email = self.cleaned_data['email']

            if commit:
                user.save()
        
    def __init__(self, *args, **kwargs ):
            super(CustomUserCreationForm,self).__init__(*args, **kwargs)
        
            for label, field in self.fields.items():
                field.widget.attrs.update({'class':'mt-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"',})
        

class CustomUserUpdateForm(UserChangeForm):
    #profile_image = forms.ImageField()
    text = forms.CharField()
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )
        def save(self):
            
            
            user = super(CustomUserUpdateForm, self).save(commit= False) 
            user.save()
            
        
    def __init__(self, *args, **kwargs ):
            super(CustomUserUpdateForm,self).__init__(*args, **kwargs)
            for label, field in self.fields.items():
                field.widget.attrs.update({'class':'mt-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"',})
        

class SubModelForm(ModelForm):
    class Meta:
        model = Subscription
        fields = "__all__"
        
    def __init__(self, *args, **kwargs ):
        super(SubModelForm,self).__init__(*args, **kwargs)
        
        for label, field in self.fields.items():
            field.widget.attrs.update({'class':'mt-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"',})
        

class PlanModelForm(ModelForm):
    class Meta:
        model = Plan
        fields = "__all__"
        
    def __init__(self, *args, **kwargs ):
        super(PlanModelForm,self).__init__(*args, **kwargs)
        
        for label, field in self.fields.items():
            field.widget.attrs.update({'class':'mt-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"',})
        



class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs = {
                'placeholder': 'User Name',
                'type': 'username',
                'name' : 'username',
                'id': 'username',
                'class': 'w-full py-4 px-8 bg-slate-200 placeholder:font-semibold rounded hover:ring-1 outline-blue-500'
            }
        )
    )
