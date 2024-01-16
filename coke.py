amount_due = 50
while amount_due > 0:
    print("Amount Due:", amount_due)
    inserted = int(input("Insert Coin:"))
    if inserted == 25 or inserted == 10 or inserted == 5:
        amount_due = amount_due-inserted
        if amount_due <= 0:
            print("Change Owed:",(amount_due*-1))
            break