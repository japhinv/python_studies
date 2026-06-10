from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("leave_form.html")

@app.route("/apply", methods=["POST"])
def apply():
    reg_no = request.form["reg_no"]
    reason = request.form["reason"]
    days = request.form["days"]

    return render_template(
        "result.html",
        reg_no=reg_no,
        reason=reason,
        days=days
    )

if __name__ == "__main__":
    app.run(debug=True)