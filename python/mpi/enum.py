# copied from mpi4py-examples/09-task-pull.py

def enum(*sequential, **named):
    """
    Handy way to fake an enumerated type in Python
    """
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)

tags = enum('READY', 'DONE', 'EXIT', 'START')

tags.READY # == 0

tags.READY == tags.DONE # == False