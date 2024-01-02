import random
MAX_LINES=3 # constant value that will not change
MAX_BET=100
MIN_BET=1
ROWN=3
COLS=3
count_for_symbol={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}
def get_slot_machine_spinning(rows,cols,symbols):
    all_symbols=[]
    for symbol,count_for_symbol in symbols.items():
        for _ in range(count_for_symbol):
            all_symbols.append(symbol)
    columns=[]
    
    for col in range(cols):
        column=[]
        current_symbols=all_symbols[:]# copying
        for row in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            columns.append(value)
        columns.append(column)
    return columns

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
            print(f"you do not have anough to bet that amount, your current balance is : ${balance}  ")
        else:
            break    
    print(f"you are betting on ${bet} on ${lines} lines. total bet is equal to: $ ${total_bet}")
    

main()    