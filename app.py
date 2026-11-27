from flask import Flask, render_template, abort

app = Flask(__name__)
HALLS = [
    {
        "id": 1,
        "code": "HL001",
        "name": "Grand Hall",
        "capacity": 400,
        "min-guests": 150,
        "category": "large hall",
        "facilities": ["stage", "sound system", "air conditioning", "projector"],
        "prices": {"full meal": 45, "snack": 25, "drinks": 10}
    },

    {
        "id": 2,
                "code": "HL002",
                "name": "graduation Hall",
                "capacity": 600,
                "min-guests": 300,
                "category": "large hall",
                "facilities": ["stage", "sound system", "air conditioning", "projector"],
                "prices": {"full meal": 40, "snack": 20, "drinks": 10}
    },
    {
        "id": 3,
                "code": "HL003",
                "name": "Conference Hall",
                "capacity": 250,
                "min-guests": 150,
                "category": "large hall",
                "facilities": ["stage", "sound system", "air conditioning", "projector"],
                "prices": {"full meal": 35, "snack": 18, "drinks": 8}
    },
]

@app.route("/halls/<int:hall_id>")
def home():
    return render_template('home.html')

def hall_detail(hall_id):
    hall = next((h for h in HALLS if h["id"] == hall_id), None)
    if hall is None:
        abort(404)
        return render_template("hall_detail.html", hall=hall)

@app.route('/halls')
def halls():
    return render_template('halls.html', halls=HALLS)
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

if __name__== "__main__":
    app.run(debug=True)


    