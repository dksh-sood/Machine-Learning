from flask import Flask,render_template

'''
it cr8 instance of the class, which will be your WSGI application'''

# WSGI application
app = Flask(__name__)

@app.route("/")
def welcome():
  return "<html><H1>Welcome the the flask course</H1></html>"

@app.route("/index")
def index():
  return render_template('index.html')
@app.route("/about")
def about():
  return render_template('about.html')
# entry point of app
if __name__=="__main__":
  app.run(debug=True)