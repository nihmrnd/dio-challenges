customers = {}

def add_customer(cpf, name, age, city):
    customers[cpf] = {
        "name": name,
        "age": age,
        "city": city
    }
    return customers

cpf = input()
name = input()
age = input()
city = input()

add_customer(cpf, name, age, city)

print("Customer Registered!")
print("Document:", cpf)
print("Name:", name)
print("Age:", age)
print("City:", city)