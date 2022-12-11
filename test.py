from os import system

class menu:
  def __init__(self, food, price):
    self.item = food
    self.pay = price

  def takeaway(self):
    print(self.item, self.pay)

class sub_menu(menu):
  pass

x = sub_menu("beef", 10)

x.takeaway()

