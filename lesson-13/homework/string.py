1.Age Calculator: Ask the user to enter their birthdate. Calculate 
and print their age in years, months, and days

from datetime import datetime
from dateutil.relativedelta import relativedelta
sana22=input()
tug_k=datetime.strptime(sana22, '%Y-%m-%d')
bugun=datetime.today()
farrk= relativedelta (bugun,tug_k)
print(f'Yoshiz: {farrk.years} yil, {farrk.months} oy, {farrk.days} kun')

2.Days Until Next Birthday: Similar to the first exercise, but this time, calculate and print the number of days 
remaining until the user's next birthday

from datetime import *

sana23=input()
tyg_ku=datetime.strptime(sana23, '%Y-%m-%d')

bugun=datetime(2025,3,4)

fa=tyg_ku-bugun
print(f'keyingi tug kunga {fa} kun koldi')


3.Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of 
a meeting in hours and minutes. Calculate and print the date and 
time when the meeting will end.

from datetime import datetime,timedelta

maj_bosh_vak=input()
tugash_vak=datetime.strptime(maj_bosh_vak, '%Y-%m-%d %H:%M')
soat=int(input())
dakika=int(input())

davomilik= timedelta(hours=soat, minutes=dakika)

tug_vv=tugash_vak+davomilik

print("Uchrashuv tugash vaqti:", tug_vv.strftime("%Y-%m-%d %H:%M"))

4.Timezone Converter: Create a program that allows the user to enter a date and time 
along with their current timezone, and then convert and print the date and time in another 
timezone of their choice

from datetime import datetime
import pytz

# 1. Foydalanuvchidan sana, vaqt va vaqt zonasini olish
sana_vaqt_str = input("Sana va vaqtni kiriting (YYYY-MM-DD HH:MM): ")
joriy_zona_nomi = input("Joriy vaqt zonasini kiriting (masalan, Asia/Tashkent): ")
maqsad_zona_nomi = input("Qaysi vaqt zonasiga o‘tkazmoqchisiz? (masalan, America/New_York Europe/London): ")

# 2. Matndan datetime obyekt yaratish
sana_vaqt = datetime.strptime(sana_vaqt_str, "%Y-%m-%d %H:%M")

# 3. Vaqt zonalarini olish
joriy_zona = pytz.timezone(joriy_zona_nomi)
maqsad_zona = pytz.timezone(maqsad_zona_nomi)

# 4. Vaqtga zona biriktirish (aware datetime)
sana_vaqt_joriy = joriy_zona.localize(sana_vaqt)

# 5. Boshqa zonaga o‘tkazish
sana_vaqt_maqsad = sana_vaqt_joriy.astimezone(maqsad_zona)

# 6. Natijani chiqarish
print("=== Natija ===")
print("Joriy zonadagi vaqt:", sana_vaqt_joriy.strftime("%Y-%m-%d %H:%M (%Z)"))
print("Maqsad zonadagi vaqt:", sana_vaqt_maqsad.strftime("%Y-%m-%d %H:%M (%Z)"))

5.Countdown Timer: Implement a countdown timer. Ask the user to input a future date 
and time, and then continuously print the time remaining until that point in 
regular intervals (e.g., every second)


from datetime import datetime
import time

ber_v=input()
beer_vva=datetime.strptime(ber_v,'%Y-%m-%d %H:%M:%S')

while True:
    hoz_v=datetime.now()
    qol_w=beer_vva-hoz_v

    if qol_w.total_seconds()<=0:
            print("Vakt tugadi")
            break

    kunlar=qol_w.days
    sekundlar=qol_w.seconds
    soat=sekundlar//3600
    minut=(sekundlar%3600)//60
    sekund=sekundlar%60
    print(f'Qolgan vakt: {kunlar} kunlar, {soat} soat, {minut} minut, {sekund} sekund',end='\r')

    time.sleep(1)


6.Email Validator: Write a program that validates email addresses. Ask the
user to input an email address, and 
check if it follows a valid email format


email = input("Email manzilingizni kiriting: ")

if "@" in email and "." in email:
    at_index = email.index("@")
    dot_index = email.rfind(".")
    
    if 0 < at_index < dot_index < len(email) - 1:
        print("✅ Email manzilingiz to‘g‘ri formatda.")
    else:
        print("❌ Email noto‘g‘ri: belgilar noto‘g‘ri joylashgan.")
else:
    print("❌ Email noto‘g‘ri: '@' yoki '.' yetishmayapti.")


7. Phone Number Formatter: Create a program that takes a phone number as input and 
formats it according to a standard format. For example, convert
  "1234567890" to "(123) 456-7890"
  
son = input()

if son.isdigit() and len(son)==10:
    new_son = f'({son[0:3]}){son[3:6]}-{son[6:9]}-{son[9:13]}'
    print(new_son)
else: 
    print('No')  

8. Password Strength Checker: Implement a password strength checker. Ask the user to input a password and check
if it meets certain criteria (e.g., minimum length, contains at least one uppercase letter,
one lowercase letter, and one digit).


Parol=input()

if len(Parol)>5:
    print('\u274c' "Parol uzun")
elif len(Parol)<5:
     print('\u274c' "Parol kichik")
elif not any(s.isupper() for s in Parol):
    print('\u274c'  "Parolga bitta Katta harif kiritilmagan")
elif not any(s.islower() for s in Parol):
    print('\u274c'  "Parolda bitta kichik harf yok")
elif not any(s.isdigit() for s in Parol):
    print('\u274c'  'son kirit son yok')
elif not "@" in Parol:
    print('\u274c'  "'@' yok")
else:
    print('Hammasi zor' '\u2705')


9.Word Finder: Develop a program that finds all occurrences of a specific word in a
given text. Ask the user to input a word, and then search for and print all 
occurrences of that word in a sample text

matn = """
Python dasturlash tili oson va qulay. Python va yordamida siz web dasturlar, sun’iy intellekt, 
data analysis, va boshqa ko‘plab sohalarda Tili tili ishlash mumkin. Python ayniqsa yangi boshlovchilar va uchun juda foydali.
"""

soz= input().lower()
matt=matn.lower()
sooz=matt.split()
x=sooz.count(soz)
if x>0:
    print (f'SHu soz "{soz}"  {x} ta joyda bor ')
else:
    print(f" \u274c Bunaka '{soz}' yok")

index=0
while True:
    index = matt.find(soz,index)
    if index==-1:
        break
    print(f'Indexi: {index} da')
    index=index+1










