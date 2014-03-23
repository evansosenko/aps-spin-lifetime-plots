from scipy_data_fitting.figure import Fit

class Fit(Fit):

    def __init__(self, path=None):
        super().__init__(path=path)
        self.maps['siunitx'] = {
            'T': r'\tesla',
            'μm': r'\micro \meter',
            'Ω': r'\ohm',
            'mΩ': r'\milli \ohm',
            'mS': r'\milli \siemens',
            'Ω nm': r'\ohm \nano \meter',
            'nm':  r'\nano \meter',
            'kΩ': r'\kilo \ohm',
            'ps': r'\pico \second',
            'm^2 / s': r'\square \meter \per \second',
        }
        self.maps['tex_symbol'] = {
            'τ': r'\tau',
            'Ω_C': 'R_C',
        }
        self.maps['value_transforms'] = {
            '__default__': lambda x: round(x, 2),
        }
