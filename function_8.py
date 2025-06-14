# #function definition
# # def avg():
# #     a=int(input("enetr the number"))
# #     b=int(input("enetr the number"))
# #     c=int(input("enetr the number"))
# #     average=(a+b+c)/3
# #     print(average)
# # avg()


# def calculator(num1,op,num2):
#     if op=="+":
#         print(num1+num2)
#     if op=="/":
#         prin(num1/num2)
#     if op=="*":
#         print(num1*num2)
#     if op=="-":
#         print(num1-num2) 
# num1=int(input("enter the number"))
# num2=int(input("enter the number"))
# op=(input("enter the number"))
# res=calculator(num1,op,num2)
# print(res)
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
n=int(input("enter the number"))
print(f"the factorial of this number{factorial(n)}")