class Doctor:
    def __init__(self, name, id, specialization):
        self.name = name
        self.id = id
        self.specialization = specialization
        self.appointments = []


class Patient:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.appointment_history = []

    def book_appointment(self):
        pass

    def cancel_appointment(self):
        pass


class Appointment:
    def __init__(self, doctor, patient, date, time):
        self.doctor = doctor
        self.patient = patient
        self.date = date
        self.time = time
        self.status = "Scheduled"


class Hospital:
    def __init__(self, name):
        self.name = name
        self.doctors = []
        self.patients = []
        self.appointments = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def add_patient(self, patient):
        self.patients.append(patient)

    def schedule_appointment(self, doctor, patient, date, time):
        appointment = Appointment(doctor, patient, date, time)
        self.appointments.append(appointment)
        doctor.appointments.append(appointment)
        patient.appointment_history.append(appointment)
        print("appointment scheduled successfully")
        return appointment

    def cancel_appointment(self, appointment):
        appointment.status = "Cancelled"
        if appointment in appointment.doctor.appointments:
            appointment.doctor.appointments.remove(appointment)
        if appointment in appointment.patient.appointment_history:
            appointment.patient.appointment_history.remove(appointment)
        if appointment in self.appointments:
            self.appointments.remove(appointment)
        print("appointment cancelled successfully")


doctor1 = Doctor("dr varun", "v77", "dentist")
patient1 = Patient("john", "j55")

hospital = Hospital("kims hospital")
hospital.add_doctor(doctor1)
hospital.add_patient(patient1)

appointment1 = hospital.schedule_appointment(
    doctor1, patient1, "1-11-2026", "11:00 am"
)
hospital.cancel_appointment(appointment1)
