from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^signup_form/', views.signup_form, name='signup_form'),
]