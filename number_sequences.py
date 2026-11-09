# Display several number sequences using range().

print("Numbers from 1 to 20:")
for number in range(1, 19):
    print(number)

print()

print("Odd numbers from 1 to 19:")
for number in range(1, 20, 1):
    print(number)

print()

print("Countdown from 10 to 0")
for number in range(10, -1, -1):
    print(number)
