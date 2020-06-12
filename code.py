#This program is made to be used to give a number to each individuals 
#and to find a number of the specific person

#User inputting names, genders, and ages of people

def inputting (name,gender,age): 
    more = ""
    while (more != "Done"):
        nam = input("What is your name?")
        name.append(nam)
        
        gende = input ("Are you \"male\" or \"female?\"")
        gender.append(gende)
        
        ag = int(input("What is your age? "))
        age.append (ag)
        
        more = input("Want to add another one? (Type \"Done\" to stop)")
        
#User finding a number of specific person

def find (name, gender, age,a = "", b = "" , c = 0):

    #This array is a storage of numbers that has a same name with what the user inputted
    
    pos = []
    
    #This array is a storage of numbers that has a same gender with what the user inputted
    
    pos1 = []
    
    #This array is a storage of numbers that has a same age with what the user inputted
    
    pos2 = []
    
    #This loop store informations in the array:
    
    for i in range (len(name)):
        if (name[i] == a):
            
            #storing a number that has a same name
            
            pos.append(i)
        if (gender[i] == b):
            
            #storing a number that has a same gender
            
            pos1.append(i)
        if (age[i] == c):
            
            #storing a number that has a same age
            
            pos2.append(i)

    #finding x(longest length of the arrays)
    
    x = max(len(pos2),len(pos1),len(pos))
    
    #this loop equalizes the length of the arrays by adding elements until it is long as the x
    
    print (x)
    for k in range (x):
        if (len(pos) != x):
            pos.append("@")
        if (len(pos1) != x):
            pos1.append("@")
        if (len(pos2) != x):
            pos2.append("@")
    print (pos)
    print (pos1)
    print (pos2)
    
    #this loop finds a number that is located in all 3 arrays and return the number to the main function
    
    for j in range (x):
        for l in range (x):
            if(pos[j] == pos1[l]):
                for o in range (x):
                    if(pos1[l] == pos2[o]):
                        return (pos[j])
    
        
#lists that hold the info that user inputted    

name = []
gender = []
age = []

#user inputting the info

inputting(name,gender,age)

#asking if the user is willing to find specific person

search = input("Are you serching for somebody? (Type \"No\" to don't)")

#finding a specific person and printing out the number

if (search != "No"):
    next = ""
    while (next != "Ok"):
        next = input ("Give all information about a person you are seaching (Type \"Ok\" to move on)")
    
    if (next == "Ok"):
        name1 = input ("What is his/her name?")
        gender1 = input ("Is he male or female?")
        age1 = int(input ("What is his/her age?"))
        print ("Person's number is #"+str(find (name, gender, age,name1, gender1, age1)))
    
    
