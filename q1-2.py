def total_salary(path):
    try:
        with open(path, 'r') as file:
            line = [int(x.split(',')[1].rstrip()) for x in file]
            if len(line) == 0:
                print('Файл пустий')
            else:
                print(f"Загальна сума заробітної плати: {sum(line)}, Середня заробітна плата: {sum(line)/len(line)}")
                return (sum(line), sum(line)/len(line))
    except FileNotFoundError:
        print('Файл не знайдено')

def get_cats_info(path):
    cats = []
    try:
        with open(path, 'r') as file:
            line = [x.rstrip().split(',') for x in file]
            if len(line) == 0:
                print('Файл пустий')
            else:
                for x in line:
                    cats.append({'id': x[0], 'name': x[1], 'age': x[2]})
                return cats
    except FileNotFoundError:
        print('Файл не знайдено')
