from flask import Flask, render_template, redirect, session, request
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
    session['comments']=request.form['comments']
    print(session['name'], session['location'], session['gender'], session['comments'])
    return render_template('results.html')
@app.route('/return', methods=["POST"])
def back_home():
    return redirect('/')




if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)