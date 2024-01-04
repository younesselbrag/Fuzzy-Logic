# Fuzzy Inference System for Internship Report Evaluation

## Exercise Description

The objective of this exercise is to create a Mamdani type fuzzy inference system using the Python Fuzzy-Expert package. The system evaluates an internship report based on three input variables: Results obtained (out of 20), Methods used (out of 20), and Presentation (out of 20). The system returns the overall evaluation of the report (out of 20). Linguistic values for each variable are defined as 'Poor', 'Average', and 'Excellent'. The overall evaluation has five linguistic values: 'Mediocre', 'Bad', 'Average', 'Good', and 'Excellent'.

### Tasks:

1. **Define Linguistic Value Membership Functions:**
   - For each variable ('Result', 'Methods', 'Presentation', 'Evaluation'), define membership functions for linguistic values ('Poor', 'Average', 'Excellent').

2. **Transform Rule Base into Normal Form:**
   - Transform the rule base into normal form, if necessary.

3. **Create Fuzzy System in Python:**
   - Use the Fuzzy-Expert package to create a fuzzy inference system.
   - Implement six rules based on the provided conditions.
   
4. **Apply the System to Internship Report:**
   - Given an internship report with specific scores for results, methods, and presentation, apply the fuzzy system to obtain the corresponding overall rating.

5. **Assign Certainty Factors to Rules:**
   - Assign certainty factors to the rules of the base.
   
6. **Repeat Evaluation with Certainty Factors:**
   - Repeat the evaluation of the internship report, considering the assigned certainty factors.

## Solution Overview

The provided Python code implements the fuzzy inference system according to the exercise requirements. Here's an overview of the solution:

- **Class Structure:**
  - `FuzzySystem` class is defined to encapsulate the entire fuzzy system.

- **Initialization:**
  - Linguistic variables for 'Result', 'Methods', 'Presentation', and 'Evaluation' are defined with their respective linguistic values.
  - Membership functions for each linguistic value are defined using the `Membership.trimf` function.
  - Rule base is defined based on the provided conditions.

- **Fuzzy System Creation:**
  - The Fuzzy-Expert package is used to create the fuzzy inference system.
  - Input variables include 'Result', 'Methods', and 'Presentation', while the output variable is 'Evaluation'.
  - Rules are applied to create the fuzzy system.

- **Evaluation of Internship Report:**
  - The system is applied to an internship report with specific scores for results, methods, and presentation.
  - The overall rating is obtained.

- **Certainty Factors:**
  - Certainty factors are assigned to the rules of the base.

- **Repeat Evaluation with Certainty Factors:**
  - The system is reapplied to the same internship report, considering the assigned certainty factors.
  - The overall rating with certainty factors is obtained.

#### Requirements questions are clearly addressed:

1. Define linguistic value membership functions for each variable.

```python

self.define_membership(self.result_values, 'Poor', [0, 0, 10], 'Average', [5, 10, 15], 'Excellent', [10, 20, 20])
self.define_membership(self.methods_values, 'Poor', [0, 0, 10], 'Average', [5, 10, 15], 'Excellent', [10, 20, 20])
self.define_membership(self.presentation_values, 'Poor', [0, 0, 10], 'Average', [5, 10, 15], 'Excellent', [10, 20, 20])
self.define_membership(self.evaluation_values, 'Mediocre', [0, 0, 4], 'Bad', [2, 5, 8], 'Average', [6, 10, 14],
                       'Good', [12, 15, 18], 'Excellent', [16, 20, 20])
```

1. Create this system in Python using the Fuzzy-Expert package.

```python

from fuzzy_expert import Membership, LinguisticVariable, Rule, InferenceEngine

class FuzzySystem:
    ## check the source File fuzzy_logic.py
```

4. Apply the system to obtain the corresponding overall rating.

```python
# Internship report details
report_results = 12
report_methods = 6
report_presentation = 19

# Apply the system
output_evaluation = fuzzy_system_instance.evaluate_internship_report(report_results, report_methods, report_presentation)
print("Overall Rating:", output_evaluation)
```


5. Assign certainty factors to the rules of the base and repeat question 4.

```python

# Assign certainty factors to rules
certainty_factors = [0.8, 0.9, 0.7, 1.0, 0.6, 0.5]
fuzzy_system_instance.assign_certainty_factors(certainty_factors)

# Repeat evaluation with certainty factors
output_evaluation_with_certainty = fuzzy_system_instance.evaluate_internship_report(
    report_results, report_methods, report_presentation
)
print("Overall Rating with Certainty Factors:", output_evaluation_with_c
```
## How to Run the Code

1. Install the required package using
2. Run the provided Python script.



```bash
pip install -r requirements.txt
```

```bash
python fuzzy_system.py
