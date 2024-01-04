from fuzzy_expert import Membership, LinguisticVariable, Rule, InferenceEngine

class FuzzySystem:
    def __init__(self):
        """
        FuzzySystem class for evaluating internship reports using fuzzy logic.

        Attributes:
        - result_values: LinguisticVariable for the 'Result' input variable.
        - methods_values: LinguisticVariable for the 'Methods' input variable.
        - presentation_values: LinguisticVariable for the 'Presentation' input variable.
        - evaluation_values: LinguisticVariable for the 'Evaluation' output variable.
        - inference_engine: InferenceEngine for handling fuzzy inference.
        - fuzzy_system: Fuzzy system created using inference_engine.

        Methods:
        - define_membership_functions(): Define membership functions for linguistic variables.
        - define_membership(variable, label1, points1, label2, points2, label3, points3):
            Define a triangular membership function for a linguistic variable.
        - define_rule_base(): Define the rule base using linguistic variables.
        - assign_certainty_factors(certainty_factors): Assign certainty factors to rules.
        - evaluate_internship_report(report_results, report_methods, report_presentation):
            Evaluate an internship report using the fuzzy system.
        """
        self.result_values = LinguisticVariable('Result', ['Poor', 'Average', 'Excellent'])
        self.methods_values = LinguisticVariable('Methods', ['Poor', 'Average', 'Excellent'])
        self.presentation_values = LinguisticVariable('Presentation', ['Poor', 'Average', 'Excellent'])
        self.evaluation_values = LinguisticVariable('Evaluation', ['Mediocre', 'Bad', 'Average', 'Good', 'Excellent'])

        # Define membership functions
        self.define_membership_functions()

        # Define rule base
        self.define_rule_base()

        # Create fuzzy system
        self.inference_engine = InferenceEngine(self.rules)
        self.fuzzy_system = self.inference_engine.create_system(
            input_variables=[self.result_values, self.methods_values, self.presentation_values],
            output_variable=self.evaluation_values
        )

    def define_membership_functions(self):
        """
        Define a triangular membership function for a linguistic variable.

        Parameters:
        - variable: LinguisticVariable to which the membership function is added.
        - label1, label2, label3: Labels for membership functions.
        - points1, points2, points3: Parameters defining the triangular membership functions.
        """
    
        self.define_membership(self.result_values, 'Poor', [0, 0, 10], 'Average', [5, 10, 15], 'Excellent', [10, 20, 20])
        self.define_membership(self.methods_values, 'Poor', [0, 0, 10], 'Average', [5, 10, 15], 'Excellent', [10, 20, 20])
        self.define_membership(self.presentation_values, 'Poor', [0, 0, 10], 'Average', [5, 10, 15], 'Excellent', [10, 20, 20])
        self.define_membership(self.evaluation_values, 'Mediocre', [0, 0, 4], 'Bad', [2, 5, 8], 'Average', [6, 10, 14],
                               'Good', [12, 15, 18], 'Excellent', [16, 20, 20])

    def define_membership(self, variable, label1, points1, label2, points2, label3, points3):
        variable.add_value(label1, Membership.trimf, points1)
        variable.add_value(label2, Membership.trimf, points2)
        variable.add_value(label3, Membership.trimf, points3)

    def define_rule_base(self):
        """
        Assign certainty factors to rules.

        Parameters:
        - certainty_factors: List of certainty factors corresponding to each rule.
        """
        rule1 = Rule([self.result_values['Average'], self.methods_values['Poor']], self.evaluation_values['Bad'])
        rule2 = Rule([self.result_values['Average'], self.methods_values['Excellent']], self.evaluation_values['Good'])
        rule3 = Rule([self.result_values['Poor'], self.methods_values['Average']], self.evaluation_values['Bad'])
        rule4 = Rule([self.result_values['Excellent'], self.methods_values['Excellent'],
                      self.presentation_values['Excellent']], self.evaluation_values['Excellent'])
        rule5 = Rule([self.result_values['Poor'], self.methods_values['Average']], self.evaluation_values['Average'])
        rule6 = Rule([self.result_values['Average'], self.methods_values['Poor']], self.evaluation_values['Poor'])

        self.rules = [rule1, rule2, rule3, rule4, rule5, rule6]

    def assign_certainty_factors(self, certainty_factors):
        # Assign certainty factors to rules
        self.inference_engine.assign_certainty_factors(certainty_factors)

    def evaluate_internship_report(self, report_results, report_methods, report_presentation):
        """
        Evaluate an internship report using the fuzzy system.

        Parameters:
        - report_results: Numeric value representing the result of the internship report.
        - report_methods: Numeric value representing the methods used in the internship report.
        - report_presentation: Numeric value representing the presentation quality of the internship report.

        Returns:
        - Overall evaluation based on fuzzy logic.
        """
        return self.fuzzy_system.evaluate([report_results, report_methods, report_presentation])

if __name__ == "__main__":
    fuzzy_system_instance = FuzzySystem()

    report_results = 12
    report_methods = 6
    report_presentation = 19

    output_evaluation = fuzzy_system_instance.evaluate_internship_report(report_results, report_methods, report_presentation)
    print("Overall Rating:", output_evaluation)

    certainty_factors = [0.8, 0.9, 0.7, 1.0, 0.6, 0.5]
    fuzzy_system_instance.assign_certainty_factors(certainty_factors)

    output_evaluation_with_certainty = fuzzy_system_instance.evaluate_internship_report(
        report_results, report_methods, report_presentation
    )
    print("Overall Rating with Certainty Factors:", output_evaluation_with_certainty)
