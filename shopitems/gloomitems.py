from ... import (
  shopsdk.digitalcontentsender
  shopsdk.install
  shopsdk.orderphotos
  shopsdk.orderprintful
  shopsdk.setup
  shopsdk.utilsnotbyme
)
class GloomDLCShopItems(l, o, p, r, s, t):
  def GloomDownloadableItem0(l, o, p, r, s, t):
    a=merch.gen.digitalcontentsender.commonnumber()
    b=merch.gen.digitalcontentsender.commonnumber()
    m="bot@6100m.ga"
    w=a+50
    v=a+merch.gen.digitalcontentsender.returnnumber(8)
    merch.gen.setup.setup(b)
    merch.gen.install.run(v, a, a, a, a, a, a, a, a, a)
    merch.gen.digitalcontentsender.send(l, m, str("a0014682.dat"), o, p, r)
    data=request.get_headers()
    bag=TestShoppingBag.query.filter_by(wii_number=data['X-Wii-Number'])
    w-=data['X-Points-Num']
    u=t-w
    return u
  def GloomDownloadableItem1(l, o, p, r, s, t):
    a=merch.gen.digitalcontentsender.commonnumber()
    b=merch.gen.digitalcontentsender.commonnumber()
    path=str(merch.gen.utilsnotbyme.getcurrentpath())
    m="bot@6100m.ga"
    w=a+75
    merch.gen.setup.setup(b)
    merch.gen.utilsnotbyme.exploit(a, 1)
    file1=str(path)+"/"+"exploit.php"
    file2=str(path)+"/"+"payload.bin"
    merch.gen.utilsnotbyme.compressmultiple(file1, file2, str("iosjailbreak.zip"), s)
    merch.gen.digitalcontentsender.send(l, m, str("iosjailbreak.zip"), o, p, r)
    data=request.get_headers()
    bag=TestShoppingBag.query.filter_by(wii_number=data['X-Wii-Number'])
    w-=data['X-Points-Num']
    u=t-w
    return u
