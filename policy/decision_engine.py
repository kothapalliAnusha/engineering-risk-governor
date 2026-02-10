def policy_decision(risk_score):
    if risk_score < 0.3:
        return "APPROVE"
    elif risk_score < 0.7:
        return "REVIEW"
    else:
        return "BLOCK"
