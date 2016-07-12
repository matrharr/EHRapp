from django import forms

class PatientForm(forms.Form):
  # make datetime
  # patient_date_of_birth = forms.DateField(label='DOB', max_length=300)
  patient_first_name = forms.CharField(label='First_Name', max_length=20)
  patient_last_name = forms.CharField(label='Last_Name', max_length=300)
  patient_gender = forms.CharField(label='Gender')
  patient_email = forms.CharField(label='Email', max_length=300)
  patient_cell_phone = forms.CharField(label='Cell_Phone', max_length=300)
  patient_address = forms.CharField(label='Address', max_length=300)
  patient_city = forms.CharField(label='City', max_length=300)


class AppointmentForm(forms.Form):
  appointment_duration = forms.IntegerField(label='Duration')
  appointment_exam_room = forms.IntegerField(label='Exam_Room')
  appointment_doctor = forms.IntegerField(label='Doctor_ID')
  appointment_office = forms.IntegerField(label='office')
  appointment_patient = forms.IntegerField(label='patient_id')
  appointment_scheduled_time = forms.DateField(label='Scheduled_Time')


class EmailForm(forms.Form):
  patient_email = forms.CharField(label='Email', max_length=50)

