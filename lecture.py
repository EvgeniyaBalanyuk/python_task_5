print("Ищем обший элемент. Пересечение множеств ")
set_a = {1, 2, 3}
set_b = {3, 4, 5}
set_c = {6, 7, 3}
set_d = {6, 7}
e = {5, 6, 3}
print(set_a & set_b & set_c & e)
intersection_set = set_a.intersection(set_b, set_c, e)
print(intersection_set)


print("объединение множества")
print(set_a | set_b | set_c | set_d)
union_set = set_a.union(set_b, set_c, set_d)
print(union_set)


print("Вычитание множеств")
print(set_a - set_b - e)
print(set_a - (set_b - e))
print(set_b - set_a)
difference_set = set_a.difference(set_b, e)
print(difference_set)


print("Симетрическая разность множества")
print(set_a ^ set_b ^ e ^ set_c)
print(set_b ^ set_a)
symm_diff_set = set_a.symmetric_difference(set_b)
print(symm_diff_set)

# Симетрическая разность состоит объединения и пересечения множеств
print("Пересекаем 4 множества")
set_diff = set_a & set_b & set_c & e
print(set_diff)

print("Объединяем 4 множества")
set_diff_sym = set_a | set_b | set_c | e
print(set_diff_sym)

print("Симетрическая разность")
print(set_diff_sym - set_diff)



# БЛОК КЕЙСА
# исходные данные взяты отсюда:
# https://netology.ru/programs/python#/experts
# https://netology.ru/programs/java-developer#/experts
# https://netology.ru/programs/fullstack-python-dev#/experts
# https://netology.ru/programs/front-end#/experts

courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"]
mentors = [
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
# массивы = list
print("Какие преподаватели преподают на рвзных курсвх:")
py_set = set(mentors[0])
jv_set = set(mentors[1])
fspy_set = set(mentors[2])
fr_set = set(mentors[3])
print("py & jv: ", py_set & jv_set)
print("py & fspy: ", py_set & fspy_set)
print("jv & fr", jv_set & fr_set)
print("fspy & fr", fspy_set & fr_set)


print("Сколько преподавателей преподают на всех курсах (множества) вариант 1:")
py_set = set(mentors[0])
jv_set = set(mentors[1])
fspy_set = set(mentors[2])
fr_set = set(mentors[3])
union_set = py_set | jv_set | fspy_set | fr_set
print(union_set)
print(len(union_set))

print("Сколько преподавателей преподают на всех курсах (множества) вариант 2:")
all_mentors_union = set(mentors[0]) | set(mentors[1]) | set(mentors[2]) | set(mentors[3])
print(all_mentors_union)
print(len(all_mentors_union))

print("Сколько преподавателей преподают на всех курсах (множества) вариант 3:")
all_mentors = mentors[0] + mentors[1] + mentors[2] + mentors[3]
all_mentors_honest = set(all_mentors)
print(all_mentors_honest)
print(len(all_mentors_honest))

print("Сколько преподавателей преподают на всех курсах (списки):")
all_mentors = mentors[0] + mentors[1] + mentors[2] + mentors[3]
print(all_mentors)
print(len(all_mentors))


print("Сколько преподавателей преподают на всех курсах (Цикл):")
all_mentors_honest = set()
for mentor in mentors:
	# all_mentors_honest = all_mentors_honest | set(mentor)
	all_mentors_honest |= set(mentor)
print(all_mentors_honest)
print(len(all_mentors_honest))



# БЛОК ИНТЕРАКТИВА
import time

n = 10_000
print(f"\n==========\nСкорость поиска в списке и множестве из {n} элементов\n==========")

# функция, сравнивающая два списка
def fn1(x, y):
	print(f"\nСравнение двух списков из {len(x)} элементов. Первые 10 элементов:")
	print(x[:10])
	print(y[:10])
	start = time.time()
	z = []
	for x1 in x:
		for y1 in y:
			if x1 == y1:
				z.append(y1)
	print(f"Длительность выполнения: {time.time() - start} cек")
	print(f"Совпало элементов: {len(z)}")

# функция, сравнивающая два множества
def fn2(x, y):
	print(f"\nСравнение двух множеств из {len(x)} элементов. Первые 10 элементов:")
	print(list(x)[:10])
	print(list(y)[:10])
	start = time.time()
	z = x & y
	print(f"Длительность выполнения: {time.time() - start} сек")
	print(f"Совпало элементов: {len(z)}")

# в каждом списке у нас по 10 тыс элементов
xl = list(range(1,n+1))
yl = list(range(1,n+1))

# выводим первые 10 элементов (для иллюстрации) и вызываем функцию сравнения списков
fn1(xl, yl)

# будет ли работать дольше, если развернуть второй список?
print("\nПусть первый список теперь идет в прямом направлении, а второй - в обратном")
yl.reverse()
fn1(xl, yl)

# выводим первые 10 элементов (для иллюстрации) и вызываем функцию сравнения множеств
xs = set(xl)
ys = set(yl)
fn2(xs, ys)
