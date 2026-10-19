# How to run
1. pip install fastapi uvicorn prometheus-client
2. uvicorn main:app --reload
3. Test: curl -X POST http://localhost:8000/api/v1/consultations/attention -H "traceparent: 123"
4. Check metrics: curl http://localhost:8000/metrics