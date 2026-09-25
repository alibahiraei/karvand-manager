

while True:
    menu=input("1 add" \
    "2 show" \
    "3 Edit" \
    "4 delet" \
    "5 Report" \
    "6 exite")
    if menu==1:
        name=input('enter name : ')
        with open ("data/karvand.txt", "w") as f:
            f.write(name)
        print(" name ezafe shod")
    if menu==2:
        edit=input(" enter new nam:  ")
        with open ("data/karvand.txt","r") as f:
            for i in f:
                f.read()
                if i==edit:
                    i=edit
        print(" edit anjam shod")
    if menu==3:
        pass

