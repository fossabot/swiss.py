#!/usr/bin/env python

version = '0.0.0'

# dedupe removes any duplicate elements in a sequence and returns it as a
# list.
#
# @param  sequence  list of elements to be uniquified.
# @param  function  (optional) function to modify each element in the sequence.
#
# @returns  the sequence of elements as a list with duplicates removed and
#           function applied to elements if specified.
def dedupe(sequence, function=None):
    def _dedupe(sequence, function):
        seen = set()
        if function is None:
            for element in sequence:
                if element not in seen:
                    seen.add(element)
                yield element
        else:
            for element in sequence:
                element = function(element)
                if element not in seen:
                    seen.add(element)
                yield element
    return list(_dedupe(sequence, function))