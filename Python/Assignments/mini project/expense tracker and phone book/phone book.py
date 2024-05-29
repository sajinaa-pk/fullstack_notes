phonebook={}
while True:
    print("1.Insertion \n2.Updation \n3.Deletion \n4.Display \n5.Exit")

    c=int(input("Enter your choice :"))

    if c==1:
        n=input("Enter the name :")
        p=int(input("Enter phone number :"))
        if n in phonebook.keys():
            print("Already exists")
        else:
            phonebook.update({n:p})

    if c==2:
        print("1.Name Updation.\n2.Phone number updation.")
        up=int(input("What do you want to update :"))

        if up==1:
            old=input("Enter the old name :")
            new=input("Enter the new name :")
            if new in phonebook.keys():
                print("Already Exists")
            else:
                #phonebook.pop(old)
                phonebook[new]=phonebook.pop(old)

        if up==2:
            oldph=input("Enter the name :")
            newph=int(input("Enter the new phone number :"))
            phonebook[oldph]=newph
              
    if c==3:
        d=input("Enter the name to remove:")
        del phonebook[d] 

    if c==4:
        print("Details\n",phonebook.items())

    if c==5:
        exit()