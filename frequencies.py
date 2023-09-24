"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        if frequencies.get(str(item)):
            frequencies.update({str(item): (frequencies.get(str(item)) + 1)})
        else:
            frequencies[str(item)] = 1
    return frequencies
