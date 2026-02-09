# Абстракция
# Abstract class
# Абстратными классами называются:
# 1) обязательные к реализации методы
# 2) от абстрактного класса нельзя создать экземляр


from abc import ABC, abstractmethod

# class AbstractClass():
#     def test(self):
#         raise NotImplementedError

class AbstractClass(ABC):
    @abstractmethod
    def test(self):
        pass

class ChildClass(AbstractClass):
    def test(self):
        return 'реализация'


# obj_abc = AbstractClass()
obj_child = ChildClass()

print(obj_child.test())