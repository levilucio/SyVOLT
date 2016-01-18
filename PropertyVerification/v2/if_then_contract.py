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

        return then_result

    def draw(self):
        self.if_contract.draw()
        self.then_contract.draw()