class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return self.address

    def available_menus(self, time):
        menus_available = []
        for menu in self.menus:
            if int(menu.start_time) <= time <= int(menu.end_time):
                menus_available.append(menu.name)
        return 'The following menus are currently available: ' + ', '.join(menus_available)


class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        if int(self.start_time) < 1300:
            simple_start_time = self.start_time[:2] + 'AM'
        elif int(self.start_time) >= 2200:
            simple_start_time = str(int(self.start_time) - 1200)[:2] + 'PM'
        else:
            simple_start_time = str(int(self.start_time) - 1200)[:1] + 'PM'

        if int(self.end_time) < 1300:
            simple_end_time = self.end_time[:2] + 'AM'
        elif int(self.end_time) >= 2200:
            simple_end_time = str(int(self.end_time) - 1200)[:2] + 'PM'
        else:
            simple_end_time = str(int(self.end_time) - 1200)[:1] + 'PM'
        return '{} menu available from {} to {}'.format(self.name, simple_start_time, simple_end_time)

    def calculate_bill(self, purchased_items):
        bill_total = 0
        for item in purchased_items:
            bill_total += self.items[item]
        return bill_total


brunchitems = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50,
               'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}

earltbirditems = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00,
                  'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50,
                  'coffee': 1.50, 'espresso': 3.00}

dinneritems = {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00,
               'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}

kidsitems = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}

# Menus, Franchises, and Business for Basta Fazoolin'
brunch = Menu('Brunch', brunchitems, '1100', '1600')
early_bird = Menu('Early Bird', earltbirditems, '1500', '1800')
dinner = Menu('Dinner', dinneritems, '1700', '2300')
kids = Menu('Kids', kidsitems, '1100', '2100')

flagship_store = Franchise('1232 West End Road', [brunch, early_bird, dinner, kids])
new_installment = Franchise('12 East Mulberry Street', [brunch, early_bird, dinner, kids])

basta_fazoolin = Business('Basta Fazoolin\' with my Heart', [flagship_store, new_installment])

# Menus, Franchises, and Business for Take a’ Arepa
arepasitems = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}

arepas_menu = Menu('Arepas', arepasitems, '1000', '2000')

arepas_place = Franchise('189 Fitzgerald Avenu', [arepas_menu])

take_arepa = Business('Take a\' Arepa', [arepas_place])

# print(brunch)
# print(early_bird)
# print(dinner)
# print(kids)
# print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
# print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))
# print(new_installment.available_menus(1700))

# print(arepas_menu, arepas_menu.items)
# print(arepas_place, arepas_place.menus)
