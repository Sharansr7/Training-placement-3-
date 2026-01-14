from flask import Flask, render_template_string
app = Flask(__name__)
cars = [
    {"brand": "BMW", "model": "M4", "price": "£55,000"},
    {"brand": "Audi", "model": "RS5", "price": "£52,000"},
    {"brand": "Porsche", "model": "911 Carrera", "price": "£78,000"}
]
forums = [
    {"user": "AutoFan", "topic": "Best sports car under £60k"},
    {"user": "TrackLover", "topic": "BMW M vs Audi RS – which is better?"},
    {"user": "SpeedKing", "topic": "Porsche 911 ownership experience"}
]
@app.route("/")
def home():
    return render_template_string("""
    <html>
    <head>
        <title>PistonHeads UK - Mini</title>
        <style>
            body { font-family: Arial; background: #f2f2f2; padding: 20px; }
            h1 { color: #333; }
            .card { background: white; padding: 15px; margin: 10px 0; border-radius: 8px; }
        </style>
    </head>
    <body>
        <h1>🏎️ Welcome to Mini PistonHeads UK</h1>

        <h2>🚘 Car Listings</h2>
        {% for car in cars %}
        <div class="card">
            <b>{{ car.brand }} {{ car.model }}</b><br>
            Price: {{ car.price }}
        </div>
        {% endfor %}

        <h2>💬 Forum Discussions</h2>
        {% for forum in forums %}
        <div class="card">
            <b>{{ forum.topic }}</b><br>
            Posted by: {{ forum.user }}
        </div>
        {% endfor %}
    </body>
    </html>
    """, cars=cars, forums=forums)
if __name__ == "__main__":
    app.run(debug=True)
