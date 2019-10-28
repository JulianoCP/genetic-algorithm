from knn import *

#Função que le o arquivo.
def readDataFun(fileName): 
  
    data = [] 
    f = open(fileName, 'r') 
    lines = f.readlines()
    f.close() 
    for i in range(0, len(lines)): 
        line = lines[i];
        data.append(line) 

    return data 

#Função que cria o arquivo de saida para usar no knn.
def createOutput(caract):
    f = open('train.txt','w')

    for i in caract:
        f.write(str(i))
    f.close()

#Função que seleciona os pais de base para o ag.
def selectParents(data,comp):
    seed = 60
    identify = []
    numSelect = []
    f = open('parents.txt','w')
    p = open('resultParents.txt','w')

    for i in range(seed):
        numSelect.append(randint(0,130))

    p.write("Parents: ")
    p.write(str(numSelect))
    for i in range(len(data)):
        a = data[i]
        k = a.split()

        for j in range(seed):
            f.write(str(k[numSelect[j]]) + ' ')
        f.write(a[-2])
        f.write('\n')
    f.close()

    p.close()

    if comp == True:
        return 

    combinationParents(data,numSelect)

#Função que seleciona a característica que vai ser modificada
def mutation(train):

    select = randint(0,train)
    return select;

#Função que faz a combinação afim de melhorar a accuracy.
def combinationParents(data,numSelect):
    seed = 20
    result = 0.0
    numGeneration = 0
    currentAccuracy = 0.0
    changeParents = 0
    while True:
        parents = readDataFun('resultParents.txt')
        train = readDataFun('parents.txt')
        print()
        print("GERAÇÃO DE NUMERO : ",numGeneration)

        f = open('combination.txt','w')

        numMutation = mutation(len(train))

        for i in range(len(train)):
            a = train[i]
            k = a.split()
            x = data[i]
            y = x.split()

            listSelect = []
            f.write(str(a[:-2]))
            for j in range(seed):
                num = (numSelect[j]/5)+randint(1,50)

                if num > 133:
                    num = 133
                    num -= randint(1,50)
                    
                if j == numMutation:
                    num += 1

                listSelect.append(num)

                f.write(str(y[int(num)])+ ' ')

            if currentAccuracy < result:
                    currentAccuracy = result
                    p = open('result.txt','w')
                    p.write(str(parents[0]))
                    p.write("\nCombination: ")
                    p.write(str(listSelect))
                    p.write("\nAccuracy: ")
                    p.write(str(currentAccuracy))
                    p.close()
            
            f.write(a[-2])
            f.write('\n')

        f.close()

        if changeParents == 10:
            changeParents = 0
            selectParents(data,True)
        else:
            changeParents += 1

        result = main_knn(3,'combination.txt',300)
        numGeneration += 1

#Função main.
def main():

    data = readDataFun('treinamento.txt')
    selectParents(data,False)

if __name__ == '__main__': 
    main() 
