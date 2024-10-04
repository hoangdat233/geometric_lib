
# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
# Oбщее описание решения:
1. Выполните команду git clone
2. Создайте новую ветку с названием new_features_<ISU> и переключитесь на нее.
3. Добавьте новый файл в эту ветку (rectangle.py)
4. Сделайте коммит с сообщением о том, что был добавлен новый файл.
5. Добавьте еще один файл в эту ветку (triangle.py)
6. Исправьте ошибку в вычислении периметра в файле rectangle.py
7. Создайте еще один коммит внутри этой же ветки, его сообщение о том, что была исправлен ошибка.
8. Постройте граф истории всего репозитория с однострочным выводом коммитов.
9. Постройте граф истории только текущей ветки.
10. Возьмите хэши двух последних коммитов из истории
11. Сделайте Pull Request
12. Yдалим ветку new_features_<ISU>.

# ** Oписание каждой функции с примерами вызова**
## **Rectangle**
```
def area(a, b): 
    '''Принимает число a и b (длина и ширина прямоугольника), возвращает площадь  прямоугольника'''
    return a * b 
    
def perimeter(a, b): 
    '''Принимает число a и b (длина и ширина прямоугольника), возвращает периметр прямоугольника'''
    return (a + b)*2
```
_Example:_
_Input: `5,6`_
_Output: `30 22`_


## **Triangle**
```
def area(a, h): 
    '''Принимает число a, h (основание и высота треугольника) возвращает площадь треугольника'''
    return a * h / 2 
def perimeter(a, b, c): 
    '''Принимает число a, b, c (стороны треугольника), возвращает периметр треугольника'''
    return a + b + c
```
_Example:_
_Input: `1,2` `1,2,3`_
_Output: `1 6`_


## **Square**
```
def area(a):
    '''Принимает число a (сторона квадрата), возвращает площадь  квадрата'''
    return a * a

def perimeter(a):
    '''Принимает число a (сторона квадрата), возвращает периметр квадрата'''
    return 4 * a
```
_Example:_
_Input: `3`_
_Output: `9 12`_

## **Circle**
```
import math
    '''Подключит библиотеку math'''

def area(r):
    '''Принимает число r (радиус круга), возвращает площадь круга'''
    return math.pi * r * r


def perimeter(r):
    '''Принимает число r (радиус круга), возвращает периметр круга'''
    return 2 * math.pi * r
```
_Example:_
_Input: `4`_
_Output: `50.24 25.12`_

# История изменения проекта с хешами комитов
- _**commit 9dd27b94ab39c1ad4266f3a9ff9276239e9d987e**_
``` 
Author: Hoang Ngoc Dat <407880@niuitmo.ru>
Date:   Thu Oct 3 18:59:55 2024 +0300
    
    Update Readme.md file the second time
```

- _**commit 4f6015fb35ea095d4e57523ffc2b4c987bb1a035**_
``` 
Author: Hoang Ngoc Dat <407880@niuitmo.ru>
Date:   Thu Oct 3 12:43:35 2024 +0300
    
    Update Readme.md file
```

- _**commit 7e6c710e085053112323b22d896087f3639a9102**_
``` 
Author: Hoang Ngoc Dat <407880@niuitmo.ru>
Date:   Thu Oct 3 12:19:51 2024 +0300
    
    Add more to explain
```

- _**commit 746c3a18de806c396070b8a71e764e69c3d7176d**_
``` 
Author: Hoang Ngoc Dat <407880@niuitmo.ru>
Date:   Thu Oct 3 11:43:35 2024 +0300
    
    Add comment to circle.py
```

- _**commit c5c3db2f82030561f4f7669a87429941126d3a35**_
``` 
Author: Hoang Ngoc Dat <407880@niuitmo.ru>
Date:   Thu Oct 3 11:42:59 2024 +0300
    
    Add comment to square.py
```

- _**commit c5c3db2f82030561f4f7669a87429941126d3a35**_
``` 
Author: Hoang Ngoc Dat <407880@niuitmo.ru>
Date:   Thu Oct 3 11:42:10 2024 +0300
    
    Add comment to triangle.py
```

- _**commit 0be759905089e1944aea66b89b7f6fb212466629**_
``` 
Author: Hoang Ngoc Dat <407880@niuitmo.ru>
Date:   Thu Oct 3 11:41:42 2024 +0300
    
    Add comment to rectangle.py
```









