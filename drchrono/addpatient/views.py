from django.shortcuts import render
from django.http import HttpResponse
from .forms import PatientForm

def signup_form(request):
  if request.method == "POST":
    form = PatientForm(request.POST)
    if form.is_valid():
      print request.POST
      date_of_birth = request.POST.get('patient_date_of_birth')
      first_name = request.POST.get('patient_first_name')
      last_name = request.POST.get('patient_last_name')
      email = request.POST.get('patient_email')
      cell_phone = request.POST.get('patient_cell_phone')
      address = request.POST.get('patient_address')
      city = request.POST.get('patient_city')
      # API POST TO /api/patients
      # patient_obj = Patient(title=title, body=body, created_at=timezone.now())
      # todo_obj.save()
      return HttpResponse('thanks')
  else:
    form = PatientForm()
    return render(request, 'addpatient/sign_up.html', {'form':form})