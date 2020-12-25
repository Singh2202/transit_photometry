l = [80.03, 5.06, 12.12, 6.07, 6.04, 5.09, 15.26, 5.10, 10.26]
l2 = []
for element_1 in l:
    boolean = True
    for element_2 in l2:
        lower_bound = .95*element_2
        upper_bound = 1.05*element_2
        if lower_bound < element_1 and element_1 < upper_bound:
            boolean = False # not unique
    if boolean is True:
        l2.append(element_1)
l2.sort()
index_initial = 0
while index_initial < len(l2):
    index_after = index_initial + 1
    while index_after < len(l2):
        if l2[index_after]%l2[index_initial] < .05*l2[index_initial] or l2[index_after]%l2[index_initial] >= .95*l2[index_initial]:
            l2.remove(l2[index_after])
        else:
            index_after = index_after + 1
    index_initial = index_initial + 1
print(l2)
