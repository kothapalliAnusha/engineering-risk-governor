def explain_risk(features, risk_score):
    explanation = (
        f"The code change modifies {features['lines_changed']} lines "
        f"and {features['functions_changed']} functions, "
        f"with an estimated complexity of {features['complexity']}. "
        f"This results in a predicted risk score of {risk_score:.2f}, "
        "indicating potential stability concerns."
    )
    return explanation
