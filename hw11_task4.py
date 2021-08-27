import re

class Warehouse:
    def __init__(self, items, departments):
        self.items = items
        self.departments = departments

    def to_warehouse(self, item_type, quantity):
        if re.match(r'[0-9]+', str(quantity)):
            if len(self.items) == 0:
                self.items[item_type] = int(quantity)
            else:
                same = False
                for key in self.items:
                    if key == item_type:
                        same = True
                        self.items[key] = self.items[key] + int(quantity)
                if not same:
                    self.items[item_type] = int(quantity)
        else:
            print('Wrong values!')

    def show_warehouse(self):
        print(self.items)

    def from_warehouse(self, item_type, quantity, department):
        for el in self.items:
            if el == item_type:
                if self.items[el] >= quantity:
                    self.departments[department] = {item_type: quantity}
                    self.items[el] = self.items[el] - quantity
                elif self.items[el] < quantity:
                    print('Wrong quantity')
        found = False
        for el in self.items:
            if self.items[el] == 0:
                found = True
        if found:
            del self.items[el]

    def show_departments(self):
        print(self.departments)

class Office_Equipment:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

class Printer(Office_Equipment):
    def __init__(self, name, price, weight, type):
        super().__init__(name, price, weight)
        self.type = type

class Scaner(Office_Equipment):
    def __init__(self, name, price, weight, resolution):
        super().__init__(name, price, weight)
        self.resolution = resolution

class Xerox(Office_Equipment):
    def __init__(self, name, price, weight, modes):
        super().__init__(name, price, weight)
        self.modes = modes


a = Warehouse({}, {})
a.to_warehouse('printer', 5)
a.to_warehouse('scaner', 2)
a.to_warehouse('xerox', 3)
a.to_warehouse('scaner', 2)
a.show_warehouse()

a.from_warehouse('printer', 1, 'IT')
a.from_warehouse('xerox', 3, 'HR')
a.show_departments()
a.show_warehouse()

a.to_warehouse('xerox', '6')
a.show_warehouse()
