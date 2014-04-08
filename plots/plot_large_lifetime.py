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

    data_path = lambda x: os.path.join('json', 'fig_4d_difference_' + x + '_lifetime.json')
    fits = [ Fit(data_path(fig)) for fig in ['large', 'larger'] ]

    for fit in fits:
        fit.maps['value_transforms']['τ'] = lambda x: '%.2E' % round(x, 2)
        fit.meta['contact_type'] = 'transparent'

    plots = []
    for idx, fit in enumerate(fits):
        n, m = 2, 1

        options = {}
        if idx != 0: options['sharex'] = plots[idx - 1].plt

        plot = Plot(fit, figure.add_subplot(n, m, (m * idx + 1), **options))
        plot.id = 'd.' + str(idx + 1)
        plots.append(plot)

    for plot in plots:
        plot.plot_data()
        plot.plot_fit()
        plot.add_ylabel()
        plot.add_parameter_overlay()

    plots[-1].add_xlabel()
    matplotlib.pyplot.setp(plots[0].plt.get_xticklabels(), visible=False)

    figure.savefig(os.path.join('build', 'plot_large_lifetime.eps'), transparent=True)
    Plot.close_figure(figure)

    info = [ '$' + v['tex_symbol'] + ' = \SI{' + v['disply_value'] + '}{' + v['siunitx'] + '}$'
        for v in plots[0].fit.meta['fixed_parameters']
        if v['symbol'] != 'L' ]

    open('build/plot_large_lifetime_info.tex', 'w').write(
        r'\newcommand{\plotLargeLifetimeInfo}{' + ', '.join(info) + '}')

if __name__ == '__main__':
    main()
