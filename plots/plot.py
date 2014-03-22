class Plot():
    """
    """

    def __init__(self, fit=None, subplot=None):
        self.fit = fit
        """
        The fit object for this plot.
        """

        self.subplot = subplot
        """
        The subplot object.
        """

    @property
    def fit(self):
        return self._fit

    @fit.setter
    def fit(self, value):
        self._fit = value

    @property
    def subplot(self):
        return self._subplot

    @subplot.setter
    def subplot(self, value):
        self._subplot = value

    @property
    def settings(self):
        if not hasattr(self, '_settings'):
            self._settings = {
                'data': {'marker': '.', 'linestyle': 'None', 'markersize': 3},
                'fit': {},
            }
        return self._settings

    @settings.setter
    def settings(self, value):
        self._settings = value

    def plot_data(self):
        self.subplot.plot(*self.fit.data, **self.settings['data'])

    def plot_fit(self):
        self.subplot.plot(*self.fit.fit, **self.settings['fit'])
