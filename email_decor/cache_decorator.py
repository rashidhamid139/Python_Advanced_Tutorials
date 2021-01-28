""" A decorator which cache function calls """

import time
from functools import wraps


def cached(timeout, logged=False):
    """Cache decorator"""
    def cache_decorator(func):
        if logged:
            print(f"""
            Cache for function: { func.__name__ }
            """)
        cache = {}

        @wraps(func)
        def decorated_function(*args, **kwargs):
            if logged:
                print("Function called ", func.__name__)

            key = (args, frozenset(kwargs.items()))
            result = None
            if key in cache:
                if logged:
                    print("Cache hit for ", func.__name__, key)

                cache_hit, expiry = cache[key]
                if (time.time() - expiry) < timeout:
                    result = cache_hit
                elif logged:
                    print("Cache expired for ", func.__name__, key)
            elif logged:
                print("Cache miss for ", func.__name__, key)

            if result is None:
                result = func(*args, **kwargs)
            cache[key] = (result, time.time())
            return result

        return decorated_function
    return cache_decorator


def dump_closure(f):
    print( dir(f))
    print( f.__closure__ is not None )
    if hasattr(f, "__closure__") and f.__closure__ is not None:
        print( "- Dumping function closure for %s:" % f.__name__ )
        for i, c in enumerate(f.__closure__):
            print("-- cell %d  = %s" % (i, c.cell_contents) )
    else:
        print(" - %s has no closure!" % f.__name__ )

def add( x, y ):
    print(x, y)
    z = 10
    return x + y
@cached( 10, True )
def fib(n):
    """Return the Nth fibonacci number"""
    print( n )
    if n==0 and n==1:
        return 1
    return fib( n -1 ) + fib( n-2 )


print( dump_closure( add ))
