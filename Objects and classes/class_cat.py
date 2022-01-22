# You can start with the
# Cat class or erase this
# and use your own!
class Cat:
  def __init__(self, input_name, input_breed, input_age = 0):
    self.name = input_name
    self.breed = input_breed
    self.age = input_age
    self.is_cuddly = True
    self.has_cuddled = []
  
  # Create method to change
  def change_name(self, new_name):
    self.name = new_name
    print(self.name)
  # at least one attribute.
  
  def cat_cuddling(self, second_pet):
    if self.is_cuddly == True:
      if second_pet.is_cuddly == True:
        self.has_cuddled.append(second_pet.name)
        second_pet.has_cuddled.append(self.name)
        print("{name} and {other_name} are cuddling together".format(name = self.name, other_name = second_pet.name))
  
  def __repr__(self):
    if len(self.has_cuddled) ==1:
      cuddle_number = 'cat'
    else:
      cuddle_number = 'cats'
    description = "This cat's name is {cat_name}, they are a {cat_breed}, and are {cat_age} years old. {cat_name} has cuddled with {cuddle_number} other {if_cats}.".format(cat_name = self.name, cat_breed = self.breed, cat_age = self.age, cuddle_number = len(self.has_cuddled), if_cats = cuddle_number)
    return description




first_cat = Cat("Prince", "Himalayen", 10)


# Create your new pet.
new_cat = Cat("Leo", "Tabby", 3)
new_cat3 = Cat("Stubby", "Tabby", 4)
# Call your method on your


new_cat.change_name("Kitty")
first_cat.cat_cuddling(new_cat)
first_cat.cat_cuddling(new_cat3)
print(new_cat.has_cuddled)



print('\n', first_cat, '\n')
