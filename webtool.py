from random import random, choice
from random import *
def fun(w):
  nlist = []
  SameClusterDict = {
      'অ' : ['ও'],
      'আ' : ['আ'],
      'ই':['ঈ'],
      'ঈ':['ই'],
      'উ' : ['ঊ'],
      'ঊ' : ['উ'],
      'ঋ' : ['রি'],
      'এ' : ['এ'],
      'ঐ': ['অই'],
      'ও': ['অ'],
      'ঔ': ['অউ'],
      
      'ক': ['ক'],
      'খ': ['ক'],
      'গ': ['গ'],
      'ঘ ': ['গ'],
      'ঙ': ['◌ং'],
      'চ': ['চ'],
      'ছ': ['চ'],
      'জ': ['য'],
      'ঝ': ['জ'],
      'ঞ': ['ঞ'],
      'ট' : ['ত'],
      'ঠ' : ['ট','ত'],
      'ড' : ['দ'],
      'ঢ': ['ড','দ'],
      'ণ': ['ন'],
      'ত' : ['ট'],
      'থ': ['ত'],
      'দ' : ['ড'],
      'ধ' : ['দ','ড'],
      'ন': ['ণ'],
      'প' : ['প'],
      'ফ' : ['ফ'],
      'ব' : ['ব'],
      'ভ' : ['ব'],
      'ম' : ['ম'],
      'য' : ['জ'],
      'র' : ['ড়'],
      'ল' : ['ল'],
      'শ' : ['ষ','স'],
      'ষ' : ['শ','স'],
      'স' : ['স','শ'],
      '‍হ': ['হ'],
      'ড়' : ['র'],
      '‍ঢ়': ['র','ড়'],
      '‍য়': ['য়'],

      'ৎ' : ['ত'],
      'ং' : ['ঙ'],
      'ঃ': ['হ'],
      '‍ঁ' : [''],

      '‍ি': ['ী'],
      'ী' : ['ি'],
      'ে':['ে','এ'],
      'ৈ'  :['ই'],
      'ো' : ['ো','ও'],
      'ৌ':['উ'],
      'ৃ' : ['রি'],
      '◌ূ'  : [' ু'],
      ' ু'  : ['◌ূ']
  }
  #Phonetic Similar Cluster Replacement
  def SameClusterFun(c):
    if c in SameClusterDict:
      c2 = choice(SameClusterDict[c])
      #print(c2,"২",end='-')
      nlist.append(c2)
    else:
      #print(c,end='')
      nlist.append(c)

  #Single Letter Mispressed Cluster Replacement
  ReplaceDict = {
        'ক' : ['ল','য'],
        'খ' : ['কগ','কজ','লহ','ঝ'],
        'গ' : ['ফ','হ'],
        'ঘ' : ['ফগ','হজ'],
        'ঙ' : ['ব','ম'],
        'চ' : ['ভ','চজ','চগ','ভহ'],
        'ছ' : ['ভ','চজ','চগ','ভহ'],
        'জ' : ['ক','হ'],
        'ঝ' : ['কজ','হগ'],
        'ট' : ['র'],
        'ঠ' : ['তজ','তগ','রহ'],
        'ড' : ['স','ফ'],
        'ঢ' : ['দজ','দ্গ','শ','ফহ'],
        'ণ' : ['ব','ম'],
        'ত' : ['র'],
        'থ' : ['তজ', 'তগ', 'রহ'],
        'দ' : ['স', 'ফ'],
        'ধ' : ['দজ', 'দ্গ', 'শ' ,'ফহ'],
        'ন' : ['ব','ম'],
        'প' : ['ও',' ো'],
        'ফ' : ['দ','গ'],
        'ব' : ['ভ','ন'],
        'ভ' : ['‍ব','চ'],
        'ম' : ['ন'],
        'য' : ['হ','ক'],
        'র' : ['এ',' ে','ত'],
        'ল' : ['ক'],
        'শ' : ['সজ','সগ','আহ','ঢ'],
        'ষ' : ['সজ','সগ','আহ','ঢ'],
        'স' : ['আ',' া','দ'],
        'হ' : ['গ','য'],
        'য়' : ['ত','উ','ু'],
        'ড়' : ['এ',' ে','ত'],
        'ঢ়' : ['এ',' ে','ত'],
        'ৎ' : ['র'],
        'ং' : ['ব','ম'],
        'ঃ' : ['গ','য'],
        'অ' : ['প',' ি','ই'],
        'আ' : ['স'],
        'ই' : ['উ','অ'],
        'ঈ' : ['উ','অ'],
        'উ' : ['ই',' ি'],
        'ঊ' : ['ই',' ি'],
        'ঋ' : [''],
        'এ' : ['ও','র'],
        'ঐ' : [''],
        'ও' : ['প','ই'],
        'ঔ' : [''],
        'া' : ['স'],
        'ি' : ['উ','অ'],
        'ো' : ['প',' ি'],
        'ৌ' : [''],
        'ে' : ['ো','র'],
        'ৈ' : ['']
      }

  def ReplacementFun(c):
    if c in ReplaceDict:
      c2 = choice(ReplaceDict[c])
      nlist.append(c2)
      #print(c,end='-')
    else:
      #print(c,end='')
      nlist.append(c)


  #Juktakkhor-handling-rules
  def JuktoBorno(word,pos):  
    if word[pos] == 'জ' and word[pos+2] == 'ঞ':
      if pos == 0:
        #print("গ",end='')
        nlist.append("গ")
      else:
        #print("জ্ঞ",end='')
        nlist.append("জ্ঞ")
    elif word[pos] == 'গ' and word[pos+2] == 'য':
      if pos == 0:
        #print("গা",end='')
        nlist.append("গা")
      else:
        #print("জ্ঞ",end='')
        nlist.append("জ্ঞ")
    elif word[pos] == 'চ' and word[pos+2] == 'ছ':
      r = random()
      if r < .5:
        #print("ছছ",end='')
        nlist.append("ছছ")
      else:
        #print("ছ",end='')
        nlist.append("ছ")
    elif word[pos+2] == 'য':
      if pos+2 == len(word):
        #print(word[pos],end='')
        nlist.append(word[pos])
        nlist.append(word[pos])
        #print(word[pos],end='')
      else:
        r = random()
        if r < .5:
          #print(word[pos],end='')
          nlist.append(word[pos])
          nlist.append("া")
          #print("া",end='')
        else:
          #print("ে",end='')
          nlist.append("ে")
          nlist.append(word[pos])
          #print(word[pos],end='')
    elif word[pos] == 'স' and word[pos+2] == 'ম':
      SameClusterFun(word[pos])
    elif word[pos] == 'দ' and word[pos+2] == 'ম':
      SameClusterFun(word[pos])
      SameClusterFun(word[pos])
    elif word[pos] == 'ম':
      SameClusterFun(word[pos+2])
    elif word[pos+2] == 'ম':
      SameClusterFun(word[pos])
    elif word[pos] == 'ব':
      #print(word[pos+2],end='')
      nlist.append(word[pos+2])
    elif word[pos+2] == 'ব':
      #print(word[pos],end='')
      nlist.append(word[pos])
    elif word[pos] == 'র':
      #print(word[pos],end='')
      nlist.append(word[pos])
      SameClusterFun(word[pos+2])
    elif word[pos+2] == 'র':
      SameClusterFun(word[pos])
      #print(word[pos+2],end='')
      nlist.append(word[pos+2])
    elif word[pos] == 'ক' and word[pos+2] == 'ষ':
      if pos == 0:
        #print("খ",end='')
        nlist.append("খ")
      else:
        #print("ক্ক",end='')
        nlist.append("ক্ক")
    elif word[pos+2] == 'ঙ':
      if word[pos+3] == "া" :
        SameClusterFun(word[pos])
        #print("ঙ্গা",end='')
        nlist.append("ঙ্গা")
      else:
        SameClusterFun(word[pos])
        #print("ং",end='')
        nlist.append("ং")
    elif word[pos] == 'ঙ':
      #print("ং",end='')
      nlist.append("ং")
      SameClusterFun(word[pos+2])
    elif word[pos] == 'ঞ':
      #print("ঞ",end='')
      nlist.append("ঞ")
      SameClusterFun(word[pos+2])
    elif word[pos] == 'হ' and word[pos+2] == 'ন':
      #print("ন্ন",end='')
      nlist.append("ন্ন")
    elif word[pos] == 'ন' and word[pos+2] == 'ন':
      #print("হ্ন",end='')
      nlist.append("হ্ন")
    elif word[pos] == word[pos+2]:
      SameClusterFun(word[pos+2])
      SameClusterFun(word[pos+2])
    elif word[pos] == 'ল' or word[pos] == 'ত' or word[pos] == 'থ' or word[pos] == 'দ' or word[pos] == 'ধ' or word[pos] == 'ট' or word[pos] == 'ঠ' or word[pos] == 'স' or word[pos] == ' শ' or  word[pos] == 'ষ':
      #print(word[pos],end='')
      nlist.append(word[pos])
      SameClusterFun(word[pos+2])
    elif word[pos+2] == 'ল' or word[pos+2] == 'ত' or word[pos+2] == 'থ' or word[pos+2] == 'দ' or word[pos+2] == 'ধ' or word[pos+2] == 'ট' or word[pos+2] == 'ঠ' or word[pos+2] == 'স' or word[pos+2] == ' শ' or  word[pos+2] == 'ষ':
      SameClusterFun(word[pos])
      #print(word[pos+2],end='')
      nlist.append(word[pos+2])
    elif word[pos] == 'ন' or word[pos] == 'ণ':
      SameClusterFun(word[pos])
      SameClusterFun(word[pos+2])
    elif word[pos+2] == 'ন' or word[pos+2] == 'ণ':
      SameClusterFun(word[pos])
      SameClusterFun(word[pos+2])
    else:
      #print(word[pos],end='')
      nlist.append(word[pos])
      nlist.append(word[pos+1])
      nlist.append(word[pos+2])
      #print(word[pos+1],end='')
      #print(word[pos+2],end='')

  char_list = ['া', 'ো', 'ে']
  def MakeError(word):
    pos=0
    flag1=0
    flag2=0
    flag3=0
    while(pos<len(word)):
      if flag1 == 1 and flag2 == 1 and flag3 == 1:
        #print(word[pos],end='')
        nlist.append(word[pos])
        pos += 1
      elif word[pos] in char_list:
        r = random()
        if r <= .2:
           nlist.append("")
        else:
           nlist.append(word[pos])
        pos += 1
      else:
        if(pos+1<len(word) and word[pos+1] == '্'):
          r = random()
          if r <= 1 and flag1 == 1:
            #print(word[pos],end='')
            nlist.append(word[pos])
            #print(word[pos+1],end='')
            nlist.append(word[pos+1])
            #print(word[pos+2],end='')
            nlist.append(word[pos+2])
            pos=pos+3
          else:
            flag1=1
            error = 1
            JuktoBorno(word,pos)
            pos=pos+3
        else:
          r = random()
          #Same Cluster
          if r < 1 and r >=.6:
            error = 1
            flag2=1
            SameClusterFun(word[pos])
          #Replacement
          elif r <.6 and r>=2:
            if flag3 == 1:
              #print(word[pos],end='')
              nlist.append(word[pos])
            else:
              flag3=1
              error = 1
              ReplacementFun(word[pos])
          else:
            #print(word[pos],end='')
            nlist.append(word[pos])
          pos+=1
    #data.append(nlist)
    nlist.append(" ")

  def listToString(s):  
      # initialize an empty string
      str1 = ""
      # traverse in the string
      for ele in s:  
          str1 += ele   
      # return string   
      nlist.clear() 
      return str1  
  MakeError(w)
  return listToString(nlist)

def convert(lst): 	
    return ([i for item in lst for i in item.split()]) 
