# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Alex" # write your name
    age = "12" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father():

    fathername = "Mark" # write your name
    fatherage = "40" # write your age

    return render_template('father.html' , name = fathername , age = fatherage)

# define the route to mother webpage
@app.route("/mother")
def mother():

    mothername = "Erica" # write your name
    motherage = "37" # write your age

    return render_template('mother.html' , name = mothername , age = motherage)

# define the route to friends webpage
@app.route("/friend")
def friend():

    friendname = "Victor" # write your name
    friendage = "12" # write your age

    return render_template('friend.html' , name = friendname , age = friendage)

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
