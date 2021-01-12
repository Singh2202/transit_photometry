min_fluxes = [0.99947375911145686, 0.99859591938153613, 0.99956234254866916, 0.99865517128565569, 0.99952370911155686, 0.99866017148565545]
min_fluxes = list(set(min_fluxes) - set(unique_fluxes))

correspondence_list = [] 
for value in min_fluxes:
    list_of_differences = []
    for value2 in unique_fluxes: 
        information = (value2, value, abs(value - value2)) 
        list_of_differences.append(information) 
    list_of_differences = sorted(list_of_differences, key = lambda x: x[2]) 
    minimum = [list_of_differences[0][0], list_of_differences[0][1]]  
    correspondence_list.append(minimum)
    

list_of_classes = [[] for n in range(len(unique_fluxes))] 

for index in range(len(list_of_classes)):
    list_of_classes[index].append(unique_fluxes[index]) 
    
for a_list in list_of_classes: 
    for value in correspondence_list:
        if value[0] in a_list:
            a_list.append(value[1]) 
