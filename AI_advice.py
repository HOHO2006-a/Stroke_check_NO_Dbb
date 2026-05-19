import os
import sys
import logging
import json
from groq import Groq

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
logging.getLogger("absl").setLevel(logging.CRITICAL)

API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    # Fallback pour le développement local
    API_KEY = "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" 

client = Groq(api_key=API_KEY)

def generate_health_advice(risk_factors_json):
    try:
        risk_factors = json.loads(risk_factors_json)
    except Exception as e:
        return f"Error parsing risk factors: {str(e)}"

    increasing_factors = risk_factors

    if not increasing_factors:
        return "Your profile currently doesn't have any specific lifestyle or metabolic factors significantly increasing your immediate risk. Keep maintaining a healthy lifestyle!"

    factors_str = "\n".join([f"- {f['name']} (Current Value: {f['value']})" for f in increasing_factors])

    prompt = f"""
You are a professional medical advisor.

The following modifiable factors increase this person's stroke risk:
{factors_str}

Provide:
- Short encouraging introduction
- Brief explanation per factor + immediate goal
- 3-5 personalized lifestyle "Golden Rules"
- A short bold medical disclaimer

Use clean Markdown formatting.
Be professional and empathetic.
Return only formatted text.
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.4,
        )
        content = response.choices[0].message.content
        return content if content else "No valid content returned."

    except Exception as e:
        return f"Error generating advice: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Missing input argument (risk factors JSON).")
        sys.exit(1)

    risk_factors_input = sys.argv[1]
    print(generate_health_advice(risk_factors_input))
