from datetime import datetime, timedelta
from limiter import TokenBucket


def test_token_bucket_caps_at_max_capacity():
    now = datetime(2026, 1, 1, 12, 0, 0)
    bucket = TokenBucket(capacity=10.0, refill_rate_per_sec=2.0, tokens=5.0, last_refill=now)
    later = now + timedelta(seconds=60)
    bucket.refill(later)
    assert bucket.tokens == 10.0


def test_consume_tokens_deducts_properly():
    now = datetime(2026, 1, 1, 12, 0, 0)
    bucket = TokenBucket(capacity=10.0, refill_rate_per_sec=1.0, tokens=10.0, last_refill=now)
    assert bucket.allow_request(4.0, now) is True
    assert bucket.tokens == 6.0
