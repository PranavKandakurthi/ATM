class ATM:
    def __init__(self,card_number,pin):
        self.card_number=card_number
        self.pin=pin
    def check_balance(self):
        print('Current balance $100000')
    def withdrawl(self,amount):
        new_amount=100000-amount
        print('You withdrew '+str(amount)+'. Your remaining balance is '+str(new_amount))
    def deposit(self,amount):
        new_amount=new_amount+amount
        print('You deposited '+str(amount)+'. Your remaining balance is '+str(new_amount))

def main():
    cardnumber=input('Enter card number')
    pin_number=input('Enter pin number')
    newuser=ATM(cardnumber,pin_number)
    print('Optioons:')
    print('1. Check Balance  2. Withdraw  3.Deposit')
    activity=int(input('Enter option:'))

    if(activity==1):
        newuser.check_balance()
    elif(activity==2):
        amount=int(input('Enter the amount'))
        newuser.withdrawl(amount)
    elif(activity==3):
        amount=int(input('Enter the amount'))
        newuser.deposit(amount)
    else:
        print('Please enter a valid number')

if __name__=='__main__':
    main()
        