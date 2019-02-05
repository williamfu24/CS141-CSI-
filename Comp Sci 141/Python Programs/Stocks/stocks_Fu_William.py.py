#Name: William Fu.
#Project: Stock Market.
#Honor Code: I have neither given nor received unauthorized aid on this program
#Description: This program will run a simulation of a stock exchange including
#    the trading of stock and the gain/loss of money
#Input: User types in variables for the "value of stocks' or "amount of stock
#    purchased"
#Output: The state of the stock market, after each command, including about the
#    value of stock, the amount purchased, and in the end the profit or lost

#This part finds the total cost of purchasing x amount of stock
stock_x=float(input("How much is the value of stock X?")) #needs float for program to work
num_shares=float(input("How many shares would you like to buy?"))
cost_shares=(stock_x * num_shares)  #Solves to find how much it would take to buy the shares
print("The starting value of stock is", cost_shares)
print("Commission for this exchange is 2%")
commission=0.02 #The amount commision would charge
total_cost = (cost_shares + (cost_shares*commission)) 
print("The total cost will be", total_cost, "after commission")
#This part works


#This part finds the amount recieved after selling the stocks at a new value
stock_x2=float(input("What is the ending price of stock X?"))
new_cost=stock_x2*num_shares
print("Your stocks are now valued at", new_cost)
new_total= (new_cost - (new_cost*commission))
print("You will recieve", new_total, "after commission")
#This part works


#This part of the program will find the profit made from the stocks
profit=new_cost-total_cost
print("Your profit is",profit,"dollars")
percent_made=(profit/total_cost)*100
print("for a",percent_made,"percent increase in value")
#This part works
