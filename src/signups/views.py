# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm
# Create your views here.
def home(request):

    return render(request,'signup/signup.html')

def thankyou(request):
    form=SignUpForm(request.POST or None)
    context={
        'form':form,
    }
    if form.is_valid():
        save_it=form.save(commit=False)
        save_it.save()
        #send_mail(subject,message,from_email,to_list,fail_silently=True)
        subject='Thankyou for pre-ordering from rakib'
        message='wellcome to our site ,we apprecaiteo your business. /n we will be touch soon'
        from_email=settings.EMAIL_HOST_USER
	print(from_email)
	to_list=[form.cleaned_data.get('email')]
	print(to_list)

        #to_list=['save_it.email']
        send_mail(subject,message,from_email,to_list,fail_silently=True)
        messages.success(request,"Thankyou for your order")
        return HttpResponseRedirect('/thank-you/')


    return render(request,'signup/thankyou.html',context)
def aboutus(request):

    return render(request,'signup/about-us.html')
