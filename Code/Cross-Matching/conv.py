#Functions:
def hms2dec(a,b,c):
  return 15*a+b/4+c/240

def dms2dec(a,b,c):
  if a<0:
    b*=-1
    c*=-1
  return a+b/60+c/3600 



if __name__ == '__main__':
  print(hms2dec(23, 12, 6))

  print(dms2dec(22, 57, 18))

  print(dms2dec(-66, 5, 5.1))