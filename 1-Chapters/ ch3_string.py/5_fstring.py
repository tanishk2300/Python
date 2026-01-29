#string formatting 
template="dear tanish{}, you are awesome.take this {}$ bag"
a="john"
a1=200
b="jack"
b1=1000
c="marie"
c1=300

s1 = template.format(a,a1) #you have to choose 
print(s1)
#the upper command state the string formatting 
# now the f-string is starts 
print(f"{a}you are awsome and take this {a1}$ bag")
print(f"{b}you are awsome and take this {b1}$ bag")
print(f"{c}you are awsome and take this {c1}$ bag")