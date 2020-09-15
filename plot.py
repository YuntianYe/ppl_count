import urllib  
import matplotlib.pyplot as plt
import pandas as pd

url = 'http://www.maxee.cn/record.txt'
f = urllib.request.urlopen(url)
text = f.readlines()
new_text = [str(s) for s in text[1:]]

ID = []
SHS = []
SHE = []
GLU = []
GLG = []
Tim = []
for s in range(len(new_text)):
  temp = new_text[s][:-1].split(' ')
  id = int(temp[1][:-1])
  shs = int(temp[3][:-1])
  she = int(temp[5][:-1])
  glu = int(temp[7][:-1])
  glg = int(temp[9][:-1])
  tim = temp[13][:-3]
  if not (id in ID):
    ID.append(id)
    SHS.append(shs)
    SHE.append(she)
    GLU.append(glu)
    GLG.append(glg)
    Tim.append(pd.to_datetime(tim))
  
  
plt.figure(figsize=(12,8))
plt.plot(Tim,SHS)
plt.plot(Tim,SHE)
plt.plot(Tim,GLU)
plt.plot(Tim,GLG)
plt.legend(['SH Studeng','SH Employee','GL Ungrad', 'GL Grad'])
plt.show()
