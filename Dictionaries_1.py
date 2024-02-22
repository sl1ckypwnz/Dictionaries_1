pets = {}
print("Введите данные о питомце:") 
pet_name = input("Введите кличку питомца: ")
pet_species = input("Введите породу питомца: ")
pet_age = int(input("Введите возраст питомца: "))
owner_name = input("Введите имя владельца: ")
 
pets[pet_name] = {
    "Вид питомца": pet_species,
    "Возраст питомца": pet_age,
    "Имя владельца": owner_name
}
 
pet_info = pets[pet_name]
age_determinant = ""
if pet_age % 10 == 1 and pet_age != 11 and pet_age % 100 != 11:
    age_determinant = "год"
elif 1 < pet_age % 10 <= 4 and pet_age != 12 and pet_age != 13 and pet_age != 14:
    age_determinant = "года"
else:
    age_determinant = "лет"

info = f"Это {pet_info['Вид питомца']} по кличке \"{pet_name}\". Возраст питомца: {pet_info['Возраст питомца']} {age_determinant}. Имя владельца: {pet_info['Имя владельца']}"
 
print(info)