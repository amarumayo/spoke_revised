class Hub:
    """
    Represents a bicycle hub with all geometric parameters required
    for spoke length calculation.

    Parameters
    ----------
    lfo : float | None
        Left flange offset. Distance from the locknut to the center
        of the left flange.
    rfo : float | None
        Right flange offset. Distance from the locknut to the center
        of the right flange.
    old : float | None
        Over-locknut dimension (OLD). Measurement from locknut to 
        locknut.
    dl : float | None
        Spoke circle diameter on the non‑drive side.
    dr : float | None
        Spoke circle diameter on the drive side.
    shd : float | None
        Spoke hole diameter. Typically between 2.0 mm and 2.5 mm.
    osb : float | None
        Offset spoke bed. Distance from the center of the spoke hole
        to the center of the rim.
    """
    
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

        if lfo is not None and lfo < 0:
            raise ValueError("Left flange offset (lfo) cannot be negative")

        if rfo is not None and rfo < 0:
            raise ValueError("Right flange offset (rfo) cannot be negative")

        if old is not None and old < 0:
            raise ValueError("Over-locknut dimension (old) cannot be negative")

        if dl is not None and dl < 0:
            raise ValueError("Non-drive flange diameter (dl) cannot be negative")

        if dr is not None and dr < 0:
            raise ValueError("Drive-side flange diameter (dr) cannot be negative")

        if shd is not None and shd < 0:
            raise ValueError("Spoke hole diameter (shd) cannot be negative")

        if osb is not None and osb < 0:
            raise ValueError("Offset spoke bed (osb) cannot be negative")
        
        self.lfo = lfo
        self.rfo = rfo
        self.old = old
        self.dl = dl
        self.dr = dr
        self.shd = shd
        self.osb = osb

    def __repr__(self):        
        return f"Hub({self.lfo}, {self.rfo}, {self.old}, {self.dl}, {self.dr}, {self.shd}, {self.osb})"
