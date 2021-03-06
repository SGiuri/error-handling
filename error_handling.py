def handle_error_by_throwing_exception():
    raise ValueError("Something wrong")
    pass


def handle_error_by_returning_none(input_data):
    try:
        a = int(input_data)
        return a
    except:
        return None
    pass


def handle_error_by_returning_tuple(input_data):
    try:
        a = int(input_data)
        return True, a
    except:
        return False, None
    pass


def filelike_objects_are_closed_on_exception(filelike_object):
    filelike_object.open()
    try:
        filelike_object.do_something()
    except:
        filelike_object.close()
        handle_error_by_throwing_exception()
    filelike_object.close()
    pass
