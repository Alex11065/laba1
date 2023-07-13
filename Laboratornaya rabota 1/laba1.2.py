# TODO Найдите количество книг, которое можно разместить на дискете
info_disc = 1.44
list_book = 100
str_book = 50
simb = 25
b = 4  # Для хранения кода одного символа нужно 4 байта.

simb_book = (str_book * simb) * list_book
#print(simb_book)
bai = simb_book * b
#print(bai)
info_disc_bit = (info_disc * 1024) * 1024
#print(info_disc_bit)
by = round((info_disc_bit / bai),)
#print(by)

print("Количество книг, помещающихся на дискету:", by)
