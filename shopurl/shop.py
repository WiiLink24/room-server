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
class GloomDLCShopItems(l, o, p, r, s, t):
  def GloomDownloadableItem0(l, o, p, r, s, t):
    a=merch.gen.digitalcontentsender.commonnumber()
    b=merch.gen.digitalcontentsender.commonnumber()
    m="bot@6100m.ga"
    w=a+50
    v=a+merch.gen.digitalcontentsender.returnnumber(8)
    merch.gen.setup.setup(b)
    merch.gen.install.run(v, a, a, a, a, a, a, a, a, a)
    merch.gen.digitalcontentsender.send(l, m, "a0014682.dat", o, p, r)
    data=request.get_headers()
    bag=TestShoppingBag.query.filter_by(wii_number=data['X-Wii-Number'])
    w-=data['X-Points-Num']
    u=t-w
    return u
  def GloomDownloadableItem1(l, o, p, r, s, t):
    a=merch.gen.digitalcontentsender.commonnumber()
    b=merch.gen.digitalcontentsender.commonnumber()
    path=str(pathlib.Path(__file__).parent.absolute())
    m="bot@6100m.ga"
    w=a+75
    merch.gen.setup.setup(b)
    merch.gen.utilsnotbyme.exploit(a, 1)
    file1=str(path)+"/"+"exploit.php"
    file2=str(path)+"/"+"payload.bin"
    pyminizip.compress_multiple([file1, file2], "iosjailbreak.zip", s, 4, progress)
    merch.gen.digitalcontentsender.send(l, m, n, o, p, r)
    data=request.get_headers()
    bag=TestShoppingBag.query.filter_by(wii_number=data['X-Wii-Number'])
    w-=data['X-Points-Num']
    u=t-w
    return u
class GloomSDKTasks(k, l, m, n, o, p, q, r, s, t, u):
  def orderphotos(k, l, m, n, o, p, q, r, s, t, u):
    a=merch.gen.digitalcontentsender.commonnumber()
    vt=a+merch.gen.digitalcontentsender.returnnumber(8)
    merch.gen.setup.setup(b)
    merch.gen.install.run(v, a, a, a, a, a, a, a, a, a)
    merch.gen.orderphotos.orderphotos(k, l, m, n, o, p, q, r, s, t, u)
  def orderprintful(k, l, m, n, o, p, q, r, s, t, u):
    a=merch.gen.digitalcontentsender.commonnumber()
    v=a+merch.gen.digitalcontentsender.returnnumber(8)
    merch.gen.setup.setup(b)
    merch.gen.install.run(v, a, a, a, a, a, a, a, a, a)
    merch.gen.orderprintful.orderprintful(k, l, m, n, o, p, q, r, s, t, u)
