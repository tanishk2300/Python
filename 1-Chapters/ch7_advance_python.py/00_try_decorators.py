# decorator is a function that takes another function as argument and returns a function 
# def =definetion 


def decorator(func):#here func as an arguement 
    def wrapper(): # jo kaam hum karna chate h vo wrapper k ander hoga 
        #or kaya karna chate ho vo chiz return karega "return" function se 
        print('transection initiated')
        func() # ye kaya karta h ki agar start ho raha h to uss se pahele ek msg aajaye and khatam ho jaye to uss ka bhi msg aajaye 
        print('transection completed')
    return wrapper # ye function ko return kar raha h 

def hello(): # idher origenal function k ander kuch karna chate ho to yaha se iss tarah kar sakte ho 'func()' ki jaga per , phir end ka msg print hota h 
    # function k bahar se app add kar sakte ho kuch bhi yaha se 
    print('executing all step of transection...')# ye original function h jo wrapper k ander wrap ho jata h .

# agar iss ko print karna h mean call karna h to 
hello1=decorator(hello) # idher isse manually call kiya h , hello1 ko decorater ki value pass kar di 
hello1() # ider hello1 ko humne exicute kiya , mean call kiya .