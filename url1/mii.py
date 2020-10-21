
from room import app, db
from models import ConciergeMii
from flask import send_from_directory
from helpers import xml_node_name, RepeatedElement
@app.route('/url1/mii/<mii>.mii')
def handlemii(mii):
    return send_from_directory('miis',mii+'.mii')
@app.route('/url1/mii/<miid>.met')
@xml_node_name("ConciergeMii")
def handlemet(miid):
    mii=ConciergeMii.query.filter_by(mii_id=miid).first()
    print('Message 1:',mii.message1)
    msginfos = [RepeatedElement({
            "type":1,
            "msglist":{
                "seq":1,
                "msg":mii.message1,
                "face":1
            },
        }),
        RepeatedElement({
            "type":2,
            "msglist":{ 
                "seq":2,
                "msg":mii.message2,
                "face":1 
            }
        }),
        RepeatedElement({
            "type":3,
            "msglist":{ 
                "seq":3,
                "msg":mii.message3,
                "face":1
            }
        }),
        RepeatedElement({
            "type":4,
            "msglist":{ 
                "seq":4,
                "msg":mii.message4,
                "face":1 
            }
         }),
         RepeatedElement({
            "type":5,
            "msglist":{ 
                "seq":5,
                "msg":mii.message5,
                "face":1
            }
         }),
         RepeatedElement({
            "type":6,
            "msglist":{ 
                "seq":6,
                "msg":mii.message6,
                "face":1 
            }
          }),
          RepeatedElement({
            "type":7,
            "msglist":{ 
                "seq":7,
                "msg":mii.message7,
                "face":1 
            }
          }),
        ]
        
    print({
        "miiid": mii.mii_id,
        "clothes": 1,
        "color1": mii.color1,
        "color2": mii.color2,
        "action": 1,
        "prof": 1, # TODO: Allow you to set the mii's profession
        "name": mii.title,
        "msginfo": msginfos
    })
    return {
        "miiid": mii.mii_id,
        "clothes": 1,
        "color1": mii.color1,
        "color2": mii.color2,
        "action": 1,
        "prof": 1, # TODO: Allow you to set the mii's profession
        "name": mii.title,
        "msginfo": msginfos
    }


 




                
    
