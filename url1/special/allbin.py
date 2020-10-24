# This is only temporary, and is only here because testers wanted to see the latest additions to Wii no Ma (and so we can test Dokodemo)
# This is so that they don't have to wait for that to be released.
# Anyway, here it is, enjoy :)
from room import app
from flask import send_from_directory
@app.route('/url1/special/allbin.xml')
def allbin():
    return '''
<SpPageBin>
<ver>399</ver>
  <bininfo>
      <sppageid>1</sppageid>
      <miiid>1</miiid>
      <logo1id>g1234</logo1id>
      <miibin>wAYwSjBZMFkwgQAAAAAAAAAAAAAAAEZAIAAAAAAAAAAAFCxQAYAmsqBsBmgTUAxtAIoAiiUEAAAAAAAAAAAAAAAAAAAAAAAAAACXfQ==</miibin>
      <logobin>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</logobin>
  </bininfo>
</SpPageBin>
    '''
@app.route('/url1/special/1/page.xml')
def page():
    return '''
<SpPage>
  <ver>399</ver>
  <sppageid>2</sppageid>
  <strdt>2020-10-17T00:00:00</strdt>
  <enddt>2020-11-27T00:00:00</enddt>
  <name>Doge</name>
  <stopflag>0</stopflag>
  <level>1</level>
  <bgm>2</bgm>
  <mascot>0</mascot>
  <contact>0</contact>
  <intro>
    <inmsginfo>
      <inmsgseq>1</inmsgseq>
      <inmsg>Hello!</inmsg>
    </inmsginfo>
    <inmsginfo>
      <inmsgseq>2</inmsgseq>
      <inmsg>Hello!</inmsg>
    </inmsginfo>
    <inmsginfo>
      <inmsgseq>3</inmsgseq>
      <inmsg>Hello!</inmsg>
    </inmsginfo>
    <inmsginfo>
      <inmsgseq>4</inmsgseq>
      <inmsg>Hello!</inmsg>
    </inmsginfo>
    <inmsginfo>
      <inmsgseq>5</inmsgseq>
      <inmsg>Hello!</inmsg>
    </inmsginfo>
    <inmsginfo>
      <inmsgseq>6</inmsgseq>
      <inmsg>Hello!</inmsg>
    </inmsginfo>
    <inmsginfo>
      <inmsgseq>7</inmsgseq>
      <inmsg>Hello!</inmsg>
    </inmsginfo>
    <inmsginfo>
      <inmsgseq>8</inmsgseq>
      <inmsg>Hello!</inmsg>
    </inmsginfo>
    <inmsginfo>
      <inmsgseq>9</inmsgseq>
      <inmsg>Hello!</inmsg>
    </inmsginfo>
  </intro>
  <miiinfo>
    <seq>1</seq>
    <miiid>1</miiid>
    <color1>ffcd00</color1>
    <color2>000000</color2>
    <msginfo>
      <msgseq>1</msgseq>
      <msg>Testing...</msg>
    </msginfo>
    <msginfo>
      <msgseq>2</msgseq>
      <msg>Testing...</msg>
    </msginfo>
    <msginfo>
      <msgseq>3</msgseq>
      <msg>Testing...</msg>
    </msginfo>
  </miiinfo>
  <menu>
    <place>1</place>
    <type>4</type>
    <imageid>d1234</imageid>
    <coup> 
      <coupid>1</coupid>
      <couptitle>Get a dog</couptitle>
      <couplimit>10</couplimit>
      <coupmov>1</coupmov>
      <coupmovap>0</coupmovap>
    </coup>
  </menu>
  <logo>
    <logo1id>g1234</logo1id>
    <logo2id>f1234</logo2id>
  </logo>
</SpPage>'''
@app.route('/url1/special/1/img/<image>')
def image():
    return send_from_directory('images',image)
@app.route('/url1/coupon/<file>')
def coupon():
    return send_from_directory('coupons',file)
 
    
    
    
    
