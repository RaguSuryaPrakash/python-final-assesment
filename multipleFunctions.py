class multipleFunctions():
    def triangle():
        Height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle: ",(Height*breadth)/2)
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        breadth=int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle: ",Height1+Height2+breadth)
    def Percentage():
        mark1=int(input("subject1:"))
        mark2=int(input("subject2:"))
        mark3=int(input("subject3:"))
        mark4=int(input("subject4:"))
        mark5=int(input("subject5:"))
        Total=mark1+mark2+mark3+mark4+mark5
        print("Total:",mark1+mark2+mark3+mark4+mark5)
        percent=(Total/500)*100
        print("Percentage:",percent)
    def elegible():
        gender=input("enter your gender:")
        age=int(input("enter your age:"))
        if(gender=='male'):
            if(age>=20):
                print("elegible")
            else:
                print("not elegible")    
        elif(gender=='female'):
            if(age>=18):
                    print("elegible")
            else:
                print("not elegible")
    def OddEven():
        num=int(input("Enter a number:"))
        if(num%2)== 0:
            print("{0} is Even number".format(num))
        else:
            print("{0} is Odd number".format(num))
    def Subfields():
        print("Sub-fields in AI are:")
        List=['Machine Learning', 'Neural Networks', 'Vision', 'Robotics', 'Speech Processing', 'Natural Language Processing']
        for temp in List:
            print(temp) 
               