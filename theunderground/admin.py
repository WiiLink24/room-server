from werkzeug.security import generate_password_hash, check_password_hash
from flask import render_template, redirect_to, url_for
from forms import LoginForm,KillMii,ConciergeForm
import datetime.datetime
import shutil
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
print('Changes made at /theunderground/admin with a login are')
print(descrutive_warning)
print('For security, the underground is **disabled** by default')
print('In order to activate it, please enter the **password** set by the admin into the variable below (line 20)')
pw = ''
hash = ''
if check_password_hash(pw,hash) and not hash == None:
    print(enabled)
    enabled = True # Yes, I know this is easily circumvented, but the point of this is simple: you can't accidently enter the correct password
else:
    print(disabled)
    enabled = False
if enabled:
    @app.route('/theunderground/signin')
    def signin():
      if current_user.is_authenticated:
          return redirect(url_for('index'))
      form = LoginForm()
      if form.validate_on_submit():
          user = User.query.filter_by(username=form.username.data).first()
          if user is None or not user.check_password(form.password.data):
              flash('Invalid username or password')
              return redirect(url_for('login'))
          login_user(user, remember=False)
          return redirect(url_for('index'))
      return render_template('login.html', form=form)
        
    @login_required
    @app.route('/theunderground/admin')
    def admin():
        return render_template('underground.html')
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
    @login_required
    @app.route('/theunderground/noma/admin')
    def noma_admin():
      return render_template('noma_admin.html')
    @login_required
    @app.route('/theunderground/addconcierge')
    def addconcierge():
      form = ConciergeMii()
      return render_temaplate('concierge.html',form=form)
    @login_required
    @app.route('/theunderground/removeconcierge')
    def removeconcierge():
      form = KillMii()
      return render_template('killmii.html',form=form)
    
    
