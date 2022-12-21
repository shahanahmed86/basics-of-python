class Student:
  def __init__(self, name, major, gpa, is_on_probation):
    self.name = name
    self.major = major
    self.gpa = gpa
    self.is_on_probation = is_on_probation

  def on_honor_role(self):
    return self.gpa >= 3.5


class Question:
  def __init__(self, prompt, answer):
    self.prompt = prompt
    self.answer = answer

class Chef:
  def make_chicken(self):
    print('The chef makes a chicken')
  def make_salad(self):
    print('The chef makes a salad')
  def make_special_dish(self):
    print('The chef makes BBQ ribs')

class ChineseChef(Chef):
  def make_fried_rice(self):
    print('The chef makes fried rice')
  def make_special_dish(self):
    print('The chef makes orange chicken')
