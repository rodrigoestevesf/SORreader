import pyotdr
import matplotlib.pyplot as plt
from os import getcwd as path

class TraceOTDR():
    def __init__(self, filename: any):

        self.__points = []

        
        self.__filename = filename.strip('.sor') #entrada 'filename' com ou sem extensao .sor

        #leitura de arquivo .sor
        self.__status, self.__especificacoes, self.__trace = pyotdr.sorparse(path()+'/SORfiles/'+self.__filename+'.sor') 

        #armazena dados em uma lista de pontos em forma de dicionario 'x' e 'y'
        for data in self.__trace:
            dataX, dataY = data.strip().split('\t')
            dataX, dataY = float(dataX), float(dataY)
            self.__points.append({'x': dataX, 'y': dataY})

    #plota um grafico com os pontos do traco da leitura do OTDR
    def plotTrace(self) -> None:
        
        plt.plot([point['x'] for point in self.__points], [point['y'] for point in self.__points])
        plt.xlabel('Distance (km)')
        plt.ylabel('Power (dB)')
        plt.title(self.__filename+'.sor')
        plt.grid()
        plt.show()

    #retorna os pontos do traco em forma de lista de dicionarios
    def getPoints(self) -> list[dict['x':float, 'y':float]]:
        return self.__points
    
    #retorna uma lista com as distancias de cada ponto do traco
    def getDistances(self) -> list:
        return [point['x'] for point in self.__points]
    
    #retorna uma lista com as reflexoes de cada ponto do traco
    def getReflections(self) -> list:
        return [point['y'] for point in self.__points]
    
    #retorna o numero de pontos do traco
    def getNumberOfPoints(self) -> int:
        return len(self.__points)
    
    #retorna o nome do arquivo .sor
    def getFilename(self) -> str:
        return self.__filename+'.sor'
    
    def getSpecs(self) -> dict:
        return self.__especificacoes
    
    #salva os pontos do traco em um arquivo .csv
    #   newfilename -> novo nome do arquivo .csv caso queira mudar
    def saveAsCSV(self, newfilename:str = None) -> None:
        if newfilename==None: savepath = path()+'/savedFiles/'+self.__filename+'.csv'
        else: savepath = path()+'/savedFiles/'+newfilename.split('.')[0]+'.csv'
        
        with open(savepath, 'w') as file:
            file.write('distancia,reflexao\n')
            for point in self.__points:
                file.write(f"{point['x']},{point['y']}\n")
            file.close()
