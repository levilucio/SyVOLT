import subprocess
import os

def get_avg(l):
    if len(l) == 0:
        return -1
    return sum(l) / float(len(l))

times_to_run = 5

experiments = [

    # Parallel
    # (F2P)
    # --Off
    # --Shuffle
    # --Bin packing
    # no pruning

    #Re-run these
    ["test_atlTrans_extended", "--skip_pruning"],
    ["test_atlTrans_extended", "--skip_parallel", "--skip_pruning"],
    ["test_atlTrans_extended", "--shuffle", "--skip_pruning"],

    ["test_mbeddr", "--slice=2", "--skip_parallel", "--skip_pruning"],
    ["test_mbeddr", "--slice=2", "--shuffle", "--skip_pruning"],
    ["test_mbeddr", "--slice=2", "--skip_pruning"],

    ["test_GM2Autosar_transformation", "--skip_pruning"],
    ["test_GM2Autosar_transformation", "--skip_parallel", "--skip_pruning"],
    ["test_GM2Autosar_transformation", "--shuffle", "--skip_pruning"],

    ["test_umlToKiltera", "--skip_pruning"],
    ["test_umlToKiltera", "--skip_parallel", "--skip_pruning"],
    ["test_umlToKiltera", "--shuffle", "--skip_pruning"],

    ["test_RSS2ATOM", "--skip_pruning"],
    ["test_RSS2ATOM", "--skip_parallel", "--skip_pruning"],
    ["test_RSS2ATOM", "--shuffle", "--skip_pruning"],

    # --Rounds: Number of pcs per thread
    # (can be fastest of shuffle or bin packing)

    # ["test_atlTrans_extended", "--skip_pruning", "--max_chunk_size=5"],
    # ["test_atlTrans_extended", "--skip_pruning", "--max_chunk_size=10"],
    # ["test_atlTrans_extended", "--skip_pruning", "--max_chunk_size=20"],
    # ["test_atlTrans_extended", "--skip_pruning", "--max_chunk_size=100"],
    # ["test_atlTrans_extended", "--skip_pruning", "--max_chunk_size=200"],
    # ["test_atlTrans_extended", "--skip_pruning", "--max_chunk_size=500"],
    # ["test_atlTrans_extended", "--skip_pruning", "--max_chunk_size=1000"],
    # ["test_atlTrans_extended", "--skip_pruning", "--max_chunk_size=2000"],
    #
    # ["test_mbeddr", "--slice=2", "--skip_pruning", "--max_chunk_size=5"],
    # ["test_mbeddr", "--slice=2", "--skip_pruning", "--max_chunk_size=10"],
    # ["test_mbeddr", "--slice=2", "--skip_pruning", "--max_chunk_size=20"],
    # ["test_mbeddr", "--slice=2", "--skip_pruning", "--max_chunk_size=100"],
    # ["test_mbeddr", "--slice=2", "--skip_pruning", "--max_chunk_size=200"],
    # ["test_mbeddr", "--slice=2", "--skip_pruning", "--max_chunk_size=500"],
    # ["test_mbeddr", "--slice=2", "--skip_pruning", "--max_chunk_size=1000"],
    # ["test_mbeddr", "--slice=2", "--skip_pruning", "--max_chunk_size=2000"],
    #
    # ["test_atlTrans_extended", "--skip_pruning", "--max_chunk_size=5", "--skip_pickle"],
    # ["test_atlTrans_extended", "--skip_pruning", "--max_chunk_size=10", "--skip_pickle"],
    # ["test_atlTrans_extended", "--skip_pruning", "--max_chunk_size=20", "--skip_pickle"],
    # ["test_atlTrans_extended", "--skip_pruning", "--max_chunk_size=100", "--skip_pickle"],
    # ["test_atlTrans_extended", "--skip_pruning", "--max_chunk_size=200", "--skip_pickle"],
    # ["test_atlTrans_extended", "--skip_pruning", "--max_chunk_size=500", "--skip_pickle"],
    # ["test_atlTrans_extended", "--skip_pruning", "--max_chunk_size=1000", "--skip_pickle"],
    # ["test_atlTrans_extended", "--skip_pruning", "--max_chunk_size=2000", "--skip_pickle"],
    #
    # ["test_mbeddr", "--slice=2", "--skip_pruning", "--max_chunk_size=5", "--skip_pickle"],
    # ["test_mbeddr", "--slice=2", "--skip_pruning", "--max_chunk_size=10", "--skip_pickle"],
    # ["test_mbeddr", "--slice=2", "--skip_pruning", "--max_chunk_size=20", "--skip_pickle"],
    # ["test_mbeddr", "--slice=2", "--skip_pruning", "--max_chunk_size=100", "--skip_pickle"],
    # ["test_mbeddr", "--slice=2", "--skip_pruning", "--max_chunk_size=200", "--skip_pickle"],
    # ["test_mbeddr", "--slice=2", "--skip_pruning", "--max_chunk_size=500", "--skip_pickle"],
    # ["test_mbeddr", "--slice=2", "--skip_pruning", "--max_chunk_size=1000", "--skip_pickle"],
    # ["test_mbeddr", "--slice=2", "--skip_pruning", "--max_chunk_size=2000", "--skip_pickle"],

    # Pruning
    # (F2P, GM, UML, mbeddr, RSS2ATOM)
    # Do with/without parallel
    #
    # ["test_atlTrans_extended", "--skip_pruning", "--skip_parallel"],
    # ["test_atlTrans_extended", "--skip_parallel"],
    # ["test_atlTrans_extended", "--skip_pruning"],
    # ["test_atlTrans_extended",],
    #
    # ["test_GM2Autosar_transformation", "--skip_pruning", "--skip_parallel"],
    # ["test_GM2Autosar_transformation", "--skip_parallel"],
    # ["test_GM2Autosar_transformation", "--skip_pruning"],
    # ["test_GM2Autosar_transformation",],
    #
    # ["test_umlToKiltera", "--skip_pruning", "--skip_parallel"],
    # ["test_umlToKiltera", "--skip_parallel"],
    # ["test_umlToKiltera", "--skip_pruning"],
    # ["test_umlToKiltera",],
    #
    # ["test_mbeddr", "--slice=2", "--skip_pruning", "--skip_parallel"],
    # ["test_mbeddr", "--slice=2", "--skip_parallel"],
    # ["test_mbeddr", "--slice=2", "--skip_pruning"],
    # ["test_mbeddr", "--slice=2",],
    #
    # ["test_RSS2ATOM", "--skip_pruning", "--skip_parallel"],
    # ["test_RSS2ATOM", "--skip_parallel"],
    # ["test_RSS2ATOM", "--skip_pruning"],
    # ["test_RSS2ATOM",],

    # Slicing
    # --Time taken for slicing
    # --Slicing results for each transformation
    # (F2P, GM, UML, mbeddr, RSS2ATOM)

    # ---->DO CONTRACT SELECTION<-----------

    # ["test_atlTrans_extended", "--skip_pruning", "--skip_parallel"],
    ["test_atlTrans_extended", "--skip_pruning", "--skip_parallel", "--contract=0"],
    ["test_atlTrans_extended", "--skip_pruning", "--skip_parallel", "--contract=1"],
    ["test_atlTrans_extended", "--skip_pruning", "--skip_parallel", "--contract=2"],
    ["test_atlTrans_extended", "--skip_pruning", "--skip_parallel", "--contract=3"],
    ["test_atlTrans_extended", "--skip_pruning", "--skip_parallel", "--contract=4"],
    ["test_atlTrans_extended", "--skip_pruning", "--skip_parallel", "--contract=5"],
    ["test_atlTrans_extended", "--skip_pruning", "--skip_parallel", "--contract=6"],
    ["test_atlTrans_extended", "--skip_pruning", "--skip_parallel", "--contract=7"],
    ["test_atlTrans_extended", "--skip_pruning", "--skip_parallel", "--contract=8"],
    ["test_atlTrans_extended", "--skip_pruning", "--skip_parallel", "--contract=9"],
     ["test_atlTrans_extended", "--skip_pruning", "--skip_parallel", "--slice=9"],
    #
    # ["test_GM2Autosar_transformation", "--skip_pruning", "--skip_parallel"],
    # ["test_GM2Autosar_transformation", "--skip_pruning", "--skip_parallel", "--slice=0"],
    # ["test_GM2Autosar_transformation", "--skip_pruning", "--skip_parallel", "--slice=1"],
    # ["test_GM2Autosar_transformation", "--skip_pruning", "--skip_parallel", "--slice=2"],
    # ["test_GM2Autosar_transformation", "--skip_pruning", "--skip_parallel", "--slice=3"],
    # ["test_GM2Autosar_transformation", "--skip_pruning", "--skip_parallel", "--slice=4"],
    # ["test_GM2Autosar_transformation", "--skip_pruning", "--skip_parallel", "--slice=5"],
    # ["test_GM2Autosar_transformation", "--skip_pruning", "--skip_parallel", "--slice=6"],
    # ["test_GM2Autosar_transformation", "--skip_pruning", "--skip_parallel", "--slice=7"],
    # ["test_GM2Autosar_transformation", "--skip_pruning", "--skip_parallel", "--slice=8"],

    #["test_umlToKiltera", "--skip_pruning", "--skip_parallel"],
    ["test_umlToKiltera", "--skip_pruning", "--skip_parallel", "--contract=0"],
    ["test_umlToKiltera", "--skip_pruning", "--skip_parallel", "--contract=1"],
    ["test_umlToKiltera", "--skip_pruning", "--skip_parallel", "--contract=2"],
    ["test_umlToKiltera", "--skip_pruning", "--skip_parallel", "--contract=3"],
    ["test_umlToKiltera", "--skip_pruning", "--skip_parallel", "--contract=4"],
    ["test_umlToKiltera", "--skip_pruning", "--skip_parallel", "--contract=5"],
    ["test_umlToKiltera", "--skip_pruning", "--skip_parallel", "--contract=6"],
    ["test_umlToKiltera", "--skip_pruning", "--skip_parallel", "--contract=7"],
    ["test_umlToKiltera", "--skip_pruning", "--skip_parallel", "--contract=8"],
    ["test_umlToKiltera", "--skip_pruning", "--skip_parallel", "--contract=9"],
    ["test_umlToKiltera", "--skip_pruning", "--skip_parallel", "--contract=10"],
    ["test_umlToKiltera", "--skip_pruning", "--skip_parallel", "--contract=11"],
    ["test_umlToKiltera", "--skip_pruning", "--skip_parallel", "--contract=12"],
    ["test_umlToKiltera", "--skip_pruning", "--skip_parallel", "--contract=13"],
    ["test_umlToKiltera", "--skip_pruning", "--skip_parallel", "--contract=14"],
    ["test_umlToKiltera", "--skip_pruning", "--skip_parallel", "--contract=15"],

    # ["test_RSS2ATOM", "--skip_pruning", "--skip_parallel"],
    # ["test_RSS2ATOM", "--skip_pruning", "--skip_parallel", "--slice=0"],
    # ["test_RSS2ATOM", "--skip_pruning", "--skip_parallel", "--slice=1"],

    # Pickling
    # Do with/without parallel
    # (F2P, GM, UML, mbeddr, RSS2ATOM)
    # ["test_atlTrans_extended", "--skip_pruning", "--skip_parallel"],
    # ["test_atlTrans_extended", "--skip_pruning", "--skip_parallel", "--skip_pickle"],
    #
    # ["test_GM2Autosar_transformation", "--skip_pruning", "--skip_parallel"],
    # ["test_GM2Autosar_transformation", "--skip_pruning", "--skip_parallel", "--skip_pickle"],
    #
    # ["test_mbeddr", "--slice=2", "--skip_pruning", "--skip_parallel"],
    # ["test_mbeddr", "--slice=2", "--skip_pruning", "--skip_parallel", "--skip_pickle"],
    #
    # ["test_umlToKiltera", "--skip_pruning", "--skip_parallel"],
    # ["test_umlToKiltera", "--skip_pruning", "--skip_parallel", "--skip_pickle"],
    #
    # ["test_RSS2ATOM", "--skip_pruning", "--skip_parallel"],
    # ["test_RSS2ATOM", "--skip_pruning", "--skip_parallel", "--skip_pickle"],

    # TEST DISK SPACE FOR COMPRESSION

    ["test_atlTrans_extended", "--skip_pruning", "--skip_parallel"],
    ["test_atlTrans_extended", "--skip_pruning", "--skip_parallel", "--compression=0"],
    ["test_atlTrans_extended", "--skip_pruning", "--skip_parallel", "--compression=9"],

    ["test_GM2Autosar_transformation", "--skip_pruning", "--skip_parallel"],
    ["test_GM2Autosar_transformation", "--skip_pruning", "--skip_parallel", "--compression=0"],
    ["test_GM2Autosar_transformation", "--skip_pruning", "--skip_parallel", "--compression=9"],

    ["test_mbeddr", "--slice=2", "--skip_pruning", "--skip_parallel"],
    ["test_mbeddr", "--slice=2", "--skip_pruning", "--skip_parallel", "--compression=0"],
    ["test_mbeddr", "--slice=2", "--skip_pruning", "--skip_parallel", "--compression=9"],

    ["test_umlToKiltera", "--skip_pruning", "--skip_parallel"],
    ["test_umlToKiltera", "--skip_pruning", "--skip_parallel", "--compression=0"],
    ["test_umlToKiltera", "--skip_pruning", "--skip_parallel", "--compression=9"],

    ["test_RSS2ATOM", "--skip_pruning", "--skip_parallel"],
    ["test_RSS2ATOM", "--skip_pruning", "--skip_parallel", "--compression=0"],
    ["test_RSS2ATOM", "--skip_pruning", "--skip_parallel", "--compression=9"],

    #Old match set generation
    ["test_atlTrans_extended", "--skip_pruning",],
    ["test_atlTrans_extended", "--skip_pruning", "--old_match_gen"],

    ["test_GM2Autosar_transformation", "--skip_pruning", ],
    ["test_GM2Autosar_transformation", "--skip_pruning", "--old_match_gen"],

    ["test_mbeddr", "--slice=2", "--skip_pruning", ],
    ["test_mbeddr", "--slice=2", "--skip_pruning", "--old_match_gen"],

    ["test_umlToKiltera", "--skip_pruning", ],
    ["test_umlToKiltera", "--skip_pruning", "--old_match_gen"],

    ["test_RSS2ATOM", "--skip_pruning", ],
    ["test_RSS2ATOM", "--skip_pruning", "--old_match_gen"],


    #Per number of threads
    ["test_atlTrans_extended", "--skip_pruning", "--num_threads=1"],
    ["test_atlTrans_extended", "--skip_pruning", "--num_threads=2"],
    ["test_atlTrans_extended", "--skip_pruning", "--num_threads=3"],
    ["test_atlTrans_extended", "--skip_pruning", "--num_threads=4"],
    ["test_atlTrans_extended", "--skip_pruning", "--num_threads=5"],
    ["test_atlTrans_extended", "--skip_pruning", "--num_threads=6"],
    ["test_atlTrans_extended", "--skip_pruning", "--num_threads=7"],
    ["test_atlTrans_extended", "--skip_pruning", "--num_threads=8"],

    ["test_GM2Autosar_transformation", "--skip_pruning", "--num_threads=1"],
    ["test_GM2Autosar_transformation", "--skip_pruning", "--num_threads=2"],
    ["test_GM2Autosar_transformation", "--skip_pruning", "--num_threads=3"],
    ["test_GM2Autosar_transformation", "--skip_pruning", "--num_threads=4"],
    ["test_GM2Autosar_transformation", "--skip_pruning", "--num_threads=5"],
    ["test_GM2Autosar_transformation", "--skip_pruning", "--num_threads=6"],
    ["test_GM2Autosar_transformation", "--skip_pruning", "--num_threads=7"],
    ["test_GM2Autosar_transformation", "--skip_pruning", "--num_threads=8"],

    ["test_mbeddr", "--slice=2", "--skip_pruning", "--num_threads=1"],
    ["test_mbeddr", "--slice=2", "--skip_pruning", "--num_threads=2"],
    ["test_mbeddr", "--slice=2", "--skip_pruning", "--num_threads=3"],
    ["test_mbeddr", "--slice=2", "--skip_pruning", "--num_threads=4"],
    ["test_mbeddr", "--slice=2", "--skip_pruning", "--num_threads=5"],
    ["test_mbeddr", "--slice=2", "--skip_pruning", "--num_threads=6"],
    ["test_mbeddr", "--slice=2", "--skip_pruning", "--num_threads=7"],
    ["test_mbeddr", "--slice=2", "--skip_pruning", "--num_threads=8"],

    ["test_umlToKiltera", "--skip_pruning", "--num_threads=1"],
    ["test_umlToKiltera", "--skip_pruning", "--num_threads=2"],
    ["test_umlToKiltera", "--skip_pruning", "--num_threads=3"],
    ["test_umlToKiltera", "--skip_pruning", "--num_threads=4"],
    ["test_umlToKiltera", "--skip_pruning", "--num_threads=5"],
    ["test_umlToKiltera", "--skip_pruning", "--num_threads=6"],
    ["test_umlToKiltera", "--skip_pruning", "--num_threads=7"],
    ["test_umlToKiltera", "--skip_pruning", "--num_threads=8"],

    ["test_RSS2ATOM", "--skip_pruning", "--num_threads=1"],
    ["test_RSS2ATOM", "--skip_pruning", "--num_threads=2"],
    ["test_RSS2ATOM", "--skip_pruning", "--num_threads=3"],
    ["test_RSS2ATOM", "--skip_pruning", "--num_threads=4"],
    ["test_RSS2ATOM", "--skip_pruning", "--num_threads=5"],
    ["test_RSS2ATOM", "--skip_pruning", "--num_threads=6"],
    ["test_RSS2ATOM", "--skip_pruning", "--num_threads=7"],
    ["test_RSS2ATOM", "--skip_pruning", "--num_threads=8"],
]

results_dir = os.path.expanduser("~/Dropbox/University/PHD/results")
results_filename = os.path.join(results_dir, "000-all_results.txt")

with open(results_filename, "w") as a:
    for i, experiment in enumerate(experiments):

        experiment_name = experiment[0]
        experiment_args = experiment[1:]

        #print(i)
        #print(experiment_name)
        #print(experiment_args)

        args_string = "".join(experiment_args)
        args_string = args_string.replace("=", "").replace("-", "")

        #print(args_string)

        ex_filename = os.path.join(results_dir, str(i) + "-" + experiment_name + "-" + args_string + ".txt")

        #print(ex_filename)

        #open fresh file, and write header
        with open(ex_filename, 'w') as h:
            h.write("Starting experiments for: " + experiment_name + "-" + args_string)


        with open(ex_filename, 'w+') as g:

            for x in range(times_to_run):

                print("Running " + str(i) + "-" + experiment_name +"-" + args_string + " for time " + str(x))
                command = ["/usr/bin/time", "python3", experiment_name + ".py"] + experiment_args

                print("Command: " + " ".join(command))
                command.append("--skip_progress_bar")
                proc = subprocess.check_call(command, stdout=g, stderr=subprocess.STDOUT)

        time_build_pcs = []
        time_contract_proof = []
        memory = []
        num_pcs = []

        pruning_time = []
        slicing_time = []
        dividing_time = []

        with open(ex_filename) as f:

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
                elif "Time taken for: -Dividing pcs-" in line:
                    t = line.split(" ")[5]
                    dividing_time.append(float(t))
                    print(line)
                # elif "Time taken for: -Pruning pcs-" in line:
                #     t = line.split(" ")[5]
                #     pruning_time.append(float(t))
                elif "Time taken for: -slicing-" in line:
                    t = line.split(" ")[4]
                    slicing_time.append(float(t))
                    print(line)

                #print(line.strip())

        with open(ex_filename, "a") as f:
            avg_build_time = get_avg(time_build_pcs)
            avg_proof_time = get_avg(time_contract_proof)

            s1 = "\nResults for '" + experiment_name +"-" + args_string +"'"
            s2 = "Time build: " + str(round(avg_build_time, 2))
            s3 = "Time proof: " + str(round(avg_proof_time, 2))
            s4 = "Memory: " + str(int(get_avg(memory)))
            s5 = "Number of path conditions: " + str(int(get_avg(num_pcs)))

            s6 = "Dividing time: " + str(round(get_avg(dividing_time), 4))
            #s7 = "Pruning time: " + str(round(get_avg(pruning_time), 2))

            slicing_time = round(get_avg(slicing_time), 4)
            if slicing_time > -1:
                s8 = "Slicing time: " + str()
            else:
                s8 = None

            for s in [s1, s2, s3, s4, s5, s6, s8]:
                if s is None:
                    continue

                print(s)
                f.write(s + "\n")
                a.write(s + "\n")


