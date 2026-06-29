from .models import Opportunity


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
