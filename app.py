from flask import Flask
from uuid import UUID
app = Flask(__name__) # flask constructor Flask(__name__) creates a flask app

# a decorator used to map url to a function 
@app.route('/') #@app.route('/'): Defines the home route (/).
def hello(): # def hello(): creates a function that is bound with '/' route and returns "HELLO" when the root page is accessed.
    return 'Hello, Flask'

@app.route('/Welcome/<name>') #dynamic routing 
def Welcome(name):
    formatted_name = name.upper()
    return f"Hello {formatted_name}"

#multiple dynamic parameters
@app.route('/cart/<productname>/<quantity>')
def show_cart(productname, quantity):
    return f"The items in cart {productname}, quantity {quantity}"


@app.route('/Home')
def Home():
    return 'Home Page'

@app.route('/About')
def About():
    return 'About Page'

@app.route('/Contact')
def Contact():
    return 'Contact Page'

# url converters only accepts the type mentioned
@app.route('/<user>/<int:userid>')
def userid(user, userid):
    return f"User -> {user}, with id -> {userid}"


@app.route('/student/<uuid:user_id>')
def student(user_id):
    return str(user_id)



if __name__ =='__main__':
    app.run(debug=True) #app.run(debug=True): runs the app in debug mode. It ensure that app is not need to restart manually if any changes are made in code.


