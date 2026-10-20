# ================================================
# ИГРА «ПИТЕРСКИЕ ПОДВОРОТНИ»
# Автор: Лина Юматова
# Дата: сентябрь 2026
#
# Пункт 4 — «разглядеть наркомана»: герой замирает
# и рассматривает, что происходит в ним. Пока
# пункт только выводится в меню — обрабатывать
# его будем на третьем занятии.
#
# Рекорд врага в таблице лидеров: если враг бил одинаково сильно
# несколько раз, берётся первый из таких раундов. Это выбор,
# а не случайность: max возвращает первую из равных строк.
# ================================================

import random

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
menu_last = 8
enemies = ["гопник", "бродячий пёс", "алкаш", "дилер"]
log = []
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
        print("7 - зайти глубже")
        print("8 - таблица лидеров")
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
            case "7":
                if not enemies:
                    print("Вы заходите глубже во дворы, но там пусто: врагов не осталось.")
                else:
                    enemy = random.choice(enemies)
                    enemy_hp = 45
                    round_n = 0
                    print(f"Вы заходите глубже во дворы. Из темноты выходит {enemy}!")
                    while enemy_hp > 0 and health > 0:
                        round_n += 1
                        if round_n % 3 == 0:
                            hit_damage = crit_damage
                            hit_end = " — критический!"
                        else:
                            hit_damage = damage
                            hit_end = "."
                        enemy_hp -= hit_damage
                        enemy_damage = 0
                        if enemy_hp <= 0:
                            print(f"Раунд {round_n}: вы наносите {hit_damage:.1f} урона{hit_end} Враг падает.")
                        else:
                            enemy_damage = random.randint(2, 6)
                            health -= enemy_damage
                            print(f"Раунд {round_n}: вы наносите {hit_damage:.1f} урона{hit_end} "
                                  f"Здоровье врага: {enemy_hp:.1f}. {enemy.capitalize()} бьёт в ответ на {enemy_damage}.")
                        log.append([round_n, hit_damage, enemy_damage])
                    if enemy_hp <= 0:
                        enemies.remove(enemy)
                        print(f"{enemy.capitalize()} повержен! Врагов в подворотне осталось: {len(enemies)}.")
                    print(f"Раундов в бою: {round_n}.")
                    print(f"Последний раунд: урон героя {log[-1][1]:.1f}, урон врага {log[-1][2]}.")
            case "8":
                if not log:
                    print("Вы ещё не дрались.")
                else:
                    top = sorted(log, key=lambda r: r[1], reverse=True)[:3]
                    print("Таблица лидеров (урон героя):")
                    for i in range(len(top)):
                        print(f"{i + 1}. Раунд {top[i][0]}: {top[i][1]:.1f}")
                    worst = max(log, key=lambda r: r[2])
                    print(f"Самый сильный удар врага: {worst[2]} (раунд {worst[0]}).")
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
        print(f"Здоровье: {health}   Запас сил: {stamina}   Врагов осталось: {len(enemies)}")

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
    total = sum(r[1] for r in log)
    rounds = len(log)
    if rounds > 0:
        print(f"Общий урон: {total:.1f}, раундов: {rounds}, средний урон: {total / rounds:.1f}.")
    else:
        print("В этом забеге боёв не было.")
    print(frame)