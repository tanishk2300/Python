questions=[
    ["Which is the smallest prime number?" ,"0","1","2","3",3],
    ["Which Indian scientist is known as the Missile Man of India? " ,"Vikram Sarabhai","C.V. Raman"," A.P.J. Abdul Kalam","Homi Bhabha",3] ,   
    ["Which gas do humans exhale in large amounts?" ,"Oxygen","Carbon Dioxide","Nitrogen","Hydrogen",2],
    ["Who is the author of Harry Potter ?","J.R.R. Tolkien ","J.K. Rowling George"," R.R. Martin ","Suzanne Collins",2],
]
prize=[1000,2000,3000,4000]
i=0

for question in questions:
    print("\n" +question[0])
    print(f"1. {question[1]}")
    print(f"2. {question[2]}")
    print(f"3. {question[3]}")
    print(f"4. {question[4]}")
    
    a=int(input("Choose your answer (1-4);"))
    #cheak weather the anwswer is correct or not .
    if question[5] == a:
                    print("the answer is correct")
                    print(f"you won:{prize[i]}")
        
    else:
        print(f"better luck next time , correct answer is {question[5]}")
    i +=1
    

