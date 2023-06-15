def find_units_of_z_n(n):
    units = []
    for i in range(n):
        for j in range(n):
            if i * j % n == 1:
                units.append(i)
                # print(i, 'is a unit: multiply by', j)
    return units


def find_order_of_x_in_z_n(x, n):
    for p in range(1, n + 1):
        if x**p % n == 1:
            return p


# print(find_units_of_z_n(20), len(find_units_of_z_n(20)))

# for unit in find_units_of_z_n(20):
#     print('order of', unit, 'is', find_order_of_x_in_z_n(unit, 20))
#     if find_order_of_x_in_z_n(unit, 20) == len(find_units_of_z_n(20)):
#         print(unit, 'generates U')

print(find_units_of_z_n(4), find_units_of_z_n(5))
