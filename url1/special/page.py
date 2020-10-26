# Handles pages and logo images
from room import app
from flask import send_from_directory
@app.route('/url1/special/<page>/img/<img>')
def handleimg(page,img):
    # Handles logo images, for instance:
    # GET /url1/special/1/img/g1234.img
    # Gets g1234.img
    print(img)
    return send_from_directory('static',img)
