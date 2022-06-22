# # Создать класс Dog. Класс имеет четыре атрибута: height, weight, name, age. Класс
# # имеет три метода: jump, run, bark. Каждый метод выводит сообщение на экран.
# # Создать объект класса Dog, вызвать все методы объекта и вывести на экран все его атрибуты
#
# class Dog:
#
#      def __init__(self, name, age, height,  weight):
#          self.name = name
#          self.age = age
#          self.height = height
#          self.weight = weight
#
#      def jump(self, m):
#         return f" прыжок {self.name}, {m} метров"
#
#      def run(self, km):
#         return f" {self.name} пробежал, {km} км"
#
#      def bark(self, wof_wof):
#         return f" {self.name} подаёт голос {wof_wof}"
#
#
# dog1 = Dog("Lola", 3, 15, 34)
# dog2 = Dog("bob", 7, 17, 50)
# print(dog1.__dict__)
# print(dog1.jump(5),dog1.run(7),dog1.bark("wof_wof"))
# print(dog1.__dict__)
# print(dog1.jump(6), dog1.run(9), dog1.bark("wof_wof"))
#
# # Добавить в класс Dog метод change_name. Метод принимает на вход новое имя и меняет
# # атрибут имени у объекта. Создать один объект класса. Вывести имя.Вызвать метод change_name. Вывести имя.
#
# class Dog:
#
#     def __init__(self, name, age, height, weight):
#         self.name = name
#         self.age = age
#         self.height = height
#         self.weight = weight
#
#     def jump(self, m):
#         return f" прыжок {self.name}, {m} метров"
#
#     def run(self, km):
#         return f" {self.name} пробежал, {km} км"
#
#     def bark(self, wof_wof):
#         return f" {self.name} подаёт голос {wof_wof}"
#
#     def change_name(self, new_name):
#         self.name = new_name
#
#
# dog1 = Dog("Lola", 3, 15, 34)
# dog2 = Dog("bob", 7, 17, 50)
# dog1.change_name("Lili")
# print(dog1.__dict__)

