# Top Super Hit Movies of Famous Actors

movies = {
    "vijay": [
        "Leo",
        "Master",
        "Thuppakki",
        "Ghilli",
        "Pokkiri",
        "Kaththi",
        "Bigil",
        "Mersal",
        "Sarkar",
        "Theri"
    ],
    "ajith": [
        "Mankatha",
        "Viswasam",
        "Veeram",
        "Billa",
        "Valimai",
        "Yennai Arindhaal",
        "Vedalam",
        "Aarambam",
        "Dheena",
        "Citizen"
    ],
    "surya": [
        "Soorarai Pottru",
        "Singam",
        "Ghajini",
        "Ayan",
        "Vaaranam Aayiram",
        "24",
        "Kaakha Kaakha",
        "Jai Bhim",
        "Etharkkum Thunindhavan",
        "Vel"
    ],
    "dhanush": [
        "Asuran",
        "VIP",
        "Karnan",
        "Raanjhanaa",
        "Thiruchitrambalam",
        "Maari",
        "Polladhavan",
        "Yaaradi Nee Mohini",
        "Aadukalam",
        "Captain Miller"
    ]
}

top_x = int(input("Please enter top x number (1-10): "))
actor = input("Please enter the actor name: ").lower()

if actor not in movies:
    print("Error: Unknown actor")
elif top_x < 1 or top_x > 10:
    print("Error: Please enter a number between 1 and 10")
else:
    print(f"\nHere are the top {top_x} super hit movies of {actor.title()}")

    for i in range(top_x):
        print(f"{i+1}. {movies[actor][i]}")
