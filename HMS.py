import tkinter as tk
from tkinter import messagebox

# ---------------- DATA STORAGE ----------------
users = {
    "mbq": {"password": "123", "role": "admin"}
}

patients = {}
doctors = {}
appointments = []
reports = []
bills = []

# doctor-patient assignment
doctor_patient_map = {}

# ---------------- HELPERS ----------------
def error(msg):
    messagebox.showerror("Error", msg)

def success(msg):
    messagebox.showinfo("Success", msg)

# ---------------- LOGIN ----------------
def login():
    u = username.get()
    p = password.get()

    if u in users and users[u]["password"] == p:
        role = users[u]["role"]
        success("Login Successful")

        root.withdraw()

        if role == "admin":
            admin_panel()
        elif role == "doctor":
            doctor_panel(u)
        elif role == "patient":
            patient_panel(u)
    else:
        error("Invalid Credentials")


# ---------------- ADMIN PANEL ----------------
def admin_panel():
    admin = tk.Toplevel()
    admin.title("Admin Panel")
    admin.geometry("500x500")

    # Add Doctor
    tk.Label(admin, text="Doctor Username").pack()
    du = tk.Entry(admin)
    du.pack()

    tk.Label(admin, text="Password").pack()
    dp = tk.Entry(admin)
    dp.pack()

    tk.Label(admin, text="Specialization").pack()
    spec = tk.Entry(admin)
    spec.pack()

    def add_doc():
        u = du.get()
        p = dp.get()
        s = spec.get()

        if not u or not p:
            error("Doctor fields required")
            return

        users[u] = {"password": p, "role": "doctor"}
        doctors[u] = {"spec": s, "patients": []}

        success("Doctor Added")

    tk.Button(admin, text="Add Doctor", command=add_doc).pack(pady=5)

    # Add Patient
    tk.Label(admin, text="Patient Username").pack()
    pu = tk.Entry(admin)
    pu.pack()

    tk.Label(admin, text="Password").pack()
    pp = tk.Entry(admin)
    pp.pack()

    def add_patient():
        u = pu.get()
        p = pp.get()

        if not u or not p:
            error("Patient fields required")
            return

        users[u] = {"password": p, "role": "patient"}
        patients[u] = {"reports": [], "bills": [], "appointments": []}

        success("Patient Added")

    tk.Button(admin, text="Add Patient", command=add_patient).pack(pady=5)

    # Assign Patient to Doctor
    tk.Label(admin, text="Assign Doctor → Patient").pack()
    ad = tk.Entry(admin)
    ad.pack()
    ap = tk.Entry(admin)
    ap.pack()

    def assign():
        d = ad.get()
        p = ap.get()

        if d in doctors and p in patients:
            doctor_patient_map.setdefault(d, []).append(p)
            success("Assigned Successfully")
        else:
            error("Invalid Doctor or Patient")

    tk.Button(admin, text="Assign", command=assign).pack(pady=10)


# ---------------- DOCTOR PANEL ----------------
def doctor_panel(doc_user):
    doc = tk.Toplevel()
    doc.title("Doctor Panel")
    doc.geometry("400x400")

    tk.Label(doc, text=f"Doctor: {doc_user}").pack()

    tk.Label(doc, text="Patient Username").pack()
    pu = tk.Entry(doc)
    pu.pack()

    tk.Label(doc, text="Diagnosis Report").pack()
    rep = tk.Entry(doc)
    rep.pack()

    def add_report():
        p = pu.get()
        r = rep.get()

        if p not in doctor_patient_map.get(doc_user, []):
            error("Not assigned to this patient")
            return

        patients[p]["reports"].append(r)
        success("Report Added")

    tk.Button(doc, text="Submit Report", command=add_report).pack()


# ---------------- PATIENT PANEL ----------------
def patient_panel(user):
    p = tk.Toplevel()
    p.title("Patient Panel")
    p.geometry("400x400")

    tk.Label(p, text=f"Patient: {user}").pack()

    def show_data():
        data = patients.get(user, {})
        messagebox.showinfo(
            "Your Data",
            f"Reports: {data.get('reports')}\nBills: {data.get('bills')}\nAppointments: {data.get('appointments')}"
        )

    tk.Button(p, text="View My Records", command=show_data).pack()


# ---------------- MAIN LOGIN UI ----------------
root = tk.Tk()
root.title("HMS Login System")
root.geometry("300x200")

tk.Label(root, text="Username").pack()
username = tk.Entry(root)
username.pack()

tk.Label(root, text="Password").pack()
password = tk.Entry(root, show="*")
password.pack()

tk.Button(root, text="Login", command=login).pack(pady=10)

root.mainloop()