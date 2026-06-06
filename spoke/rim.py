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
        
        if num_spokes is not None and num_spokes <= 0:
            raise ValueError("Number of spokes must be greater than zero")

        if erd is not None and erd <= 0:
            raise ValueError("erd must be greater than zero")

        if num_crosses is not None and num_crosses < 0:
            raise ValueError("Number of crosses cannot be negative")
        
        self.erd = erd
        self.num_spokes = num_spokes
        self.num_crosses = num_crosses
    
    def __repr__(self):        
        return f"Rim({self.erd}, {self.num_spokes}, {self.num_crosses})"
