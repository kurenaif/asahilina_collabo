class LCG:
    multiplier = 0x5DEECE66D
    addend = 0xB
    mask = (1 << 48) - 1
    seed = 0

    def __init__(self, seed):
        self.seed = (seed ^ self.multiplier) & self.mask
    
    def set_seed(self, seed):
        self.seed = seed

    def next(self, bits):
        self.seed = (self.seed * self.multiplier + self.addend) & self.mask
        return self.seed >> (48-bits)