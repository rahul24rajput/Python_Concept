from django import forms

class StudentRegistration(forms.Form):
    name  = forms.CharField()
    marks  = forms.CharField()

class FeedBackForms(forms.Form):
    name = forms.CharField()
    rollno = forms.IntegerField()
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)
    
