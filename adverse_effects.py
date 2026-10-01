import anthropic
import json
client = anthropic.Anthropic()

SYSTEM_PROMPT = """
You are a clinical pharmacovigilance assistant apecialized in drug safety information.
Your role is to provide accurate, structured information about known adverse drug effects based on established pharmacological knowledge.
When given a drug name, always respond with a JSON object following this exact structure:
{
    "drug_name": "standardized drug name",
    "drug_class": "therapeutic class",
    "common_adverse_effect": [
        {"effect": "description", "frequency": "very common/common/uncommon/rare","severity": "mild/moderate/severe"}
    ],
    "serious_adverse_effects": [
        {"effect": "description", "organ_system": "affected syatem", "severity": "severe/life-threatening"}
    ],
    "contradictions": ["list of contradictions"],
    "monitoring_parameters": ["what clinicians should monitor"],
    "source_note": "brief note about data limitations"
}

Aways include a source_note acknowledging that this information is from training data and should be verified againt current prescribing information.
Respond with ONLY the JSON object - no preamble, no explanations, no markdown code fences.
"""

def get_adverse_effects(drug_name: str) -> dict:
    """
    Query Claude for known adverse effects of a drug.
    Returns a structured dictionary of adverse effect information.
    """

    user_prompt = f"""Provide adverse effect information for the drug: {drug_name}
                      Include:
                      - Common adverse effects with frequency and severity
                      - Serious or life-threatening adverse effects and which organ systems they affect
                      - Key contradictions
                      - Important monitoring parameters for clinicians
                      Return ONLY the JSON object. No explanation, no markdown fences."""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2048.
        system=SYSTEM_PROMPT,
        messages=[
            {"role":"user","content":user_prompt}
        ]
    )

    response_text = message.content[0].text

    try:
        result = json.loads(response_text)
    except json.JSONDecodeError as e:
        result = {
            "error": "Failed to parse response as JSON",
            "raw_response": response_text,
            "parse_error": str(e)
        }

    return result