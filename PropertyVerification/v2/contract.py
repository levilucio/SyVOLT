class Contract(object):
    def __init__(self):

        self.NOT_CHECKED = "Not checked"
        self.NO_ISOLATED = "Isolated did not match"
        self.ISOLATED = "Isolated did match"

        self.NO_CONNECTED = "Connected did not match"
        self.NO_COMPLETE = "Complete did not match"
        self.COMPLETE_FOUND = "Complete did match"

        # detail the status of the property
        self.status = self.NOT_CHECKED

        self.debug = False

    def to_string(self):
        pass

    def merge_pivots(self, pivots_1, pivots_2):

        pivot_debug = False

        if pivots_1 is None or pivots_2 is None:
            if pivot_debug:
                print("No pivots in either if or then contract.")
            return self.COMPLETE_FOUND
        # print("If pivots")
        # print(pivots_1)
        #
        # print("Then pivots, matches")
        # print(pivots_2)

        all_if_pivots_succeed = True
        for pivot, if_guids in pivots_1.items():
            # the pivot is only defined on the if graph
            if pivot not in pivots_2:
                continue

            then_guids = pivots_2[pivot]
            if "FAILURE" in then_guids:
                if pivot_debug:
                    print("Pivot failure on " + str(pivot))
                return self.NO_COMPLETE

            if_guid_succeed = False

            for if_guid in if_guids:
                # these two matches are on different nodes in the source graph
                # so the pivots don't match
                # FAILURE is returned from an AND contract if the guids were different
                if if_guid in then_guids:
                    if_guid_succeed = True

            all_if_pivots_succeed = all_if_pivots_succeed and if_guid_succeed

        if all_if_pivots_succeed:
            return self.COMPLETE_FOUND
        else:
            return self.NO_COMPLETE

