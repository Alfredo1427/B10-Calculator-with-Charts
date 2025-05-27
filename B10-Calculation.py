

import numpy as np
from reliability.Distributions import Weibull_Distribution
from reliability.Fitters import Fit_Weibull_2P

data = [146,104,150,150,150,150]

fit = Fit_Weibull_2P(failures=data, show_probability_plot=False, show_pdf_plot=False)

fitted_dist = fit.distribution

B10_life = fitted_dist.inverse_SF(0.90)

print(f"B10 Life: {B10_life:.2f}")
