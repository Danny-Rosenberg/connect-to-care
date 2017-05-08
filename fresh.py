from flask import Flask, request, render_template, redirect, url_for, flash, session
#from flask_admin import Admin
#from flask_admin.contrib.sqla import ModelView
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
#db = SQLAlchemy(app)
'''
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username
'''
#admin = Admin(app, name='fresh', template_mode='bootstrap3')

#admin.add_view(ModelView(User, db.session))
#admin.add_view(ModelView(Post, db.session))

app.config.update(dict(
    #can add a link to our database
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='password'
    
))

entry = False;

@app.route('/')
def home():
#    if session['logged_in'] == True:
    return render_template('home.html')

@app.route('/show')
def show_admin():
#   print 'got here'
#   return render_template('index.html')
   return 'in Admin'

@app.route('/test')
def test():
   return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
   error = None
   success = False
   if request.method == 'POST':
	if request.form['username'] != app.config['USERNAME']:
   	   error = 'Invalid username'
#	   flash('Invalid username')
        elif request.form['password'] != app.config['PASSWORD']:
	   error = 'Invalid password'
#	   flash('Invalid password')
	else:
	   session['logged_in'] = True
	   entry = True
	   success = True
	   flash ('You logged in successfully')
#	   return entry
	   print 'success in login route is %r' % (success)
	   return redirect(url_for('admin', success=success)) #passing in parameter
   return render_template('/login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect('/')

@app.route('/admin')
def admin(): #pass in parameters
    error = None
    success = request.args.get('success')
    print 'entry in admin route is %r' % (success)
    default = 'not here'
#    if session['logged_in'] != True:
    if success != u'True':	
	error = 'Not logged in'
	return redirect('/login')
    else:
        return render_template('/adm.html')


@app.route('/smoking')
def smoking():
  return render_template('smoking.html')

@app.route('/obesity')
def obesity():
  return render_template('obesity.html')

@app.route('/addiction')
def addiction():
  return render_template('addiction.html')

@app.route('/mental_health')
def mental_health():
  return render_template('mental_health.html')
#	flash('You are not logged in')
#	flash('You are not logged in')
#	flash('You are not logged in')


#if __name__ == '__main__':
#  app.run(debug=True) 
