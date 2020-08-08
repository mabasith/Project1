value = "cat picture is cat picture"
i = value.find("picture")
print(i)
#b = value.find("picture",i+1)
#print (b)

#get right most index of the string
i = value.rfind("picture")
print(i)
b = value.rfind("picture", 0, i - 1)
print(b)