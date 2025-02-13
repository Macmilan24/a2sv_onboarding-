# Problem: Frequency Tracker - https://leetcode.com/problems/frequency-tracker/description/

class FrequencyTracker:

    def __init__(self):
        self.count_map = {}    
        self.frequency_map = {}  

    def add(self, number: int) -> None:
        old_frequency = self.count_map.get(number, 0)
        
        if old_frequency in self.frequency_map:
            self.frequency_map[old_frequency] -= 1
            if self.frequency_map[old_frequency] == 0:
                del self.frequency_map[old_frequency]

        new_frequency = old_frequency + 1
        self.count_map[number] = new_frequency

        self.frequency_map[new_frequency] = self.frequency_map.get(new_frequency, 0) + 1

    def deleteOne(self, number: int) -> None:
        if number not in self.count_map:
            return

        old_frequency = self.count_map[number]
        
        self.frequency_map[old_frequency] -= 1
        if self.frequency_map[old_frequency] == 0:
            del self.frequency_map[old_frequency]

        if old_frequency == 1:
            del self.count_map[number]
        else:
            new_frequency = old_frequency - 1
            self.count_map[number] = new_frequency
            self.frequency_map[new_frequency] = self.frequency_map.get(new_frequency, 0) + 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.frequency_map.get(frequency, 0) > 0
