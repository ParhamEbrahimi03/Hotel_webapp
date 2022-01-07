import food_menu

def room():
    condition = False
    while (not condition):
        try:
            room_number = int(input("Pleas enter your room number "))
            room_number_confirmation = int(input("pleas confrim your room number "))
            if(room_number == room_number_confirmation):
                print("ok your room number is",room_number)
                condition = True
            else:
                print("your room number should match the previous one.")
        except:
            print("invalid input, please enter a number")

menu_apetizer=["soap","garlic bread"]
menu_entree=["pizza","burger","fried chicken fillet"]
menu_dissert=["caramel panna cotta","nutella cheesecake"]
menu_drink=["mohito","coca"]

apetizer_list=[]
apetizer_quantity=[]

entree_list=[]
entree_quantity=[]

dessert_list=[]
desert_quantity=[]

drink_list=[]
drink_quantity=[]


# apetizer foods: 

def food():

    done = False
    while(not done):
        apetizer = input("Please enter your apetizer from menue. Type done when you are done. ")

        if(apetizer == "done"):
            for count in range (len(apetizer_list)-1):
                print("you have orderd",apetizer_quantity[count],"of",apetizer_list[count])
            done = True

        else:
            order =0
            if(order < len(menu_apetizer)):
                    
                if(apetizer == menu_apetizer[order]):
                    while(done == False):
                        try:
                            apetizer_number = int(input("how many",apetizer,"do you want? "))
                            apetizer_quantity.append(apetizer_number)
                            
                        except:
                            print("")
                        
                if(apetizer != menu_apetizer[order]):
                    print("write from menu list and atention to writing",menu_apetizer)
                order +=1
                
        if(apetizer == "done"):
            done = True
            for count in range (len(apetizer_list)-1):
                print("you orderd",apetizer_quantity[count],"of",apetizer_list[count])
food()
