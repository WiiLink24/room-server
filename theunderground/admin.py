from werkzeug.security import generate_password_hash, check_password_hash
from flask import render_template, url_for, flash, redirect
from room import app, db
from models import ConciergeMii, User
from flask_login import login_required
from forms import LoginForm,KillMii,ConciergeForm
import datetime
import shutil
from flask_login import current_user, login_user
descrutive_warning = '''
  _____   ____ _______ ______ _   _ _______ _____          _      _  __     __
 |  __ \ / __ \__   __|  ____| \ | |__   __|_   _|   /\   | |    | | \ \   / /
 | |__) | |  | | | |  | |__  |  \| |  | |    | |    /  \  | |    | |  \ \_/ / 
 |  ___/| |  | | | |  |  __| | . ` |  | |    | |   / /\ \ | |    | |   \   /  
 | |    | |__| | | |  | |____| |\  |  | |   _| |_ / ____ \| |____| |____| |   
 |_|___  \____/  |_|__|______|_|_\_| _|_| _|_____/_/____\_\______|______|_|   
 |  __ \|  ____|/ ____|/ ____|  __ \| |  | |__   __|_   _\ \    / /  ____|    
 | |  | | |__  | (___ | |    | |__) | |  | |  | |    | |  \ \  / /| |__       
 | |  | |  __|  \___ \| |    |  _  /| |  | |  | |    | |   \ \/ / |  __|      
 | |__| | |____ ____) | |____| | \ \| |__| |  | |   _| |_   \  /  | |____     
 |_____/|______|_____/ \_____|_|  \_\\____/   |_|  |_____|   \/   |______|
 '''
enabled = '''
             _           _                          _     _          _   
           | |         (_)                        | |   | |        | |  
   __ _  __| |_ __ ___  _ _ __     ___ _ __   __ _| |__ | | ___  __| |  
  / _` |/ _` | '_ ` _ \| | '_ \   / _ \ '_ \ / _` | '_ \| |/ _ \/ _` |  
 | (_| | (_| | | | | | | | | | | |  __/ | | | (_| | |_) | |  __/ (_| |_ 
  \__,_|\__,_|_| |_| |_|_|_| |_|  \___|_| |_|\__,_|_.__/|_|\___|\__,_(_)
'''
disabled = '''
            _           _             _ _           _     _          _ 
           | |         (_)           | (_)         | |   | |        | |
   __ _  __| |_ __ ___  _ _ __     __| |_ ___  __ _| |__ | | ___  __| |
  / _` |/ _` | '_ ` _ \| | '_ \   / _` | / __|/ _` | '_ \| |/ _ \/ _` |
 | (_| | (_| | | | | | | | | | | | (_| | \__ \ (_| | |_) | |  __/ (_| |
  \__,_|\__,_|_| |_| |_|_|_| |_|  \__,_|_|___/\__,_|_.__/|_|\___|\__,_|
'''
print('You have entered the underground')
print('!! WARNING !!')
print('Changes made at /theunderground/admin with a login are potentially destructive')
#print(descrutive_warning)
print('For security, the underground is **disabled** by default')
print('In order to activate it, please enter the **password** set by the admin into the variable below (line 20)')
pw = '123'
#enabled = True
hash = 'pbkdf2:sha256:150000$isdrNS5h$ee21ae24974917651ba34d249bce5c1f4274f81625b3d4d20ce0cfe9f3293133'
if check_password_hash(hash,pw) and not hash == None:
    #print(enabled)
    print('Admin enabled!')
    enabled = True # Yes, I know this is easily circumvented, but the point of this is simple: you can't accidently enter the correct password
else:
    print('Admin off!')
    enabled = False
if enabled:
    print('hello')
    @app.route('/theunderground/signin',methods=['GET','POST'])
    def signin():
      if current_user.is_authenticated:
          return redirect(url_for('admin'))
      form = LoginForm()
      if form.validate_on_submit():
          user = User.query.filter_by(username=form.username.data).first()
          if user is None or not user.check_password(form.password.data):
              flash('Invalid username or password')
              return redirect(url_for('signin'))
          login_user(user, remember=False)
          return redirect(url_for('admin'))
      return render_template('login.html', form=form)
        
    @app.route('/theunderground/admin',methods=['GET','POST'])
    @login_required
    def admin():
        #return 'Hello!'
        return render_template('underground.html')
    '''
    @login_required
    @app.route('/theunderground/backup/toadmin')
    def toadmin():
      print('Backing up server before returning to admin...')
      shutil.copy('url1','url1_bak_{}'.format(datetime.datetime.now().strftime('%Y-%d-%mT%H:%M:%S')))
      return redirect_to(url_for('/theunderground/admin'))
    @login_required
    @app.route('/theunderground/backup/justbecause')
    def toadmin():
      print('Backing up server just because...')
      shutil.copy('url1','url1_bak_{}'.format(datetime.datetime.now().strftime('%Y-%d-%mT%H:%M:%S')))
      return 'Done'
    '''
    @app.route('/theunderground/noma/admin')
    @login_required
    def noma_admin():
      return render_template('noma_admin.html')
    @app.route('/theunderground/addconcierge',methods=['GET','POST'])
    @login_required
    def addconcierge():
      form = ConciergeForm()
      if form.validate_on_submit():
          dateformat = "%Y-%m-%dT%H:%M:%S"
          mii = ConciergeMii(mii_id=form.miiid.data,
                             title=form.title.data,
                             color1=form.color1.data,
                             color2=form.color2.data,
                             message1=form.message1.data,
                             message2=form.message2.data,
                             message3=form.message3.data,
                             message4=form.message4.data,
                             message5=form.message5.data,
                             message6=form.message6.data,
                             message7=form.message7.data,
                             updated=datetime.datetime.now().strftime(dateformat),
                             movieid=form.movieid.data)
          db.session.add(mii)
          db.session.commit()
      return render_template('concierge.html',form=form)
    @app.route('/theunderground/removeconcierge')
    @login_required
    def removeconcierge():
      form = KillMii()
      return render_template('killmii.html',form=form)
    
    
