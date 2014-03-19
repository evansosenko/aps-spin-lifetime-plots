import json
import numpy

class Fit:
    """
    """

    def __init__(self, name=None):
        self.name = name
        """
        The identifier name for this object.
        """

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def path(self):
        """
        Path to the file containing fit to load.
        """
        return self._path

    @path.setter
    def path(self, value):
        self._path = value

    @property
    def data(self):
        """
        """
        if not hasattr(self, '_data'): self.load()
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def fit(self):
        """
        """
        if not hasattr(self, '_fit'): self.load()
        return self._fit

    @fit.setter
    def fit(self, value):
        self._fit = value

    @property
    def meta(self):
        """
        """
        if not hasattr(self, '_meta'): self.load()
        return self._meta

    @meta.setter
    def meta(self, value):
        self._meta = value

    def load(self):
        """
        """
        raw = json.load(open(self.path))
        self.data = numpy.array(raw['data']).T
        self.fit = numpy.array(raw['fit']).T
        self.meta = raw['meta']
