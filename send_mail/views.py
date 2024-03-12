from django.shortcuts import render
from django.views import View
from core import settings
from django.core.mail import send_mail
from django.http import HttpResponse


# Create your views here.
class EmailSenderView(View):
    template_name = "sendmail.html"

    def get(self,request):
        return render(request,self.template_name)
    
    def post(self,request):
        # get data we need
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        # attention to getlist in this line pls
        recep_list = request.POST.getlist("email")
        

        # send email
        try:
            # You need to add your email and password to settings.py first
            send_mail(subject,message,from_email=settings.EMAIL_HOST_USER,recipient_list=recep_list)
            return HttpResponse("Email Sent Successfully")
        except Exception as error:
            return HttpResponse(error)

