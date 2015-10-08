class Contract:
    def __init__(self):

        self.NOT_CHECKED = "Not checked"
        self.NO_ISOLATED = "Isolated did not match"
        self.ISOLATED = "Isolated did match"

        self.NO_CONNECTED = "Connected did not match"
        self.NO_COMPLETE = "Complete did not match"
        self.COMPLETE_FOUND = "The complete property was found"

        # detail the status of the property
        self.status = self.NOT_CHECKED