def show_registration(patient_name, age, disease):
    print("---- Patient Registration Details ----")
    print(f"Patient Name : {patient_name}")
    print(f"Age          : {age}")
    print(f"Disease      : {disease}")
    print("--------------------------------------")

show_registration("Rahul", 25, "Fever")
show_registration("Priya", 30, "Headache")


# Default Parameter

def show_registration(patient_name, age, disease="General Checkup"):
    print(f"{patient_name} (Age: {age}) : {disease}")

show_registration("Kiran", 22)                # uses default
show_registration("Anbu", 35, "Diabetes")     # overrides default
