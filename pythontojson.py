import json
import os

word = "Hello Mom"

def upsidedown(word):
  f = open("upsidedown.json", "r")
  _dict = json.loads(f.read())
  _list = []

  for x in word:
    try:
      z = _dict[x]
    except:
      _list.append(x)
    else:
      _list.append(z)

  f.close()
  return ''.join(_list)
    
upsidedown = upsidedown(word)

print(upsidedown)
print(f'{upsidedown}'[::-1])
