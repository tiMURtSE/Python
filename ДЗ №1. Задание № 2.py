first_num = int(input())
sign = input()
second_num = int(input())

if sign == "+":
    print(f"{first_num} {sign} {second_num} = {first_num + second_num}")
elif sign == "-":
    print(f"{first_num} {sign} {second_num} = {first_num - second_num}")
elif sign == "-":
    print(f"{first_num} {sign} {second_num} = {first_num * second_num}")
elif sign == "-":
    print(f"{first_num} {sign} {second_num} = {first_num / second_num}")
else:
    print("Введите правильный знак операции")