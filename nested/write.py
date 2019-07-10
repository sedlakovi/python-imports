from . import module


def update_neighbor():
    module.VARIABLE += 1
    print('My neighbor lives now at', module.VARIABLE)
