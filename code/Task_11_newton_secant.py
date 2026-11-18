"""
TASK J: Root Finding - Newton-Raphson and Secant Methods
Real-world case: calculating the internal rate of return of an investment.
"""
from scipy.optimize import root_scalar

# Initial investment followed by annual cash inflows.
cash_flows = [-10000, 3000, 3500, 4000, 2500]

def npv(rate):
    """Net present value at a proposed annual discount rate."""
    return sum(cf / (1 + rate) ** period
               for period, cf in enumerate(cash_flows))

def d_npv(rate):
    """Derivative of NPV with respect to the discount rate."""
    return sum(-period * cf / (1 + rate) ** (period + 1)
               for period, cf in enumerate(cash_flows) if period > 0)

# Newton uses an explicit derivative and one initial estimate.
newton = root_scalar(
    npv, fprime=d_npv, x0=0.10, method="newton", xtol=1e-12
)

# Secant estimates the derivative using two initial estimates.
secant = root_scalar(
    npv, x0=0.05, x1=0.20, method="secant", xtol=1e-12
)

print(f"IRR using Newton-Raphson: {newton.root:.6%}")
print(f"IRR using Secant method: {secant.root:.6%}")
print(f"NPV at Newton solution: {npv(newton.root):.8f}")
print("Newton converged:", newton.converged)
print("Secant converged:", secant.converged)
