from os import system

def commitAdd(message:str, file="."):
    system(f"git add {file}") 
    """ Description
        :type message:str:
        :param message:str:
    
        :type file:
        :param file:
    
        :raises:
    
        :rtype:
    """
    system(f'git commit -m "{message}"')