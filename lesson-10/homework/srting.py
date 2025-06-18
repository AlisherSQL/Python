1.Create a Task class with attributes such as task title, description, due date, and status.
class Task:
    def __init__(self, sarlavha, tavsif, muddat, holat="Bajarilmagan"):
        self.sarlavha = sarlavha
        self.tavsif = tavsif
        self.muddat = muddat
        self.holat = holat

    def korsat(self):
        print(f"Vazifa: {self.sarlavha}")
        print(f"Tavsif: {self.tavsif}")
        print(f"Muddat: {self.muddat}")
        print(f"Holat: {self.holat}")

# Namuna ishlatish
vazifa = Task("Dars tayyorlash", "Python darsini tayyorlash", "2025-06-20")
vazifa.korsat()

2.Define ToDoList Class:
Create a ToDoList class that manages a list of tasks.
class ToDoList:
    def __init__(self):
        self.vazifalar = []  # har bir element: {'nom': str, 'bajarildi': bool}

    def add_task(self, nom):
        self.vazifalar.append({'nom': nom, 'bajarildi': False})
        print(f'"{nom}" vazifasi qo‘shildi.')

    def mark_complete(self, nom):
        for vazifa in self.vazifalar:
            if vazifa['nom'] == nom:
                vazifa['bajarildi'] = True
                print(f'"{nom}" vazifasi bajarildi deb belgilandi.')
                return
        print(f'"{nom}" vazifasi topilmadi.')

    def list_all(self):
        if not self.vazifalar:
            print("Vazifalar mavjud emas.")
            return
        print("Barcha vazifalar:")
        for vazifa in self.vazifalar:
            status = "Bajarildi" if vazifa['bajarildi'] else "Bajarilmagan"
            print(f"- {vazifa['nom']} [{status}]")

    def list_incomplete(self):
        incomplete = [v for v in self.vazifalar if not v['bajarildi']]
        if not incomplete:
            print("Barcha vazifalar bajarilgan.")
            return
        print("Bajarilmagan vazifalar:")
        for vazifa in incomplete:
            print(f"- {vazifa['nom']}")

# Namuna ishlatish
todo = ToDoList()
todo.add_task("Dars tayyorlash")
todo.add_task("Uy ishlarini bajarish")

todo.list_all()
todo.mark_complete("Dars tayyorlash")
todo.list_incomplete()

3.Create Main Program:
Develop a simple CLI to interact with the ToDoList.
Include options to add tasks, mark tasks as complete, list all tasks, and display only incomplete tasks.

class ToDoList:
    def __init__(self):
        self.vazifalar = []

    def add_task(self, nom):
        self.vazifalar.append({'nom': nom, 'bajarildi': False})
        print(f'"{nom}" vazifasi qo‘shildi.')

    def mark_complete(self, nom):
        for vazifa in self.vazifalar:
            if vazifa['nom'] == nom:
                vazifa['bajarildi'] = True
                print(f'"{nom}" vazifasi bajarildi deb belgilandi.')
                return
        print(f'"{nom}" vazifasi topilmadi.')

    def list_all(self):
        if not self.vazifalar:
            print("Vazifalar mavjud emas.")
            return
        print("Barcha vazifalar:")
        for vazifa in self.vazifalar:
            status = "Bajarildi" if vazifa['bajarildi'] else "Bajarilmagan"
            print(f"- {vazifa['nom']} [{status}]")

    def list_incomplete(self):
        incomplete = [v for v in self.vazifalar if not v['bajarildi']]
        if not incomplete:
            print("Barcha vazifalar bajarilgan.")
            return
        print("Bajarilmagan vazifalar:")
        for vazifa in incomplete:
            print(f"- {vazifa['nom']}")

def main():
    todo = ToDoList()
    while True:
        print("\n--- ToDoList Menyu ---")
        print("1. Vazifa qo‘shish")
        print("2. Vazifani bajarildi deb belgilash")
        print("3. Barcha vazifalarni ko‘rsatish")
        print("4. Faqat bajarilmagan vazifalarni ko‘rsatish")
        print("5. Chiqish")

        tanlov = input("Tanlovingizni kiriting (1-5): ")

        if tanlov == "1":
            nom = input("Vazifa nomini kiriting: ")
            todo.add_task(nom)
        elif tanlov == "2":
            nom = input("Bajarildi deb belgilanishi kerak bo‘lgan vazifa nomi: ")
            todo.mark_complete(nom)
        elif tanlov == "3":
            todo.list_all()
        elif tanlov == "4":
            todo.list_incomplete()
        elif tanlov == "5":
            print("Dastur tugadi. Xayr!")
            break
        else:
            print("Noto‘g‘ri tanlov. Qayta urinib ko‘ring.")

if __name__ == "__main__":

4.Test the Application:
Create instances of tasks and test the functionality of your ToDoList.

todo = ToDoList()
todo.add_task("Dars tayyorlash")
todo.add_task("Uy ishlarini bajarish")
todo.add_task("Kitob o‘qish")

print("\n--- Barcha vazifalar ---")
todo.list_all()

# 2. Vazifani bajarildi deb belgilash
todo.mark_complete("Uy ishlarini bajarish")

print("\n--- Bajarilmagan vazifalar ---")
todo.list_incomplete()

print("\n--- Barcha vazifalar ---")
todo.list_all()

# 3. Noto‘g‘ri vazifa nomini bajarildi deb belgilashga urinish
todo.mark_complete("Sport bilan shug‘ullanish")

1.Define Post Class:
Create a Post class with attributes like title, content, and author.


todo = ToDoList()

# 1. Vazifalarni qo‘shamiz
todo.add_task("Dars tayyorlash")
todo.add_task("Uy ishlarini bajarish")
todo.add_task("Kitob o‘qish")

print("\n--- Barcha vazifalar ---")
todo.list_all()

# 2. Vazifani bajarildi deb belgilash
todo.mark_complete("Uy ishlarini bajarish")

print("\n--- Bajarilmagan vazifalar ---")
todo.list_incomplete()

print("\n--- Barcha vazifalar ---")
todo.list_all()

# 3. Noto‘g‘ri vazifa nomini bajarildi deb belgilashga urinish
todo.mark_complete("Sport bilan shug‘ullanish")

2.Define Blog Class:
Create a Blog class that manages a list of posts.
Include methods to add a post, list all posts, and display posts by a specific author.

class Blog:
    def __init__(self):
        self.posts = []  # har bir post: {'sarlavha': str, 'muallif': str, 'matn': str}

    def add_post(self, sarlavha, muallif, matn):
        self.posts.append({'sarlavha': sarlavha, 'muallif': muallif, 'matn': matn})
        print(f'"{sarlavha}" nomli post qo‘shildi.')

    def list_all_posts(self):
        if not self.posts:
            print("Hech qanday post mavjud emas.")
            return
        print("Barcha postlar:")
        for post in self.posts:
            print(f"- {post['sarlavha']} (Muallif: {post['muallif']})")

    def list_posts_by_author(self, muallif):
        author_posts = [p for p in self.posts if p['muallif'] == muallif]
        if not author_posts:
            print(f'"{muallif}" muallifining postlari topilmadi.')
            return
        print(f'"{muallif}" muallifining postlari:')
        for post in author_posts:
            print(f"- {post['sarlavha']}")

# Namuna ishlatish
blog = Blog()
blog.add_post("Python haqida", "Ali", "Python dasturlash tili haqida maqola.")
blog.add_post("Dasturlash", "Vali", "Dasturlash asoslari haqida.")
blog.add_post("Python darslari", "Ali", "Python bo‘yicha darslik.")

blog.list_all_posts()
blog.list_posts_by_author("Ali")

1.Define Account Class:
Create an Account class with attributes like account number, account holder name, and balance.

class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def show_info(self):
        print(f"Hisob raqami: {self.account_number}")
        print(f"Egasi: {self.holder_name}")
        print(f"Balans: {self.balance} so'm")

# Namuna ishlatish
hisob = Account("1234567890", "Ali", 100000)
hisob.show_info()

2.Define Bank Class:
Create a Bank class that manages a list of accounts.
Include methods to add an account, check balance, deposit money, and withdraw money.

class Bank:
    def __init__(self):
        self.accounts = {}  # hisob raqami: balans

    def add_account(self, account_number, initial_balance=0):
        self.accounts[account_number] = initial_balance
        print(f"Hisob qo‘shildi: {account_number}")

    def check_balance(self, account_number):
        if account_number in self.accounts:
            print(f"{account_number} hisobidagi balans: {self.accounts[account_number]} so'm")
        else:
            print("Hisob topilmadi.")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number] += amount
            print(f"{amount} so'm qo‘shildi. Yangi balans: {self.accounts[account_number]} so'm")
        else:
            print("Hisob topilmadi.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number] >= amount:
                self.accounts[account_number] -= amount
                print(f"{amount} so'm yechildi. Yangi balans: {self.accounts[account_number]} so'm")
            else:
                print("Hisobda yetarli mablag‘ yo‘q.")
        else:
            print("Hisob topilmadi.")

# Namuna ishlatish
bank = Bank()
bank.add_account("1234", 50000)
bank.check_balance("1234")
bank.deposit("1234", 10000)
bank.withdraw("1234", 20000)
bank.check_balance("1234")
bank.withdraw("1234", 50000)  # Mablag‘ yetarli emas




























