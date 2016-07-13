from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PatientForm, EmailForm
import requests

def home(request):
  if request.method == "POST":
    form = EmailForm(request.POST)
    if form.is_valid():
      email = request.POST.get('patient_email')
      payload = {'access_token' : 'JkflzvxwYojWvkbuq9bBYVtQyNVXjm', 'email' : email}
      req = requests.get('https://drchrono.com/api/patients', params=payload)
      res = req.json()
      if len(res['results']) > 0:
         return HttpResponseRedirect('/addpatient/make_appointment')
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
                'access_token' : 'Q35WExlSWLkgylJ7RYfkSpZcdFVwrL',
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
      # before redirect, store session
      return HttpResponseRedirect('/addpatient/make_appointment')
      # curl -X POST -d "access_token=Q35WExlSWLkgylJ7RYfkSpZcdFVwrL&gender=Male&doctor=102394" https://drchrono.com/api/patients

      # curl -X GET -d "access_token=" https://drchrono.com/api/doctors
  else:
    form = PatientForm()
    return render(request, 'addpatient/sign_up.html', {'form':form})


def make_appointment(request):


  # response = req.json()
  if request.method == "POST":
    location = request.POST.get('location')
    # payload = {'access_token' : 'Q35WExlSWLkgylJ7RYfkSpZcdFVwrL', 'city' : location}
    # req = requests.get('https://drchrono.com/api/offices', params=payload)
    # res = req.json()
    return render(request, 'addpatient/dateselection.html', {'office_obj' : location})


  else:
    office_locations = ['San Francisco', 'New York', 'Chicago']
  # for i in response['results']:
  #   if i['city'] != None:
  #     if i['city'] not in storage:
  #       office_locations.append(i['city'])
    return render(request, 'addpatient/make_appointment.html', {'office_locations' : office_locations})


def show_dates(request):
  # get location from params
  location_selection = request.POST.get('location_selection')
  # api call
  payload = {'access_token' : 'JkflzvxwYojWvkbuq9bBYVtQyNVXjm'}
  req = requests.get('https://drchrono.com/api/offices', params=payload)
  response = req.json()

  office_objects = []

  # find corresponding office objects
  for i in response['results']:
    if i['city'] != None:
      if i['city'] == location_selection:
        office_objects.append(i)

  return render(request, 'addpatient/make_appointment.html', {'office_object' : office_object})


