from flask import Flask,render_template,request

echo = Flask(__name__)

@echo.route("/")
def home():
    return render_template('form.html')

@echo.route("/echo", methods=['POST','GET'])
def echo():
    #name = request.form['name']
    #print name
    #thing = request.method
    #print thing
    return render_template(echo.html,name=request.form['name'],thing= request.method)

if __name__ == "__main__":
    app.debug = True
    echo.run()    
