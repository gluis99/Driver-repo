import numpy as np
import pyvisa
from digitizer_base import Digitizer

class Oscilloscope(Digitizer):
    def __init__(self, visa_address: str = 'TCPIP0::k-dx3024g-60147.local::inst0::INSTR'):
        self.rm = pyvisa.ResourceManager()
        self.scope = None
        self.address = visa_address
        self.channel = 1
        self._last_t = None
        self._last_y = None

        self.connect(visa_address)

    def connect(self, address: str | None = None) -> None:
        if address:
            self.address = address
        self.scope = self.rm.open_resource(self.address)
        self.scope.timeout = 30000
        self.scope.read_termination = '\n'
        self.scope.write_termination = '\n'
        self.scope.visalib.set_buffer(self.scope.session, pyvisa.constants.VI_IO_OUT_BUF, 16*1024*1024)
        _ = self.scope.query('*IDN?')
        self.scope.write('*CLS')
        self.scope.write(':WAVeform:POINts:MODE MAXimum')
        self.scope.write(':WAVEFORM:FORMAT WORD')
        self.scope.write(':WAVEFORM:BYTEORDER LSBFirst')
        self.scope.write(':ACQuire:TYPE PEAK')



    def disconnect(self) -> None:
        try:
            if self.scope is not None:
                self.scope.close()
        except Exception:
            pass
        self.scope = None

    def set_trigger(self, ...):
        ...

    def acquire(self, channels=1, ...):
        ...

    def save_data(self, ...):
        ...
