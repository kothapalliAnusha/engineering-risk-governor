def analyze_code_change(lines_added, functions_changed, complexity):
    return {
        "lines_changed": lines_added,
        "functions_changed": functions_changed,
        "complexity": complexity
    }
