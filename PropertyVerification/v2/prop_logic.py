from PropertyVerification.v2.contract import Contract

class NotContract(Contract):

    def __init__(self, atomic_contract):
        super(NotContract, self).__init__()

        self.contract = atomic_contract

    def check_isolated(self, pc):
        return self.contract.check_isolated(pc)

    def check(self, pc, verbosity=0):
        result = self.contract.check(pc, verbosity)

        if verbosity > 1:
            print("NotContract: Result was " + result)

        if result == self.contract.NO_COMPLETE:
            return self.contract.COMPLETE_FOUND
        elif result == self.contract.COMPLETE_FOUND:
            return self.contract.NO_COMPLETE
        else:
            return result

    def draw(self):
        self.contract.draw()

    def get_pivots(self):
        return self.contract.get_pivots()

class AndContract(Contract):
    def __init__(self, atomic_contract_1, atomic_contract_2):
        super(AndContract, self).__init__()

        self.contract_1 = atomic_contract_1
        self.contract_2 = atomic_contract_2

    def check_isolated(self, pc):

        result_1 = self.contract_1.check_isolated(pc)
        if result_1 == self.NO_ISOLATED:
            return result_1

        return self.contract_2.check_isolated(pc)

    def check(self, pc, verbosity = 0):
        result_1 = self.contract_1.check(pc, verbosity)

        if result_1 != self.COMPLETE_FOUND:
            return result_1

        if verbosity > 1:
            print("And Contract: First contract is " + result_1)

        result_2 = self.contract_2.check(pc, verbosity)

        if verbosity > 1:
            print("And Contract: Second contract is " + result_2)

        return result_2

    def draw(self):
        self.contract_1.draw()
        self.contract_2.draw()

    def get_pivots(self):
        pivots_1 = self.contract_1.get_pivots()
        pivots_2 = self.contract_2.get_pivots()

        # print("Contract 1")
        # print(pivots_1)
        #
        # print("Contract 2")
        # print(pivots_2)

        #put these two together
        #report a FAILURE if they are inconsistent

        result = dict(pivots_1)
        for key in pivots_2:
            if key in result and result[key] != pivots_2[key]:
                result[key] = "FAILURE"
            else:
                result[key] = pivots_2[key]
        return result

class OrContract(Contract):
    def __init__(self, atomic_contract_1, atomic_contract_2):
        super(OrContract, self).__init__()

        self.contract_1 = atomic_contract_1
        self.contract_2 = atomic_contract_2

    def check_isolated(self, pc):

        result_1 = self.contract_1.check_isolated(pc)
        if result_1 == self.ISOLATED:
            return result_1

        return self.contract_2.check_isolated(pc)

    def check(self, pc, verbosity = 0):
        result_1 = self.contract_1.check(pc, verbosity)

        if result_1 == self.COMPLETE_FOUND:
            return result_1

        if verbosity > 1:
            print("Or Contract: First contract is " + result_1)

        result_2 = self.contract_2.check(pc, verbosity)

        if verbosity > 1:
            print("Or Contract: Second contract is " + result_2)

        return result_2

    def draw(self):
        self.contract_1.draw()
        self.contract_2.draw()

    def get_pivots(self):
        pivots_1 = self.contract_1.get_pivots()
        pivots_2 = self.contract_2.get_pivots()

        # print("Contract 1")
        # print(pivots_1)
        #
        # print("Contract 2")
        # print(pivots_2)

        #put these two together
        #report a FAILURE if they are inconsistent

        return pivots_1.update(pivots_2)