"""
TASK I: Root Finding - Bisection and Fixed-Point Methods
Real-world case: finding the temperature where heat gain equals heat loss.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar

def heat_balance(T):
    """A zero indicates equilibrium in this simplified heat-balance model."""
    return T - 25 - 10 * np.exp(-T / 20)

# Bisection requires an interval whose endpoint function values have opposite signs.
solution = root_scalar(
    heat_balance, bracket=[20, 40], method="bisect", xtol=1e-10
)

# Rearrange heat_balance(T)=0 into T=g(T).
def g(T):
    return 25 + 10 * np.exp(-T / 20)

T = 30.0
history = [T]
for _ in range(100):
    new_T = g(T)
    history.append(new_T)
    if abs(new_T - T) < 1e-10:
        break
    T = new_T

print(f"Bisection equilibrium temperature: {solution.root:.6f} °C")
print(f"Fixed-point equilibrium temperature: {history[-1]:.6f} °C")
print("Fixed-point iterations:", len(history) - 1)

temperatures = np.linspace(20, 40, 300)
plt.plot(temperatures, heat_balance(temperatures), label="Heat-balance function")
plt.axhline(0, linewidth=0.8)
plt.axvline(solution.root, linestyle="--", label="Bisection root")
plt.xlabel("Temperature (°C)")
plt.ylabel("Heat-balance function")
plt.title("Equilibrium temperature")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
