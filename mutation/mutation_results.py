from collections import defaultdict

import matplotlib.pyplot as plt
import numpy

class Result:

    def __init__(self, mut_type, schemes, results):
        self.mut_type = mut_type
        self.schemes = schemes
        self.results = results

    def __repr__(self):
        return "result - " + str(self.mut_type) + "-" + str(self.results)



class MutationResults:

    def __init__(self, sbfl_dir):
        self.sbfl_dir = sbfl_dir

        self.trans_array = ["F2P", "RSS", "UML2ER", "GM", "Kiltera"]


    def calc(self):

        all_results = []
        for trans in self.trans_array:
            results_dir = "models_" + trans + "/results/"
            results_file = self.sbfl_dir + results_dir + "results_AC.csv"

            print("Opening file: " + results_file)

            results_arr = []
            schemes = []

            first_line = True
            with open(results_file) as f:
                for line in f:

                    if first_line:
                        first_line = False


                        for s in line.split(";"):
                            if not s:
                                continue
                            if "PCs" in s:
                                break
                            schemes.append(s)
                        continue

                    tokens = line.split(";")

                    mut_type = tokens[0].split("'")[1]

                    results = {}
                    for i, t in enumerate(tokens):
                        if i == 0:
                            continue
                        if not t.strip():
                            break
                        scheme = schemes[i-1]
                        results[scheme] = t

                    result = Result(mut_type, schemes, results)
                    results_arr.append(result)

            all_results += results_arr

            self.parse_results(trans, schemes, results_arr)


        self.examine_muts(schemes, all_results)

    def examine_muts(self, schemes, results):

        results_by_type = defaultdict(list)
        for r in results:
            results_by_type[r.mut_type].append(r)
            print(results_by_type[r.mut_type])

        for rbt, results_arr in results_by_type.items():

            print("For mut type: " + rbt)
            bins = list(numpy.arange(0, 1, 0.1))

            # order schemes by avg
            schemes_with_avg = []

            for scheme in schemes:
                scores = [float(result.results[scheme]) for result in results_arr]
                schemes_with_avg.append((scheme, numpy.average(scores)))
            schemes_with_avg.sort(key=lambda t: t[1])
            print(schemes_with_avg)

            fig, axs = plt.subplots(len(schemes))
            fig.suptitle("Scores for " + rbt)

            for i, scheme_and_score in enumerate(schemes_with_avg):
                scheme, avg = scheme_and_score
                scores = [float(result.results[scheme]) for result in results_arr]

                #print("Scheme: " + scheme + " - " + str(avg))
                #print(scores)

                axs[i].title.set_text(scheme + " - " + str(round(avg, 2)))
                axs[i].hist(scores, bins=bins)
            #plt.show()
            filename = rbt + ".png"
            plt.savefig(filename)


    def parse_results(self, trans, schemes, results_arr):

        print("For trans: " + trans)
        bins = list(numpy.arange(0, 1, 0.1))

        if len(results_arr) == 0:
            print("No results")
            return

        # order schemes by avg
        schemes_with_avg = []

        for scheme in schemes:
            scores = [float(result.results[scheme]) for result in results_arr]
            schemes_with_avg.append((scheme, numpy.average(scores)))
        schemes_with_avg.sort(key=lambda t: t[1])
        print(schemes_with_avg)

        fig, axs = plt.subplots(len(schemes))
        fig.suptitle("Scores for " + trans)

        for i, scheme_and_score in enumerate(schemes_with_avg):
            scheme, avg = scheme_and_score
            scores = [float(result.results[scheme]) for result in results_arr]

            #print("Scheme: " + scheme + " - " + str(avg))
            #print(scores)

            axs[i].title.set_text(scheme + " - " + str(round(avg, 2)))
            axs[i].hist(scores, bins=bins)
        #plt.show()
        filename = trans + ".png"
        plt.savefig(filename)

if __name__ == "__main__":

    sbfl_dir = "/home/xubuntu/Projects/SBFL/"
    mr = MutationResults(sbfl_dir)

    mr.calc()

