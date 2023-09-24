"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
#if the thing is already in there, value +1
def frequencies(items):
    frequencies = {}
    
    for item in items:
        if frequencies.get(str(item)):
            frequencies.update({str(item): (frequencies.get(str(item)) + 1)})
        else:
            frequencies[str(item)] = 1
    return frequencies
