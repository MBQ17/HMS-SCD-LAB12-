users = {
    "mbq": {"password": "123", "role": "admin"}
}

patients = {}
doctors = {}
doctor_patient_map = {}


# ---------------- LOGIN LOGIC ----------------
def check_login(username, password):
    if username in users and users[username]["password"] == password:
        return users[username]["role"]
    return None


# ---------------- ADD DOCTOR ----------------
def add_doctor(username, password, specialization):
    if not username or not password:
        return "error"

    users[username] = {"password": password, "role": "doctor"}
    doctors[username] = {"spec": specialization, "patients": []}
    return "success"


# ---------------- ADD PATIENT ----------------
def add_patient(username, password):
    if not username or not password:
        return "error"

    users[username] = {"password": password, "role": "patient"}
    patients[username] = {"reports": [], "bills": [], "appointments": []}
    return "success"


# ---------------- ASSIGN DOCTOR TO PATIENT ----------------
def assign_patient(doctor, patient):
    if doctor in doctors and patient in patients:
        doctor_patient_map.setdefault(doctor, []).append(patient)
        return "success"
    return "error"


# ---------------- ADD REPORT ----------------
def add_report(doctor, patient, report):
    if patient not in doctor_patient_map.get(doctor, []):
        return "not_assigned"

    patients[patient]["reports"].append(report)
    return "success"