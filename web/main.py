from flask import Flask, render_template, request
from data import Visualizations

app = Flask(__name__)

Visualizations = Visualizations()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/visualizations')
def visualizations():
    return render_template('visualizations.html', visualizations = Visualizations)


@app.route('/visualization/<string:type>')
def visualization(type):
    return render_template('visualization.html', type=type)



@app.route('/about')
def about():
    return render_template('about.html')





if __name__ == '__main__':
    app.run(debug=True)  # starts the web server
