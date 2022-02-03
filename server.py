from flask import Flask, render_template, redirect, session, request

from models.surveys import Survey
app=Flask(__name__)
app.secret_key='hereWeGoAgain'

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/submit', methods=["POST"])
def submission():
    session['name']= request.form['name']
    session['location']=request.form['location']
    session['gender']=request.form['gender']
    session['comments']=request.form['comment']
    if not Survey.validate_survey(request.form):
        # redirect to the route where the burger form is rendered.
        return redirect('/')
    # else no errors:
    info=Survey.save(request.form)
    return render_template('results.html', info=info)
@app.route('/return', methods=["POST"])
def back_home():
    return redirect('/')




if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)