def find_mean(dataset):
    return sum(dataset) / len(dataset)


def find_standard_deviation(dataset):
    mean = find_mean(dataset)
    N = len(dataset)
    top_half = sum([(x - mean) ** 2 for x in dataset])
    return (top_half / (N - 1)) ** 0.5


def find_standard_error(dataset):
    standard_deviation = find_standard_deviation(dataset)
    N = len(dataset)
    return standard_deviation / (N**0.5)


pure_water_data = [36, 42, 46, 42, 42]
water_and_soap_data = [20, 22, 19, 16, 13]

print(find_standard_error(pure_water_data))
