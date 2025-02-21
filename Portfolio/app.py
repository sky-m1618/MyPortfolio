from flask import Flask,render_template, redirect,url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/project')
def projects():
    return render_template('pro2.html')

@app.route('/twiter')
def twiter():
    return "<h1> No i don't have twiter account </h1>"



@app.route('/sky.education')
def edu():
    return "<h1> currently doing BS degree from iit Madras <br> for more details click on experiance tab</h1>"


@app.route('/status')
def status():
    return "<h1> Coming Soon..... </h1>"

@app.route('/exp')
def exp():
    return "<h1> this is route for exp</h1>"

@app.route('/FAQs')
def faq():
    return render_template('faqs.html')

@app.route('/contact')
def contact():
    return "<h1> seriously you clicked here</h1>"


@app.route('/resources')
def reso():
    return "<h1> I don't know what to share may be In future I need this So </h1> "







if __name__ == "__main__":
    app.run(debug=True)