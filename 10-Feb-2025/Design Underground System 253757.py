# Problem: Design Underground System - https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.checkInMap = {}
        self.totalMap = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInMap[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation , time = self.checkInMap[id]

        if (startStation, stationName) not in self.totalMap:
            self.totalMap[(startStation, stationName)] = [0, 0]
        
        self.totalMap[(startStation, stationName)][0] += t - time
        self.totalMap[(startStation, stationName)][1] += 1
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.totalMap[(startStation, endStation)]
        return total / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)