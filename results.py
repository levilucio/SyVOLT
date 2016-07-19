import sys

def do_average(l):
    s = sum(l)
    n = s/len(l)
    n = int(n * 100)/100.0
    return n

if len(sys.argv) < 2:
    print("Please use filename as argument")

filename = sys.argv[1]

print("Opening " + filename)

last_contract = "default"

contracts = [last_contract]

succeed = {}
fail = {}

time_to_prove = {}
time_pc_building = {}

rules_after = {}

num_pcs = {}

mem = {}

handbuilt = False

for line in open(filename):

    line = line.strip()

    if "Handbuilt" in line:
        handbuilt = True
    elif "Run" in line:
        handbuilt = False

    if "Name:" in line:

        last_contract = line.split(":")[1]

        if handbuilt:
            last_contract += '-Handbuilt'

        contracts.append(last_contract)
        #print("Name: " + last_contract)

    elif "Num Succeeded Contracts:" in line:
        #print(line)
        num_succeed = int(line.split(" ")[3])

        if not last_contract in succeed:
            succeed[last_contract] = [num_succeed]

    elif "Num Failed Contracts:" in line:
        #print(line)
        num_fail = int(line.split(" ")[3])

        if not last_contract in fail:
            fail[last_contract] = [num_fail]

    elif "seconds to prove" in line:
        #print(line)
        time_prove = float(line.split(" ")[1])

        if not last_contract in time_to_prove:
            time_to_prove[last_contract] = [time_prove]
        else:
            time_to_prove[last_contract].append(time_prove)

    elif "Time to build the set of path conditions" in line:
        # print(line)
        time_build = float(line.split(" ")[8])

        if not last_contract in time_pc_building:
            time_pc_building[last_contract] = [time_build]
        else:
            time_pc_building[last_contract].append(time_build)

    elif "Number of path conditions:" in line:
        #print(line)
        pcs = int(line.split(" ")[4])

        if not last_contract in num_pcs:
            num_pcs[last_contract] = [pcs]

    elif "Number rules after:" in line:
        rules = line.split(" ")[3]
        print(line)
        print(rules)
        if not last_contract in rules_after:
            rules_after[last_contract] = [rules]

    elif "maxresident" in line:
        #print(line)
        #time_prove = float(line.split(" ")[1])

        maxresident = int(line[-18:-13])

        if not last_contract in mem:
            mem[last_contract] = [maxresident]
        else:
            mem[last_contract].append(maxresident)

total_time = 0
max_mem = 0
print(contracts)
for contract in sorted(set(contracts)):



    if contract == "default" and len(contracts) > 1:
        continue

    print("\nContract: " + contract)
    prove_time = do_average(time_to_prove[contract])
    total_time += prove_time
    print("Time to prove: " + str(prove_time))
    print("Time to build PCs: " + str(do_average(time_pc_building[contract])))
    print("Num PCs: " + str(num_pcs[contract]))
    print("Num Succeeded: " + str(succeed[contract]))
    print("Num Failed: " + str(fail[contract]))

    m = do_average(mem[contract])
    max_mem = max(max_mem, m)
    print("Memory: " + str())
    try:
        print("Rules for slicing: " + str(rules_after[contract]))
    except KeyError:
        pass

print("Total prove time: " + str(total_time))
print("Max mem: " + str(max_mem))