from hms_logic import (
    check_login,
    add_doctor,
    add_patient,
    assign_patient,
    add_report,
    doctors,
    patients
)

# ---------------- TEST LOGIN ----------------
def test_login_success():
    assert check_login("mbq", "123") == "admin"

def test_login_fail():
    assert check_login("wrong", "123") is None


# ---------------- TEST DOCTOR ----------------
def test_add_doctor():
    result = add_doctor("doc1", "pass", "Cardiology")
    assert result == "success"
    assert "doc1" in doctors


# ---------------- TEST PATIENT ----------------
def test_add_patient():
    result = add_patient("pat1", "pass")
    assert result == "success"
    assert "pat1" in patients


# ---------------- TEST ASSIGN ----------------
def test_assign():
    add_doctor("d1", "123", "ENT")
    add_patient("p1", "123")

    result = assign_patient("d1", "p1")
    assert result == "success"


# ---------------- TEST REPORT ----------------
def test_report():
    add_doctor("d2", "123", "ENT")
    add_patient("p2", "123")
    assign_patient("d2", "p2")

    result = add_report("d2", "p2", "Fever detected")
    assert result == "success"