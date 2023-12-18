import pyvisa as visa


rm = visa.ResourceManager()
print(rm.list_resources())

sm = rm.open_resource('GPIB0::25::INSTR')
print(sm.query("*IDN?"))

sm.write("*RST")
sm.write(':SOUR:FUNC CURR')
sm.write(':SYST:RSEN OFF')
sm.write(':SENS:RES:MODE MAN')
sm.write(':SENS:FUNC "RES"')
sm.write(':SYST:GUAR CABL')
sm.write(':SENS:RES:OCOM OFF')

try:
    q = sm.query('*idn?')
    q=q.strip()
    print(q)
except:
    pass