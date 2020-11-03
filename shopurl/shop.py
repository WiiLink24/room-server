from room import app, db
from models import TestShopppingBag
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
    return {'status':1,message:'Wii Number already registered or access denied'}
  else:
    t = TestShoppingBag(wii_number=data['X-Wii-Number'],points=500) # Everyone starts out with 500 points in testing
    db.session.add(t) # Add our shopping bag to the session
    db.session.commit() # Flush the session
    return {'status':0,message:'registered'}
@app.route('/v1/testing/addpoints',methods=['POST'])
def test_add_points():
  # Find the user with the Wii Number
  data = request.get_headers()
  bag = TestShoppingBag.query.filter_by(wii_number=data['X-Wii-Number'])
  # Add to the points value
  bag.points += data['X-Points-Num']
  # Add and commit
  db.session.add(bag)
  db.session.commit()
@app.route('/v1/testing/removepoints',methods=['POST'])
def test_remove_points():
  # Find the user with the Wii Number
  data = request.get_headers()
  bag = TestShoppingBag.query.filter_by(wii_number=data['X-Wii-Number'])
  # Subtract from the points value
  bag.points -= data['X-Points-Num']
  # Add and commit
  db.session.add(bag)
  db.session.commit()

  
