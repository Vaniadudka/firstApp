def add(*args, **kwargs):  # *args - специальній параметр который может обеспечить передачу множества аргументов функции
    result = 0
    for arg in args:
        if type(arg) == int or type(arg) == bool or type(arg) == float:
            result += arg
        else:
            try:
                result += float(arg)
                continue
            except (ValueError, TypeError):
                pass
    for arg in kwargs.values():
        if type(arg) == int or type(arg) == bool or type(arg) == float:
            result += arg
        else:
            try:
                result += float(arg)
                continue
            except (ValueError, TypeError):
                pass
    return result