import math
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
        
        self.lfo = lfo
        self.rfo = rfo
        self.old = old
        self.dl = dl
        self.dr = dr
        self.shd = shd
        self.osb = osb

    def __repr__(self):        
        return f"Hub({self.lfo}, {self.rfo}, {self.old}, {self.dl}, {self.dr}, {self.shd}, {self.osb})"


class Rim:
    """
    Represents a bicycle rim with the geometric parameters required
    for spoke length calculation.

    Parameters
    ----------
    erd : float | None
        Effective Rim Diameter (ERD). The diameter measured between
        the ends of two opposite spokes when fully seated in the rim.
    num_spokes : int | None
        Total number of spokes in the wheel.
    num_crosses : int | None
        Number of times each spoke crosses other spokes on the same side
        before reaching the rim (e.g., 2‑cross, 3‑cross).
    """
    
    def __init__(self, erd = None, num_spokes = None, num_crosses = None):
        self.erd = erd
        self.num_spokes = num_spokes
        self.num_crosses = num_crosses
    
    def __repr__(self):        
        return f"Rim({self.erd}, {self.num_spokes}, {self.num_crosses})"

class Wheel:
    """
    Represents a complete bicycle wheel composed of a hub and a rim.

    This class bundles the geometric properties of both components and
    provides methods for computing spoke lengths based on their combined
    geometry.

    Parameters
    ----------
    hub : Hub
        The hub object containing flange offsets, flange diameters,
        spoke hole diameter, and other hub-specific geometry.
    rim : Rim
        The rim object containing ERD, spoke count, and lacing pattern.
    """

    def __init__(self, hub, rim):
        self.hub = hub
        self.rim = rim
    def __repr__(self):
        return f"Wheel(hub={self.hub!r}, rim={self.rim!r})"

    def make_calc(self)-> tuple[float, float]:
        
        """
        Compute the left and right spoke lengths for the wheel.

        The calculation uses standard spoke length geometry based on the hub
        flange offsets, flange diameters, rim ERD, number of spokes, and
        number of crosses.

        Returns
        -------
        tuple[float, float]
            A tuple containing:
            - right_length : float
                The calculated spoke length for the drive side.
            - left_length : float
                The calculated spoke length for the non‑drive side.
        """

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