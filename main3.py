import asyncio

# Parolni tekshiruvchi asinxron funksiya
async def check_password():
    while True:
        password = input("Enter password: ")  # Foydalanuvchidan parolni so'raymiz
        print("Checking your password...")  # Parol tekshirilayotgani haqida xabar
        await asyncio.sleep(3)  # 3 soniya kutamiz

        if password == "admin123":  # Agar parol to'g'ri bo‘lsa
            print("Password is correct!")  # To‘g‘ri parol haqida xabar
            break  # Dasturdan chiqamiz
        else:
            print("Incorrect password. Please try again.\n")  # Noto‘g‘ri parol haqida xabar

# Asosiy funksiya
async def main():
    await check_password()  # Parolni tekshirish funksiyasini chaqiramiz

# Dastur ishga tushirilmoqda
asyncio.run(main())
