selling = float(input("Enter the selling price"))
cost = float(input("Enter the cost price"))
if(selling>cost):
    print("We will be in profit")
    profit = selling - cost
    print(f"We get profit of {profit}Rs")
else:
    print("We are in the loss")
    loss = selling - cost
    print(f"We are in loss of {loss}Rs")
