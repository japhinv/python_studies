def create_patient_id(patient_name, disease):
    patient_id = patient_name[:3].upper() + "_" + disease[:3].upper()
    return patient_id

id1 = create_patient_id("Rahul Kumar", "Fever")
id2 = create_patient_id("Priya", "Cough")

print(id1)
print(id2)
