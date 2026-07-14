"""
AMONOS - NMC Protocol v98 Final
Atomic Infinity - Level 2026
NMC = Number → Measure → Combination
100% PROCEEDS TO GREEK CHARITIES
Author: Georgios Velonakis
Date: 14 July 2026
"""

class Amonos:
    """
    Atomic Measure and Number Organizational System (AMONOS)
    NMC Protocol v98 Final - Atomic Infinity Level 2026
    """
    
    def __init__(self, epipedo_max=2026):
        """
        Initialize Amonos with maximum level (epipedo_max).
        Default level is 2026 for atomic subdivision.
        """
        self.epipedo_max = epipedo_max
        self.total_atoms = 2 ** epipedo_max
        print(f"Amonos NMC v98: 2^{epipedo_max} atoms ready")
    
    def find_atom_for_number(self, x):
        """
        Find the atom interval [k/2^n, (k+1)/2^n] for number x in [0,1].
        
        Parameters:
        -----------
        x : float
            A number in the range [0, 1]
        
        Returns:
        --------
        dict : Contains atom information with keys:
            - 'interval': tuple of (lower_bound, upper_bound)
            - 'k': numerator of the lower bound
            - 'n': level of subdivision
            - 'atom_index': index of the atom at maximum level
        """
        if not (0 <= x <= 1):
            raise ValueError(f"Number x must be in [0, 1], got {x}")
        
        # Find the atom at the maximum level
        k = int(x * (2 ** self.epipedo_max))
        if k == 2 ** self.epipedo_max:
            k -= 1
        
        n = self.epipedo_max
        lower_bound = k / (2 ** n)
        upper_bound = (k + 1) / (2 ** n)
        
        return {
            'interval': (lower_bound, upper_bound),
            'k': k,
            'n': n,
            'atom_index': k,
            'x_input': x,
            'atom_string': f"[{k}/2^{n}, {k+1}/2^{n}]"
        }


if __name__ == "__main__":
    am = Amonos()
    result = am.find_atom_for_number(0.3333)
    print(f"\nAtom for x=0.3333: {result['atom_string']}")
    print(f"Interval: [{result['interval'][0]:.10f}, {result['interval'][1]:.10f}]")
    print(f"Atom index: {result['atom_index']}")
