# n = int(input("enter a num :"))
# for i in range (2,n):
#     if n%i==0:
#         print ("not a prime")
#         break
#     else :
#         print ( n, "is a prime num")
# ------------------------------------------------------
# x = int(input('enter a num'))
# if x < 400:
#     a = (x/4)
#     print (a)
# -------------------------------------------------------
# elif x > 400:
#     b = (x/100)
#     if b == 0:
#         print("not a leap year")
#     elif b != 0:
#         c = (x/400)
#         if c == 0:
#             print("yes a leap year")
#         else:
#             print("1")
        
#     else :
#         print ("2")
# else :
#     print("invalid statement 9baaka")
# ---------------------------------------------------------

yr = int(input("Enter the year : "))
if yr % 4 == 0 and yr % 400 == 0:
    print ("Leap year")
else:
    print ("Not a Leap year")


