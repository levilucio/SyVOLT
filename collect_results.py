import subprocess

def get_avg(l):
    return sum(l) / float(len(l))

times_to_run = 1

experiments = [
    #"test_atlTrans",
    "test_atlTrans_extended",
    "test_competition",
    "test_GM2Autosar_transformation",
    #"test_mbeddr",
    "test_umlToKiltera",
]

for ex_file in experiments:

    ex_filename = ex_file + "_results.txt"
    with open(ex_filename, 'w') as g:

        for x in range(times_to_run):

            print("Running " + ex_file + " for time " + str(x))
            print("Command: " + "/usr/bin/time " + "python3 " + ex_file + ".py")
            proc = subprocess.check_call(['/usr/bin/time', 'python3', ex_file + ".py"], stdout=g, stderr=subprocess.STDOUT)


    with open(ex_filename) as f:

        time_build_pcs = []
        time_contract_proof = []
        memory = []
        num_pcs = []


        for line in f:

            if "Time to build the set of path conditions" in line:
                t = line.split(" ")[8]
                time_build_pcs.append(float(t))
            elif "seconds to prove" in line:
                t = line.split(" ")[1]
                time_contract_proof.append(float(t))
            elif "maxresident" in line:
                line = line.replace("maxresident)k", "")
                m = line.split(" ")[5]
                memory.append(int(m)/1000)
            elif "Number of path conditions:" in line:
                pcs = line.split(" ")[4]
                num_pcs.append(int(pcs))

            #print(line.strip())


        avg_build_time = get_avg(time_build_pcs)
        avg_proof_time = get_avg(time_contract_proof)

        print("\nResults for '" + ex_file +"'")
        print("Time build: " + str(round(avg_build_time, 2)))
        print("Time proof: " + str(round(avg_proof_time, 2)))
        print("Memory: " + str(int(get_avg(memory))))
        print("Number of path conditions: " + str(int(get_avg(num_pcs))))



