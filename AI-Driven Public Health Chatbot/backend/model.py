import pandas as pd


class HealthChatbot:

    def __init__(self, file_path="data/diseases.csv"):

        self.df = pd.read_csv(file_path)

    def respond(self, user_input):

        user_input = user_input.lower()

        # Disease search
        for _, row in self.df.iterrows():

            disease = row["Disease"].lower()

            if disease in user_input:

                return f"""
Disease: {row['Disease']}

Category: {row['Category']}

Symptoms:
{row['Symptoms']}

Prevention:
{row['Prevention']}

Risk Level:
{row['Risk_Level']}
"""

        # Symptom search
        possible_diseases = []

        for _, row in self.df.iterrows():

            symptoms = row["Symptoms"].lower()

            words = symptoms.split(";")

            for symptom in words:

                symptom = symptom.strip()

                if symptom in user_input:

                    possible_diseases.append(
                        row["Disease"]
                    )

                    break

        if possible_diseases:

            return (
                "Possible related diseases:\n\n• "
                + "\n• ".join(possible_diseases)
                + "\n\nPlease consult a healthcare professional for diagnosis."
            )

        return """
I can help with:

• Disease Information
• Symptoms
• Prevention Tips
• Health Awareness

Try asking:
- What is dengue?
- Tell me about diabetes.
- I have fever and headache.
"""