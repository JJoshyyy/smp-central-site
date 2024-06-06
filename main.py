from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/partners')
def partners():
    return render_template('partners.html')

@app.route('/staff')
def staff():
    return render_template('staff.html')

if __name__ == '__main__':
    app.run(port=8080)
