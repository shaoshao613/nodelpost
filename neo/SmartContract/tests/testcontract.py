from boa.interop.Neo import Output
from boa.interop.Neo.Account import Account, GetScriptHash
from boa.interop.Neo.Block import GetTransactionCount
from boa.interop.Neo.Contract import GetScript
from boa.interop.Neo.Output import GetAssetId,GetScriptHash, GetValue
from boa.interop.Neo.Runtime import Log,GetTime
from boa.interop.Neo.Blockchain import GetHeight,GetAccount,GetBlock
from boa.interop.Neo.Transaction import GetOutputs, GetReferences, GetTXHash, GetType, GetAttributes, GetInputs, \
    GetUnspentCoins
from boa.interop.System.ExecutionEngine import GetScriptContainer, GetExecutingScriptHash, GetCallingScriptHash
from boa.builtins import range, concat
from boa.interop.Neo.Storage import GetContext, Get, Put
from boa.interop.Neo.Runtime import Notify

from neo.SmartContract import ApplicationEngine

def Main(operation, add_from,add_to, value):

    if operation == 'transfer':
        tx = GetScriptContainer();
        output = GetOutputs(tx);
        if not output:
            return "no output"
        else:
            for item in output:
                Notify(GetScriptHash(item))
                Notify(GetAssetId(item))
                value += GetValue(item)
        return value
    elif operation == 'receive':
        tx = GetExecutingScriptHash();
        return tx
    elif operation == 'output':
        tx = GetScriptContainer();
        output = GetOutputs(tx);
        out = 0
        if not output:
            return "no output"
        else:
            for item in output:
                Notify(GetScriptHash(item))
                Notify(GetAssetId(item))
                out += GetValue(item)
                Notify(out)
        return out
    elif operation == 'tx':
        tx = GetScriptContainer();
        if not tx:
            return "no tx"
        return tx
    elif operation == 'GetInputs':
        tx = GetScriptContainer();
        output = GetInputs(tx);
        if not output:
            return "no output"
        return len(output)
    elif operation == 'GetAttributes':
        tx = GetScriptContainer();
        output = GetAttributes(tx);
        if not output:
            return "no output"
        return len(output)
    elif operation == 'GetUnspentCoins':
        tx = GetScriptContainer();
        output = GetUnspentCoins(tx);
        if not output:
            return "no output"
        return len(output)
    elif operation == 'GetReferences':
        tx = GetScriptContainer();
        output = GetReferences(tx);
        if not output:
            return "no output"
        return len(output)
    elif operation == 'GetTXHash':
        tx = GetScriptContainer();
        if not tx:
            return "no tx"
        return GetTXHash(tx)
    elif operation == 'GetType':
        tx = GetScriptContainer();
        if not tx:
            return "no tx"
        return GetType(tx)




# def GetReceiver():
#     return ExecutionEngine.ExecutingScriptHash;