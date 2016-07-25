import time, sys

class ProgressBar:

    def __init__(self, num_items, bar_length=50):
        self.num_items = num_items
        self.bar_length = bar_length # Modify this to change the length of the progress bar
        self.step_size = num_items/bar_length
        self.current_num = 0

    # update_progress() : Displays or updates a console progress bar
    ## Accepts the current item number (out of the total num_items)
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