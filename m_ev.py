class mae():
    def evneed(STAT,BAS,IV,EV,LVL):
        D = (2*BAS+IV+(EV/4))*(LVL/100)
        return ((((STAT/1.0-D)*400)/LVL)/4)*4