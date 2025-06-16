1. Write a Python program to create a class representing a Circle. Include methods
 to calculate its area and perimeter.
import math

class Doira:
    def __init__(self,radius):
        self.radius=radius

    def yuza (self):
        return math.pi*self.radius**2
    def perimetr(self):
        return 2* math.pi*self.radius
    r=float(input())
    doira=Doira(r)
    print(f'Doirani yuzi: {doira.yuza():}')
    print(f'Doira perimetri {doira.perimetr():}')

2.Write a Python program to create a Person class. Include attributes like name, country, and 
date of birth. Implement a method to determine the person's age.
from datetime import date

class Shaxs:
    def __init__(self, ism, davlat, tugilgan_yil):
        self.ism = ism
        self.davlat = davlat
        self.tugilgan_yil = int(tugilgan_yil)
    def yosh(self):
        hozorgi_yil=date.today().year
        return hozorgi_yil-self.tugilgan_yil
    
    ism=input("Izm kirit")
    davlat=input("Davlat kirit")
    t_yil=input()
    
    shaxs= Shaxs(ism, davlat, t_yil)
    print(f'\n{shaxs.ism}({shaxs.davlat})hozirda{shaxs.yosh()} yoshda')

3.Write a Python program to create a Calculator class. Include methods 
for basic arithmetic operations.
class c:
    def plus(self,a,b):
        return a+b
    def minus(self,a,b):
        return a-b
    def kopayt(self,a,b):
        return a*b
    def boliv (self,a,b):
        if b==0:
            return "0 ga bo\‘lish mumkin emas!"
        return a/b
    

a=float(input())
b=float(input())
calc = c()
print(f'{a}-{b}= {calc.minus(a,b)}')
print(f'{a}/{b}= {calc.boliv(a,b)}')
print(f'{a}+{b}= {calc.plus(a,b)}')
print(f'{a}*{b}= {calc.kopayt(a, b)}')

4.Write a Python program to create a class that represents a 
shape. Include methods to calculate its area and perimeter. Implement
subclasses for different shapes like Circle, Triangle, and Square.

import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclassda area metodini yozish kerak")
    
    def perimeter(self):
        raise NotImplementedError("Subclassda perimeter metodini yozish kerak")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return 4 * self.side

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3
    
    def area(self):
        # Heron formulasi yordamida yuzani hisoblaymiz
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

# Misol uchun ishlatish:
aylana = Circle(5)
print(f"Aylana yuzasi: {aylana.area():.2f}")
print(f"Aylana perimetri: {aylana.perimeter():.2f}")

kvadrat = Square(4)
print(f"Kvadrat yuzasi: {kvadrat.area():.2f}")
print(f"Kvadrat perimetri: {kvadrat.perimeter():.2f}")

uchburchak = Triangle(3, 4, 5)
print(f"Uchburchak yuzasi: {uchburchak.area():.2f}")
print(f"Uchburchak perimetri: {uchburchak.perimeter():.2f}")

5.Write a Python program to create a class representing a binary search tree. 
Include methods for inserting and searching for elements in the binary tree.

class Node:
    """Binary Search Tree tuguni"""
    def __init__(self, kalit):
        self.kalit = kalit  # tugundagi qiymat
        self.chap = None    # chap farzand
        self.ong = None     # o‘ng farzand

class BinarySearchTree:
    """Binary Search Tree klassi"""
    def __init__(self):
        self.korinish = None  # daraxtning ildizi (root)

    def qo‘shish(self, kalit):
        """Daraxtga yangi kalit qo‘shish"""
        if self.korinish is None:
            self.korinish = Node(kalit)
        else:
            self._rekursiv_qo‘shish(self.korinish, kalit)

    def _rekursiv_qo‘shish(self, joriy, kalit):
        if kalit < joriy.kalit:
            if joriy.chap is None:
                joriy.chap = Node(kalit)
            else:
                self._rekursiv_qo‘shish(joriy.chap, kalit)
        elif kalit > joriy.kalit:
            if joriy.ong is None:
                joriy.ong = Node(kalit)
            else:
                self._rekursiv_qo‘shish(joriy.ong, kalit)
        else:
            print(f"{kalit} kaliti allaqachon daraxtda mavjud.")

    def qidirish(self, kalit):
        """Berilgan kalitni daraxtda qidirish"""
        return self._rekursiv_qidirish(self.korinish, kalit)

    def _rekursiv_qidirish(self, joriy, kalit):
        if joriy is None:
            return False
        if kalit == joriy.kalit:
            return True
        elif kalit < joriy.kalit:
            return self._rekursiv_qidirish(joriy.chap, kalit)
        else:
            return self._rekursiv_qidirish(joriy.ong, kalit)

# Namuna:
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.qo‘shish(50)
    bst.qo‘shish(30)
    bst.qo‘shish(70)
    bst.qo‘shish(20)
    bst.qo‘shish(40)
    bst.qo‘shish(60)
    bst.qo‘shish(80)

    print("60 ni qidirish:", bst.qidirish(60))  # True
    print("25 ni qidirish:", bst.qidirish(25))  # False
  
  6.Write a Python program to create a class representing a stack data structure.
 Include methods for pushing and popping elements.

class Stack:
    """Stack (steck) ma'lumotlar tuzilmasi"""
    def __init__(self):
        self.obyektlar = []

    def push(self, element):
        """Stack'ga yangi element qo‘shish"""
        self.obyektlar.append(element)
        print(f"{element} stack'ga qo‘shildi.")

    def pop(self):
        """Stack'dan elementni olib tashlash (oxirgi qo‘shilgan)"""
        if self.boshmi():
            print("Stack bo‘sh — olib tashlash mumkin emas.")
            return None
        else:
            olingan = self.obyektlar.pop()
            print(f"{olingan} stack'dan olib tashlandi.")
            return olingan

    def boshmi(self):
        """Stack bo‘shligini tekshirish"""
        return len(self.obyektlar) == 0

    def korish(self):
        """Stack'dagi elementlarni ko‘rsatish"""
        print("Stack:", self.obyektlar)

# Namuna:
if __name__ == "__main__":
    steck = Stack()
    steck.push(10)
    steck.push(20)
    steck.push(30)
    steck.korish()
    steck.pop()
    steck.korish()
    steck.pop()
    steck.pop()
    steck.pop()  # Bo‘sh holatda olib tashlash

7.Write a Python program to create a class representing a linked list data structure. Include methods 
for displaying linked list data, inserting, and deleting nodes.
# Tugun (Node) klassi

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List klassi
class LinkedList:
    def __init__(self):
        self.head = None

    # Ma'lumot qo‘shish (oxiriga)
    def qoshish(self, data):
        yangi = Node(data)
        if self.head is None:
            self.head = yangi
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = yangi
        print(f"{data} qo‘shildi.")

    # Ma'lumot o‘chirish (qiymat bo‘yicha)
    def ochirish(self, data):
        temp = self.head
        old = None

        while temp and temp.data != data:
            old = temp
            temp = temp.next

        if temp is None:
            print(f"{data} topilmadi.")
            return

        if old is None:
            self.head = temp.next  # boshidagi tugun
        else:
            old.next = temp.next  # o‘rtadagi yoki oxiridagi tugun

        print(f"{data} o‘chirildi.")

    # Ma'lumotlarni ko‘rsatish
    def korsat(self):
        if self.head is None:
            print("Ro'yxat bo‘sh.")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Namuna
ll = LinkedList()
ll.qoshish(10)
ll.qoshish(20)
ll.qoshish(30)
ll.korsat()

ll.ochirish(20)
ll.korsat()

ll.ochirish(50)  # mavjud bo'lmagan qiymat

8.Write a Python program to create a class representing a shopping cart. Include methods for adding and removing
 items, and calculating the total price.
class Savatcha:
    def __init__(self):
        self.mahsulotlar = {}

    def qoshish(self, nomi, narxi, soni):
        if nomi in self.mahsulotlar:
            self.mahsulotlar[nomi]['soni'] += soni
        else:
            self.mahsulotlar[nomi] = {'narxi': narxi, 'soni': soni}
        print(f"{nomi} qo‘shildi.")

    def ochirish(self, nomi):
        if nomi in self.mahsulotlar:
            del self.mahsulotlar[nomi]
            print(f"{nomi} olib tashlandi.")
        else:
            print(f"{nomi} topilmadi.")

    def jami_narx(self):
        jami = 0
        for m in self.mahsulotlar.values():
            jami += m['narxi'] * m['soni']
        return jami

    def korsat(self):
        if not self.mahsulotlar:
            print("Savatcha bo‘sh.")
        else:
            print("Savatchadagi mahsulotlar:")
            for nomi, info in self.mahsulotlar.items():
                print(f"{nomi}: {info['soni']} dona x {info['narxi']} so‘m")
            print(f"Jami narx: {self.jami_narx()} so‘m")

# Namuna
sav = Savatcha()
sav.qoshish("Olma", 3000, 2)
sav.qoshish("Non", 2000, 1)
sav.korsat()

sav.ochirish("Non")
sav.korsat()

9. Write a Python program to create a class representing a stack data structure. Include methods for
 pushing, popping, and displaying elements.

 class Stack:
    def __init__(self):
        self.uyum = []

    def push(self, element):
        self.uyum.append(element)
        print(f"{element} qo‘shildi.")

    def pop(self):
        if len(self.uyum) == 0:
            print("Stack bo‘sh. Olib bo‘lmaydi.")
        else:
            chiqarilgan = self.uyum.pop()
            print(f"{chiqarilgan} olib tashlandi.")

    def show(self):
        if len(self.uyum) == 0:
            print("Stack bo‘sh.")
        else:
            print("Stackdagi elementlar (tepadan pastga):")
            for element in reversed(self.uyum):
                print(element)

# Namuna
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.show()

s.pop()
s.show()

10.Write a Python program to create a class representing a queue data structure. Include methods for
 enqueueing and dequeueing elements.

 class Queue:
    def __init__(self):
        self.navbat = []

    def enqueue(self, element):
        self.navbat.append(element)
        print(f"{element} navbatga qo‘shildi.")

    def dequeue(self):
        if len(self.navbat) == 0:
            print("Navbat bo‘sh. Olib bo‘lmaydi.")
        else:
            chiqarilgan = self.navbat.pop(0)
            print(f"{chiqarilgan} navbatdan olib tashlandi.")

    def show(self):
        if len(self.navbat) == 0:
            print("Navbat bo‘sh.")
        else:
            print("Navbatdagi elementlar:")
            for element in self.navbat:
                print(element)

# Namuna
q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.show()

q.dequeue()
q.show()

11.Write a Python program to create a class representing a bank. Include methods for managing
 customer accounts and transactions.
 class Bank:
    def __init__(self):
        self.accounts = {}  # mijozlar ro'yxati: ism -> balans

    def add_account(self, name):
        if name in self.accounts:
            print(f"{name} allaqachon mavjud.")
        else:
            self.accounts[name] = 0
            print(f"{name} uchun hisob ochildi.")

    def deposit(self, name, amount):
        if name in self.accounts:
            self.accounts[name] += amount
            print(f"{amount} so'm {name} hisobiga qo‘shildi.")
        else:
            print(f"{name} topilmadi.")

    def withdraw(self, name, amount):
        if name in self.accounts:
            if self.accounts[name] >= amount:
                self.accounts[name] -= amount
                print(f"{amount} so'm {name} hisobidan yechildi.")
            else:
                print("Hisobda yetarli mablag‘ yo‘q.")
        else:
            print(f"{name} topilmadi.")

    def show_balance(self, name):
        if name in self.accounts:
            print(f"{name} balansi: {self.accounts[name]} so'm")
        else:
            print(f"{name} topilmadi.")

# Namuna
bank = Bank()
bank.add_account("Ali")
bank.deposit("Ali", 100000)
bank.withdraw("Ali", 30000)
bank.show_balance("Ali")

bank.withdraw("Ali", 80000)  # yetarli mablag‘ yo‘q
bank.show_balance("Vali")    # mavjud bo‘lmagan hisob


























