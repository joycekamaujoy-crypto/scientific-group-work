"""MODIFIED VERSION of Task I: raise the ambient/reference temperature."""
import numpy as np
from scipy.optimize import root_scalar
REFERENCE_TEMP = 28.0  # CHANGED PARAMETER: was 25°C
def heat_balance(T):
    return T - REFERENCE_TEMP - 10*np.exp(-T/20)
result = root_scalar(heat_balance, bracket=[20, 45], method="bisect", xtol=1e-10)
print("MODIFIED reference temperature:", REFERENCE_TEMP, "°C")
print(f"New equilibrium root: {result.root:.6f} °C")
print(f"Function at root: {heat_balance(result.root):.3e}")
