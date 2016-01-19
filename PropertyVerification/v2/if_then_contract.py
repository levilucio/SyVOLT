from PropertyVerification.v2.contract import Contract

class IfThenContract(Contract):

    def __init__(self, if_contract, then_contract):
        super(IfThenContract, self).__init__()

        self.if_contract = if_contract
        self.then_contract = then_contract

    def check_isolated(self, pc):
        return self.if_contract.check_isolated(pc)

    def check(self, pc, verbosity=0):
        result = self.if_contract.check(pc, verbosity)

        if verbosity > 1:
            print("Result for if contract: " + result)

        #don't fail if if_contract is not found
        if result == self.NO_COMPLETE:
            return self.NO_CONNECTED

        if result != self.COMPLETE_FOUND:
            return result


        then_result = self.then_contract.check(pc, verbosity)

        if verbosity > 1:
            print("Result for then contract: " + then_result)

        # do a final check for pivots
        if then_result == self.COMPLETE_FOUND:
            then_result = self.check_pivots(pc)
        return then_result

    def check_pivots(self, pc):

        if_pivots = self.if_contract.get_pivots()

        then_pivots = self.then_contract.get_pivots()

        # print("If pivots")
        # print(if_pivots)
        #
        # print("Then pivots, matches")
        # print(then_pivots)

        for pivot, if_guid in if_pivots.items():

            #the pivot is only defined on the if graph
            if pivot not in then_pivots:
                continue

            then_guid = then_pivots[pivot]

            #these two matches are on different nodes in the source graph
            #so the pivots don't match
            #FAILURE is returned from an AND contract if the guids were different
            if if_guid != then_guid or then_guid == "FAILURE":
                return self.COMPLETE_NOT_FOUND
        return self.COMPLETE_FOUND


    def draw(self):
        self.if_contract.draw()
        self.then_contract.draw()