from boa.builtins import range, concat
from boa.interop.Neo.Runtime import Notify


def Main(operation, key, value):

    if operation == 'transfer':

        # Put(context, key, value)
        #
        # item = Get(context, key)
        Notify("heelo","world",3);
        return True
    else:
        return True
