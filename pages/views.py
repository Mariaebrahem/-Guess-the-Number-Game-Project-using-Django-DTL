
from django.shortcuts import render
import random

def home(request):
    message = ""
    correct_number = 5  # يمكنك استخدام random.randint(1, 10) لجعل الرقم عشوائي
    user_guess = None

    if request.method == "POST":
        try:
            user_guess = int(request.POST.get("guess"))
            if user_guess == correct_number:
                message = "<strong style='color:green;'>✔️ صحيح! أحسنت!</strong>"
            elif user_guess < correct_number:
                message = "🔼 الرقم أكبر من " + str(user_guess)
            else:
                message = "🔽 الرقم أصغر من " + str(user_guess)
        except:
            message = "<span style='color:red;'>⚠️ أدخل رقمًا صحيحًا!</span>"

    return render(request, 'pages/home.html', {
        'message': message,
        'guess': user_guess
    })

