def converterStringParaFloat(value):
    print('Valor convertido de str para float')
    return float(value)

def bitParaByte(valorASerConvertido):
    print('Valor convertido de bit para byte')
    bytesCalculado = valorASerConvertido / 8
    return bytesCalculado

def byteParaBit(valorASerConvertido):
    print('Valor convertido de byte para bit')
    bitsCalculado = valorASerConvertido * 8
    return bitsCalculado

#print('Insira o valor a ser convertido')
#entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
#valorConvertido = byteParaBit(entradaDoTecladoValorASerConvertido)
#print(valorConvertido)


def converterStringParaFloat(value):
    print('Valor convertido de str para float')
    return float(value)

def byteParakilobyte(valorASerConvertido):
    print('Valor convertido de byte para kilobyte')
    kilobyteCalculado = valorASerConvertido / 1024
    return kilobyteCalculado

def kilobyteParabyte(valorASerConvertido):
    print('Valor convertido de kilobyte para byte')
    byteCalculado = valorASerConvertido * 1024
    return byteCalculado

print('Insira o valor a ser convertido')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = kilobyteParabyte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)
