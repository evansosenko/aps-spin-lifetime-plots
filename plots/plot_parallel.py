import matplotlib.pyplot
import os

from fit import Fit
from plot import Plot

class Plot(Plot):

    def add_ylabel(self):
        y = self.fit.meta['dependent']
        text = r'$R_{\text{NL}}^+$' + '$(\si{' + y['siunitx'] +  r'})$'
        super().add_ylabel(text)

def main():
    figure = Plot.new_figure(figsize=(5,10/3))

    fit = Fit(os.path.join('json', 'fig_4c_parallel.json'))
    fit.maps['value_transforms']['Ω_C'] = lambda x: '%.2E' % round(x, 2)
    fit.meta['contact_type'] = 'pinhole'

    plot = Plot(fit, figure.add_subplot(111))
    plot.id = 'c'
    plot.plot_data()
    plot.plot_fit()
    plot.add_xlabel()
    plot.add_ylabel()
    plot.add_parameter_overlay()
    figure.tight_layout()
    figure.savefig(os.path.join('build', 'plot_parallel.eps'), transparent=True)
    Plot.close_figure(figure)

    info = [ '$' + v['tex_symbol'] + ' = \SI{' + v['disply_value'] + '}{' + v['siunitx'] + '}$'
        for v in fit.meta['fixed_parameters']
        if v['symbol'] != 'L' ]

    open('build/plot_parallel_info.tex', 'w').write(
        r'\newcommand{\plotParallelInfo}{' + ', '.join(info) + '}')

if __name__ == '__main__':
    main()
