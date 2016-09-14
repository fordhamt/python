"""Paul Fordham | ptf06c """
#!/user/bin/env python
from __future__ import print_function # print()

import time # function exec time 
import sys  # redirect stdout to a file

def log(output = None):
    no_file = False
    f = None
    # callable checks if output is a function call
    if callable(output):
        # if no file provided output = function call
        # need to set our func arg as the function
        func = output
        no_file = True
    else:
        # try/catch incase bad file name
        try:
            f = open(output, "w")
            sys.stdout = f
        except:
            print("File does not exist!")
            # return output to stdout
            sys.stdout = sys.__stdout__     
    def func_info(func):
        def func_wrapper(*args, **kwargs):
            print("\nCalling function ", func.__name__, ".", sep='')
            if args:
                print("Arguments:")
                for arg in args:
                    print("  - ", arg, " of ", type(arg), ".", sep='')
            else:
                print("No arguments.")
            print("Output:")
            # call function to get output, return val, and exec time
            ts = time.time()
            return_val = func(*args, **kwargs)
            te = time.time()
            rtype = type(return_val)
            # %.5f sets exec time to 5 decimal places
            print("Execution time: %.5f s." % (te-ts))
            if return_val != None:
                print("Return Value: ", return_val, " of ", rtype, '.', sep='')
            else:
                print("No return value.")
            #return func(*args, **kwargs)
        return func_wrapper
    if no_file:
        return func_info(func) # no file provided
    else:
        return func_info # file provided
        f.close()
