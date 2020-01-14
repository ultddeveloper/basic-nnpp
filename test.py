import bnp as bn

bn.createnetwork(5, 3, 3)
bn.modifyLayer("addNeuron", [1])
bn.modifyLayer("overwrite", [2, 10, 1,2,3,4,5])
bn.modifyLayer("remove", [3])
print(bn.displayNetwork())
print(bn.getLayer(2))
bn.createConnectionAll()
print(bn.flow([10,20,30,40,50]))