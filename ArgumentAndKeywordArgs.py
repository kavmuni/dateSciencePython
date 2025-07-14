def argumentTest(*args, **kwargs):
    """

    :param args: tuple
    :param kwargs: Dictionary
    :return: void
    """
    print(args)
    print(type(args))
    print(kwargs)
    print(type(kwargs))

argumentTest("Muni","Test","Devi", age=36)