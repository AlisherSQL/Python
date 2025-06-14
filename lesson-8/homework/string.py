1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
try:
    a=int(input())
    b=int(input())
    q= a/b
    print(f'Javob: {q}')
except ZeroDivisionError as e:
    print(f'Javob:  {e}')
except :
    print('No')
2. Write a Python program that prompts the user to input an integer and raises 
a ValueError exception if the input is not a valid integer.
try:
    a=int(input())
    print(f'Javob {a}')
except ValueError :
    print('Javob ')

3. Write a Python program that opens a file and handles a FileNotFoundError
exception if the file does not exist.
try:
    w=input()
    with open (w,'r') as file:
        content=file.read
    print('Fayll')
    print(content)
except FileNotFoundError:
    print('Fayl No')

4.Write a Python program that prompts the user to input two numbers and
raises a TypeError exception if the inputs are not numerical.
try:
    a=float(input())
    b=float(input())
    print('Javob ')
except TypeError:
    print("TypeError")
    
5.Write a Python program that opens a file and handles a PermissionError
exception if there is a permission issue.
  try:
    a=input()
    with open (a, 'w') as f:
        f.write
        print("Bir nima")
except PermissionError:
    print('No')

6.Write a Python program that executes an operation on a list and
    handles an IndexError exception if the index is out of range.
my_list = [10, 20, 30, 40, 50]

try:
    index=int(input())
    print(f"Index: {my_list[index]}")
except IndexError:
    print("Bunaka Index yok")
except ValueError:
    print ("No")

7.Write a Python program that prompts the user to input a number 
and handles a KeyboardInterrupt exception if the user cancels the input.

try:
    number = float(input("Iltimos, biror son kiriting: "))
    print(f"Siz kiritgan son: {number}")
except KeyboardInterrupt:
    print("\nKiritish bekor qilindi (Ctrl+C bosildi).")
except ValueError:
    print("Xatolik: Bu son emas.")

8.Write a Python program that executes division and handles 
an ArithmeticError exception if there is an arithmetic error.
try:
    a = float(input("Birinchi sonni kiriting: "))
    b = float(input("Ikkinchi sonni kiriting: "))
    result = a / b
    print(f"Natija: {result}")
except ArithmeticError as e:
    print(f"Arifmetik xatolik: {e}")
except ValueError:
    print("Xatolik: Faqat son kiriting.")
9.Write a Python program that opens a file and handles 
a UnicodeDecodeError exception if there is an encoding issue.
try:
    filename = input("Fayl nomini kiriting: ")
    with open(filename, 'r') as file:
        content = file.read()
        print(content)
except UnicodeDecodeError:
    print("Xatolik: Faylni o'qishda kodlash muammosi yuz berdi.")
except FileNotFoundError:
    print("Xatolik: Fayl topilmadi.")

10. Write a Python program that executes a list operation and handles an AttributeError
exception if the attribute does not exist.
  my_list = [1, 2, 3, 4, 5]

try:
    
    my_list.appendd(6)  
except AttributeError as e:
    print(f"Xatolik: {e}")
else:
    print("Amal muvaffaqiyatli bajarildi:", my_list)

1.Write a Python program to read an entire text file.
def num(w):
    try:
        with open(w,'r') as s:
            r = s.read()
            print('Hello')
            print(f'{r}')
    except FileNotFoundError:
        print('File not found.')
    except Exception as e:
        print(f'An error occurred: {e}')
num('a.txt')
2.Write a Python program to read first n lines of a file.
def num ():
    ss=input()
    try:
        with open (ss,'r') as d:
            con=d.readline()
            print("Hello")
            print(con)
    except Exception:
        print("No")
num() 
3.Write a Python program to append text to a file and display the text.
def num ():
    ss=input()
    try:
        with open (ss,'a') as d:
            d.write("wouuu \n")
            print("Hello")
            # print(d)
    except Exception:
        print("No")
num() 
4.Write a Python program to read last n lines of a file.
def num (s,n):
    try:
        with open (s,'r') as d:
            con=d.readlines()
            las_l=con[-n:]
            for co in las_l:
                # print("OOK")
                print(co.strip())
    except Exception:
        print ('No')
num('a.txt',3)

5.Write a Python program to read a file line by line and store it into a list.
def num ():
    a=input()
    ss=[]
    try:
        with open (a,'r') as d:
           for s in d:
             ss.append(s.strip())
        return ss
    except Exception:
        print('No')

num()

6.Write a Python program to read a file line by line and store it into a variable.
def num ():
    a=input()

    try:
        with open (a, 'r') as d:
          matn= ""
          for s in d:
            matn +=s
        return matn 
    except Exception:
        print('No')
        return ""
print(num())

7.Write a Python program to read a file line by line and store it into an array.
def faylni_royxatga_olish(fayl_nomi):
    royxat = []
    try:
        with open(fayl_nomi, 'r', encoding='utf-8') as fayl:
            royxat = fayl.readlines()
            
            royxat = [qator.strip() for qator in royxat]
    except FileNotFoundError:
        print(f"'{fayl_nomi}' nomli fayl topilmadi.")
    return royxat


fayl_nomi = 'namuna.txt'  
qatorlar = faylni_royxatga_olish(fayl_nomi)
print(qatorlar)

8.Write a Python program to find the longest words.
def num (w):
    with open (w,'r') as d:
        con=d.read()
        qq=con.strip().split()
        if qq: dd=max(qq,key=len)
    return dd
print(num('a.txt'))

9.Write a Python program to count the number of lines in a text file.

def num (w):
    with open (w,'r') as dd:
        # count=0
        con=dd.read()
        qq=con.strip().split()
        return len(qq)
    # return count
print(num('a.txt'))

10.Write a Python program to count the frequency of words in a file.
fayl_nomi = input("Fayl nomini kiriting: ")

try:
 
    with open(fayl_nomi, 'r', encoding='utf-8') as fayl:
        matn = fayl.read()


    matn = matn.lower()

  
    for belgi in '.,!?":;()[]{}\n':
        matn = matn.replace(belgi, ' ')

   
    sozlar = matn.split()

 
    chastota = {}

  
    for soz in sozlar:
        if soz in chastota:
            chastota[soz] += 1
        else:
            chastota[soz] = 1

   
    for soz in chastota:
        print(f"{soz}: {chastota[soz]}")

except FileNotFoundError:
    print("❗ Fayl topilmadi.")






















