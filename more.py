l = []
for thing in itertools.combinations(x_coords, 2):
    l.append((abs(thing[1] - thing[0])))


l2 = []
for element_1 in l:
    print(element_1)
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

no_planets = False
minima_found = False

if len(l2) == 0:
    no_planets = True

if len(l2) == 1:
    minima_found = True
    number_of_planets = 1

elif len(l2) > 1:
    segregated_fluxes = []
    min_fluxes = minima_y
    for index1 in range(len(min_fluxes)):
        for index2 in range(index1 + 1, len(min_fluxes)):
            if .9999*min_fluxes[index2] < min_fluxes[index1] < 1.0001*min_fluxes[index2]:
                segregated_fluxes.append((min_fluxes[index1], min_fluxes[index2]))
                
    number_of_planets = len(segregated_fluxes)
    
    filtered_fluxes = [a_flux for a_class in segregated_fluxes for a_flux in a_class] 
    unmatched_fluxes = []

    for a_flux in min_fluxes:
        if not a_flux in filtered_fluxes:
            unmatched_fluxes.append(a_flux)

    if 1 < number_of_planets < 9:
        minima_found = True
        
    unique_fluxes = []
    for element_1 in min_fluxes:
        boolean = True
        for element_2 in unique_fluxes:
            lower_bound = (1 - .0001) * element_2
            upper_bound = (1 + .0001) * element_2
            if lower_bound < element_1 < upper_bound:
                boolean = False
        if boolean is True:
            unique_fluxes.append(element_1)
            
    nested_list = [[] for n in range(len(unique_fluxes))]
    placeholder = []
    
    for value in unique_fluxes:
        list_of_differences = []
        for value2 in min_fluxes:
            if not value2 in unique_fluxes:
                list_of_differences.append((abs(value2 - value), value, value2))
        list_of_differences = sorted(list_of_differences, key = lambda x: x[0])
        minimum = list_of_differences[0]
        placeholder.append(minimum)
        
    for index1 in range(len(unique_fluxes)):
        nested_list[index1].append(unique_fluxes[index1])
    
    for element in placeholder:
        for a_list in nested_list:
            if element[1] in a_list:
                a_list.append(element[2])
                
    print(nested_list)
    
