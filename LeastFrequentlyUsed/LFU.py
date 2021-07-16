import collections
# print(dir(collections.OrderedDict))

class LFUCache(object):
    def __init__(self, capacity):
        self.keyToVal = dict()
        self.keyToFreq = dict()
        self.freqToKeys = dict()

        self.cap = capacity
        self.minFreq = 0

    def get(self, key):
        if key not in self.keyToVal.keys():
            return -1
        
        self.increaseFreq(key)

        return self.keyToVal.get(key)
    
    def put(self, key, val):
        if self.cap <= 0:
            return
        
        if key in self.keyToVal.keys():
            self.keyToVal[key] = val
            self.increaseFreq(key)
            return 
        
        if self.cap <= len(self.keyToVal):
            self.removeMinFreqKey()
        
        self.keyToVal[key] = val
        self.keyToFreq[key] = 1

        self.freqToKeys[1] = self.freqToKeys.get(1, [])
        self.freqToKeys[1].append(key)

        self.minFreq = 1
    

    def removeMinFreqKey(self):
        keyList = self.freqToKeys.get(self.minFreq)
        # for i in keyList:
        #     deleteKey = i
        #     break
        # deleteKey = keyList.iterator().next()
        deleteKey = keyList[0]
        keyList.remove(deleteKey)
        # deleteKey = keyList.pop()

        if len(keyList) == 0:
            self.freqToKeys.pop(self.minFreq)
        
        self.keyToVal.pop(deleteKey)
        self.keyToFreq.pop(deleteKey)
    
    def increaseFreq(self, key):
        freq = self.keyToFreq.get(key, 0)
        self.keyToFreq[key] = freq + 1

        self.freqToKeys.get(freq).remove(key)
        self.freqToKeys[freq + 1] = self.freqToKeys.get(freq + 1, [])
        self.freqToKeys[freq + 1].append(key)

        if len(self.freqToKeys[freq]) == 0:
            self.freqToKeys.pop(freq)
            if (freq == self.minFreq):
                self.minFreq += 1
        
        
