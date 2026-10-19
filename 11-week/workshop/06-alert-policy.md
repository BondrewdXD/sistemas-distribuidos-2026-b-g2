# Alert Policy

## Budget consumed before firing
- **Fast Alert (14.4x):** Fires after 5 minutes. Consumes 2% of the 30-day budget. Good for catching severe outages.
- **Slow Alert (6x):** Fires after 30 minutes. Consumes 5% of the budget. Good for catching slow degradations.

## Cause-based alerts we will NOT create
1. **High CPU Usage (> 90%):** CPU spikes do not necessarily mean the user experience is degraded. We alert on symptoms (latency/errors), not causes.
2. **High Memory Usage (> 85%):** Similar to CPU, high memory might be normal for the Python runtime. We prefer to alert if memory causes OutOfMemory errors (which would reflect in the error rate).