from .models import Opportunity, ResearchQuestion


def calculate_priority_score(item: Opportunity) -> float:
    positive = (
        item.novelty
        + item.ip_potential
        + item.market_size_score
        + item.manufacturing_feasibility
        + item.chance_of_success
        + item.long_term_moat
        + item.team_fit
    )
    penalty = item.technical_difficulty + item.capital_required + item.time_required
    raw = positive - 0.45 * penalty
    return round(max(0.0, min(10.0, raw / 4.0)), 2)


def score_explanation(item: Opportunity) -> str:
    score = calculate_priority_score(item)
    if score >= 8:
        return "High-priority opportunity. Strong candidate for deeper investigation."
    if score >= 6:
        return "Promising but needs more evidence before commitment."
    if score >= 4:
        return "Moderate priority. Keep in atlas but do not invest heavily yet."
    return "Low priority for current team and constraints."


def calculate_question_score(item: ResearchQuestion) -> float:
    positive = (
        item.scientific_importance
        + item.engineering_impact
        + item.commercial_relevance
        + item.novelty
        + item.capability_creation
        + item.urgency
    )
    feasibility_bonus = 0.7 * item.feasibility
    raw = positive + feasibility_bonus
    return round(max(0.0, min(10.0, raw / 6.7)), 2)


def question_score_explanation(item: ResearchQuestion) -> str:
    score = calculate_question_score(item)
    if score >= 8:
        return "High-value question. Convert into evidence collection and experiment design."
    if score >= 6:
        return "Promising question. Clarify unknowns and define the smallest useful experiment."
    if score >= 4:
        return "Moderate-value question. Preserve, but do not prioritize heavily yet."
    return "Low-priority question for the current research program."
