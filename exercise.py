EXERCISE3:
pending_registrations = []
pending_registrations.append("jaffi")
pending_registrations.append("jarshi")
pending_registrations.append("Suba")
print("Total Registrations:", len(pending_registrations))
pending_registrations.pop(1)
print(pending_registrations)

EXERCISE4:

citizens = [
    {"city":"Chennai","name":"jaffi"},
    {"city":"Madurai","name":"jarshi"},
    {"city":"Chennai","name":"Suba"}
]

for citizen in citizens:
    if citizen["city"] == "Chennai":
        print(citizen["name"])
