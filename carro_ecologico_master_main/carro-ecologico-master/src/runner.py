from src.carro import Carro

if __name__ == '__main__':
    #Criando um carro
    carro = Carro()
    print(carro)

    #Embarcando duas pessoas
    carro.embarcar()
    carro.embarcar()
    print(carro)

    #Tentando embarcar mais uma pessoas
    if carro.embarcar():
        print("Nao foi possivel realizar o embarque")

    #Desembarcando
    carro.desembarcar()
    carro.desembarcar()
    if carro.desembarcar():
        print("Nao foi possivel desembarcar")

    #Abastecendo
    carro.abastecer(60)
    print(carro)

    #Dirigir
    if carro.dirigir(10):
        print("Nao foi possivel dirigir porque o carro estava vazio")

    # Embarcando e dirigindo
    carro.embarcar()
    carro.dirigir(10)
    print(carro)

    # Dirigindo ate acabar o combustivel
    quilometragemAntigo = carro.getQuilometragem()
    if carro.dirigir(70):
        distancia = carro.getQuilometragem() - quilometragemAntigo
        print("O combustivel acabou ao percorrer " + distancia + " kms")

    print(carro)

    #Abastecendo
    carro.abastecer(200)
    print(carro)