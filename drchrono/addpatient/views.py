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
      payload = {'access_token' : 'UwCDz7nKvDkNQjOumpXgPKcxl8eije', 'email' : email}
      req = requests.get('https://drchrono.com/api/patients', params=payload)
      res = req.json()

      if len(res['results']) > 0:
        request.session['patient_id'] = res['results'][0]['id']
        return HttpResponseRedirect('/addpatient/date_selection')

      else:
        # if nothing returned, redirect to signup_form

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
      # print request.POST
      date_of_birth = request.POST.get('patient_date_of_birth')
      first_name = request.POST.get('patient_first_name')
      last_name = request.POST.get('patient_last_name')
      gender = request.POST.get('patient_gender')
      email = request.POST.get('patient_email')
      cell_phone = request.POST.get('patient_cell_phone')
      address = request.POST.get('patient_address')
      city = request.POST.get('patient_city')

      payload = {
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

      req = requests.post('https://drchrono.com/api/patients', data=payload)
      # res = req.json()
      # before redirect, store session
      # return HttpResponse(req)
      request.session['patient_id'] = res['id']
      return HttpResponseRedirect('/addpatient/date_selection')
      # curl -X POST -d "access_token=Q35WExlSWLkgylJ7RYfkSpZcdFVwrL&gender=Male&doctor=102394" https://drchrono.com/api/patients

      # curl -X GET -d "access_token=" https://drchrono.com/api/doctors
  else:
    form = PatientForm()
    return render(request, 'addpatient/sign_up.html', {'form':form})


# def make_appointment(request):
#   # response = req.json()
#   if request.method == "POST":
#     location = request.POST.get('location')
#     payload = {'access_token' : 'Q35WExlSWLkgylJ7RYfkSpZcdFVwrL', 'city' : location}

#     req = requests.get('https://drchrono.com/api/offices', params=payload)
#     res = req.json()

#     return render(request, 'addpatient/date_selection.html', {'doctor_name' : res['results'][0]['name'], 'doctor_id' : res['results'][0]['doctor'], 'start_time' : res['results'][0]['start_time'], 'end_time' : res['results'][0]['end_time'], 'office_id' : res['results'][0]['id']})

#   else:
#     office_locations = ['San Francisco', 'New York', 'Chicago']
#     # for i in response['results']:
#     #   if i['city'] != None:
#     #     if i['city'] not in storage:
#     #       office_locations.append(i['city'])
#     return render(request, 'addpatient/make_appointment.html', {'office_locations' : office_locations})


def date_selection(request):
  if request.method == "POST":
    office_id = request.POST.get('office_id')
    doctor_id = request.POST.get('doctor_id')
    start_time = request.POST.get('start_time')
    end_time = request.POST.get('end_time')

    payload = {'access_token' : 'UwCDz7nKvDkNQjOumpXgPKcxl8eije', 'doctor' : doctor_id, 'duration' : 60, 'exam_room' : 1, 'office' : office_id, 'patient' : request.session['patient_id'], 'scheduled_time' : datetime.datetime.now()}

    req = requests.post('https://drchrono.com/api/appointments', data=payload)

    return HttpResponse(req)

  else:
    payload = {'access_token' : 'UwCDz7nKvDkNQjOumpXgPKcxl8eije', 'verbose' : 'true'}

    # response object req
    req = requests.get('https://drchrono.com/api/offices', params=payload)

    res = req.json()
    office_info = parse_office(res)
    appointments = parse_appointments(res)

    return render(request, 'addpatient/date_selection.html', {'office_info' : office_info, 'appointments' : appointments})


