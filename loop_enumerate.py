FOR LOOP:
citizens = ["jaffi", "jarshi", "suba"]
for citizen in citizens:
    print("Citizen:", citizen)

ENUMERATE:
citizens = ["jaffi", "jarshi", "suba"]
for index, citizen in enumerate(citizens, start=1):
    print(f"{index}. {citizen}")

WHILE LOOP:
count = 0
max_citizens = 3
while count < max_citizens:
    print(f"Processing Aadhaar Registration #{count+1}")
    count += 1
print("Registration Closed")
