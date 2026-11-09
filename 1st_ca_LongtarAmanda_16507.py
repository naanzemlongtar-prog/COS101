while True:
    number = int(input("Enter a number greater than 1: "))

    if number <= 1:
        print("The number must be greater than 1.")
        continue
    for i in range (1,13):
        print(number, "x", i, "=", number*i)

    my_choice = input("Enter E to end the program : ").strip()
    if my_choice == "E":
        print("Program ended")
        break
    
    
