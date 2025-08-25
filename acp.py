decimal = float(input("Enter a decimal number: "))
reversed_binary = 0
place = 1  

while decimal > 0:
    remainder = decimal % 2
    for i in range(1):
        reversed_binary += remainder * place

    decimal = decimal // 2
    place *= 10 
binary = 0
while reversed_binary > 0:
    digit = reversed_binary % 10
    for i in range(1):
        binary = binary * 10 + digit

    reversed_binary = reversed_binary // 10
print("Binary number:", binary)