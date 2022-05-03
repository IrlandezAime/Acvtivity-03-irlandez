class aime():
    def hpcal(BAS,IV,EV,LVL):
        return ((2*BAS+IV+(EV/4)*LVL)/100)+LVL+10
    
    def otherstat(BAS,IV,EV,LVL):
        return ((((2*BAS+IV+(EV/4))*LVL)/100)+5)*1.0