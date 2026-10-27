import re
from patterns import PATTERNS

def rule_based_detect(page_text: str, page_url: str) -> list:
    """Fast keyword-based detection — runs instantly, no API needed."""
    found = []
    text_lower = page_text.lower()

    for pattern in PATTERNS:
        matched_keywords = []
        for keyword in pattern["keywords"]:
            if keyword.lower() in text_lower:
                matched_keywords.append(keyword)

        if matched_keywords:
            found.append({
                "id": pattern["id"],
                "name": pattern["name"],
                "category": pattern["category"],
                "severity": pattern["severity"],
                "explanation": pattern["explanation"],
                "matched_on": matched_keywords[:3],  # show top 3 matches
                "source": "rule-based"
            })

    return found


def llm_detect(page_text: str, url: str) -> list:
    """Claude-powered semantic detection — catches subtle patterns."""
    import anthropic
    import json

    client = anthropic.Anthropic()

    # Trim text to avoid token limits
    trimmed = page_text[:4000]

    prompt = f"""You are a dark patterns expert. Analyze this webpage text from {url} and identify any dark patterns present.

PAGE TEXT:
{trimmed}

Return a JSON array of dark patterns found. Each item must have:
- "name": pattern name
- "category": one of [Nagging, Obstruction, Sneaking, Interface Interference, Forced Action, Social Engineering]  
- "severity": one of [low, medium, high]
- "explanation": one sentence explaining why this is manipulative
- "evidence": the specific text that triggered this finding (max 80 chars)

If no dark patterns found, return an empty array [].
Return ONLY valid JSON, no other text."""

    try:
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )
        raw = message.content[0].text.strip()
        # Clean markdown code blocks if present
        raw = raw.replace("```json", "").replace("```", "").strip()
        patterns = json.loads(raw)
        for p in patterns:
            p["source"] = "llm"
        return patterns
    except Exception as e:
        print(f"LLM detection error: {e}")
        return []


def merge_results(rule_results: list, llm_results: list) -> list:
    """Combine and deduplicate results from both detectors."""
    seen_names = {r["name"].lower() for r in rule_results}
    combined = list(rule_results)

    for result in llm_results:
        if result["name"].lower() not in seen_names:
            combined.append(result)
            seen_names.add(result["name"].lower())

    # Sort by severity
    severity_order = {"high": 0, "medium": 1, "low": 2}
    combined.sort(key=lambda x: severity_order.get(x["severity"], 3))
    return combined