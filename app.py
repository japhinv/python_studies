from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mock database of movies
movies = {
    "M001": {
        "title": "Dune: Part Two",
        "genre": "Sci-Fi",
        "showtime": "06:30 PM",
        "seats": 12,
        "price": 250,
        "rating": "8.8",
        "banner": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=60",
        "synopsis": "Paul Atreides unites with Chani and the Fremen while seeking revenge against the conspirators who destroyed his family."
    },
    "M002": {
        "title": "Oppenheimer",
        "genre": "Drama",
        "showtime": "03:00 PM",
        "seats": 8,
        "price": 220,
        "rating": "8.9",
        "banner": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&auto=format&fit=crop&q=60",
        "synopsis": "The story of American scientist J. Robert Oppenheimer and his role in the development of the atomic bomb."
    },
    "M003": {
        "title": "Spider-Man: Across the Spider-Verse",
        "genre": "Animation",
        "showtime": "11:00 AM",
        "seats": 15,
        "price": 180,
        "rating": "9.0",
        "banner": "https://images.unsplash.com/photo-1635805737707-575885ab0820?w=800&auto=format&fit=crop&q=60",
        "synopsis": "Miles Morales catapults across the Multiverse, where he encounters a team of Spider-People charged with protecting its very existence."
    },
    "M004": {
        "title": "Interstellar",
        "genre": "Sci-Fi",
        "showtime": "09:00 PM",
        "seats": 5,
        "price": 300,
        "rating": "8.7",
        "banner": "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=800&auto=format&fit=crop&q=60",
        "synopsis": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival."
    },
    "M005": {
        "title": "The Dark Knight",
        "genre": "Action",
        "showtime": "08:00 PM",
        "seats": 20,
        "price": 200,
        "rating": "9.0",
        "banner": "https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?w=800&auto=format&fit=crop&q=60",
        "synopsis": "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice."
    }
}

# Route 1: Show Home Dashboard with search feature
@app.route("/")
def home():
    # Render search page and pass all movies to display on the dashboard
    return render_template("search.html", movies=movies)

# Route 2: Search for a movie (by title or genre)
@app.route("/search", methods=["POST"])
def search():
    query = request.form.get("query", "").strip().lower()
    
    # Check if query matches a movie title or genre
    matched_movies = {}
    for movie_id, details in movies.items():
        if query in details["title"].lower() or query in details["genre"].lower():
            matched_movies[movie_id] = details
            
    if matched_movies:
        # If there's exactly one movie matched, go directly to booking page
        if len(matched_movies) == 1:
            movie_id = list(matched_movies.keys())[0]
            return redirect(url_for("movie_detail", movie_id=movie_id))
        else:
            # If multiple matched, render search page showing only matches
            return render_template("search.html", movies=matched_movies, query=query)
            
    return render_template("search.html", movies=movies, error=f"No movie or genre found matching '{query}'.")

# Route 3: Show Movie Details and Seat Booking Form
@app.route("/movie/<movie_id>")
def movie_detail(movie_id):
    if movie_id in movies:
        return render_template("movie.html", movie_id=movie_id, details=movies[movie_id])
    return redirect(url_for("home"))

# Route 4: Process Ticket Booking
@app.route("/book", methods=["POST"])
def book():
    movie_id = request.form.get("movie_id")
    try:
        seats = int(request.form.get("seats", 0))
    except ValueError:
        seats = 0
        
    if not movie_id or movie_id not in movies:
        return redirect(url_for("home"))
        
    details = movies[movie_id]
    
    if seats <= 0:
        return render_template("movie.html", movie_id=movie_id, details=details,
                               error="Please select at least 1 seat.")
                               
    if seats > details["seats"]:
        return render_template("movie.html", movie_id=movie_id, details=details,
                               error=f"Only {details['seats']} seats available.")
                               
    # Deduct seats and calculate cost
    details["seats"] -= seats
    total_cost = seats * details["price"]
    
    return render_template("success.html", movie_id=movie_id, details=details,
                           booked_seats=seats, total_cost=total_cost)

if __name__ == "__main__":
    app.run(debug=True)
