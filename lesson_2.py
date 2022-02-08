#
# ram = int(input("хотите выбрать компьютер, то нажмите 2"))
# while ram not in range(4, 9):
#     ram = int(input("какая память устраивает вас ram от 4 до 8 GB: "))
# memory = ["HHD", "SSD"]
# kind_memory = input("если хотите выбрать SSD или HDD диск нажмите 2")
# while kind_memory not in memory:
#     kind_memory = input("ведите HDD или SSD")
#
# if kind_memory == "HHD":
#     disk_size = int(input("вы доллжны выбрать размер диска, если да то нажмите 2"))
#     while disk_size < 1:
#         disk_size = int(input("выберите размер диска min 1TB"))
#     kind_size = "TB"
#
# if kind_memory == "SSD":
#     disk_size = int(input("вы доллжны выбрать размер диска, если да то нажмите 2"))
#     while disk_size < 256:
#         disk_size = int(input("выберите размер диска min 256"))
#     kind_size = "GB"
#
# cost = int(input("хотите узнать  цену нажмите 2"))
# while cost > 1000:
#     cost = int(input("цена недолжна быть больше 1000$"))
# condition = input("мы в поиске вашего запроса, а пока нажмите нажмите 2")
# while condition != "new":
#     condition = input("Есть только новые ноутбуки, если устраивает нажмите новый")
# print("поздравляю с покупкой ноутбука!!!")
# print("Оперативная память:", ram, "GB")
# print("вид диска:", kind_memory)
# print("вид памяти:", kind_size)
# print(" размер диска:", disk_size)
# print("стоимость ноутбука:", cost)
# print("состояние ноутбука:", condition)

# покупка машины
type_of_car = input("input car:")
print(type_of_car.lower())
car_millage = int(input("millage car:"))
print(car_millage)
price = int(input("price car:"))
color = input("color car:")
year = int(input("years car:"))
side = input("side car:")
count_own = int(input("count_owner car:"))

if ((type_of_car.lower() == "lexus" or
    type_of_car.lower() == "toyota") and \
        (count_own <= 2) and (year >= 2004) and \
            (color == "white" or color == "grey") and \
            (side == "left")):
    if price <= 10000 and car_millage <= 150000:
        print("есть машина Lexus lx 470")
    elif price <= 8000 and car_millage >= 200000:
        print("есть машина Toyota camry")
    else:
        print("такой машины нет")
else:
    print("у нас нет такой машины")



