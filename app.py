weight = float(input("اكتب وزنك بالكيلو: "))
height = float(input("اكتب طولك بالمتر (مثلاً 1.75): "))

bmi = weight / (height ** 2)

print("مؤشر كتلة الجسم (BMI) =", round(bmi, 2))

if bmi < 18.5:
    print("أنت نحيف 🥶")
elif bmi < 25:
    print("وزنك مثالي ✅")
elif bmi < 30:
    print("وزنك زايد شوي 😅")
else:
    print("عندك سمنة 😔 حاول تنتبه لصحتك")