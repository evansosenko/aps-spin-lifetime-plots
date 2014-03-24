from scipy_data_fitting.figure import Plot

class Plot(Plot):
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    def add_parameter_overlay(self):
        rows = self.parameter_table(self.fit.meta['fixed_parameters'][0])

        text = []
        text.append('(' + self.id + ') ')
        text.append(' '.join(rows[0]))
        text.append(', ' + self.fit.meta['contact_type'] + ' contacts')
        self.plt.text(0.5, 1.1, ''.join(text),
            horizontalalignment='center',
            verticalalignment='top',
            transform=self.plt.axes.transAxes)

        rows = self.parameter_table(self.fit.meta['fitted_parameters'])
        self.add_text_table(rows[0:2], (0.05, 0.8), (0.07, -0.1),
            horizontalalignment='left',
            verticalalignment='top')

        self.add_text_table(rows[2:4], (0.6, 0.8), (0.07, -0.1),
            horizontalalignment='left',
            verticalalignment='top')
