roman_numeral = input("Enter the Roman numeral: ")
roman = {'M': 1000,'D': 500,'C': 100,'L': 50, 'X': 10,'V': 5, 'I': 1}
result = 0

for i in range(0, len(roman_numeral)-1):
    if roman[roman_numeral[i]] < roman[roman_numeral[i+1]]:
        result = result - roman[roman_numeral[i]]
    else:
        result = result + roman[roman_numeral[i]]

result = result + roman[roman_numeral[-1]]

print(f"{roman_numeral} = {result}")