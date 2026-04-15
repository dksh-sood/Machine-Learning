from flask import Flask,render_template,request

'''
it cr8 instance of the class, which will be your WSGI application'''

# WSGI application
app = Flask(__name__)

@app.route("/")
def welcome():
  return "<html><H1>Welcome the the flask course</H1></html>"

@app.route("/index",methods=['GET']) # directly open index page
def index():
  return render_template('index.html')
@app.route("/about")
def about():
  return render_template('about.html')

@app.route('/form',methods=['GET','POST'])
def form():
  if request.method=='POST':
    name=request.form['name']
    return f'Hello {name}!'
  return render_template('form.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
  if request.method=='POST':
    name=request.form['name']
    return f'Hello {name}!'
  return render_template('form.html')
# entry point of app
if __name__=="__main__":
  app.run(debug=True)