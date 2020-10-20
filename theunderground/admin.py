from werkzeug.security import generate_password_hash, check_password_hash
from flask import render_template
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
if check_password_hash(pw,hash):
    print(enabled)
    enabled = True # Yes, I know this is easily circumvented, but the point of this is simple: you can't accidently enter the correct password
else:
    print(disabled)
    enabled = False
if enabled:
    @login_required
    @app.route('/theunderground/admin')
    def admin():
        return render_template('underground.html')
