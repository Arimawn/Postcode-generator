from random import randint

#? Quastion 
print("Wich country do you want?")

#? Countries
Countries = ['USA', 'UK', 'Germany', 'Australia', 'Japan', 'Iran']
List_Num = 1
for country in Countries:
    print(f'{(List_Num)}-{country}')
    List_Num += 1

Client_Answer = int(input())

def postGenerator():

    #! USA
    if Client_Answer == 1:

        postCode = []
        PostCode = ""
        for i in range(5):
            postCode.insert(i,str(randint(1,9)))

        for a in (postCode):
            PostCode += a
        return PostCode
    
    #! UK
    elif Client_Answer == 2:
        
        postCode = []
        PostCode = ""
        for i in range(7):
            postCode.insert(i,str(randint(1,9)))

        for a in (postCode):
            PostCode += a
        return PostCode
    
    #! Germany
    elif Client_Answer == 3:

        postCode = []
        PostCode = ""
        for i in range(5):
            postCode.insert(i,str(randint(1,9)))

        for a in (postCode):
            PostCode += a
        return PostCode
    
    #! Australia
    elif Client_Answer == 4:

        postCode = []
        PostCode = ""
        for i in range(6):
            postCode.insert(i,str(randint(1,9)))

        for a in (postCode):
            PostCode += a
        return PostCode
    
    #! Japan
    elif Client_Answer == 5:

        postCode = []
        PostCode = ""
        for i in range(7):
            postCode.insert(i,str(randint(1,9)))

        for a in (postCode):
            PostCode += a
        return PostCode
    
    #! Iran
    elif Client_Answer == 5:

        postCode = []
        PostCode = ""
        for i in range(10):
            postCode.insert(i,str(randint(1,9)))

        for a in (postCode):
            PostCode += a
        return PostCode
    
    #! Error
    else:
        print('Something went wrong! Please try again.')

print(postGenerator())


