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
    
    def __init__(self, ERD = None, num_spokes = None, num_crosses = None):
        self.ERD = ERD
        self.num_spokes = num_spokes
        self.num_crosses = num_crosses

    def __repr__(self):
        
        return f"Wheel({self.ERD}, {self.num_crosses}, {self.num_crosses})"