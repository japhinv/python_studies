# EXERCISE 1 :

patient_name = input("Enter Patient Name: ")
city = input("Enter City: ")
disease = input("Enter Disease: ")

print(f"Registration: {patient_name} from {city} for {disease}")

# EXERCISE 2 :

def check_medical_report_uploaded(medical_report_uploaded):
    if medical_report_uploaded:
        print("Medical report attached")
    else:
        print("No medical report - PLEASE CROSSCHECK")

check_medical_report_uploaded(True)
check_medical_report_uploaded(False)
