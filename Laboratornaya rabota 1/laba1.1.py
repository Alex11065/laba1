numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

numbers[4] = 0 # присвоил none 0 для того что бы произвести расчет,так как оно не повлияет на сумму но будет учитыватся в колличестве.
b = sum(numbers) / len(numbers) # расчет средне арифмет.
numbers[4] = b # замена символа 0 на ср.ариф

print("Измененный список:", numbers)

#Длинное решение , но затрагивает все наши темы .Но я решил оставить свое решение,так как я к нему пришел .
# Если не прав ,поправте.

# numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
# index_missing_item = 4
# # print(index_missing_item)
# sum_of_numbers = sum(numbers[:index_missing_item]) + sum(numbers[index_missing_item+1:])
# # print(sum_of_numbers)
# # count_of_numbers = len(numbers)
# # print(count_of_numbers)
# average_of_numbers = sum_of_numbers / count_of_numbers
# # print(average_of_numbers)
# numbers[index_missing_item] = average_of_numbers
# print("Измененный список:", numbers)
