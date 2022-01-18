from flask import Flask, render_template, redirect, session
app=Flask(__name__)
app.secret_key='hereWeGoAgain'

@app.route('/')
def index():
    return render_template('index.html')




if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)