# BIT 2118 Scientific Computing — Study Notes for Sections A–J

These notes explain the concepts used by the assignment programs. The examples follow the supplied PDF; explanations add learning context to help you defend your implementation.

---

## A. NumPy Arrays and Numerical Computation

### Core idea
An array is an organised collection of values. A vector is one-dimensional; a matrix is two-dimensional. NumPy stores numerical data in arrays and performs operations over all elements efficiently.

### Mathematical operation
For Celsius temperature `C`, Fahrenheit is:

`F = 1.8C + 32`

For readings `C₁, C₂, ..., Cₙ`, the mean is:

`mean = (C₁ + C₂ + ... + Cₙ) / n`

The minimum and maximum identify the lowest and highest recorded readings.

### Important syntax
- `import numpy as np`: imports NumPy using the conventional alias `np`.
- `np.array([...])`: creates an array.
- `np.mean(a)`, `np.min(a)`, `np.max(a)`: calculate summary statistics.
- `1.8 * a + 32`: applies the conversion to every array element.
- `a[:6]`: slicing; selects the first six values.
- `:.2f`: formats a number to two decimal places.

### Execution flow
1. Store the 24 hourly readings in an array.
2. Calculate mean, minimum and maximum.
3. Convert the full array to Fahrenheit.
4. Print the statistics and a sample of converted values.

### Why NumPy?
A normal Python list does not support the same direct element-wise arithmetic. NumPy makes numerical operations concise and efficient.

### Modified-input experiment
Increase every temperature by 2°C. The mean, minimum and maximum should each rise by 2°C. Each Fahrenheit reading should rise by 3.6°F because a 2°C difference corresponds to `1.8 × 2 = 3.6°F`.

### How to explain it
"The array holds all hourly sensor readings. NumPy calculates the daily summary and applies the Celsius-to-Fahrenheit formula to every reading without a manual loop."

---

## B. Mathematical Functions and Vectorization

### Core idea
Vectorization means applying an operation to an entire array rather than processing each element in a Python loop.

### Mathematical operation
For latency `L` in milliseconds:
- Convert to seconds: `s = L / 1000`
- Square the converted value: `q = s²`

### Important syntax
- `np.random.default_rng(42)`: creates a random generator. The seed makes the sample reproducible.
- `rng.uniform(5, 250, 1_000_000)`: generates one million values from the specified range.
- `def function():`: defines a reusable function.
- `for value in array`: visits values one at a time.
- `timeit.timeit(function, number=3)`: measures repeated execution.
- `array / 1000`: vectorized division.
- `array ** 2`: element-wise squaring.
- `result[:5]`: displays a small sample.

### Execution flow
1. Generate simulated latency measurements.
2. Define a loop-based implementation.
3. Define a vectorized implementation.
4. Measure both implementations.
5. Display sample values and timing comparison.

### Why vectorization?
NumPy performs array operations in optimised compiled code. This often reduces Python-level loop overhead. Actual speed-up depends on hardware, array size and operation.

### Modified-input experiment
Reduce the number of observations from 1,000,000 to 200,000. The program processes fewer values, so execution should generally take less time. The measured speed-up ratio may vary.

### How to explain it
"Both versions calculate the same mathematical result. The loop handles values individually, while the NumPy expression handles the array as a whole. Timeit allows us to compare their execution times."

---

## C. Floating-Point Arithmetic and Numerical Errors

### Core idea
Computers store many real numbers using finite binary precision. Consequently, some decimal values cannot be represented exactly.

### Error formulas
Absolute error:

`absolute error = |true value − approximate value|`

Relative error:

`relative error = absolute error / |true value|`

Percentage relative error is relative error multiplied by 100%.

### Important syntax
- `0.1 + 0.2`: demonstrates floating-point arithmetic.
- `==`: exact equality comparison.
- `np.isclose(a, b)`: checks whether values are sufficiently close within a tolerance.
- `np.sqrt(2)`: computes the square root of 2.
- `abs(a - b)`: absolute difference.
- `1e-8`: scientific notation for 0.00000001.

### Cancellation and a stable expression
The expressions

`(sqrt(1+x) - 1) / x`

and

`1 / (sqrt(1+x) + 1)`

are algebraically equivalent for suitable nonzero `x`, after rationalising the numerator. When `x` is very small, subtracting two nearly equal numbers in the first expression can lose significant digits. The second form is generally more numerically stable.

### Execution flow
1. Calculate `0.1 + 0.2`.
2. Compare exact equality with 0.3.
3. Use `np.isclose` for a tolerance-based comparison.
4. Calculate absolute and relative approximation errors for √2.
5. Compare direct and stable expressions for small values of x.

### Modified-input experiment
Use `1.414213` instead of `1.414` as the approximation to √2. The absolute and relative errors should decrease because the approximation is closer to the true value.

### How to explain it
"Floating-point values are approximations. Exact equality can therefore be unreliable for some decimal calculations. A tolerance-based comparison is more appropriate for numerical work."

---

## D. Matrix Algebra and Matrix Operations

### Core idea
A matrix is a rectangular arrangement of numbers in rows and columns. Matrices can represent coordinate transformations, systems of equations and many scientific models.

### Mathematical operations
Matrix multiplication:

`cᵢⱼ = Σₖ aᵢₖ bₖⱼ`

A 2-D rotation matrix is:

`R = [[cos θ, -sin θ], [sin θ, cos θ]]`

A scaling matrix is:

`S = [[sx, 0], [0, sy]]`

The determinant of a square matrix gives information about invertibility. A nonzero determinant indicates that the matrix is invertible.

### Important syntax
- `np.deg2rad(45)`: converts degrees to radians.
- `np.cos(angle)`, `np.sin(angle)`: trigonometric functions.
- `@`: matrix multiplication.
- `.T`: transpose.
- `np.linalg.det(A)`: determinant.

### Execution flow
1. Store the square's four coordinate points.
2. Convert the rotation angle to radians.
3. construct rotation and scaling matrices.
4. Combine the transformations.
5. Multiply the points by the transposed transformation matrix.
6. Display the transformed coordinates and determinant.

### Why transpose?
The points are stored as rows, while the conventional transformation matrix acts on column vectors. Multiplying row-wise points by the transpose gives the equivalent transformation.

### Modified-input experiment
Change the rotation angle from 45° to 90°. The object should rotate further while preserving the scaling factors. The transformed coordinates will change.

### How to explain it
"The points describe an object in 2-D space. Matrix multiplication applies rotation and scaling consistently to every point."

---

## E. Solution of Systems of Linear Equations

### Core idea
A collection of simultaneous linear equations can be represented compactly as `Ax = b`.

- `A`: coefficient matrix.
- `x`: vector of unknowns.
- `b`: vector of known results.

### Example model
`4x + 2y = 20`

`8x + 12y = 72`

Therefore:

`A = [[4, 2], [8, 12]]`

`x = [x, y]`

`b = [20, 72]`

The solution is `x = 3`, `y = 4`.

### Important syntax
- `np.linalg.solve(A, b)`: solves the linear system.
- `A @ solution`: reconstructs the known-value vector.
- `b - A @ solution`: residual vector.
- `np.linalg.norm(residual)`: measures the residual magnitude.

### Execution flow
1. Enter the coefficient matrix.
2. Enter the known-value vector.
3. Solve for the unknowns.
4. Substitute the solution back into the equations.
5. Calculate the residual to assess numerical accuracy.

### Why use solve instead of inverse?
A direct linear-system solver is generally more efficient and numerically appropriate than explicitly calculating `A⁻¹` and multiplying it by `b`.

### Modified-input experiment
Increase total CPU usage from 20 to 24 while retaining the other values. The solution changes to reflect the new resource totals. The verification multiplication should reproduce the new `b`.

### How to explain it
"The coefficient matrix describes resource consumption, while the right-hand-side vector describes observed totals. The solver estimates the unknown quantities that satisfy both equations."

---

## F. Gaussian Elimination and LU Decomposition

### Core idea
Gaussian elimination transforms a linear system into upper-triangular form through row operations, then solves it using back-substitution.

LU decomposition factors a matrix into:
- `L`: lower-triangular factor.
- `U`: upper-triangular factor.

With pivoting, the factorisation may be represented as `PA = LU`.

### Why factor once?
If the same matrix `A` is used with several different measurement vectors `b`, its LU factors can be reused. This avoids repeating the full factorisation.

### Important syntax
- `from scipy.linalg import lu_factor, lu_solve`
- `lu_factor(A)`: computes reusable LU factorisation data and pivot information.
- `lu_solve((lu, piv), b)`: solves using those factors.
- `enumerate(collection, start=1)`: loops with a numbered counter.

### Execution flow
1. Define the coefficient matrix.
2. Define multiple right-hand-side measurement vectors.
3. Factor the coefficient matrix once.
4. Solve each system using the same factors.
5. Calculate residual norms.
6. Compare one result with `np.linalg.solve`.

### Modified-input experiment
Change the first entry of one measurement vector from 15 to 18. The solution should change, but the coefficient matrix and its LU factorisation remain the same.

### How to explain it
"LU decomposition is useful when many systems share the same coefficient matrix. We factor the matrix once and reuse the factors for each new set of measurements."

---

## G. Iterative Methods for Linear Systems

### Core idea
Iterative methods begin with an initial guess and repeatedly improve it. This is useful for some large sparse systems.

### Jacobi method
Split `A` into its diagonal part `D` and remaining part `R`:

`x(new) = (b − R x(old)) / D`

All new values are calculated using the previous iteration's values.

### Gauss-Seidel method
The method updates unknowns sequentially and immediately uses newly calculated values during the same iteration. It often converges faster than Jacobi for suitable systems.

### Important syntax
- `np.diag(A)`: extracts the diagonal.
- `np.diagflat(D)`: constructs a diagonal matrix.
- `np.zeros_like(b)`: creates a zero array with matching shape.
- `x.copy()`: makes a separate copy.
- `np.linalg.norm(..., ord=np.inf)`: maximum absolute component norm.
- `tol`: convergence tolerance.
- `max_iter`: maximum number of iterations.
- `plt.semilogy`: plots values with a logarithmic vertical axis.

### Execution flow
1. Define the coefficient matrix and right-hand-side vector.
2. Start with zero estimates.
3. Calculate improved estimates.
4. Measure the maximum change.
5. Stop when the change falls below tolerance or the iteration limit is reached.
6. Compare both methods with the direct solution.
7. Plot convergence history.

### Graph interpretation
A decreasing error curve indicates that successive estimates are getting closer together. A curve that levels off may indicate slow convergence or a numerical limit.

### Modified-input experiment
Change the right-boundary influence from 20 to 40. The calculated steady-state temperatures should change, reflecting the warmer boundary.

### How to explain it
"Jacobi and Gauss-Seidel approach the solution through repeated updates. The error tolerance controls when the program considers the estimates sufficiently stable."

---

## H. Eigenvalues and Eigenvectors

### Core idea
An eigenvector is a non-zero vector whose direction remains unchanged under a matrix transformation. The eigenvalue describes the scaling factor.

### Mathematical relationship
`Av = λv`

Where:
- `A` is a square matrix.
- `v` is an eigenvector.
- `λ` is its corresponding eigenvalue.

### Network application
An adjacency matrix represents connections between network nodes. The dominant eigenvector can provide an eigenvector-based measure of node importance.

### Important syntax
- `np.linalg.eig(A)`: returns eigenvalues and eigenvectors.
- `np.argmax(...)`: returns the index of the largest value.
- `eigenvectors[:, index]`: selects a complete eigenvector column.
- `np.abs(...)`: obtains absolute component magnitudes.
- `zip(nodes, scores)`: pairs each node with its score.

### Execution flow
1. Build an adjacency matrix.
2. Calculate all eigenvalues and eigenvectors.
3. Find the dominant eigenvalue.
4. Extract its eigenvector.
5. Normalize the absolute components so the scores sum to one.
6. Verify the eigenvector equation.

### Modified-input experiment
Add a connection between nodes A and D. The network structure changes, so the eigenvalue calculation and node-importance scores may change.

### How to explain it
"The adjacency matrix represents network connections. The dominant eigenvector provides scores that reflect how a node is connected to other important nodes."

---

## I. Root Finding: Bisection and Fixed-Point Methods

### Core idea
A root is an input value that makes a function equal to zero:

`f(r) = 0`

### Bisection method
Bisection starts with an interval `[a, b]` where the endpoint function values have opposite signs. It repeatedly halves the interval while retaining the half that contains the sign change.

The sign-change condition is:

`f(a) × f(b) < 0`

For a continuous function, this brackets at least one root.

### Fixed-point iteration
Rewrite an equation into the form:

`x = g(x)`

Then repeatedly calculate:

`x(n+1) = g(x(n))`

Convergence depends on the chosen rearrangement and starting value. A common local sufficient condition is that `|g'(x)| < 1` near the fixed point.

### Important syntax
- `root_scalar`: SciPy's scalar root-finding interface.
- `bracket=[20, 40]`: interval containing a sign change.
- `method="bisect"`: selects bisection.
- `xtol`: stopping tolerance for the root estimate.
- `np.exp`: exponential function.
- `np.linspace`: creates evenly spaced values for plotting.
- `plt.axhline(0)`: draws the zero reference line.

### Execution flow
1. Define the heat-balance function.
2. Choose an interval that brackets a root.
3. Solve using bisection.
4. Rearrange the equation into fixed-point form.
5. Start from an initial temperature.
6. Repeatedly update until successive estimates differ by less than the tolerance.
7. Plot the function and root location.

### Graph interpretation
The root is where the plotted function crosses the horizontal zero line.

### Modified-input experiment
Increase the reference temperature from 25°C to 28°C. The heat-balance function changes, so its equilibrium root changes.

### How to explain it
"Bisection narrows an interval containing a root, while fixed-point iteration repeatedly substitutes an estimate into a rearranged equation."

---

## J. Root Finding: Newton-Raphson and Secant Methods

### Core idea
Both methods estimate a root of a nonlinear equation, but they use different information to update the estimate.

### Newton-Raphson formula
`x(n+1) = x(n) − f(x(n)) / f'(x(n))`

It requires the derivative and one starting estimate.

### Secant method
The secant method estimates the derivative using two recent points:

`x(n+1) = x(n) − f(x(n))(x(n) − x(n−1)) / (f(x(n)) − f(x(n−1)))`

It does not require an explicitly supplied derivative, but it needs two starting estimates.

### Financial application: internal rate of return
The net present value is:

`NPV(r) = Σ [CF(t) / (1+r)^t]`

The internal rate of return is the rate `r` for which:

`NPV(r) = 0`

### Important syntax
- `root_scalar`: root-finding interface.
- `fprime=d_npv`: supplies the derivative to Newton's method.
- `x0`: initial estimate.
- `x1`: second initial estimate for the secant method.
- `method="newton"`: selects Newton-Raphson.
- `method="secant"`: selects the secant method.
- `.root`: estimated root.
- `.converged`: indicates whether the solver reports convergence.

### Execution flow
1. Store the investment and future cash flows.
2. Define the NPV function.
3. Define its derivative.
4. Run Newton-Raphson using the derivative.
5. Run the secant method using two starting estimates.
6. Compare the estimated rates.
7. Substitute the Newton estimate into NPV to check that it is close to zero.

### Modified-input experiment
Increase the initial investment from 10,000 to 12,000 while keeping the future cash inflows unchanged. The rate that makes NPV zero will change. This demonstrates how investment assumptions affect the estimated IRR.

### How to explain it
"Newton-Raphson uses the derivative to improve a single starting estimate. The secant method estimates the slope from two points. Both search for the discount rate that makes net present value zero."

---

# Cross-topic Python and scientific-computing revision

## 1. Imports
`import numpy as np` makes NumPy available under the short name `np`.

`import matplotlib.pyplot as plt` imports Matplotlib's plotting interface.

`from scipy.optimize import root_scalar` imports one selected function directly.

## 2. Variables and data types
- Integer: `count = 10`
- Float: `temperature = 25.5`
- String: `name = "Sensor A"`
- List: `values = [1, 2, 3]`
- NumPy array: `values = np.array([1, 2, 3])`

## 3. Functions
A function groups reusable instructions:

```python
def square(number):
    return number ** 2
```

`return` sends a calculated value back to the caller. `print` displays information but does not replace a returned result.

## 4. Loops
A `for` loop repeats instructions for each item or over a range. Iterative numerical algorithms use loops to update estimates.

## 5. Conditions
An `if` statement tests a condition. Root solvers and iterative methods use conditions to determine whether a stopping criterion has been reached.

## 6. Numerical tolerance
A tolerance is an acceptable numerical threshold. For example, if the change between iterations is smaller than `1e-8`, the algorithm may stop.

A tolerance is not the same as an exact answer. Numerical methods generally produce approximations.

## 7. Residuals and verification
For a linear system, residual:

`r = b − Ax`

A small residual norm indicates that the computed solution approximately satisfies the original equations.

For a root, evaluate `f(root)`. A value close to zero indicates that the estimate is a good approximate root.

## 8. Graph interpretation
Always identify:
- Horizontal axis: independent variable.
- Vertical axis: calculated quantity.
- Units on both axes.
- What the line or points represent.
- What trend, crossing, convergence or difference is visible.

## 9. General debugging checklist
1. Check that the correct Python interpreter is selected in VS Code.
2. Confirm NumPy, SciPy and Matplotlib are installed.
3. Check file names and working directory.
4. Check array dimensions before matrix multiplication.
5. Check units and input ranges.
6. Check root brackets for a sign change.
7. Check iterative methods for convergence.
8. Read the full error message and identify the line number.

## 10. A useful oral explanation pattern
For each task, explain it in this order:

1. **Problem:** What real-world issue are you modelling?
2. **Input:** What values enter the program, and what do they represent?
3. **Mathematics:** Which formula or algorithm is used?
4. **Code:** Which Python functions implement the mathematics?
5. **Output:** What numerical result or graph is produced?
6. **Interpretation:** What does the result mean?
7. **Experiment:** Which input did you change, and why did the result change?
8. **Limitation:** What assumptions or numerical limitations should be considered?

