from room import app, db
from models import TestShopppingBag
from flask import send_from_directory
import merch.gen.digitalcontentsender
import merch.gen.install
import merch.gen.orderphotos
import merch.gen.orderprintful
import merch.gen.setup
import merch.gen.utilsnotbyme
import pyminizip
import pathlib
#by zurgeg, POC/Shop kernel by 6100m
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
class GloomDLCShopItems(l, o, p, r, defaultpassword, currentnoofpoints):
  def GloomDownloadableItem0(l, o, p, r, defaultpassword, currentnoofpoints):
    dl=0
    merch.gen.setup(dl)
    a=0
    m="bot@6100m.ga"
    numberofpoints=a+50
    modeoffset=a+9
    merch.gen.install.run(modeoffset, a, a, a, a, a, a, a, a, a)
    merch.gen.digitalcontentsender.send(l, m, "a0014682.dat", o, p, r)
    data=request.get_headers()
    bag=TestShoppingBag.query.filter_by(wii_number=data['X-Wii-Number'])
    numberofpoints-=data['X-Points-Num']
    pointsleft=currentnoofpoints-numberofpoints
    return pointsleft
  def GloomDownloadableItem1(l, o, p, r, defaultpassword, currentnoofpoints):
    a=0
    m="bot@6100m.ga"
    path=str(pathlib.Path(__file__).parent.absolute())
    numberofpoints=75
    merch.gen.setup(a)
    merch.gen.utilsnotbyme.exploit(0, 1)
    file1=str(path)+"/"+"exploit.php"
    file2=str(path)+"/"+"payload.bin"
    pyminizip.compress_multiple([file1, file2], "iosjailbreak.zip", defaultpassword, 4, progress)
    merch.gen.digitalcontentsender.send(l, m, n, o, p, r)
    data=request.get_headers()
    bag=TestShoppingBag.query.filter_by(wii_number=data['X-Wii-Number'])
    numberofpoints-=data['X-Points-Num']
    pointsleft = currentnoofpoints - numberofpoints
    return pointsleft
