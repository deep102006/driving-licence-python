import random
def Dlicence():
    L={}
    try:
        a=int(input("Please enter your age:"))
        if a>=18:
            print("Yor are eligible for applying Driving Licence!!👌👌")
            print("Do you want to apply for your Driving Licence?(Y/N) :")
            try:
                a1=input("")
                if a1.upper()=='Y'or a1.upper()=='YES':
                    n=input("Enter your name:")
                    n1=input("Enter your Father's name:")
                    n2=input("Enter your Mother's name:")
                    n4=input("Enter your Adhaar No. :")
                    if len(n4)!= 12 or n4[0]=='0':
                        print("Invalid Aadhar number!!Please try again!!")
                        
                    else:
                        L["Name"]=n
                        L["Father's Name"]=n1
                        L["Mother's Name"]=n2
                        L["Aadhar number"]=n4


                        try:
                            a=int(input("Enter mobile number to recieve otp: "))
                            a1=str(a)
                            l=[]
                            if len(a1)==10 and a1[0]!='0':
                                L["Mobile Number"]=a
                                print("Your details are recorded: ")
                                print(L)
                            
                                for i in range(1,7):
                                    s=random.randint(1,9)
                                    
                                    l.append(s)
                                print("Your otp is: ",end="")     
                                for j in l:
                                    print(j,end="")
                                print()
                                print("Please enter this otp to continue:")
                                b=int(input())
                                s=''.join(str(m) for m in l)
                                if str(b)==s:
                                    print("Congratulations!! your driving licence will be dileverd within next 7-14 working days after verfications!😊😊💫")
                                else:
                                    print("Invalid OTP!! Please try again after sometime!!😔")                           
                            else:
                                print("Phone number is invalid!! Please try again after sometime!!😔")     
                        except ValueError:
                            print("Phone number is invalid!! Please try again after sometime!!😔")
                elif a1.upper()=="N" or a1.upper()=="NO":
                     print("Thanks for visiting us!!😊")
                else:
                    print("Please press Y or N only!!!! Please try again after sometime!!😔")
            except ValueError:
                print("Please press Y or N only and try again after sometime!!!!😔") 
        else:
            print("Sorry you are not eligible for Driving Licence Right Now!!😔")       
    except ValueError:
        print("Please enter your age in digits only and  Please try again after sometime!!😔")


Dlicence()