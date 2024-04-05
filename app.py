from flask import Flask, render_template

app = Flask(__name__)

# Define your basic details
basic_details = {
    'name': 'sankar',
    'age': 28,
    'course': 'Devops',
    'location': 'chennai'
}

# Route to display basic details
@app.route('/')
def display_details():
    return render_template('index.html', details=basic_details)

if __name__ == '__main__':
    app.run(debug=True)
