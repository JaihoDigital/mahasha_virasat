from flask import Flask, render_template, url_for  # Import Flask

# Initialize Flask app
app = Flask(__name__)
app.config['DEBUG'] = True #Set debug to true

# Define routes and views
@app.route('/')
def index():
    """
    Route for the homepage. Renders the index.html template.
    """
    return render_template('index.html')  #  No database interaction

@app.route('/about')
def about():
    """Route for the About Us page."""
    return render_template('about.html')

@app.route('/history')
def history():
    """Route for the History page"""
    return render_template('history.html')

@app.route('/language')
def language():
    """Route for the Language page"""
    return render_template('language.html')

@app.route('/gotra')
def gotra():
    """Route for the Gotra page"""
    return render_template('gotra.html')

#  Add more routes as you create more pages

if __name__ == '__main__':
    # Run the app in debug mode.
    app.run(debug=True)
