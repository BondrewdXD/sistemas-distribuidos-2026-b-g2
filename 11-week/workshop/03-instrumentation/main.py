from fastapi import FastAPI, Request
import logging, json, time
from prometheus_client import Counter, Histogram, make_asgi_app

app = FastAPI()
REQUESTS_TOTAL = Counter("consultation_requests_total", "Total requests", ["outcome"])
LATENCY = Histogram("consultation_request_duration_seconds", "Latency")
app.mount("/metrics", make_asgi_app())

class JsonFormatter(logging.Formatter):
    def format(self, record):
        return json.dumps({"timestamp": self.formatTime(record), "level": record.levelname, "service": "medical-consultation-api", "message": record.getMessage()})

logger = logging.getLogger("consultation-api")
handler = logging.StreamHandler()
handler.setFormatter(JsonFormatter())
logger.addHandler(handler)
logger.setLevel(logging.INFO)

@app.middleware("http")
async def trace_middleware(request: Request, call_next):
    trace_id = request.headers.get("traceparent", "mock-trace-id")
    request.state.trace_id = trace_id
    start = time.time()
    response = await call_next(request)
    LATENCY.observe(time.time() - start)
    REQUESTS_TOTAL.labels(outcome="success").inc()
    response.headers["traceparent"] = trace_id 
    logger.info(f"Processed request. Trace ID: {trace_id}")
    return response

@app.post("/api/v1/consultations/attention")
async def record_attention():
    return {"status": "ok"}