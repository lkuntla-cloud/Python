Amount=int(input("Enter the Amount"))
Note1=Amount//100
Note2=(Amount%100)//50
Note3=((Amount%100)%50)//10
print("Note of 100 rupees",Note1)
print("Note of 50 rupees",Note2)
print("Note of 10 rupees",Note3)