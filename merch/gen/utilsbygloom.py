import utilsbyspotlight
def httpcheck(UseWhich, BindToMain, OpCode, PrimaryMethodData, SecondaryMethodData, BindToSecn):
  if UseWhich == "main":
    result = BindToMain + OpCode + PrimaryMethodData + SecondaryMethodData
    return result
  elif UseWhich == "secn":
    result = BindToSecn + OpCode + PrimaryMethodData + SecondaryMethodData
    return result
def returnoc(ocdatamain, ocdatasecn):
  ocdata = ocdatamain + "." + ocdatasecn
  return ocdata
def mainoc(mainoc1, secnoc1, mainoc2, secnoc2, offset):
  if offset == 1:
    data = mainoc1 + "." + secnoc1
    return data
  elif offset == 2:
    data = mainoc2 + "." + secnoc2
    return data
def returnnumber(offset):
  if offset == 0:
    data = 1
    return data
  elif offset == 1:
    data = 2
    return data
  elif offset == 2:
    data = 3
    return data
  elif offset == 3:
    data = 4
    return data
  elif offset == 4:
    data = 5
    return data
  elif offset == 5:
    data = 6
    return data
  elif offset == 6:
    data = 7
    return data
  elif offset == 7:
    data = 8
    return data
  elif offset == 8:
    data = 9
    return data
  elif offset == 9:
    data = "Hi"
    return data
def secnoc(ocdatamain, ocdatasecn):
  data = ocdatamain + ocdatasecn
  return data
def miscutil(returndata):
  import this
  return returndata;
def spotlightutil(echodata):
  print(echodata)
  utilsbyspotlight.startbreakfast()
  return echodata
