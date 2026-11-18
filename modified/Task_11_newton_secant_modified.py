"""MODIFIED VERSION of Task J: change the initial investment amount."""
from scipy.optimize import root_scalar
cash_flows = [-12000, 3000, 3500, 4000, 2500]  # CHANGED: -10000 -> -12000
def npv(rate):
    return sum(cf/(1+rate)**t for t, cf in enumerate(cash_flows))
def d_npv(rate):
    return sum(-t*cf/(1+rate)**(t+1)
               for t, cf in enumerate(cash_flows) if t > 0)
newton = root_scalar(npv, fprime=d_npv, x0=0.08, method="newton", xtol=1e-12)
secant = root_scalar(npv, x0=0.02, x1=0.20, method="secant", xtol=1e-12)
print("MODIFIED initial investment: KSh 12,000")
print(f"New Newton IRR: {newton.root:.6%}")
print(f"New Secant IRR: {secant.root:.6%}")
print(f"NPV at root: {npv(newton.root):.8f}")
