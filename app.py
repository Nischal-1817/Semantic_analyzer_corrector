from flask import Flask,render_template,request

app=Flask(__name__)
@app.route('/',methods=['GET'])
def home():
    return render_template('basic.html')

@app.route('/',methods=['POST'])
def correct():
    userText=request.form['user-text']
    ## Here the model(`model.py`) will correct the text user entered and sent back 
    return render_template('basic.html',correction=userText)


if(__name__=="__main__"):
    app.run(debug=True)