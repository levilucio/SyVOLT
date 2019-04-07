'''
Created on 2015-02-13

@author: levi
'''

import re

def is_consistent(graph, verbosity=0):


    eqs = graph["equations"]

    if not eqs:
        return True

    duplicates = []
    var_dict = {}

    if verbosity >= 2:
        print("\nis_consistent:")
        for eq in eqs:
            print(eq)

    i = -1
    for eq in eqs:

        if eq is None or eq[0] is None:
            continue

        node = eq[0][0]
        attr = eq[0][1]

        if attr == "pivot" or "ApplyAttribute" in attr:
            continue
            
        value = eq[1]

        i += 1

        if node not in var_dict:
            var_dict[node] = {attr : value}
            continue

        if attr not in var_dict[node]:
            var_dict[node][attr] = value
            continue

        #keep track of duplicates to remove
        duplicates.append(i)
        # print("Duplicate attr: " + attr + " " + str(value))

        if value != var_dict[node][attr]:
            if verbosity >= 2:
                print("Inconsistent values for " + str(eq[0]) + ": " + str(value) + " vs " + str(var_dict[node][attr]))
            return False



    #remove all duplicates
    new_eqs = [eqs[i] for i in range(len(eqs)) if i not in duplicates]
    if verbosity >= 2:
        print("New eqs: ")
        for eq in new_eqs:
            print(eq)
    graph["equations"] = new_eqs
    return True


def compare_constant_equations(patt_constant_equations, src_constant_equations, src_node):

    debug = False
    for patt_eq in patt_constant_equations:
        patt_attr = patt_eq[0]

        # skip matching pivots
        if patt_attr == "pivot" or "ApplyAttribute" in patt_attr:
            continue

        patt_value = patt_eq[1]

        found = False
        for (src_attr, src_value) in src_constant_equations:
            if patt_attr == src_attr:
                if patt_value == src_value:
                    found = True
                    break
                else:
                    if debug:
                        print("Equations do not match")
                    return False

        if found:
            continue

        try:
            if src_node[patt_attr] != patt_value:
                if debug:
                    print("Couldn't find value, found " + str(src_node[patt_attr]))
                    print("Patt eq: " + str(patt_eq))
                return False
        except KeyError:
            if debug:
                print("Couldn't find " + patt_attr + " on node " + src_node["mm__"])
            return False

    return True


def compare_variable_equations(patt_variable_equations, src_variable_equations):

    debug = False
    for patt_eq in patt_variable_equations:
        if debug:
            print("Pattern eq: " + str(patt_eq))

        patt_attr = patt_eq[0]

        patt_value = patt_eq[1]
        patt_str = var_eq_to_string(patt_value)

        if ".*" in patt_str:
            patt_expr = re.compile(patt_str)
        else:
            patt_expr = None

        found = False
        for (src_attr, src_value) in src_variable_equations:
            if debug:
                print("Source eq: " + str(src_attr) + " " + str(src_value))

            if patt_attr != src_attr:
                continue

            src_str = var_eq_to_string(src_value)

            if ".*" in src_str:
                src_expr = re.compile(src_str)
            else:
                src_expr = None

            if debug:
                print("Patt: " + patt_str)
                print("Src: " + src_str)

            if patt_str == src_str:
                found = True


            elif patt_expr or src_expr:
                if patt_expr and patt_expr.match(src_str):
                    if debug:
                        print("Matched on regex from patt")
                    found = True
                elif src_expr and src_expr.match(patt_str):
                    if debug:
                        print("Matched on regex from src")
                    found = True
                else:
                    if debug:
                        print("Failed on regex")
                    return False

            else:
                if debug:
                    print("Didn't match on attr: " + patt_attr)
                return False

        if not found:
            if debug:
                print("Patt: " + str(patt_eq) + " not found")
            return False

    return True

def var_eq_to_string(value):

    #print("To String: " + str(value))
    if len(value) == 0:
        return ""

    if value == "wildcard":
        return ".*"

    head = value[0]
    tail = value[1]

    if head == "concat":
        left = tail[0]
        right = tail[1]
        return var_eq_to_string(left) + var_eq_to_string(right)

    if head == "constant":
        return str(tail)

    if isinstance(head, int) and isinstance(tail, str):
        return tail
    elif isinstance(head, int):
        return var_eq_to_string(tail)

    print("Value: " + str(value))
    print(len(value))
    raise Exception("Error in variable equation. Value is not parsable")
