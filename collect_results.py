import subprocess
import os

def get_avg(l):
    if len(l) == 0:
        return -1
    return sum(l) / float(len(l))

times_to_run = 5

#
# Parallel
# (F2P)
# --Off
# --Shuffle
# --Bin packing
# Not Pruning vs non-pruning
#
#
# --Rounds: Number of pcs per thread
# (can be fastest of shuffle or bin packing)
#
# Slicing
# --Time taken for slicing
# --Slicing results for each transformation
# (F2P, GM, UML, mbeddr, RSS2ATOM)
#
#
# Pruning
# (F2P, GM, UML, mbeddr, RSS2ATOM)
# Do with/without parallel
#
# Pickling
# Do with/without parallel
# (F2P, GM, UML, mbeddr, RSS2ATOM)


experiments = [
    #"test_atlTrans",
    "test_atlTrans_extended",
    #"test_competition",
    #"test_GM2Autosar_transformation",
    #"test_mbeddr",
    #"test_umlToKiltera",
]

experiment_args = ["--slice=2", "--skip_parallel"]

for ex_file in experiments:

    ex_filename = os.path.join("results", ex_file + "_results.txt")

    #open fresh file, and write header
    with open(ex_filename, 'w') as h:
        h.write("Starting experiments for: " + ex_file)

    with open(ex_filename, 'w+') as g:

        for x in range(times_to_run):

            print("Running " + ex_file + " for time " + str(x))
            command = ["/usr/bin/time", "python3", ex_file + ".py"] + experiment_args

            print("Command: " + " ".join(command))
            command.append("--skip_progress_bar")
            proc = subprocess.check_call(command, stdout=g, stderr=subprocess.STDOUT)


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

        s1 = "\nResults for '" + ex_file +"'"
        s2 = "Time build: " + str(round(avg_build_time, 2))
        s3 = "Time proof: " + str(round(avg_proof_time, 2))
        s4 = "Memory: " + str(int(get_avg(memory)))
        s5 = "Number of path conditions: " + str(int(get_avg(num_pcs)))


        experiment_filename = ex_filename.replace(".txt", "")
        experiment_filename += "".join(experiment_args)
        experiment_filename = experiment_filename.replace("=", "").replace("-", "") + ".txt"

        with open(experiment_filename, 'w') as e:

            for s in [s1, s2, s3, s4, s5]:
                print(s)
                e.write(s + "\n")


