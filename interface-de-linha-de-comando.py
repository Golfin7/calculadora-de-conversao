from calculadora import converterStringParaFloat, bitParaByte, byteParaBit, byteParakilobyte, kilobyteParabyte, kilobyteParamegabyte, megabyteParakilobyte, megabyteParagigabyte, gigabyteParamegabyte, gigabyteParaterabyte, terabyteParagigabyte, terabyteParapetabyte, petabyteParaterabyte

print(' -Escreva 1 para bitParaByte \n -Escreva 2 byteParaBit \n -Escreva 3 para byteParakilobyte \n -Escreva 4 para kilobyteParabyte \n -Escreva 5 para kilobyteParamega \n -Escreva 6 para megabyteParakilobyte \n -Escreva 7 para megabyteParagigabyte \n -Escreva 8 para gigabyteParamegabyte \n -Escreva 9 para terabyteParagigabyte \n -Escreva 10 para gigabyteParaterabyte \n -Escreva 11 para petabyteParaterabyte \n -Escreva 12 para terabyteParapetabyte')
funcEscolha = input()
if(funcEscolha == '1'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = bitParaByte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '2'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat (input())
    valorConvertido = byteParaBit(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '3'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat (input())
    valorConvertido = byteParakilobyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '4'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat (input())
    valorConvertido = kilobyteParabyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '5'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat (input())
    valorConvertido = kilobyteParamegabyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '6'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat (input())
    valorConvertido = megabyteParakilobyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '7'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat (input())
    valorConvertido = megabyteParagigabyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '8'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat (input())
    valorConvertido = gigabyteParamegabyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '9'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat (input())
    valorConvertido = gigabyteParaterabyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '10'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat (input())
    valorConvertido = terabyteParagigabyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '11'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat (input())
    valorConvertido = terabyteParapetabyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '12'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat (input())
    valorConvertido = petabyteParaterabyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

else:
    print('errou')