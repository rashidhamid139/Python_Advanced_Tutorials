import time


def logged( time_format ):
    def decorator( func ):
        def decorated_func( *args, **kwargs ):
            print( f"""
                - Running { func.__name__} on { time.strftime( time_format ) }
            """)
            start_time = time.time()
            result = func( *args, **kwargs )
            end_time = time.time()

            print( f"""
                - Finished {func.__name__}, Execution time : { end_time -start_time }
            """)

            return result
        decorated_func.__name__ = func.__name__
        return decorated_func
    return decorator


@logged( "%b %d %Y - %H:%M:%S" )
def add1( x, y ):
    time.sleep(6)
    return x+y


print( add1( 3, 5))