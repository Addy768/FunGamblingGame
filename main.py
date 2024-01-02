
MAX_LINES=3 # constant value that will not change
MAX_BET=100
MIN_BET=1

def deposit():
    ## se we wrote a function deposit  here we ask what is the amount then wwe wcheck if the amount is digit then we will convert it into the int 
    #then we put the conditions for greater than 0 or lesss than 0
    
    while True:
        amount=input("what would you like to deposit ?  $ ")
        if amount.isdigit():#will tell us if this is a valid number 
            amount=int(amount) #will convert the string command into the string 
            if amount>0:
                break
            else:
                print("amount must be greater than 0")
        else:
            print("please enter a number.")
        
    return amount

def get_number_of_lines():
    while True:
        lines=input("Enter the number of the lines to bet on (1-" + str(MAX_LINES)+ ")? ")
        if lines.isdigit(): 
            lines=int(lines) 
            if 1<=lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("please enter a number.")
        
    return lines    

def get_bet():
    while True:
        amount=input("what would you like to bet on each line ?  $ ")
        if amount.isdigit():#will tell us if this is a valid number 
            amount=int(amount) #will convert the string command into the string 
            if MIN_BET <= amount <=MAX_BET:
                break
            else:
                print(f"amount must be between ${MIN_BET} - ${MAX_BET}.")
                
        else:
            print("please enter a number.")
        
    return amount
    

    
def main():
    balance=deposit()
    lines=get_number_of_lines()
    while True:
        
        bet=get_bet()
        total_bet= bet * lines
        
        if total_bet>balance:
            print("you do not have anough to bet on ")
    print(f"you are betting on ${bet} on ${lines} lines. total bet is equal to: $ ${total_bet}")
    

main()    