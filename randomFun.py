import random, string

#string.acsii_letters : both upper and lowercase + digits
#string.ascii_uppercase or use string.ascii_lowercase
letters_numbers = string.ascii_letters + string.digits
captcha1 = ''
for i in range(7):
    captcha1 += random.choice(letters_numbers)

captcha2 = ''.join(random.sample(letters_numbers,7))
captcha3 = random.choices(letters_numbers, k=7)

print('captcha1 : ',captcha1)
print('captcha2 : ',captcha2)
print('captcha3 : ',captcha3)