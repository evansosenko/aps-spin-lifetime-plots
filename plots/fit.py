import json
import numpy

class Fit:
    """
    Loads a fit from a json file into a `Fit` object.
    """

    def __init__(self, path=None):
        self.path = path
        """
        Path to the file containing fit to load.
        """

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value

    @property
    def data(self):
        """
        Data as a [`numpy.ndarray`][1] in the form

            #!python
            [
                [ x1, x2, x3, ... ],
                [ y1, y2, y3, ...]
            ]

        [1]: http://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.html
        """
        if not hasattr(self, '_data'): self._load()
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def fit(self):
        """
        Fit points as a [`numpy.ndarray`][1] in the form

            #!python
            [
                [ x1, x2, x3, ... ],
                [ y1, y2, y3, ...]
            ]

        [1]: http://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.html
        """
        if not hasattr(self, '_fit'): self._load()
        return self._fit

    @fit.setter
    def fit(self, value):
        self._fit = value

    @property
    def meta(self):
        """
        A dictionary of metadata related to the fit.
        """
        if not hasattr(self, '_meta'): self._load()
        return self._meta

    @meta.setter
    def meta(self, value):
        self._meta = value

    @property
    def maps(self):
        """
        A dictionary of A dictionaries.
        Each dictionary defines a map which is used to extend the metadata.
        """
        if not hasattr(self, '_maps'):
            maps = {}
            maps['siunitx'] = {
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
            maps['tex_symbol'] = {
                'τ': r'\tau',
                'Ω_C': 'R_C',
            }
            maps['value_transforms'] = {
                '__default__': lambda x: round(x, 2),
            }
            self._maps = maps
        return self._maps

    @maps.setter
    def maps(self, value):
        self._maps = value

    def _load(self):
        raw = json.load(open(self.path))
        self.data = numpy.array(raw['data']).T
        self.fit = numpy.array(raw['fit']).T
        self.meta = raw['meta']
        for key in self.meta: self._extend_meta(self.meta[key])

    def _extend_meta(self, meta):
        if isinstance(meta, str): return None
        if isinstance(meta, dict): meta = [meta]
        for param in meta:
            if 'name' in param: key = param['name']
            if 'symbol' in param: key = param['symbol']

            if 'units' in param:
                param['siunitx'] = self._get_siunitx(param['units'])
            else:
                param['siunitx'] = ''

            param['tex_symbol'] = self._get_tex_symbol(key)

            if 'value' in param:
                param['disply_value'] = str(self._value_transform(key)(param['value']))

    def _get_siunitx(self, key):
        table = self.maps['siunitx']
        if key in table: return table[key]
        return ''

    def _get_tex_symbol(self, key):
        table = self.maps['tex_symbol']
        if key in table: return table[key]
        return key

    def _value_transform(self, key):
        if key in self.maps['value_transforms']:
            return self.maps['value_transforms'][key]
        else:
            return self.maps['value_transforms']['__default__']
