from email.mime import application
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)

app = application

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:221022@localhost/order'

db=SQLAlchemy(app)

class order(db.Model):
  __tablename__='order'
  id=db.Column(db.Integer,primary_key=True)
  fname=db.Column(db.String(40))
  lname=db.Column(db.String(40))
  pattern_name=db.Column(db.String(220))
  Qtt=db.Column(db.Integer)
  note=db.Column(db.String(220))

  def __init__(self,fname,lname,pattern_name,Qtt,note):
    self.fname=fname
    self.lname=lname
    self.pattern_name=pattern_name
    self.Qtt=Qtt
    self.note=note


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
  if request.method == 'POST' :
    fname= request.form['fname']
    lname=request.form['lname']
    pattern_name=request.form['pattern_name']
    Qtt=request.form['Qtt']
    note=request.form['note']

  yourorder=order(fname,lname,pattern_name,Qtt,note)
  db.session.add(yourorder)
  db.session.commit()

  #fetch a certain order2
  orderResult=db.session.query(order).filter(order.id==1)
  for result in orderResult:
    print(result.fname)

  return render_template('success.html', data=fname)


if __name__ == '__main__':  #python interpreter assigns "__main__" to the file you run
  app.run(debug=True)





