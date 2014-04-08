import matplotlib.pyplot
import os

from fit import Fit
from plot import Plot

class Plot(Plot):

    def add_ylabel(self):
        y = self.fit.meta['dependent']
        text = r'$\Delta R_{\text{NL}}$' + '$(\si{' + y['siunitx'] +  r'})$'
        super().add_ylabel(text)

def main():
    figure = Plot.new_figure(figsize=(5,10))

    data_path = lambda x: os.path.join('json', 'fig_4' + x + '_difference.json')
    fits = [ Fit(data_path(fig)) for fig in ['a', 'b', 'd'] ]

    for fit in fits[0:2]:
        fit.maps['value_transforms']['Ω_C'] = lambda x: '%.2E' % round(x, 2)

    for i in (0, 1): fits[i].meta['contact_type'] = 'tunneling'
    fits[2].meta['contact_type'] = 'transparent'

    plots = []
    for idx, fit in enumerate(fits):
        n, m = 3, 1

        options = {}
        if idx != 0: options['sharex'] = plots[idx - 1].plt

        plot = Plot(fit, figure.add_subplot(n, m, (m * idx + 1), **options))

        plot.id = chr(97 + idx)
        if idx == 2: plot.id = 'd'

        plots.append(plot)

    for plot in plots:
        plot.plot_data()
        plot.plot_fit()
        plot.add_ylabel()
        plot.add_parameter_overlay()

    plots[-1].add_xlabel()
    matplotlib.pyplot.setp([ p.plt.get_xticklabels() for p in plots[0:2] ], visible=False)

    figure.savefig(os.path.join('build', 'plot_difference.eps'), transparent=True)
    plots[0].fit.save_info('build/plot_difference_info.tex', 'plotDifferenceInfo')
    Plot.close_figure(figure)

if __name__ == '__main__':
    main()
