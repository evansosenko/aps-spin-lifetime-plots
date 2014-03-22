import matplotlib.pyplot
import os

from fit import Fit
from plot import Plot

class Plot(Plot):

    def add_xlabel(self):
        x = self.fit.meta['independent']
        self.subplot.set_xlabel(
            '$' + x['tex_symbol'] + r'$ $(\si{' + x['siunitx'] +  r'})$')

    def add_ylabel(self):
        y = self.fit.meta['dependent']
        print(y)
        self.subplot.set_ylabel(
            r'$\Delta R_{\text{NL}}$' + '$(\si{' + y['siunitx'] +  r'})$')

    def add_text_table(self, rows, r0, dr, **kwargs):
        for m, row in enumerate(rows):
            for n, column in enumerate(row):
                self.subplot.text(r0[0] + dr[0] * n, r0[1] + dr[1] * m, column,
                    transform=self.subplot.axes.transAxes, **kwargs)

    def add_parameter_overlay(self):
        rows = self.parameter_table(self.fit.meta['fixed_parameters'][0])
        self.subplot.text(0.5, 1.1, ' '.join(rows[0]),
            horizontalalignment='center',
            verticalalignment='top',
            transform=self.subplot.axes.transAxes)

        rows = self.parameter_table(self.fit.meta['fitted_parameters'])
        self.add_text_table(rows[0:2], (0.05, 0.8), (0.07, -0.1),
            horizontalalignment='left',
            verticalalignment='top')

        self.add_text_table(rows[2:4], (0.6, 0.8), (0.07, -0.1),
            horizontalalignment='left',
            verticalalignment='top')

    @staticmethod
    def parameter_table(parameters):
        if not isinstance(parameters, list): parameters = [parameters]
        rows = []
        for param in parameters:
            row = []
            row.append('$' + param['tex_symbol'] + '$')
            row.append('$=$')
            row.append(r'$\SI{' + param['disply_value'] + '}{' + param['siunitx'] + '}$')
            rows.append(row)
        return rows

def main():
    figure = matplotlib.pyplot.figure(figsize=(5,10))

    data_path = lambda x: os.path.join('data', 'PhysRevLett.105.167202',
        'fig_4' + x + '_difference.json')
    fits = [ Fit(data_path(fig)) for fig in ['a', 'b', 'd'] ]

    for fit in fits[0:2]:
        fit.maps['value_transforms']['Ω_C'] = lambda x: '%.2E' % round(x, 2)

    plots = []
    for idx, fit in enumerate(fits):
        n, m = 3, 1

        options = {}
        if idx != 0: options['sharex'] = plots[idx - 1].subplot

        plot = Plot(fit, figure.add_subplot(n, m, (m * idx + 1), **options))
        plots.append(plot)

    for plot in plots:
        plot.plot_data()
        plot.plot_fit()
        plot.add_ylabel()
        plot.add_parameter_overlay()

    plots[-1].add_xlabel()
    matplotlib.pyplot.setp([ p.subplot.get_xticklabels() for p in plots[0:2] ], visible=False)

    figure.savefig(os.path.join('build', 'plot_difference.eps'), transparent=True)
    matplotlib.pyplot.close(figure)

if __name__ == '__main__':
    main()
