from scipy_data_fitting.figure import Plot

class Plot(Plot):
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
