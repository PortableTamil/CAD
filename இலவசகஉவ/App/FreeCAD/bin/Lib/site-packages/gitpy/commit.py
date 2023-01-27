from os import system

def commit(message):
    """ Description
        :type message:
        :param message:
    
        :raises:
    
        :rtype:
    """
    system(f"git commit -m '{message}'")
