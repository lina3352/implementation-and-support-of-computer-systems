# ================================================
# ИГРА «ПИТЕРСКИЕ ПОДВОРОТНИ»
# Автор: Лина Юматова
# Дата: сентябрь 2026
#
# Пункт 4 — «разглядеть наркомана»: герой замирает
# и рассматривает, что происходит в ним. Пока
# пункт только выводится в меню — обрабатывать
# его будем на третьем занятии.
# ================================================

# --- Заголовок ------------------------------------
title = "ПИТЕРСКИЕ ПОДВОРОТНИ"
frame = "=" * 22
print(frame)
print(" " + title + " ")
print(frame)
print()

# --- Знакомство с героем --------------------------
print("Как зовут героя?")
hero_name = input()
print(f"Добро пожаловать, {hero_name}!")
print("Ты входишь в подворотню. Там пахнет сыростью и марихуаной")
print()

# --- Настройка героя -------------------------------
print("Настройка героя.")
print("Здоровье, сила, ловкость, накуренность — по одному числу в строке:")
while True:
    try:
        health = int(input())
        strength = int(input())
        agility = int(input())
        curvature = int(input())
    except ValueError:
        print("Ой: одна из строк не число. Введите все четыре снова:")
        continue
    try:
        if health <= 0:
            raise ValueError(f"Здоровье должно быть положительным, а введено {health}")
        if strength < 0 or agility < 0 or curvature < 0:
            raise ValueError("Сила, ловкость и накуренность не могут быть отрицательными")
        if curvature > 10:
            raise ValueError(f"Накуренность не больше 10, а введено {curvature}")
        break
    except ValueError as e:
        print(f"{e}. Введите все четыре снова:")

# --- Расчёт урона ----------------------------------
base_attack = 10
damage = base_attack + strength * 1.5
crit_damage = damage * 2
stamina = health + ((strength + agility) / base_attack * crit_damage * curvature) * 0.5
max_stamina = stamina

# --- Формуляр героя --------------------------------
print("Характеристики героя:")
print(f"Здоровье: {health}")
print(f"Сила: {strength}")
print(f"Ловкость: {agility}")
print(f"Накуренность: {curvature}")
print()
print(f"Урон героя: {damage:.1f}")
print(f"Критический урон: {crit_damage:.1f}")
print(f"Стамина: {stamina}")

# --- Главный цикл игры -----------------------------
running = True
actions = 0
menu_last = 6
outcome = "прерывание"
try:
    while running:
        # --- Меню действий ---------------------------------
        print()
        print("Что делаешь?")
        print("1 - осмотреться")
        print("2 - идти вперёд")
        print("3 - отдохнуть")
        print("4 - разглядеть наркомана")
        print("5 - курнуть")
        print("6 - тренировка")
        print("0 - выйти из подворотни")
        print()

        # --- Выбор действия (с защитой от неверного ввода) ---
        while True:
            choice = input()
            try:
                menu_number = int(choice)
            except ValueError:
                print("Такого пункта нет. Введи номер пункта из меню.")
                continue
            if 0 <= menu_number <= menu_last:
                choice = str(menu_number)
                break
            print("Такого пункта нет. Введи номер пункта из меню.")

        match choice:
            case "1":
                print("Вы осмотрелись. Переулок тих и тёмен.")
            case "2":
                cost = 4
                if stamina >= cost:
                    stamina -= cost
                    print("Вы осторожно идёте вперёд. Шприцы ломаются под ногами.")
                else:
                    health -= cost - stamina
                    stamina = 0
                    print("Сил больше нет — вы идёте на одном упорстве.")
            case "3":
                stamina = stamina + 2
                if stamina > max_stamina:
                    stamina = max_stamina
                print("Вы садитесь у стены, предварительно ботинком отодвинув бычки от косяков")
            case "4":
                print("Наркоман лежит без сознания, только кальян тихо булькает рядом.")
            case "5":
                curvature = curvature + 2
                print("Ваше сознание медленно мутнеет, а перед глазами начинают прыгать радужные котики.")
            case "6":
                strikes = 6
                total_damage = 0
                crit_count = 0
                training_cost = 8
                print("Вы подходите к повешанному.")
                print("Он весит здесь с тех пор, как сюда приходил последний искатель")
                print()
                print(f"Наносите {strikes} ударов.")
                for i in range(1, strikes + 1):
                    if i % 3 == 0:
                        hit_damage = crit_damage
                        print(f"Удар {i}: {hit_damage:.1f} урона — критический!")
                        crit_count += 1
                    else:
                        hit_damage = damage
                        print(f"Удар {i}: {hit_damage:.1f} урона")
                    total_damage += hit_damage

                print()
                if stamina >= training_cost:
                    stamina -= training_cost
                else:
                    health -= training_cost - stamina
                    stamina = 0
                    print("Сил не хватает — тренировка идёт за счёт здоровья.")
                print(f"Итог. Ударов: {strikes}, критических ударов: {crit_count}")
                print(f"Общий урон: {total_damage:.1f}")
                print(f"Средний урон: {total_damage / strikes:.1f}")
                print(f"Стоимость тренировки: {training_cost} сил")
            case "0":
                print("Вы выходите из подворотни на шумную улицу. Сырость и запах травы остаются позади.")
                running = False
                outcome = "выход"
            case _:
                print("Такого действия нет.")

        # --- Счётчик действий и строка состояния ------------------
        if running:
            actions += 1
        print()
        print(f"Здоровье: {health}   Запас сил: {stamina}")

        # --- Проверка гибели ---------------------------------------
        if health <= 0:
            print(f"{hero_name} падает без сил. Подворотня забирает ещё одного.")
            running = False
            outcome = "гибель"
except KeyboardInterrupt:
    print()
    print("Игрок прервал сеанс.")
finally:
    print()
    print(frame)
    if outcome == "гибель":
        print(f"Ты не дошёл, {hero_name}. Действий совершено: {actions}.")
    elif outcome == "выход":
        print(f"Забег окончен, {hero_name}. Действий совершено: {actions}.")
    else:
        print(f"Тебя спугнули на полпути, {hero_name}. Действий совершено: {actions}.")
    print(frame)
