import time

class ProjectHelpers:

    def __init__(self):
        import time 
        
    def print_temporarily(self, message, duration=2):
        
        print(message, end='', flush=True)
        time.sleep(duration)
        print('\r' + ' ' * len(message) + '\r', end = '', flush=True)