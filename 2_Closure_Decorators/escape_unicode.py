# functional decorator


def escape_decorator(f):

    def wrap(*k):
        result = f(*k)
        return ascii(result)



def my_vegi():
    return "sdக"
