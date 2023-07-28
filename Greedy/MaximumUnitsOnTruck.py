class Solution: 
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        maxUnits = 0
        for boxType in boxTypes:
            numOfUnits = min(truckSize, boxType[1])
            maxUnits = numOfUnits * boxType[0]
            truckSize -= numOfUnits
            if truckSize == 0:
                break

        return maxUnits


            