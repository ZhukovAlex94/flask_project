import csv


def load_data():
    with open('hw.csv', 'r') as file:
        data = csv.reader(file, delimiter=',', quotechar='|')
        next(data)
        return [(float(line[1]), float(line[2])) for line in data if len(line) == 3]


def get_avr_data():
    l_data = load_data()
    heights = [item[0] for item in l_data]
    weights = [item[1] for item in l_data]

    return round((sum(heights) / len(heights) * 2.54), 2), round((sum(weights) / len(weights) / 2.2046), 2)
