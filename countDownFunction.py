
def countDown(n):
    """
    This function is an example to show a function can call itself
    :param n: n - Integer
    :return: Void/Null
    """
    if n == 0:
        print("Rocket Launch initiated................")
    else:
        print(n)
        countDown(n-1)


countDown(10)