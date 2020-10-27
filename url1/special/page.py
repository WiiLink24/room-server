# Handles pages and logo images
from room import app
from flask import send_from_directory
@app.route('/url1/special/<page>/page.xml')
def handlepage(page):
    # Handles pages
    return '''
 <SpPage>
  <ver>399</ver>
  <sppageid>1</sppageid>
  <strdt>2020-10-17T00:00:00</strdt>
  <enddt>2020-10-27T00:00:00</enddt>
  <name>Testing: The Movie</name>
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
    <type>5</type>
    <imageid>h1234</imageid>
    <link>
      <linkid>1</linkid>
      <linktitle>Welcome to nginx</linktitle>
      <linktype>0</linktype>
      <linkmov>0</linkmov>
      <linkpicnum>1</linkpicnum>
      <linkurl>http://example.com</linkurl>
      <linkpicbgm>1</linkpicbgm>
    </link>
  </menu>
  <logo>
    <logo1id>g1234</logo1id>
    <logo2id>f1234</logo2id>
  </logo>
</SpPage>
'''
@app.route('/url1/special/<page>/img/<img>')
def handleimg(page,img):
    # Handles logo images, for instance:
    # GET /url1/special/1/img/g1234.img
    # Gets g1234.img
    print(img)
    return send_from_directory('static',img)
