class person:
    name =" "
    address =" "


class employee(person):
    pass

class doctor(employee):
    pass

print(person.__base__)
print(employee.__base__)
