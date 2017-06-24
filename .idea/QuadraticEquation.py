from math import sqrt

def QuadraticEquation(a, b, c):
    if (b*b<4*a*c):
        return ("\nThe solution belongs to the Complex Numbers field.");

    elif ((a!=0) and ((b*b)>(4*a*c))) :
        solution = "\nFirst Solution: " + str((-b+sqrt(b*b-4*a*c))/(2*a)) + \
                   "\nSecond Solution: "+ str((-b-sqrt(b*b-4*a*c))/(2*a));
        return solution

    else:
        return ("\nThis equation is not a second degree one.");


if __name__ == "__main__":
    print("Test 1: " + str(QuadraticEquation(2,2,2)) + "\n")
    print("Test 2: " + str(QuadraticEquation(1,-5,6)) + "\n")
    print("Test 3: " + str(QuadraticEquation(0,0,0)) + "\n")



    """
    Console results:

    Test 1:
    The solution belongs to the Complex Numbers field.

    Test 2:
    First Solution: 3.0
    Second Solution: 2.0

    Test 3:
    This equation is not a second degree one.


    Process finished with exit code 0

    """
