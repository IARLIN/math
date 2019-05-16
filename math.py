a = list(input("Sheikvanet Gadasakvani Ricxvi: "))
n = input("Sheikvanet Sistema: ")
b = 0
res = 0
l = len(a)
c = len(a) - 1 
while True:
    res = res + int(a[b]) * int(n)**int(c)
    l = l - 1
    b = b + 1
    c = c - 1
    if l == 0:
      print(res)
      break

    
        

