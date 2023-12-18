import pyvisa as visa

class keith2400():
    def __init__(self, q, rm, con):
        self.con = con
        self.dev = rm.open_resource(self.con)
        self.script = q
        q.loggg('Initialized keith2400 at '+ str(self.con)+': '+ self.idn(), 'both' )
        #printN('=LIB=> Initialized: Keithley2400 at '+ str(self.dev.primary_address)+': '+ self.idn())
    
    def idn(self):
        try:
            q = self.query('*idn?')
            q=q.strip()
            return q
        except:
            return False
    def query(self,x):
        try:
            q = self.dev.query(x)
            return q
        except:
            return False
    def write(self,x):
        try:
            print(x)
            q = self.dev.write(x)
            return q
        except:
            return False

    def InitResMeas(self):
        self.dev.write("*RST")
        self.dev.write(':SOUR:FUNC CURR')
        self.dev.write(':SYST:RSEN OFF')
        self.dev.write(':SENS:RES:MODE MAN')
        self.dev.write(':SENS:FUNC "RES"')
        self.dev.write(':SYST:GUAR CABL')
        self.dev.write(':SENS:RES:OCOM OFF')

    def currentOn(self):
        self.dev.write(':OUTP ON')

    def currentOff(self):
        self.dev.write(':OUTP OFF')  
    def changeCurr(self, newCurrent):
	    self.dev.write(':SENS:CURR:PROT ' + str(newCurrent))
    def changeCurrRang(self, newCurrent):
        self.dev.write(':SENS:CURR:RANG '+ str(newCurrent))
    
    def changeCompVolt(self, newVoltage):
        self.dev.write(':SOUR:VOLT:RANG ' + str(newVoltage))

    def changeCurrMode(self, mode):
        if mode  == 0: #Changes to manual mode
            self.dev.write(':SENS:RES:MODE MAN')
        elif mode == 1: #Changes to  automatic mode
            self.dev.write(':SENS:RES:MODE AUTO')

    def readRes(self):
        return self.query(':READ?')
    
print('compiled without errors')
