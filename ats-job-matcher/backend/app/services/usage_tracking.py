from dataclasses import dataclass


@dataclass
class UsageSnapshot:
    searches: int = 0
    matches_generated: int = 0
    documents_downloaded: int = 0


FREE_MATCH_LIMIT = 3
PRO_MATCH_LIMIT = 100


def can_generate_matches(plan: str, current_matches: int, requested: int) -> bool:
    if plan == "pro":
        return current_matches + requested <= PRO_MATCH_LIMIT
    if plan == "free":
        return current_matches + requested <= FREE_MATCH_LIMIT
    # payg can always generate; charges are handled by Stripe.
    return True


def needs_upgrade_prompt(plan: str, current_matches: int) -> bool:
    if plan == "free" and current_matches >= FREE_MATCH_LIMIT:
        return True
    if plan == "pro" and current_matches >= PRO_MATCH_LIMIT:
        return True
    return False
