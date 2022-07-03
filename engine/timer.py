""" timer 
decorator to record the time when it's calling a function.
record the time when it returns and compute the difference.
"""
import time 

def timer(method):
    def execute_times(*args, **kwargs):
        start = time.time()
        result = method(*args, **kwargs)
        end = time.time()

        total_time = end - start 
        if total_time < 0.001:
            print(f'{method.__name__} took {total_time*1000}ms')
        else:
            print(f'{method.__name__} took {total_time}s')
        
        return result
    return execute_times