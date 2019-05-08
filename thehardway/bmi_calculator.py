input("Натиснете <enter>, за да започнете калкулатора за Индекс Телесна Маса!")
print("Добре дошли в калкулатора за ИТМ. Моля, отговорете на следните въпроси:")
prompt = "> "
name = str(input(f"Как се казваш? {prompt}"))
sex = str(input(f"Какъв пол си? {prompt}"))
weight = int(input(f"Колко килограма тежиш? {prompt}"))
height = float(input(f"Колко си висок/а? (пример 1.95) {prompt}"))

def bmi_calculator(name, weight, height):
    bmi = weight / (height ** 2)
    print("Изчисляване Индекс Телесна Маса...")
    print(f"Индекс Телесна маса на {name} е", round(bmi, 2))
    if bmi < 18.5:
        return name + ", " """Вашият Индекс Телесна маса е под нормата! 
                                Вземете хапнете нещо!"""
    elif bmi > 18.5 and bmi < 25:
        return name + ", " "Вашият Индекс Телесна маса е в норма!"
    else:
        return name + ", " """"Вашият Индекс Телесна Маса е над нормата! 
                            Време е май да поспортуваш малко!"""

result = bmi_calculator(name, weight, height)
print(result)
