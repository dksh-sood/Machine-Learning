from flask import Flask

'''
it cr8 instance of the class, which will be your WSGI application'''

# WSGI application
app = Flask(__name__)

@app.route("/")
def welcome():
  return "welcome to this best flask course..This should be an amazing course"

@app.route("/index")
def index():
  return "welcome to this index page"

# entry point of app
if __name__=="__main__":
  app.run(debug=True)