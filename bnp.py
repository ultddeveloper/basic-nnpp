#Copyright Andrewk 2020, all rights reserved

import random
import math

cnetwork = [] #first hidden layer is 1

null = None

def createweight():
    return random.randint(0,100)/100

def sigmoid(value):
    return 1/(1+math.pow(math.e, -value))

class Neuron():
    def __init__(self, layer, value = 0):
        self.value = value
        self.connectedwith = []
        self.tempsave = 0
        self.layer = layer

    def createConnection(self, targetPosInLayer):
        self.connectedwith.append([cnetwork[self.layer + 1].getneuron(targetPosInLayer), createweight()])

    def recievedata(self, insert):
        self.tempsave += insert

    def compiledata(self):
        sigmoid(self.tempsave)

    def passdata(self):
        self.value = self.tempsave
        for target in self.connectedwith:
            target[0].recievedata(self.value * target[1])



class Layer():
    def __init__(self, inList, inStrucure = None): #inits Layer, creates contains with input instructure
        if inStrucure == None:
            self.contains = []
        else:
            self.contains = inStrucure
        
        self.pos  = inList

    def createNeuron(self, value = 0):
        self.contains.append(Neuron(self.pos, value))

    def getneuron(self, loc):
        try:
            return self.contains[loc]
        except IndexError:
            return None

    def senddata(self):
        for target in self.contains:
            target.passdata()

    def prepdata(self):
        for target in self.contains:
            target.compiledata()

    def connectall(self):
        for containedneuron in self.contains:
            for m in range(len(cnetwork[self.pos].contains) + 1):
                try:
                    containedneuron.createConnection(m)
                except IndexError:
                    pass

def createnetwork(inputNumber = 1, hiddenLayers = 0, outputNumber = 1): # creates input, hiddenlayers, output
    cnetwork.append(Layer(0))
    for i in range(inputNumber):
        cnetwork[0].createNeuron()
    for i in range(hiddenLayers):
        cnetwork.append(Layer(0))
    cnetwork.append(Layer(0))
    for i in range(outputNumber):
        cnetwork[len(cnetwork) - 1].createNeuron()

def createlayer(place = len(cnetwork) - 1, structure = None):
    """ Stucture needs to be like following
        [neuron, neuron, neuron] ...... """
    cnetwork.insert(Layer(structure), place)

def modifyLayer(option, arguments):
    if option == "addNeuron": #arguments = [layer, position, value]  
        try:
            cnetwork[arguments[0]].createNeuron(arguments[1])
        except IndexError:
            cnetwork[arguments[0]].createNeuron()
    elif option == "overwrite": #arguments = [layer, amount, data.......]
        cnetwork[arguments[0]].contains = []
        for i in range(arguments[1]):
            try:
                cnetwork[arguments[0]].contains.append(Neuron(arguments[0], arguments[i+2]))
            except IndexError:
                cnetwork[arguments[0]].contains.append(Neuron(0))
    elif option =="remove": #[layer]
        cnetwork.remove(cnetwork[arguments[0]])



#Human Understandable Statistics below

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

def getNetworkLen():
    return len(cnetwork)

def getLayer(whichLayer):
    grabdata = [len(cnetwork[whichLayer].contains)]
    for tstorage in cnetwork[whichLayer].contains:
        grabdata.append(tstorage.value)
    return grabdata

def createConnectionAll():
    for allLayers in cnetwork:
        allLayers.connectall()

def flow(indata):
    for i in range(len(indata)):
        cnetwork[0].contains[i].recievedata(indata[i])
    for targetlayer in cnetwork:
        targetlayer.prepdata()
        targetlayer.senddata()
    tempreturn = []
    for getvalue in cnetwork[len(cnetwork) - 1].contains:
        tempreturn.append(getvalue.value)
    return tempreturn