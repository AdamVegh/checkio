__author__ = 'Vegh Adam'


from math import e, pi

def checkio():
    """
       The best number is 0! Why? It's very simple.
       The proof:
       Everybody knows that the best equation is e**(pi*1j)+1=0. An equation can be the best,
       if left side and right side of the equation is best. So the best number is 0. QED.
    """
    i_think_this_is_zero_and_the_best_number = int((0*(e**(pi*1j)+1)).real)
    return i_think_this_is_zero_and_the_best_number**(98765-4321**0)\
        if i_think_this_is_zero_and_the_best_number == 0*bool('the best number ever')\
        else 123456789/0*':P'
