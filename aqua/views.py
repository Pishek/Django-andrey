from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.
from .forms import ContactForm

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail('Заказ обслуживания','Имя: ' + form.cleaned_data['subject'] + '\n' +
                             form.cleaned_data['Text'] + '\n' + 'Email: ' + form.cleaned_data['Email'],
                             'requestaqua@yandex.ru', ['pishek5@gmail.com'], fail_silently=False)
            if mail:
                messages.success(request, 'Письмо успешно отправлено!')
                return redirect('index')
            else:
                messages.error(request, 'К сожалению, письмо не отправилось, попробуйте еще раз!')
        else:
            messages.error(request, 'К сожалению, письмо не отправилось, попробуйте еще раз!')
    else:
        form = ContactForm()
    return render(request, 'aqua/index.html', {'form': form})