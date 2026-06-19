def should_escalate(user_query, retrieved_results):

    sensitive_keywords = [
        "refund",
        "billing",
        "charge",
        "legal",
        "lawsuit",
        "account ownership"
    ]

    query_lower = user_query.lower()

    for word in sensitive_keywords:
        if word in query_lower:
            return True

    if not retrieved_results:
        return True

    return False


def generate_handoff(persona, issue, sources):

    return {
        "persona": persona,
        "issue": issue,
        "documents_used": sources,
        "attempted_steps": [
            "Knowledge base retrieval",
            "AI response generation"
        ],
        "recommendation": "Human support review required"
    }