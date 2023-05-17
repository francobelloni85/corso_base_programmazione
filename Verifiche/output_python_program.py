# ----- CONSEGNA ------ 
# Scrivi il valore che verrà stampato a video.
# ---------------------

# 1 
print("------ESE 1--------")
a : int = 10
b : int = 5
while(a < b):
    print(a)
    a = a - 1
print("Fine")  


# 2
print("------ESE 2--------")
c : int = 5
d : int = 10
while(d > c):
    print(d)
    d = d - 1
print("Fine")  


# 3
print("------ESE 3--------")
text_a = "Ciao"
i: int = len(text_a)
while(i > text_a):
    print(text_a[i])
    i = i + 1
print("Fine") 


# 4
print("------ESE 4--------")
text_a = "Ciao"
i = len(text_a)
while(i < len(text_a)):
    print(text_a[i])
    i = i + 1
print("Fine") 


# 5
print("------ESE 5--------")
text_a = "Ciao"
i: int = 2
while(i < len(text_a)):
    print(text_a[i])
    i = i + 1
print("Fine") 


# 6
print("------ESE 6 --------")
text_a = "Ciao"
i = 0
while(i < len(text_a)):
    if(i % 2 == 0):
        print(text_a[i])
    i = i + 1
print("Fine") 