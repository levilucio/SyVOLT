from PropertyVerification.contract import Contract

class NotContract(Contract):

    def __init__(self, atomic_contract):
        super(NotContract, self).__init__()

        self.contract = atomic_contract
        self.name = atomic_contract.name

        self.debug = False

    def to_string(self):
        return "NOT(" + self.name + ")"

    def get_graph(self):
        return self.contract.get_graph()

    def get_complete(self):
        return self.contract.get_complete()

    def check_isolated(self, pc):
        return self.contract.check_isolated(pc)

    def check(self, pc, verbosity=0):
        result = self.contract.check(pc, verbosity)
        new_result = result

        if self.debug:
            print("NotContract: Result was originally " + result)

        if result == self.contract.NO_COMPLETE:
            new_result = self.contract.COMPLETE_FOUND
        elif result == self.contract.COMPLETE_FOUND:
            new_result = self.contract.NO_COMPLETE

        if self.debug:
            print("NotContract: Result changed to " + new_result)

        return new_result

    def draw(self):
        self.contract.draw()

    def get_pivots(self):
        return self.contract.get_pivots()

class AndContract(Contract):
    def __init__(self, atomic_contract_1, atomic_contract_2):
        super(AndContract, self).__init__()

        self.contract_1 = atomic_contract_1
        self.contract_2 = atomic_contract_2

        self.name = atomic_contract_1.name

        self.debug = False

    def to_string(self):
        return "AND(" + self.contract_1.to_string() + ", " + self.contract_2.to_string() + ")"

    def get_graph(self):
        contract_1 = self.contract_1.get_graph()
        contract_2 = self.contract_2.get_graph()
        return contract_1 + contract_2

    def get_complete(self):
        return self.contract_1.get_complete()

    def check_isolated(self, pc):

        result_1 = self.contract_1.check_isolated(pc)
        if result_1 == self.NO_ISOLATED:
            return result_1

        return self.contract_2.check_isolated(pc)

    def check(self, pc, verbosity = 0):
        result_1 = self.contract_1.check(pc, verbosity)

        if verbosity > 1 or self.debug:
            print("And Contract: First contract is " + result_1)

        if result_1 == self.NO_COMPLETE:
            return result_1

        result_2 = self.contract_2.check(pc, verbosity)

        if verbosity > 1 or self.debug:
            print("And Contract: Second contract is " + result_2)

        if result_1 == self.COMPLETE_FOUND and result_2 == self.COMPLETE_FOUND:
            return self.COMPLETE_FOUND

        return self.NO_COMPLETE

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

        return Contract.merge_pivots(self, pivots_1, pivots_2)

class OrContract(Contract):
    def __init__(self, atomic_contract_1, atomic_contract_2):
        super(OrContract, self).__init__()

        self.contract_1 = atomic_contract_1
        self.contract_2 = atomic_contract_2

        self.name = atomic_contract_1.name

    def to_string(self):
        return "OR(" + self.contract_1.to_string() + ", " + self.contract_2.to_string() + ")"

    def get_graph(self):
        contract_1 = self.contract_1.get_graph()
        contract_2 = self.contract_2.get_graph()
        return contract_1 + contract_2

    def get_complete(self):
        return self.contract_1.get_complete()

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

        #put these two together
        #report a FAILURE if they are inconsistent

        if pivots_1 == self.COMPLETE_FOUND or pivots_2 == self.COMPLETE_FOUND:
            return self.COMPLETE_FOUND

        for pivot_key in pivots_1.keys():
            if pivot_key in pivots_2.keys():
                pivots_2[pivot_key] += pivots_1[pivot_key]
            else:
                pivots_2[pivot_key] = pivots_1[pivot_key]

        return pivots_2
