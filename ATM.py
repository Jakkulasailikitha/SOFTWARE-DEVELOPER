#WRITE A PROGRAM FOR ATM
print("ATM PROGRAM  ")
print("WELCOME TO SBI ATM ")
print("SWIPE YOUR CARD HERE")
atm_pin=1234
pin=int(input("enter your atm pin :"))
transcation=["1","2","3","4","5","6"]
if pin==atm_pin :
    print("choose your transaction")
    print("1.Balance Enquiry")
    print("2.Withdraw Money")
    print("3.Deposit")
    print("4.change_Your_Pin")
    print("5.Transfer Money")
    print("6.Quit")
    trans=input("transcation :")
else:
    print("wrong pin enter again")
if trans=="1" :
    slip=input("do you want slip")
    if slip=="yes" :
        print("here is your slip")
    else:
        print("thanks for using sbi atm,visit again")
elif trans=="2" :
    amount=int(input("enter your amount"))
    if  amount>0 :
        print("collect your cash")
    else:
        print("no,balance")
elif trans=="3" :
    deposit=int(input("enter your amount to deposit"))
    if deposit >0 :
        print("deposited successfully")
    else:
        print("enter valid amount to deposit")
elif trans=="4" :
    Change_Your_Pin=int(input("enter your new pin"))
    if Change_Your_Pin!=pin:
        print("pin changed  successfully")
    else:
        print("enter valid pin to proceed")
elif trans=="5" :
    transfer=int(input("enter amount to transfer  :"))
    if  transfer>0 :
        print("transfered")
    else:
        print("enter correct amount")
elif trans=="6" :
    Quit=input("press yes to quit")
    if Quit=="yes":
        print("quit")
    else:
        print("choose any question")
else:
    print("wrong transcaction")



