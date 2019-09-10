import numpy as np

def run_helper(options):
    my_data = np.array([[1, 2],[2, 1]])
    my_result = my_data * 2
    print("module-b, run_helper completed with options: " + options)
    return my_result
