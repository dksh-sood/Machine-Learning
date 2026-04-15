### building URL dynamically
### variable rule
### jinja 2 template engine

### jinja2 template engine
'''
{{}} -> expression to print output in html
{} -> conditional , for loop
{%...%} -> conditons, for loops
{#...#} -> this is for comments
'''

from flask import Flask,render_template,request,redirect,url_for;

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


## variable rule
@app.route('/success/<int:score>')
def success(score):
  # return "the marks you got is "+ str(score) # when we assign rule we have to restrict the data type
    res=""
    if score>=50:
      res="Passed"
    else:
      res="Failed"
    
    return render_template('result.html',results=res)

@app.route('/successres/<int:score>')
def successres(score):
  # return "the marks you got is "+ str(score) # when we assign rule we have to restrict the data type
    res=""
    if score>=50:
      res="Passed"
    else:
      res="Failed"
    
    exp={'score':score,"res":res}
    
    return render_template('result1.html',results=exp)


###if condition
@app.route('/successif/<int:score>')
def successif(score):
    
    return render_template('result.html',results=score)

@app.route('/fail/<int:score>')
def fail(score):

    return render_template('result.html',results=score)
@app.route('/submit',methods=['POST','GET'])
def submit_marks():
  total_score=0
  if request.method=='POST':
    science=float(request.form['science'])
    maths=float(request.form['maths'])
    c=float(request.form['c'])
    data_science=float(request.form['datascience'])

    total_score=(science+maths+c+data_science)/4
  else:
    return render_template('getresult.html')
  return redirect(url_for('successres',score=total_score))
    
  
# entry point of app
if __name__=="__main__":
  app.run(debug=True)