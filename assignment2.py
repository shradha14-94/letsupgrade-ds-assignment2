# find all the index of we

str1= "What we think we becomee we"
p= "we"
a= -1
c= str1.count("we")
for each in range(c):
	a=str1.find(p,a+1)
	print(a)