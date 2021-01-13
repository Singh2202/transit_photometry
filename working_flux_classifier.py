unique_fluxes = unique_fluxes

#(unique_fluxes)
# any value in unique_fluxes is considered to be a "base case"
# unqcomputed in the cell above = [0.9994737591114569, 0.9985959193815361]

# not sure why but min_fluxes isn't printing correctly, so here it is being declared again

min_fluxes = list(set(min_fluxes) - set(unique_fluxes)) # remove the base cases in unique_fluxes from min_fluxes

correspondence_list = [] #will contain tuples of flux and its closest base match, unsorted, unmatched
for value in min_fluxes:
    list_of_differences = [] #list to contain base case, value, and difference for each value in min_fluxes (two each)
    for value2 in unique_fluxes: # value2 is base case
        information = (value2, value, abs(value - value2)) #create tuple to avoid syntax errors when appending
        list_of_differences.append(information) #list will have len(unique_fluxes) elements
    list_of_differences = sorted(list_of_differences, key = lambda x: x[2]) #sort list by smallest abs(value - value2)
    minimum = [list_of_differences[0][0], list_of_differences[0][1]]  #tuple of flux and the base case closest to it
    correspondence_list.append(minimum)
    
list_of_classes = [[] for n in range(len(unique_fluxes))] #create list of lists with as many lists as unique_fluxes

for index in range(len(list_of_classes)): #populate each blank list with one unqiue flux
    list_of_classes[index].append(unique_fluxes[index]) #double loop not necessary because len(nested_list) == len(unique_fluxes)
    
for a_class in list_of_classes: #each list will correspond to one class of flux
    for value in correspondence_list:
        if value[0] in a_class: #if the base case for each flux is equal to the base case in the list
            a_class.append(value[1]) #append to the flux class the non-base flux
            
for a_tuple in tuples:
    for a_class in list_of_classes:
        for element in a_class: 
            if element == a_tuple[1]: # if a flux in the internal list is equal to the flux of a single tuple
                a_class.append(a_tuple[0]) # append to the class list the x coord associated with that flux

for index in range(len(list_of_classes)):
    list_of_classes[index] = list_of_classes[index][len(list_of_classes[index])//2:] #split internal class lists in half so that only the x_coords remain, b/c as many x_coords as fluxes by def
