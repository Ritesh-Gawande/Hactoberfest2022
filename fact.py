x =int( input("Enter any number"));
fact=1;

if(x<=0):
   print("NO such no");

else:
   for i in range(1,x+1):
       fact=fact*i;
       print(fact);