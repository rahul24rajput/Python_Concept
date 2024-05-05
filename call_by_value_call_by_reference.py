# Python’s argument-passing model is neither “Pass by Value” nor “Pass by Reference” but it is “Pass by Object Reference”.
# Depending on the type of object you pass in the function, the function behaves differently.
# Immutable objects show “pass by value” whereas mutable objects show “pass by reference”.


def call_by_balue(x):
    x = x*2
    return 



def call_by_reference(list):
    list.append("d")

    return 


lst = ['E']

call_by_balue(2)
call_by_reference(lst)

