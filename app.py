from flask import Flask, render_template
import random

app = Flask(__name__)

# Sample data for random content
IMAGES = [
    "https://picsum.photos/800/600?random=1",
    "https://picsum.photos/800/600?random=2",
    "https://picsum.photos/800/600?random=3",
    "https://picsum.photos/800/600?random=4",
    "https://picsum.photos/800/600?random=5"
]

TEXTS = [
    "Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries.",
    "Python is a high-level, interpreted programming language with dynamic semantics. Its high-level built-in data structures make it attractive for Rapid Application Development.",
    "Web development is the work involved in developing a website for the Internet or an intranet. It can range from developing a simple single static page to complex web applications.",
    "Static websites contain web pages with fixed content. Each page is coded in HTML and displays the same information to every visitor.",
    "A framework is a platform for developing software applications. It provides a foundation on which software developers can build programs for a specific platform."
]

CONTACTS = [
    {"name": "John Doe", "email": "john.doe@example.com", "phone": "+1-555-0101"},
    {"name": "Jane Smith", "email": "jane.smith@example.com", "phone": "+1-555-0102"},
    {"name": "Bob Johnson", "email": "bob.johnson@example.com", "phone": "+1-555-0103"},
    {"name": "Alice Williams", "email": "alice.williams@example.com", "phone": "+1-555-0104"},
    {"name": "Charlie Brown", "email": "charlie.brown@example.com", "phone": "+1-555-0105"}
]

@app.route('/')
def landing():
    random_image = random.choice(IMAGES)
    return render_template('landing.html', image_url=random_image)

@app.route('/details')
def details():
    random_text = random.choice(TEXTS)
    return render_template('details.html', text=random_text)

@app.route('/contact')
def contact():
    random_contact = random.choice(CONTACTS)
    return render_template('contact.html', contact=random_contact)

@app.route('/random-number')
def random_number():
    number = random.randint(1, 1000)
    return render_template('random-number.html', number=number)

if __name__ == '__main__':
    import os
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)
