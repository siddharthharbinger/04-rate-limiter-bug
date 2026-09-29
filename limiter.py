from dataclasses import dataclass
from datetime import datetime


@dataclass
class TokenBucket:
    capacity: float
    refill_rate_per_sec: float
    tokens: float
    last_refill: datetime

    def refill(self, now: datetime) -> None:
        """Refill tokens based on elapsed time up to bucket capacity."""
        elapsed = (now - self.last_refill).total_seconds()
        if elapsed > 0:
            # Bug: tokens are accumulated without clamping to self.capacity
            self.tokens += elapsed * self.refill_rate_per_sec
            self.last_refill = now

    def allow_request(self, tokens_needed: float, now: datetime) -> bool:
        """Check if request can be served and consume tokens."""
        self.refill(now)
        if self.tokens >= tokens_needed:
            self.tokens -= tokens_needed
            return True
        return False
