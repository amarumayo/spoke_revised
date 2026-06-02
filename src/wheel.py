import math

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