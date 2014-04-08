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
            'Ω_F': 'R_F',
            'Ω_C': 'R_C',
        }
        self.maps['value_transforms'] = {
            '__default__': lambda x: round(x, 2),
        }


    def save_info(self, path, macro):
        info = [ '$' + v['tex_symbol'] + ' = \SI{' + v['disply_value'] + '}{' + v['siunitx'] + '}$'
            for v in self.meta['fixed_parameters']
            if v['symbol'] != 'L' ]

        v_1 = info.pop()
        v_2 = info.pop()

        v = self.meta['quantities'][5]
        text = '$' + v['tex_symbol'] + ' = \SI{' + v['disply_value'] + '}{' + v['siunitx'] + '}$'
        info.append('and ' + text + ' (' + v_1 + ' and ' + v_2 + ')')

        open(path, 'w').write(r'\newcommand{' + '\\' + macro + '}{' + ', '.join(info) + '}')
