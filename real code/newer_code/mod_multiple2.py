differences = [8.2, 16.5, 6.7]
reduced_period_list = []
from itertools import permutations
permuted_list = list(permutations(differences, 2))
ordered_permuted_list = []
for thing in permuted_list:
    if thing[0] > thing[1]:
        ordered_permuted_list.append(thing)
modulo_list = []
for thing in ordered_permuted_list:
    modulo_list.append((thing[0]%thing[1]))
zero_indices = []
for thing in modulo_list:
    if thing < 1:
        index = modulo_list.index(thing)
        zero_indices.append(index)
zero_indices = list(set(zero_indices))
for index in zero_indices:
    reduced_period_list.append(ordered_permuted_list[index][1])
more_zero_indices = []
for thing in differences:
    lower_bound = thing - 0.05*thing
    upper_bound = thing + 0.05*thing
    for other_thing in modulo_list:
        if lower_bound < other_thing < upper_bound:
            index = modulo_list.index(other_thing)
            more_zero_indices.append(index)
for index in more_zero_indices:
    reduced_period_list.append(ordered_permuted_list[index][1])
reduced_period_list = list(set(reduced_period_list))
final_list_of_periods = []
from itertools import combinations
for period_1, period_2 in combinations(reduced_period_list, 2):
    if period_2 - 0.05*period_2 < period_1 < period_2 + 0.05*period_2:
        final_list_of_periods.append(period_1)
print(final_list_of_periods)
