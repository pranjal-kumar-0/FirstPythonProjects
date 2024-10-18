digit_word = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
              6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 0: 'Zero'}
in_word = ''
num_input = int(input("Enter the Number: "))
for i in str(num_input):
    in_word = in_word + str(digit_word.get(int(i),'!')) + ' '
print(in_word)
