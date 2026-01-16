temp=int(input("Enter the temperature: "))
if temp<5:
    print("It is very cold so wear the warmest things you have")
elif 5<temp and temp<10:
    print("You should wear both a pullover and a jacket")
elif 10<temp<20:
    print("You should wear a pullover")
else:
    print("You can wear something light and soft")