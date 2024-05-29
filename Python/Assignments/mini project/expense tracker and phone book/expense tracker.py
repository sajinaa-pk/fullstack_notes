wallet={}
initial=1000
while True:
    print("1.Add Expense.\n2.Add Balance.\n3.View Expense.\n4.Exit.")
    c=int(input("Enter the choice :"))

    if c==1:
        name=input("Enter the expense name :")
        amt=int(input("Enter the amount :"))
        bal=initial-amt
        


        if amt<initial:
            initial=bal

            if name in wallet.keys():
                
                wallet[name]=wallet.pop(name)
                wallet[name]=wallet[name]+amt
            else:
                wallet.update({name:amt})
        
            
            print("******Current Bal***** :",bal)
            print("$$$$$$$$$$$$$$$$$",initial)
        else:
            print("Insufficient amount")

    if c==2:
        addbal=int(input("Adding wallet :"))
        initial=initial+addbal 
        print("*****Wallet Amount**** :",initial)

    if c==3:
        print(wallet.items())

    if c==4:
        exit()








   # print(wallet.items())