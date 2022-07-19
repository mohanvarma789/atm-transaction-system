print("welcome")
a=int(input("enter your password:"))
b=int(input("reenter ur password:"))
if a==b:
   print("1.deposit")
   print("2.withdraw")
   print("3.balance")
   print("4.ministatement")
   print("5.pin change")

   c=int(input("choose ur choice:"))
  
   if c==1:
    print("1.savingsaccount")
    print("2.current account") 
    d=int(input("choose ur choice:"))

    if d==1 or d==2:
     m=int(input("enter number of 2000 notes:"))    
    
     e=int(input("enter number of 500 notes:"))
     f=int(input("enter number of 100 notes:"))
     g=int(input("enter number of 50 notes:"))
     h=int(input("enter number of 20 notes:"))
     i=int(input("enter number of 10 notes:"))
     j=int(input("enter number of 5 notes:"))
     k=int(input("enter number of 2 notes:"))
     l=int(input("enter number of 1 notes:"))
     print("2000*",m,"=",2000*m)
     print("500*",e,"=",500*e)
     print("100*",f,"=",100*f)
     print("50*",g,"=",50*g)
     print("20*",h,"=",20*h)
     print("10*",i,"=",10*i)
     print("5*",j,"=",5*j)
     print("2*",k,"=",2*k)
     print("1*",l,"=",1*l)
     print("total number of notes:",m+e+f+g+h+i+j+k+l)
     print("total value:",2000*m+500*e+100*f+50*g+20*h+10*i+5*j+2*k+1)
     print("thank you vist again")
     
   elif c==2:
    n=int(input("enter amount:"))
    if n<=10000:
     print("collect ur money")
     print("thankyou visit agian")
    else:
     print("no limit")   
    
   elif c==3:
    money=15000
    o=int(input("enter your account number:"))
    p=int(input("reenter ur account number "))
    if o==p:
     print( "balance is:",money)
    else:
        print("mis match")
   elif c==4:
    print("1)2/2/2002 5000rs is credit")
    print("2)14/10/2021 10000rs is diposited ") 
   elif c==5:
    q=int(input("enter old pin"))
    if a==b==q:
        r=int(input("enter new pin"))
        s=int(input("re enter new pin"))
        if r==s:
            print("ur pin succesfully changed")
        else:
            print("mismatch")                
    else:
        print("old pin is mismatch:")
else:
    print("invalid") 


       


    


           
        

  
     

 
 


               

