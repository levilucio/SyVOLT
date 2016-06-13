from PropertyVerification.v2.contract import Contract

class IfThenContract(Contract):

    def __init__(self, if_contract, then_contract):
        super(IfThenContract, self).__init__()

        self.if_contract = if_contract
        self.then_contract = then_contract

        self.name = self.if_contract.name

        self.__name__ = "IfThenContract"

        self.debug = False

    def get_graph(self):
        if_graph = self.if_contract.get_graph()
        then_graph = self.then_contract.get_graph()
        return if_graph + then_graph

    def check_isolated(self, pc):
        return self.if_contract.check_isolated(pc)

    def check(self, pc, verbosity=0):
        result = self.if_contract.check(pc, verbosity)

        if self.debug:
            print("Result for if contract: " + result)

        #don't fail if if_contract is not found
        if result == self.NO_COMPLETE:
            return self.NO_CONNECTED

        if result != self.COMPLETE_FOUND:
            return result


        then_result = self.then_contract.check(pc, verbosity)

        if self.debug:
            print("Result for then contract: " + then_result)

        # do a final check for pivots
        if then_result == self.COMPLETE_FOUND:
            then_result = self.check_pivots(pc)
            if self.debug:
                print("Result for pivots: " + then_result)

        return then_result

    def check_pivots(self, pc):

        if_pivots = self.if_contract.get_pivots()

        then_pivots = self.then_contract.get_pivots()

        if if_pivots is None or then_pivots is None:
            if self.debug:
                print("No pivots in either if or then contract.")
            return self.COMPLETE_FOUND
        # print("If pivots")
        # print(if_pivots)
        #
        # print("Then pivots, matches")
        # print(then_pivots)

        all_if_pivots_succeed = True
        for pivot, if_guids in if_pivots.items():

            #the pivot is only defined on the if graph
            if pivot not in then_pivots:
                continue

            then_guids = then_pivots[pivot]
            if "FAILURE" in then_guids:
                if self.debug:
                    print("Pivot failure on " + str(pivot))
                return self.NO_COMPLETE

            if_guid_succeed = False

            for if_guid in if_guids:
                #these two matches are on different nodes in the source graph
                #so the pivots don't match
                #FAILURE is returned from an AND contract if the guids were different
                if if_guid in then_guids:
                    if_guid_succeed = True

            all_if_pivots_succeed = all_if_pivots_succeed and if_guid_succeed

        if all_if_pivots_succeed:
            return self.COMPLETE_FOUND
        else:
            return self.NO_COMPLETE


    def draw(self):
        self.if_contract.draw()
        self.then_contract.draw()