# ----- CONSEGNA ------
# Scrivi il valore che verrà stampato a video.
# ---------------------

# 1
print("------ESE 1--------")
j: int = 10
b: int = 5
while j > b:
    print(j)
    j = j - 1
print("Fine")


# 2
print("------ESE 2--------")
c: int = 5
d: int = 10
while d > c:
    print(d)
    d = d - 2
print("Fine")


# 3
print("------ESE 3--------")
text_a = "Ciao"
i: int = len(text_a) - 1
while i >= 0:
    print(text_a[i])
    i = i - 2
print("Fine")


# 4
print("------ESE 4--------")
text_a = "Ciao"
i = len(text_a)
while i > 0:
    i = i - 1
    print(text_a[i])
print("Fine")


# 5
print("------ESE 5--------")
text_a = "Ciao"
i: int = 2
while i < len(text_a):
    print(text_a[i])
    i = i + 2
print("Fine")


# 6
print("------ESE 6 --------")
text_a = "Ciao"
i = 0
while i < len(text_a):
    if i % 2 == 1:
        print(text_a[i])
    i = i + 1
print("Fine")


# 7
print("------ESE 7 --------")
text_a = "CiaoCiao"
i = 0
while i < len(text_a):
    if i % 3 == 0:
        print(text_a[i])
    i = i + 1
print("Fine")


# 8
print("------ESE 8 --------")
text_a = "CiaoCiao"
i = 0
while i < len(text_a):
    if i % 2 == 0 or text_a[j+1] == "a":
        print(text_a[i])
    i = i + 1
print("Fine")


# 9
print("------ESE 9 --------")
text_a = "Ciao!"
i = 0
while i < len(text_a)-1:   
    print(text_a[i])
    i = i + 1
print("Fine")


# 10
print("------ESE 10 --------")
text_a = "CiaoPippo"
i = 0
j = len(text_a) - 2
while i < len(text_a)-1:   
    index = j - i
    print(text_a[index])
    i = i + 1
print("Fine")


# 11
print("------ESE 11 --------")
text_a = "CiaoPippo"
i = 0
j = 0
while i < len(text_a):       
    print(text_a[j])
    i = i + 1
    if(i % 2 == 0):
        j = j + 1        
print("Fine")


# 12
print("------ESE 12 --------")
text_a = "CiaoPippo"
i = 0
j = 0
while i < len(text_a):       
    print(text_a[j])
    i = i + 1
    if(i % 2 == 0) and (text_a[j]== "i"):
        j = j + 1        
print("Fine")


# 13
print("------ESE 13 --------")
text_a = "CiaoPippo"
i = 0
j = len(text_a)-1 
while i < len(text_a):       
    print(text_a[j])
    i = i + 1
    if(i % 2 == 1):
        j = j - 1        
print("Fine")