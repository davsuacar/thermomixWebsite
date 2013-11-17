# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from manuelaWebsite.models import MeetingRequest
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms.fields import CharField, EmailField
 
 
class meetingRequestForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(meetingRequestForm, self).__init__(*args, **kwargs)       
        self.helper = FormHelper()    
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('SEND', 'SEND'))
        

        
    class Meta:
        model = MeetingRequest
        fields = ['client_name', 'email', 'phone_number']
        
        
class contactForm(forms.Form):
    
    name = CharField(max_length=200)
    email = EmailField()
    phone = CharField()
    subject = CharField(max_length=500)
    
    def __init__(self, *args, **kwargs):
        super(contactForm, self).__init__(*args, **kwargs)       
        self.helper = FormHelper()    
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('SEND', 'SEND'))
        

        
        
        
