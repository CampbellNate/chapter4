def computeGrade(g):
    g=float(g)
    if(1>=g>=.9):
        return('A')
    elif(.9>=g>=.8):
        return('B')
    elif(.8>=g>=.7):
        return('C')
    elif(.7>=g>=.6):
        return('D')
    elif(0<=g<=.6):
        return('E')
    else:
        return('Invalid Response')
g=input("Enter Grade:")
grade=computeGrade(g)
print(grade)