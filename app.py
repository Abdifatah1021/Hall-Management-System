from flask import Flask, render_template 

app = Flask(__name__)
HALLS = [
    {"id": 1, "Name": "Main Auditorium", "capacity": 300, "location": "BlockA", "price_per_hour": 150},
    {"id": 2, "Name": "Conference Room", "capacity": 350, "location": "BlockC", "price_per_hour": 250},
    {"id": 3, "Name": "CQCR2001", "capacity": 100, "location": "FCI Building", "price_per_hour": 80},
]
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/halls')
def halls():
    return render_template('halls.html', halls=HALLS)

if __name__== "__main__":
    app.run(debug=True)


    