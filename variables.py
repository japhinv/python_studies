# Hospital Registration System

def get_details():
    patient_name = input("Enter Patient Name: ")
    age = input("Enter Age: ")
    disease = input("Enter Disease/Problem: ")

    return patient_name, age, disease


def print_details(patient_name, age, disease):
    print("\n--- Patient Registration Details ---")
    print(f"Patient Name : {patient_name}")
    print(f"Age          : {age}")
    print(f"Disease      : {disease}")


# Main Program
patient_name, age, disease = get_details()
print_details(patient_name, age, disease)
