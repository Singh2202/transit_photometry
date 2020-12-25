l = [80.03, 5.06, 12.12, 6.07, 6.04, 5.09, 15.26, 5.10, 10.26]
tolerance_parameter = float(input('Tolerance Parameter (pct): '))/100
l2 = []
for element_1 in l:
    boolean = True
    for element_2 in l2:
        lower_bound = (1 - tolerance_parameter) * element_2
        upper_bound = (1 + tolerance_parameter) * element_2
        if lower_bound < element_1 < upper_bound:
            boolean = False
    if boolean is True:
        l2.append(element_1)
l2.sort()
index_initial = 0
while index_initial < len(l2):
    index_after = index_initial + 1
    while index_after < len(l2):
        near_zero = tolerance_parameter * l2[index_initial]
        near_smaller = (1 - tolerance_parameter) * l2[index_initial]
        mod_val = l2[index_after] % l2[index_initial]
        if mod_val < near_zero or mod_val >= near_smaller:
            l2.remove(l2[index_after])
        else:
            index_after += 1
    index_initial += 1
print(l2)

