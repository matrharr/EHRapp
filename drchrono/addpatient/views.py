from django.shortcuts import render
from django.http import HttpResponse
from .forms import PatientForm
import requests

def signup_form(request):
  if request.method == "POST":
    form = PatientForm(request.POST)
    if form.is_valid():
      print request.POST
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
      return HttpResponse(req)

      # curl -X POST -d "access_token=Q35WExlSWLkgylJ7RYfkSpZcdFVwrL&gender=Male&doctor=102394" https://drchrono.com/api/patients

      # curl -X GET -d "access_token=" https://drchrono.com/api/doctors

  else:
    form = PatientForm()
    return render(request, 'addpatient/sign_up.html', {'form':form})


