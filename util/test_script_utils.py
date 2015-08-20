from core.himesis_utils import graph_to_dot

def select_rules(full_transformation, num_rules):
    selected_transformation = []

    print("Selecting " + str(num_rules) + " rules")

    i = 1
    for layer in range(len(full_transformation)):
        selected_transformation.append([])
        for rule in full_transformation[layer]:
            selected_transformation[layer].append(rule)
            i += 1
            if i > num_rules:
                print("Returning: " + str(selected_transformation))
                return selected_transformation



