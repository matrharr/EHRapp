from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^home/', views.home, name='home'),
  url(r'^signup_form/', views.signup_form, name='signup_form'),
  # url(r'^make_appointment/', views.make_appointment, name='make_appointment'),
  url(r'^date_selection/', views.date_selection, name='date_selection'),
  url(r'^thank_you/', views.thank_you, name='thank_you')
]