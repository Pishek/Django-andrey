from django import forms




class ContactForm(forms.Form):
    subject = forms.CharField(label='FullName', widget=forms.TextInput(attrs={'class':'form-control col-12', 'placeholder': 'Ваше имя'}))
    Email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class':'form-control col-12','placeholder': 'Email'}))
    Text = forms.CharField(label='Текст', widget=forms.TextInput(attrs={'class':'form-control col-12','placeholder': 'Сообщение'}))