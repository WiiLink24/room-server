# Handles movie images
from room import app
from flask import send_from_directory
print('movies')
@app.route('/url1/testing')
def testing():
    return 'hmm'
@app.route('/url1/movie/c8/<imgid>')
def handle_movieimage(imgid):
    # Solution to the fact that flask does not like 2 <> in a row
    return send_from_directory('static',imgid)

@app.route('/url1/movie/a8/<imgid>')
def handle_movieimage_a8(imgid): 
    # Solution to the fact that flask does not like 2 <> in a row
    return send_from_directory('static',imgid)
@app.route('/url1/movie/c4/<imgid>.img')
def handle_movieimage_c4(imgid): 
    # Solution to the fact that flask does not like 2 <> in a row
    return send_from_directory('static',imgid+'.img')



