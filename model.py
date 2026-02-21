def predict_disease(symptoms):
    symptoms = symptoms.lower()

    if "fever" in symptoms and "cough" in symptoms:
        return "Possible Viral Infection", "Medium – Consult Doctor"
    elif "chest pain" in symptoms or "breathing" in symptoms:
        return "Possible Heart / Lung Issue", "High – Emergency"
    elif "headache" in symptoms:
        return "Migraine / Stress", "Low – Home Care"
    else:
        return "Unknown Condition", "Consult Doctor"