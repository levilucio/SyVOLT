import subprocess
import os
import shutil
try:
    import statistics.variance as variance
except ImportError:
    from numpy import var as variance
    
def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

def calc_dir_size(dir_name):
    return sum(os.path.getsize(os.path.join(dir_name, f)) for f in os.listdir(dir_name) if os.path.isfile(os.path.join(dir_name, f)))

def get_avg(l):
    if len(l) == 0:
        return -1
    return sum(l) / float(len(l))

times_to_run = 5

experiments = []


#MBEDDR
# for i in range(22, 50):
# experiments.append(["test_mbeddr", "--skip_pruning", ])
# experiments.append(["test_mbeddr", "--skip_pruning", "--old_match_gen"])

# experiments.append(["test_mbeddr", "--skip_parallel", "--skip_pruning"],)
# experiments.append(["test_mbeddr", "--shuffle", "--skip_pruning"],)
# experiments.append(["test_mbeddr",  "--skip_pruning"],)

# experiments.append(["test_mbeddr", ])
# experiments.append(["test_mbeddr", "--skip_pruning"], )

# experiments.append(["test_mbeddr", "--slice=2", "--skip_pruning", "--skip_parallel"],)
# experiments.append(["test_mbeddr", "--slice=2", "--skip_pruning", "--skip_parallel", "--skip_pickle"],)
# experiments.append(["test_mbeddr", "--slice=2", "--skip_pruning", "--skip_parallel", "--compression=0"],)


#Experiments
# - Changing match set generation
# - FTP, UML, mbeddr
# no pruning, shuffle, parallel

#Old match set generation=================================
experiments.append(["test_atlTrans_extended", "--skip_pruning",])
experiments.append(["test_atlTrans_extended", "--skip_pruning", "--old_match_gen"])

experiments.append(["test_GM2Autosar_transformation", "--skip_pruning", ])
experiments.append(["test_GM2Autosar_transformation", "--skip_pruning", "--old_match_gen"])

experiments.append(["test_mbeddr", "--slice=2", "--skip_pruning", ])
experiments.append(["test_mbeddr", "--slice=2", "--skip_pruning", "--old_match_gen"])

experiments.append(["test_umlToKiltera", "--skip_pruning", ])
experiments.append(["test_umlToKiltera", "--skip_pruning", "--old_match_gen"])

experiments.append(["test_RSS2ATOM", "--skip_pruning", ])
experiments.append(["test_RSS2ATOM", "--skip_pruning", "--old_match_gen"])



        # Parallel================================
    # (F2P)
    # --Off
    # --Shuffle
    # --Bin packing
    # no pruning
experiments.append(["test_atlTrans_extended", "--skip_pruning"])
experiments.append(["test_atlTrans_extended", "--skip_parallel", "--skip_pruning"])
experiments.append(["test_atlTrans_extended", "--shuffle", "--skip_pruning"])

experiments.append(["test_mbeddr", "--slice=2", "--skip_parallel", "--skip_pruning"])
experiments.append(["test_mbeddr", "--slice=2", "--shuffle", "--skip_pruning"])
experiments.append(["test_mbeddr", "--slice=2", "--skip_pruning"],)
    #
experiments.append(["test_mbeddr", "--slice=0", "--skip_parallel", "--skip_pruning"],)
experiments.append(["test_mbeddr", "--slice=0", "--shuffle", "--skip_pruning"],)
experiments.append(["test_mbeddr", "--slice=0", "--skip_pruning"],)

experiments.append(["test_mbeddr", "--slice=0", "--skip_parallel", "--skip_pruning", "--num_rules=34"],)
experiments.append(["test_mbeddr", "--slice=0", "--shuffle", "--skip_pruning", "--num_rules=34"],)
experiments.append(["test_mbeddr", "--slice=0", "--skip_pruning", "--num_rules=34"],)

experiments.append(["test_mbeddr", "--slice=2", "--skip_parallel", "--skip_pruning", "--num_rules=34"],)
experiments.append(["test_mbeddr", "--slice=2", "--shuffle", "--skip_pruning", "--num_rules=34"],)
experiments.append(["test_mbeddr", "--slice=2", "--skip_pruning", "--num_rules=34"],)

experiments.append(["test_GM2Autosar_transformation", "--skip_pruning"],)
experiments.append(["test_GM2Autosar_transformation", "--skip_parallel", "--skip_pruning"],)
experiments.append(["test_GM2Autosar_transformation", "--shuffle", "--skip_pruning"],)

experiments.append(["test_umlToKiltera", "--skip_pruning"],)
experiments.append(["test_umlToKiltera", "--skip_parallel", "--skip_pruning"],)
experiments.append(["test_umlToKiltera", "--shuffle", "--skip_pruning"],)

experiments.append(["test_RSS2ATOM", "--skip_pruning"],)
experiments.append(["test_RSS2ATOM", "--skip_parallel", "--skip_pruning"],)
experiments.append(["test_RSS2ATOM", "--shuffle", "--skip_pruning"],)



   # Slicing
    # --Time taken for slicing
    # --Slicing results for each transformation
    # (F2P, GM, UML, mbeddr, RSS2ATOM)

    # ---->DO CONTRACT SELECTION<-----------

experiments.append(["test_atlTrans_extended", "--skip_pruning", "--skip_parallel"],)

for i in range(10):
    experiments.append(["test_atlTrans_extended", "--skip_pruning", "--skip_parallel", "--slice={}".format(str(i))],)

experiments.append(["test_umlToKiltera", "--skip_pruning", "--skip_parallel"], )
for i in range(16):
    experiments.append(["test_umlToKiltera", "--skip_pruning", "--skip_parallel", "--slice={}".format(str(i))],)

experiments.append(["test_GM2Autosar_transformation", "--skip_pruning", "--skip_parallel"], )
for i in range(9):
    experiments.append(["test_GM2Autosar_transformation", "--skip_pruning", "--skip_parallel", "--slice={}".format(str(i))],)

experiments.append(["test_RSS2ATOM", "--skip_pruning", "--skip_parallel"], )
for i in range(2):
    experiments.append(["test_RSS2ATOM", "--skip_pruning", "--skip_parallel", "--slice={}".format(str(i))], )





# Pruning========================================
# (F2P, GM, UML, mbeddr, RSS2ATOM)
# Do with/without parallel

experiments.append(["test_atlTrans_extended", ], )
experiments.append(["test_atlTrans_extended", "--skip_pruning"], )

experiments.append(["test_GM2Autosar_transformation", ], )
experiments.append(["test_GM2Autosar_transformation", "--skip_pruning"], )

experiments.append(["test_umlToKiltera", ], )
experiments.append(["test_umlToKiltera", "--skip_pruning"], )

experiments.append(["test_mbeddr", "--slice=2"], )
experiments.append(["test_mbeddr", "--slice=2", "--skip_pruning"], )

experiments.append(["test_mbeddr", "--slice=0"], )
experiments.append(["test_mbeddr", "--slice=0", "--skip_pruning"], )

experiments.append(["test_mbeddr", "--slice=2", "--num_rules=34"], )
experiments.append(["test_mbeddr", "--slice=2", "--num_rules=34", "--skip_pruning"], )

experiments.append(["test_mbeddr", "--slice=0", "--num_rules=34"], )
experiments.append(["test_mbeddr", "--slice=0", "--num_rules=34", "--skip_pruning"], )

experiments.append(["test_RSS2ATOM", ], )
experiments.append(["test_RSS2ATOM", "--skip_pruning"], )




    # Pickling
    # Do with/without parallel
    # (F2P, GM, UML, mbeddr, RSS2ATOM)
experiments.append(["test_atlTrans_extended", "--skip_pruning", "--skip_parallel"],)
experiments.append(["test_atlTrans_extended", "--skip_pruning", "--skip_parallel", "--skip_pickle"],)
experiments.append(["test_atlTrans_extended", "--skip_pruning", "--skip_parallel", "--compression=0"],)
    #
experiments.append(["test_GM2Autosar_transformation", "--skip_pruning", "--skip_parallel"],)
experiments.append(["test_GM2Autosar_transformation", "--skip_pruning", "--skip_parallel", "--skip_pickle"],)
experiments.append(["test_GM2Autosar_transformation", "--skip_pruning", "--skip_parallel", "--compression=0"],)

experiments.append(["test_mbeddr", "--slice=0", "--skip_pruning", "--skip_parallel"],)
experiments.append(["test_mbeddr", "--slice=0", "--skip_pruning", "--skip_parallel", "--skip_pickle"],)
experiments.append(["test_mbeddr", "--slice=0", "--skip_pruning", "--skip_parallel", "--compression=0"],)

experiments.append(["test_mbeddr", "--slice=2", "--skip_pruning", "--skip_parallel"],)
experiments.append(["test_mbeddr", "--slice=2", "--skip_pruning", "--skip_parallel", "--skip_pickle"],)
experiments.append(["test_mbeddr", "--slice=2", "--skip_pruning", "--skip_parallel", "--compression=0"],)
    #
experiments.append(["test_umlToKiltera", "--skip_pruning", "--skip_parallel"],)
experiments.append(["test_umlToKiltera", "--skip_pruning", "--skip_parallel", "--skip_pickle"],)
experiments.append(["test_umlToKiltera", "--skip_pruning", "--skip_parallel", "--compression=0"],)
    #
experiments.append(["test_RSS2ATOM", "--skip_pruning", "--skip_parallel"],)
experiments.append(["test_RSS2ATOM", "--skip_pruning", "--skip_parallel", "--skip_pickle"],)
experiments.append(["test_RSS2ATOM", "--skip_pruning", "--skip_parallel", "--compression=0"],)




    #Per number of threads
    # ["test_atlTrans_extended", "--skip_pruning", "--num_threads=1"],
    # ["test_atlTrans_extended", "--skip_pruning", "--num_threads=2"],
    # ["test_atlTrans_extended", "--skip_pruning", "--num_threads=3"],
    # ["test_atlTrans_extended", "--skip_pruning", "--num_threads=4"],
    # ["test_atlTrans_extended", "--skip_pruning", "--num_threads=5"],
    # ["test_atlTrans_extended", "--skip_pruning", "--num_threads=6"],
    # ["test_atlTrans_extended", "--skip_pruning", "--num_threads=7"],
    # ["test_atlTrans_extended", "--skip_pruning", "--num_threads=8"],
    #
    # ["test_GM2Autosar_transformation", "--skip_pruning", "--num_threads=1"],
    # ["test_GM2Autosar_transformation", "--skip_pruning", "--num_threads=2"],
    # ["test_GM2Autosar_transformation", "--skip_pruning", "--num_threads=3"],
    # ["test_GM2Autosar_transformation", "--skip_pruning", "--num_threads=4"],
    # ["test_GM2Autosar_transformation", "--skip_pruning", "--num_threads=5"],
    # ["test_GM2Autosar_transformation", "--skip_pruning", "--num_threads=6"],
    # ["test_GM2Autosar_transformation", "--skip_pruning", "--num_threads=7"],
    # ["test_GM2Autosar_transformation", "--skip_pruning", "--num_threads=8"],
    #
    # ["test_mbeddr", "--slice=2", "--skip_pruning", "--num_threads=1"],
    # ["test_mbeddr", "--slice=2", "--skip_pruning", "--num_threads=2"],
    # ["test_mbeddr", "--slice=2", "--skip_pruning", "--num_threads=3"],
    # ["test_mbeddr", "--slice=2", "--skip_pruning", "--num_threads=4"],
    # ["test_mbeddr", "--slice=2", "--skip_pruning", "--num_threads=5"],
    # ["test_mbeddr", "--slice=2", "--skip_pruning", "--num_threads=6"],
    # ["test_mbeddr", "--slice=2", "--skip_pruning", "--num_threads=7"],
    # ["test_mbeddr", "--slice=2", "--skip_pruning", "--num_threads=8"],
    #
    # ["test_umlToKiltera", "--skip_pruning", "--num_threads=1"],
    # ["test_umlToKiltera", "--skip_pruning", "--num_threads=2"],
    # ["test_umlToKiltera", "--skip_pruning", "--num_threads=3"],
    # ["test_umlToKiltera", "--skip_pruning", "--num_threads=4"],
    # ["test_umlToKiltera", "--skip_pruning", "--num_threads=5"],
    # ["test_umlToKiltera", "--skip_pruning", "--num_threads=6"],
    # ["test_umlToKiltera", "--skip_pruning", "--num_threads=7"],
    # ["test_umlToKiltera", "--skip_pruning", "--num_threads=8"],
    #
    # ["test_RSS2ATOM", "--skip_pruning", "--num_threads=1"],
    # ["test_RSS2ATOM", "--skip_pruning", "--num_threads=2"],
    # ["test_RSS2ATOM", "--skip_pruning", "--num_threads=3"],
    # ["test_RSS2ATOM", "--skip_pruning", "--num_threads=4"],
    # ["test_RSS2ATOM", "--skip_pruning", "--num_threads=5"],
    # ["test_RSS2ATOM", "--skip_pruning", "--num_threads=6"],
    # ["test_RSS2ATOM", "--skip_pruning", "--num_threads=7"],
    # ["test_RSS2ATOM", "--skip_pruning", "--num_threads=8"],


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

                #delete pickle and patterns dir for accurate disk usage
                if os.path.exists("./pickle"):
                    shutil.rmtree("./pickle")
                if os.path.exists("./patterns"):
                    shutil.rmtree("./patterns")


                print("Command: " + " ".join(command))
                command.append("--skip_progress_bar")
                proc = subprocess.check_call(command, stdout=g, stderr=subprocess.STDOUT)

                patterns_space = calc_dir_size("./patterns")
                pickle_space = calc_dir_size("./pickle")
                g.write("Space taken: " + str(patterns_space + pickle_space) + " bytes\n")


        time_build_pcs = []
        time_contract_proof = []
        memory = []
        num_pcs = []

        pruning_time = []
        slicing_time = []
        dividing_time = []

        space_taken = []

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
                    #print(line)
                # elif "Time taken for: -Pruning pcs-" in line:
                #     t = line.split(" ")[5]
                #     pruning_time.append(float(t))
                elif "Time taken for: -slicing-" in line:
                    t = line.split(" ")[4]
                    slicing_time.append(float(t))
                    #print(line)
                elif "Space taken: " in line:
                    t = line.split(" ")[2]
                    space_taken.append(int(t))
                    #print(line)

                #print(line.strip())

        with open(ex_filename, "a") as f:
            avg_build_time = get_avg(time_build_pcs)
            avg_proof_time = get_avg(time_contract_proof)

            s1 = "\nResults for '" + experiment_name +"-" + args_string +"'"
            s2 = "Time build: " + str(round(avg_build_time, 2)) + " Var: " + str(variance(avg_build_time))
            s3 = "Time proof: " + str(round(avg_proof_time, 2)) + " Var: " + str(variance(avg_proof_time))
            s4 = "Memory: " + str(int(get_avg(memory))) + " Var: " + str(variance(memory))
            s5 = "Number of path conditions: " + str(int(get_avg(num_pcs)))

            s6 = "Dividing time: " + str(round(get_avg(dividing_time), 4)) + " Var: " + str(variance(dividing_time))
            s7 = "Pruning time: " + str(round(get_avg(pruning_time), 2)) + " Var: " + str(variance(pruning_time))

            slicing_time2 = round(get_avg(slicing_time), 4)
            if slicing_time2 > -1:
                s8 = "Slicing time: " + str(slicing_time2) + " Var: " + str(variance(slicing_time))
            else:
                s8 = None

            s9 = "Space taken: " + str(get_avg(space_taken)) + " bytes"

            for s in [s1, s2, s3, s4, s5, s6, s7, s8, s9]:
                if s is None:
                    continue

                print(s)
                f.write(s + "\n")
                a.write(s + "\n")


