from django import forms

class PatientForm(forms.Form):
  patient_date_of_birth = forms.CharField(label='DOB', max_length=300)
  patient_first_name = forms.CharField(label='First_Name', max_length=20)
  patient_last_name = forms.CharField(label='Last_Name', max_length=300)
  patient_email = forms.CharField(label='Email', max_length=300)
  patient_cell_phone = forms.CharField(label='Cell_Phone', max_length=300)
  patient_address = forms.CharField(label='Address', max_length=300)
  patient_city = forms.CharField(label='City', max_length=300)
