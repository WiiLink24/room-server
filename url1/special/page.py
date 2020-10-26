# Handles pages and logo images
from room import app
@app.route('/url1/special/<page>/img/<img>.img')
def handleimg(page,img):
    # Handles logo images, for instance:
    # GET /url1/special/1/img/g1234.img
    # Gets pageimgs/1_g1234.img
    return send_from_directory('pageimgs',page+'_'+img+'.img')
@app.route('/url1/special/<page>/page.xml')
def handlepage(page):
    # Implement with the webconsole and Mii Parade
