# Задание 2
def clean_notice(text):
    words=text.split()
    return " ".join(words)
print(clean_notice(" EKEB ждёт T118! "))
print(clean_notice("Алматы\nАстана\tТараз"))
print(clean_notice(" "))

# Задание 3
def has_bug(text):
    return "bug" in text.lower()
print(has_bug("BUG найден"))
print(has_bug("Найден bug"))
print(has_bug("DEBUG"))
print(has_bug("Всё работает"))
print(has_bug(""))