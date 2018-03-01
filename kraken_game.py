tempArray = {}
def getKey(m, n):
  if(m > n):
    key = str(n) + str(m)
  else:
    key = str(m) + str(n)  
  return key

def getValue(m, n):
  # print m, n
  if(m ==1 or n == 1):
    return (m * n * 2) + 1  
  else:
    # key = getKey(m, n)
    # if key in tempArray:
    #   return tempArray[key]
    # else:
      result = getValue(m-1, n) + getValue(m-1, n-1) + getValue(m, n-1)
      # tempArray[key] = result
      return result

def krakenCount(m, n):
  rows = m
  cols = n
  # if( rows < 1 or cols < 1):
  #   raise ValueError("Invalid Input")
  #   return
  print getValue(rows, cols)



krakenCount(20, 20)