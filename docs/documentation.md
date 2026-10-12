# Документация проекта

## Что это за проект

Небольшой набор функций на Python для вычисления площади и периметра
простых фигур: круга, квадрата, прямоугольника и треугольника.
Используется только стандартный модуль `math`, никаких сторонних
библиотек не нужно.

Формулы, по которым всё считается:

- круг: `S = π·r²`, `P = 2·π·r`
- квадрат: `S = a²`, `P = 4·a`
- прямоугольник: `S = a·b`, `P = 2·(a+b)`
- треугольник: `S = √(p·(p−a)·(p−b)·(p−c))`, где `p = (a+b+c)/2`, а периметр — `a+b+c`

## Функции

### circle_area(r)

Считает площадь круга по радиусу.

Пример:

```python
from main import circle_area
print(circle_area(3))  # 28.274333882308138
```

### circle_perimeter(r)

Считает длину окружности по радиусу.

```python
from main import circle_perimeter
print(circle_perimeter(3))  # 18.84955592153876
```

### square_area(a)

Площадь квадрата по стороне.

```python
from main import square_area
print(square_area(4))  # 16
```

### square_perimeter(a)

Периметр квадрата по стороне.

```python
from main import square_perimeter
print(square_perimeter(4))  # 16
```

### rectangle_area(a, b)

Площадь прямоугольника по двум сторонам.

```python
from main import rectangle_area
print(rectangle_area(5, 3))  # 15
```

### rectangle_perimeter(a, b)

Периметр прямоугольника по двум сторонам.

```python
from main import rectangle_perimeter
print(rectangle_perimeter(5, 3))  # 16
```

### triangle_area(a, b, c)

Площадь треугольника по трём сторонам (формула Герона).

```python
from main import triangle_area
print(triangle_area(3, 4, 5))  # 6.0
```

### triangle_perimeter(a, b, c)

Периметр треугольника по трём сторонам.

```python
from main import triangle_perimeter
print(triangle_perimeter(3, 4, 5))  # 12
```

## История изменений

Здесь перечислены все коммиты проекта, кроме последнего.

| Хеш | Что сделано |
|-----|-------------|
| `b91516a` | first commit: add main.py|
| `fbb0db2` | add logic in main.py |
| `228d4bd` | add Readme.md, docs folder and documentation.md |
