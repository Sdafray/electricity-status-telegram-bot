from loader import tm


def setup():
    from . import electricity

    tm.create_tasks()
