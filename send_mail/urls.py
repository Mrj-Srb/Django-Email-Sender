from django.urls import path
from . import views


urlpatterns = [
    path('',views.EmailSenderView.as_view(),name="send_email")
]