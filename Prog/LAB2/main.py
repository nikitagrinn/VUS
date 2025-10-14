import configparser

def calculate(operand1, operand2, epsilon=0.0001):
    """
    Делит operand1 на operand2.
    Проверяет, что epsilon находится в диапазоне (1e-9, 1e-1).
    Вызывает ZeroDivisionError при делении на ноль.
    """
    if not (1e-9 < epsilon < 1e-1):
        raise ValueError("Точность (epsilon) вне допустимого диапазона.")

    if operand2 == 0:
        raise ZeroDivisionError("Деление на ноль невозможно.")

    return float(operand1) / float(operand2)


def load_params(config_file='settings.ini'):
    """
    Считывает значение epsilon из секции [Settings] в .ini файле.
    Вызывает FileNotFoundError, KeyError, ValueError при ошибках.
    """
    config = configparser.ConfigParser()
    
    if not config.read(config_file):
        raise FileNotFoundError(f"Файл конфигурации '{config_file}' не найден.")

    try:
        return config.getfloat('Settings', 'epsilon')
    except (configparser.NoSectionError, configparser.NoOptionError):
        raise KeyError("Секция [Settings] или параметр 'epsilon' не найдены.")
    except ValueError:
        raise ValueError("Неверный формат числа для epsilon в файле.")

# --- Пример использования ---
if __name__ == "__main__":
    try:
        # Для демонстрации создадим временный файл settings.ini
        config = configparser.ConfigParser()
        config['Settings'] = {'epsilon': '0.005'}
        with open('settings.ini', 'w') as configfile:
            config.write(configfile)

        loaded_epsilon = load_params()
        print(f"Загруженная точность: {loaded_epsilon}")
        
        # Теперь epsilon можно передавать и как позиционный аргумент
        # result = calculate(10, 3, 0.01) 
        
        # ...и как ключевой (как было в вашем примере)
        result = calculate(10, 3, epsilon=loaded_epsilon)
        print(f"Результат 10 / 3: {result}")

    except Exception as e:
        print(f"Ошибка: {e}")
