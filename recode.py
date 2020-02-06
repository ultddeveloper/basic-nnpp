import random
import math

cnetwork = []
 
def createweight():
    return random.randint(0,100)/100

def sigmoid(value):
    return 1/(1+math.pow(math.e, -value))

class Neuron():
    def __init__(self, data = 0):
        self.connectedto = []
        self.value = data
        self.tmprecieve = 0
    def senddata(self):
        for allin in self.connectedto:
            allin.recievedata(self.value)
    def compiledata(self):
        self.value = sigmoid(self.tmprecieve)
        self.tmprecieve = 0
    def recievedata(self, sendon):
        self.tmprecieve += sendon
    
    
class Layer():
    def __init__(self, preset = []):
        self.contains = preset
    def sendall(self):
        for targets in self.contains:
            targets.senddata()
    def returnneuron(self, loc):
        return self.contains[loc]


def createnetwork(inputLayer, hidenLayers, outputLayer):
    temp = []
    for i in range(inputLayer):
        temp.append(Neuron)
    cnetwork.append(Layer(temp))
    for i in range(hidenLayers):
        cnetwork.append(Layer())
    temp = []
    for i in range(outputLayer):
        temp.append(Neuron)
    cnetwork.append(Layer(temp))

def displayNetwork():
    fetchhidden = []
    for i in range(len(cnetwork) - 2):
        fetchhidden.append("Layer" + str(i + 1) + ": " + str(len(cnetwork[i + 1].contains)))
    return [
        "Network length: " + str(len(cnetwork)),
        "Inputs Requested:" + str(len(cnetwork[0].contains)),
        "hiddenlayers:", fetchhidden,
        "Outputs Given: "  + str(len(cnetwork[len(cnetwork)-1].contains))
    ]