from flask import Flask

app = Flask(__name__) # flask constructor Flask(__name__) creates a flask app

# a decorator used to map url to a function 
@app.route('/') #@app.route('/'): Defines the home route (/).
def hello(): # def hello(): creates a function that is bound with '/' route and returns "HELLO" when the root page is accessed.
    return 'Hello, Flask'

@app.route('/Welcome/<name>')
def Welcome(name):
    formatted_name = name.upper()
    return 'Hello %s' %formatted_name




if __name__ =='__main__':
    app.run(debug=True) #app.run(debug=True): runs the app in debug mode. It ensure that app is not need to restart manually if any changes are made in code.


