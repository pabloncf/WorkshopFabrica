

class MediaAritimetica:
    def __init__(self, numOne,numTwo):
        self.numOne = numOne
        self.numTwo = numTwo

        result = (self.numOne + self.numTwo) / 2

        print(result)


numOne = int(input("Insira o primeiro numero: "))
numTwo = int(input("Insira o segundo numero: "))

MediaAritimetica(numOne, numTwo)
