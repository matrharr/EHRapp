from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PatientForm, EmailForm
import requests
import datetime
from utils import parse_office, parse_appointments

def home(request):
  if request.method == "POST":
    form = EmailForm(request.POST)
    if form.is_valid():
      email = request.POST.get('patient_email')
      payload = {'access_token' : 'UwCDz7nKvDkNQjOumpXgPKcxl8eije',
                 'email' : email}
      req = requests.get('https://drchrono.com/api/patients', params=payload)
      res = req.json()

      if len(res['results']) > 0:
        request.session['patient_id'] = res['results'][0]['id']
        return HttpResponseRedirect('/addpatient/date_selection')

      else:
        # if empty response, redirect to signup_form

        return HttpResponseRedirect('/addpatient/signup_form')

    #invalid form error handling
    else:
      return render(request, 'addpatient/home.html', {'form' : form})

  else:
    form = EmailForm()
    return render(request, 'addpatient/home.html', {'form':form})


def signup_form(request):
  if request.method == "POST":
    form = PatientForm(request.POST)
    if form.is_valid():

      date_of_birth = request.POST.get('patient_date_of_birth')
      first_name = request.POST.get('patient_first_name')
      last_name = request.POST.get('patient_last_name')
      gender = request.POST.get('patient_gender')
      email = request.POST.get('patient_email')
      cell_phone = request.POST.get('patient_cell_phone')
      address = request.POST.get('patient_address')
      city = request.POST.get('patient_city')

      post_payload = {
                'access_token' : 'UwCDz7nKvDkNQjOumpXgPKcxl8eije',
                'gender' : gender,
                'doctor' :  102394,
                # Change template to send datetime
                # 'date_of_birth' : date_of_birth,
                'first_name' : first_name,
                'last_name' : last_name,
                'email' : email,
                'address' : address,
                'city' : city,
                'cell_phone' : cell_phone,
                }

      post_req = requests.post('https://drchrono.com/api/patients', data=post_payload)

      get_payload = {'access_token' : 'UwCDz7nKvDkNQjOumpXgPKcxl8eije', 'email' : email }
      get_req = requests.get('https://drchrono.com/api/patients', params=get_payload)
      res = get_req.json()

      request.session['patient_id'] = res['results'][0]['id']
      return HttpResponseRedirect('/addpatient/date_selection')
    else:
      return render(request, 'addpatient/home.html', {'form' : form})

  else:
    form = PatientForm()
    return render(request, 'addpatient/sign_up.html', {'form':form})

def date_selection(request):
  if request.method == "POST":
    office_id = request.POST.get('office_id')
    doctor_id = request.POST.get('doctor_id')
    start_time = request.POST.get('start_time')
    end_time = request.POST.get('end_time')

    payload = {'access_token' : 'UwCDz7nKvDkNQjOumpXgPKcxl8eije',
                'doctor' : doctor_id, 'duration' : 60,
                'exam_room' : 1, 'office' : office_id,
                'patient' : request.session['patient_id'],
                'scheduled_time' : datetime.datetime.now()}

    req = requests.post('https://drchrono.com/api/appointments', data=payload)

    return HttpResponseRedirect('/addpatient/thank_you')

  else:
    payload = {'access_token' : 'UwCDz7nKvDkNQjOumpXgPKcxl8eije',
                'verbose' : 'true'}

    req = requests.get('https://drchrono.com/api/offices', params=payload)

    res = req.json()
    office_info = parse_office(res)
    appointments = parse_appointments(res)

    return render(request, 'addpatient/date_selection.html', {'office_info' : office_info, 'appointments' : appointments})


def thank_you(request):
  return render(request, 'addpatient/thank_you.html', {})