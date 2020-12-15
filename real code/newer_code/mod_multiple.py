result = []
for x1 in range(len(differences)):
    for x2 in range(x1+1,len(differences)):
        result.append([differences[x1],differences[x2]])

for element in result:
    if element[1] > element[0]:
        if element[1]%element[0] > 1:
            lower_bound = element[0] - element[0]*.05 
            upper_bound = element[0] + element[0]*.05
            if lower_bound <= element[1]%element[0] <= upper_bound:
                is_multiple = True
            else:
                is_multiple = False
            element_1 = element[1]

                

if is_multiple is True:
    differences.remove(element_1)
    period_guess = np.median(differences)
    print(period_guess)
else:
    raise Exception("Multiple planet system detected")
