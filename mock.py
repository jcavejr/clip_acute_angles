OVERRIDE = 0



#vertexlist = [[1, 1], [0, 3], [-1, 1], [-1, -1], [1, -1], [0.5, 0], [0, 0.75], [-0.5, 0], [0, 1]]
edgelists = [[0,1,2,3,4], [5,6,7,8]]
acutelist = [1,6]

class MockPolyNodeData:
    def __init__(self, EL):
        self.PCC = []
        for i in EL:
            self.PCC.append(len(i))

        self.polychains = EL
        self.vertexlist = [[1, 1], [0, 3], [-1, 1], [-1, -1], [1, -1], [0.5, 0], [0, 0.75], [-0.5, 0], [0, 1]]

if __name__ == "__main__" or OVERRIDE:
    PND = MockPolyNodeData(edgelists)
    print(edgelists)
    print(PND.PCC)
    print(PND.polychains)
