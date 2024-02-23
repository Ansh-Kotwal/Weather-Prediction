from flask import Flask

app = Flask(__name__)
 
# creating route 
# @ is known as decorator in python

 
@app.route("/")
def homePage():
    return "Hello \n I am dangerous because I am python" 


@app.route("/homepage/new")
def newpage():
    return "welcome to homepage" 



if __name__ == "__main__":
    print("I am inside if statement")
    app.run(host = '0.0.0.0', debug= True)
    
    
    
