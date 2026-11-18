# 💻 BIT 2118 Scientific Computing – Sections A–J

## 📌 Project Overview

This project contains my Python implementations for the ten tasks covered in Sections A to J of the BIT 2118 Scientific Computing assignment.

I have organised the work into two main folders. The `code` folder contains the original programs, while the `modified` folder contains versions where I changed some input values to observe how the results would be affected.

I have also included notes to explain the concepts, calculations and operations used in each task.

## 📁 Project Structure

```text
BIT2118_Scientific_Computing_A-J/
├── code/          # Original programs for Sections A–J
├── modified/      # Programs with changed input values
├── NOTES.md       # Explanations and notes for each topic
├── requirements.txt
└── README.md
```

## ⚙️ Setting Up the Project in VS Code

To run the programs, I use Visual Studio Code and Python. The following steps explain how to set up the project.

1. Install Python 3 and the Python extension in VS Code.
2. Open the project folder in VS Code.
3. Open the terminal by selecting **Terminal → New Terminal**.
4. Create a virtual environment:

   **For Windows:**

   ```powershell
   py -m venv .venv
   ```

5. Activate the virtual environment.

   **For PowerShell:**

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   If PowerShell does not allow script execution, I can use Command Prompt instead:

   ```cmd
   .venv\Scripts\activate.bat
   ```

6. Install the required Python libraries:

   ```powershell
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

7. Run an original program from the main project folder. For example:

   ```powershell
   python code/Task_02_numpy_arrays.py
   ```

8. To run the modified version, use:

   ```powershell
   python modified/Task_02_numpy_arrays_modified.py
   ```

The same procedure can be followed when running the other tasks. Some programs use Matplotlib and will display graphs when executed. 📊

## 📚 Task Files

The table below shows how I have organised the original and modified programs according to the assignment sections.

| Section | Original program | Modified program |
|---|---|---|
| A | `code/Task_02_numpy_arrays.py` | `modified/Task_02_numpy_arrays_modified.py` |
| B | `code/Task_03_vectorization.py` | `modified/Task_03_vectorization_modified.py` |
| C | `code/Task_04_numerical_errors.py` | `modified/Task_04_numerical_errors_modified.py` |
| D | `code/Task_05_matrix_algebra.py` | `modified/Task_05_matrix_algebra_modified.py` |
| E | `code/Task_06_linear_systems.py` | `modified/Task_06_linear_systems_modified.py` |
| F | `code/Task_07_gaussian_lu.py` | `modified/Task_07_gaussian_lu_modified.py` |
| G | `code/Task_08_iterative_linear.py` | `modified/Task_08_iterative_linear_modified.py` |
| H | `code/Task_09_eigenvalues.py` | `modified/Task_09_eigenvalues_modified.py` |
| I | `code/Task_10_bisection_fixed_point.py` | `modified/Task_10_bisection_fixed_point_modified.py` |
| J | `code/Task_11_newton_secant.py` | `modified/Task_11_newton_secant_modified.py` |

## 🧮 What I Have Considered in Each Task

For each section, I have included or considered the following points when explaining the program:

- **Inputs:** The values used in the program, including their units and dimensions where applicable.
- **Mathematical operations:** The formulas, calculations or algorithms used to solve the problem.
- **Outputs:** The results produced after running the program.
- **Interpretation:** What the results mean and how they relate to the problem being solved.
- **Input changes:** The values I changed in the modified programs and how those changes affected the results.
- **Real-world application:** Other situations where the same method or program could be useful.

## ☁️ Uploading My Work to GitHub

I have created a GitHub repository where I will upload the project so that the files can be accessed through a repository link.

**🔗 My GitHub repository:**

[BIT2118-Scientific-Computing](https://github.com/blxze-neiten/BIT2118-Scientific-Computing)

To upload my work, I can open the VS Code terminal in the main project folder and run the following commands:

```powershell
git init
git add .
git commit -m "Add BIT 2118 Scientific Computing tasks A-J"
git branch -M main
git remote add origin https://github.com/blxze-neiten/BIT2118-Scientific-Computing.git
git push -u origin main
```

If the GitHub remote has already been added, I can update it using:

```powershell
git remote set-url origin https://github.com/blxze-neiten/BIT2118-Scientific-Computing.git
```

Before uploading, I will make sure that the files do not contain passwords, access tokens or other private information. 🔐

## 🎯 Conclusion

Through this project, I have worked on different areas of Scientific Computing using Python and its libraries. I have also changed some input values in the programs to observe how they affect the results.

The project has helped me understand how concepts such as NumPy arrays, vectorization, numerical errors, matrix operations, linear equations, eigenvalues and root-finding methods can be implemented in Python and applied to practical problems.

---

⭐ **BIT 2118 – Scientific Computing | Sections A–J**