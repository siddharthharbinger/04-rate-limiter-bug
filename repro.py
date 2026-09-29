from datetime import datetime, timedelta
from limiter import TokenBucket

now = datetime(2026, 1, 1, 12, 0, 0)
bucket = TokenBucket(capacity=10.0, refill_rate_per_sec=1.0, tokens=10.0, last_refill=now)

# Advance clock by 100 seconds
later = now + timedelta(seconds=100)
bucket.refill(later)

print(f"Bucket tokens after 100s: actual={bucket.tokens}, max_allowed={bucket.capacity}")
if bucket.tokens > bucket.capacity:
    print("BUG DETECTED: Tokens exceeded maximum bucket capacity!")
    raise SystemExit(1)
raise SystemExit(0)
