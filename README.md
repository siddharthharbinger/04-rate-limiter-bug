# Rate Limiter Bug

High-level bug: `TokenBucket.refill` calculates elapsed tokens and adds them to `self.tokens`, but does not clamp the total to `self.capacity`. After an idle period, the bucket accumulates far more tokens than its maximum capacity, allowing traffic bursts that violate the rate limit.

Run the reproduction with:

```powershell
python repro.py
```

Run the failing test with:

```powershell
python -m pytest -q
```

Expected result: After an idle period of 100 seconds on a bucket with capacity 10, `bucket.tokens` should equal `10.0`, but the buggy implementation returns `110.0`.
