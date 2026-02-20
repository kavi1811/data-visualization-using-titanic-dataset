# Student Performance Analysis

Brief summary of the analysis notebook and the generated charts for the student performance dataset.

## Overview
This project contains a Jupyter notebook that loads a student performance dataset, computes summary statistics, and generates several visualizations saved to the `charts/` directory.

## Contents
- `student performance analysis.ipynb` — analysis notebook
- `charts/` — directory containing generated visualization images

## Charts present (as saved by the notebook)
- `charts/Histogram of Final Grades.png` — histogram of `G3` (final grade)
- `charts/Study Time vs Final Grade.png` — scatter plot of `studytime` vs `G3`
- `charts/Average Grade by Gender.png` — bar chart of average `G3` by `sex`

## Short analysis of the chart filenames
- Current filenames contain spaces and mixed capitalization, e.g., `Histogram of Final Grades.png`.
- Spaces and inconsistent naming can make scripting and cross-platform usage harder.

Recommended, consistent naming (suggested):
- `charts/histogram_final_grades.png`
- `charts/studytime_vs_final_grade.png`
- `charts/avg_grade_by_gender.png`

Renaming to lowercase, underscore-separated names improves portability and automation.

## How to regenerate the figures
1. Open `student performance analysis.ipynb` in Jupyter or VS Code: [student performance analysis.ipynb](student%20performance%20analysis.ipynb)
2. Run all cells. The notebook saves figures into `charts/` (see the code cells that call `plt.savefig(...)`).

## Notes
- The notebook currently reads data from a local path. Update the CSV path in the notebook before re-running if the dataset location differs.
- If you want, I can rename the files in `charts/` to the recommended names and update the notebook to save with the new names.

---
Generated summary for quick reference.
