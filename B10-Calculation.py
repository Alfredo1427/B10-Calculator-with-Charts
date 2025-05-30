import numpy as np
import matplotlib.pyplot as plt
from reliability.Fitters import Fit_Weibull_2P
from reliability.Probability_plotting import PP_plot_semiparametric
from reliability.Distributions import Weibull_Distribution


data = [146, 104, 150, 150, 150, 150]

fit = Fit_Weibull_2P(
    failures=data,
    show_probability_plot=False,
    show_pdf_plot=False
)

fitted_dist = fit.distribution

B10_life = fitted_dist.inverse_SF(0.90)
print(f"\nB10 Life: {B10_life:.2f} hours")
print("\nFitted Weibull Parameters:")
print(f"  Alpha (Scale): {fitted_dist.alpha:.2f}")
print(f"  Beta (Shape):  {fitted_dist.beta:.2f}")

PP_plot_semiparametric(X_data_failures=data, Y_dist=fitted_dist)
plt.title("Weibull Probability Plot")
plt.grid(True)
plt.show()
