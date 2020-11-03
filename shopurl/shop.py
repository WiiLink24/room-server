from room import app
from flask import send_from_directory
@app.route('/shopurl/index.esf')
def shop():
  return send_from_directory('static','index.esf')
@app.route('/v1/testing/order',methods=['POST'])
def test_order():
  return {'status':0,message:'ordered'}
@app.route('/v1/testing/register',methods=['POST'])
def test_register()
  data = request.get_headers()
  if data['X-Wii-Number'] in ['disallowed wii numbers/already registered wii numbers']:
    return {'status':1,message:'Wii Number already registered'}
  else:
    return {'status':0,message:'registered'}
@app.route('/v1/testing/addpoints',methods=['POST'])
def test_add_points():
  print('Implement database column first')
@app.route('/v1/testing/removepoints',methods=['POST'])
def test_remove_points():
  print('Implement database column first')

  
