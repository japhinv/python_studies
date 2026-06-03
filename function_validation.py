def validate_registration(patient_name, age, disease):
    if patient_name == "" or age == "" or disease == "":
        print("Error: All fields are required!")
        return False

    print("Registration form is valid.")
    return True

validate_registration("Rahul", "25", "Fever")   # valid
validate_registration("", "25", "Fever")        # invalid
