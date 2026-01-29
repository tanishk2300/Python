# s= set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?
s= set()
s.add(20)
s.add(20.0)
s.add('20')

20==20.0# pahele equall kar liya innko 
hash(20)==hash('20')#phir is string or int ko kiya to abb ek hi variable kaam ayega '20' 
s = {20, '20'}


print(len(s))

