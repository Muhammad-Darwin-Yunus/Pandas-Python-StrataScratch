>.<

Title: Gender With Most Doctor Appointments
Link: https://platform.stratascratch.com/coding/10170-gender-with-most-doctor-appointments?code_type=2
Level: Easy

Find the gender that has made the most number of doctor appointments.
Output the gender along with the corresponding number of appointments.

Data medical_appointments:
patientid: float
appointmentid: int
gender: varchar
scheduledday: datetime
appointmentday: datetime
age: int
neighbourhood:varchar
scholarship: int
hipertension int
diabetes: int
alcoholism: int
handcap: int
sms_received: int
no_show: varchar

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

gender_doctor = pd.DataFrame(medical_appointments)

gender_doctor = gender_doctor.groupby('gender')['appointmentid'].count().reset_index()

gender_doctor = gender_doctor.rename(columns={'appointmentid':'total_appointments'})

Output:

gender | total_appointments
M            42
F            58
