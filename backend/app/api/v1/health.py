from fastapi import APIRouter

# router for grouping related API endpoints.
router = APIRouter()

# python decorator tells fastapi, below function immediately should handle HTTP GET requests sent to /health.
@router.get("/health")
def health() -> dict:
    return{
        "status" : "ok",
        "service" : "nexus",
    }