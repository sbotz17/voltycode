import sys
from pathlib import Path

from fastapi import APIRouter

from app.api.v1.chat import router as chat_router
from app.api.v1.health import router as health_router

PROJECT_ROOT = Path(__file__).resolve().parents[5]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

api_router = APIRouter()
api_router.include_router(health_router)
api_router.include_router(chat_router)
