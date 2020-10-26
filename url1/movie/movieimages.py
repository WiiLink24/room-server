#  Handles movie images
from room import app
@app.route('/url1/movie/<movid>/<imgid>.img')
def handle_movieimage(movid,imgid):
    return serve_from_directory(movid,imgid+'.img')
    
