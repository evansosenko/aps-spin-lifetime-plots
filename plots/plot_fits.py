import matplotlib.pyplot
import os

from fit import Fit
from plot import Plot

class Plot(Plot):

    def add_ylabel(self, diff):
        y = self.fit.meta['dependent']
        if diff:
            text = r'$\Delta R_{\text{NL}}$' + ' $(\si{' + y['siunitx'] +  r'})$'
        else:
            text = r'$R_{\text{NL}}^+$' + ' $(\si{' + y['siunitx'] +  r'})$'
        super().add_ylabel(text)

def main():
    figure = Plot.new_figure(figsize=(5,10))
    fit_ids = ['a', 'b', 'c', 'd']

    def data_path(fit_id):
        if fit_id == 'c':
            fit_type = 'parallel'
        else:
            fit_type = 'difference'
        return os.path.join('json', 'fig_4' + fit_id + '_' + fit_type + '.json')

    fits = [ Fit(data_path(fig)) for fig in fit_ids ]

    for fit in fits[0:3]:
        fit.maps['value_transforms']['Ω_C'] = lambda x: '%.2E' % round(x, 2)

    for i in (0, 1): fits[i].meta['contact_type'] = 'tunneling'
    fits[2].meta['contact_type'] = 'pinhole'
    fits[3].meta['contact_type'] = 'transparent'

    plots = []
    for idx, fit in enumerate(fits):
        n, m = 4, 1

        options = {}
        if idx != 0: options['sharex'] = plots[idx - 1].plt

        plot = Plot(fit, figure.add_subplot(n, m, (m * idx + 1), **options))
        plot.id = fit_ids[idx]
        plots.append(plot)

    for idx, plot in enumerate(plots):
        plot.plot_data()
        plot.plot_fit()

        if idx == 2:
            plot.add_ylabel(False)
        else:
            plot.add_ylabel(True)

        plot.add_parameter_overlay()

    plots[-1].add_xlabel()
    matplotlib.pyplot.setp([ p.plt.get_xticklabels() for p in plots[0:3] ], visible=False)

    figure.savefig(os.path.join('build', 'plot_fits.eps'), transparent=True)
    plots[0].fit.save_info('build/plot_fits_info.tex', 'plotFitsInfo')
    Plot.close_figure(figure)

if __name__ == '__main__':
    main()
