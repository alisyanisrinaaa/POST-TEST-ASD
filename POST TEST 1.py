import os
os.system("cls")

# NAMA : ALISYA NISRINA SATIVA
# NIM : 2209116005
# SISTEM INFORMASI A 2022

def pemisah(pisah):
    result = []
    for variable in pisah:
        if isinstance(variable, list):
            for i in variable:
               if isinstance(i, list):
                  for x in i :
                    result.append(int(x))
               elif isinstance(i, int):
                    result.append(i)
        else :
            result.append(variable)
    return result

def partition(l, bwh, ats):
  pivot = l[bwh] 
  pos_batas = bwh+1
  for j in range(bwh+1, ats):
    if l[j] < pivot :
      l[pos_batas],l[j]=l[j],l[pos_batas]
      pos_batas += 1
  l[pos_batas-1],l[bwh] = l[bwh],l[pos_batas-1]
  return pos_batas

def quicksort(l, bwh, ats):
  if bwh < ats :
   y = partition(l, bwh, ats)
   quicksort(l, bwh, y - 1)
   quicksort(l, y + 1, ats)
   return l

def coba(l) :
  z = pemisah(l)
  quicksort(z, 0, len(z)-1)
  return z

variable = [12, 1, [22, 3, [8, 14]], 2, 6, [11], 90]

print("Sebelum disort : ",variable)
akhir = coba(variable)
print("Setelah disort : ",akhir)