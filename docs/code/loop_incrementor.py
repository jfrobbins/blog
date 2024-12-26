"""
# loop_incrementor.py

For some number of start/stop/step combinations, iterate through and generate a list of all of the unique combinations 

gist: https://gist.github.com/jfrobbins/bd6c84bd8b2cf2118e7b7e1a7d4a8dc8
"""

#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#  
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following disclaimer
#    in the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of the  nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#  
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#  A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#  OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#  LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#  

class StartStopStep:
        def __init__(self, ID= 0, start = 0, stop = 0, step = 0):              
            self.ID         = ID
            self.start      = start
            self.stop       = stop
            self.step       = step
                
        def __str__(self):
            return "ID = " + str(self.ID) + ", Values= " + str(range(self.start, self.stop + 1, self.step))
                
        def nIter(self):
            return (self.stop - self.start + self.step) / self.step

        def expand(self):
            #returns a list of type Reg containing all of the values in the SSS
            regs = []
            for v in range(self.start, self.stop + 1, self.step):
                    regs.append(Reg(self.ID, v))
                    
            return regs

class RegSet:
        def __init__(self):
            self.mode       = ""
            self.nRegs      = 0
            self.regs = []
            pass
                
class Reg:
        def __init__(self, ID, value, group = -1):
            self.ID     = ID
            self.value  = value
        
        def __str__(self):
            return "[r_" + str(self.ID) + "=" + str(self.value) + "]"
        
        def __len__(self):
            return 1



##########################################
def defaultSSSValues():
    #just create some default values to test with:
    values = []
    values.append(StartStopStep(0, 00, 255, 16))
    values.append(StartStopStep(1, 00, 255, 16))
    values.append(StartStopStep(10, 10,10,1))
    return values
##########################################

def getCurrentGroup(regs, counts):
    #returns list of mipiReg
    group = []
    nr = 0
    for r in regs:
        group.append(r[counts[nr]])   #append the current item
        nr += 1
        
    return group

def increment(counts, regs, nRegs, rCount):
    
    if rCount >= nRegs:
        print("rcount exceeded, done.")
        for rc in range(0, nRegs, 1):
            counts[rc] = -1
        return counts

    if counts[rCount] >= len(regs[rCount]):
        print("reg done, reset and increment next reg")
        for rc in range(rCount, 0-1, -1):
            counts[rc] = 0 #reset reg counters
        #increment the next register:
        counts = increment(counts, regs, nRegs, rCount + 1)
    else:
        #increment current register:
        counts[rCount] += 1
        if counts[rCount] >= len(regs[rCount]):
            #out of range, reset and increment next reg:
            counts[rCount] = 0
            counts = increment(counts, regs, nRegs, rCount + 1)
    
    return counts    
        
        
    
########################################

def build(nCombos, regs):
    #builds list of unique reg/value combinations
    
    tcount = 0  #total combo count
    nr = 0      #reg counter
    counts = [] #array to track count of each reg
    o = []      #output
    nRegs = len(regs)

    #init counts:
    for nr in range(0,nRegs,1):
        counts.append(0)    # [0,0,0]
        
    nr = 0 #reset
    while tcount < nCombos:
        print("####")
        print("# " + str(tcount+1) + " / " + str(nCombos))
        o.append(getCurrentGroup(regs, counts))
        counts = increment(counts, regs, nRegs, nr)
        tcount += 1
        if counts[0] < 0:
            print("breaking loop")
            break
        
    return o


#########################

def main():
    print("#########################")
    sssList = defaultSSSValues()
    regList = []
    nCombos = 1
    for sss in sssList:
        regList.append(sss.expand())
        nCombos *= sss.nIter()
    
    #build the list of unique combinations:
    results = build(nCombos, regList)
    
    print("######")
    count = 1
    for iSet in results: #loops through lists of mipireg[]
        print("count: ", count, "/", len(results))
        for reg in iSet:
            print(str(reg))
        print("######")
        count += 1
    print("#########################")    

#########################
main()
