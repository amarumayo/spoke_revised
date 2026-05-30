import math
class Hub:
    
    def __init__(
        self, 
        lfo=None, 
        rfo=None, 
        old=None, 
        dl=None, 
        dr=None, 
        shd=None, 
        osb=None
    ):
        # lfo = left flange offset. Distance from the lock nut 
        #     to the centre of the left flange.
        # rfo = right flange offset. Distance from the lock nut 
        #     to the centre of the right flange.
        # old = measurement from lock nut to lock nut
        # dl = spoke circle diameter non-drive side
        # dr = spoke circle diameter drive side
        # shd = spoke hole diameter. The diameter of the spoke hole in the flange. 
        #     Normally in that range of 2mm to 2.5mm.
        # osb = The distance from the centre of the spoke hole to the centre of the rim. 

        self.lfo = lfo
        self.rfo = rfo
        self.old = old
        self.dl = dl
        self.dr = dr
        self.shd = shd
        self.osb = osb

    def __repr__(self):        
        return f"Hub({self.lfo}, {self.rfo}, {self.old}, {self.dl}, {self.dr}, {self.shd})"


class Rim:
    
    def __init__(self, erd = None, num_spokes = None, num_crosses = None):
        self.erd = erd
        self.num_spokes = num_spokes
        self.num_crosses = num_crosses
    
    def __repr__(self):        
        return f"Rim({self.erd}, {self.num_spokes}, {self.num_crosses})"

class Wheel:
    def __init__(self, hub, rim):
        self.hub = hub
        self.rim = rim
    def __repr__(self):
        return f"Wheel(hub={self.hub!r}, rim={self.rim!r})"

    def make_calc(self):
        print("hi")

        R = self.rim.erd / 2
        LH = self.hub.dl / 2
        LF = self.hub.lfo
        RH = self.hub.dr / 2
        RF = self.hub.rfo
        h = self.rim.num_spokes

        ML = 2 * R * LH * math.cos((4 * math.pi * self.rim.num_crosses) / h )
        left_length = round((math.sqrt(R**2 + LH**2 + LF**2 - ML)) - self.hub.shd / 2, 1)
        
        MR = 2 * R * RH * math.cos((4 * math.pi * self.rim.num_crosses) / h )
        right_length = round((math.sqrt(R**2 + RH**2 + RF**2 - MR)) - self.hub.shd / 2, 1)

        return right_length, left_length