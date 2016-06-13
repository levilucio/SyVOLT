from PropertyVerification.v2.contract import Contract

class IfThenContract(Contract):

    def __init__(self, if_contract, then_contract):
        super(IfThenContract, self).__init__()

        self.if_contract = if_contract
        self.then_contract = then_contract

        self.name = self.if_contract.name

        self.__name__ = "IfThenContract"

        self.debug = False

    def to_string(self):
        return "IF(" + self.if_contract.to_string() + "): THEN("+ self.then_contract.to_string() + ")"

    def get_graph(self):
        if_graph = self.if_contract.get_graph()
        then_graph = self.then_contract.get_graph()
        return if_graph + then_graph

    def check_isolated(self, pc):
        return self.if_contract.check_isolated(pc)

    def check(self, pc, verbosity=0):
        result = self.if_contract.check(pc, verbosity)

        # if self.debug:
        #     print("Result for if contract: " + result)

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

        return Contract.merge_pivots(self, if_pivots, then_pivots)


    def draw(self):
        self.if_contract.draw()
        self.then_contract.draw()