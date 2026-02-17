import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Ошибка: деление на ноль")
    return a / b

def square_root(a):
    if a < 0:
        return "Ошибка: нельзя извлечь корень из отрицательного числа"
    return math.sqrt(a)

def main():
    print("Простой калькулятор")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Квадратный корень")
    
    choice = input("Выберите операцию (1-5): ")
    
    if choice == '5':
        a = float(input("Введите число: "))
        print(f"Результат: {square_root(a)}")
    else:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        
        if choice == '1':
            print(f"Результат: {add(a, b)}")
        elif choice == '2':
            print(f"Результат: {subtract(a, b)}")
        elif choice == '3':
            print(f"Результат: {multiply(a, b)}")
        elif choice == '4':
            print(f"Результат: {divide(a, b)}")
        else:
            print("Неверный выбор")

if __name__ == "__main__":
    main()