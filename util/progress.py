import time, sys

class ProgressBar:

    def __init__(self, num_items, bar_length=50):
        self.num_items = num_items
        self.bar_length = bar_length # Modify this to change the length of the progress bar
        self.step_size = num_items/bar_length
        self.current_num = 0

    # update_progress() : Displays or updates a console progress bar
    ## Accepts a float between 0 and 1. Any int will be converted to a float.
    ## A value under 0 represents a 'halt'.
    ## A value at 1 or bigger represents 100%
    def update_progress(self, item_num):

        if item_num == self.num_items -1:
            print("\n")
            return

        if item_num < self.current_num + self.step_size:
            return

        self.current_num = item_num
        progress = item_num / self.num_items


        block = int(round(self.bar_length*progress))
        text = "\rPercent: [{0}] {1}%".format( "#"*block + "-"*(self.bar_length-block), progress*100)
        sys.stdout.write(text)
        sys.stdout.flush()