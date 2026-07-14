import sys
from pathlib import Path

from fastapi import APIRouter

PROJECT_ROOT = Path(__file__).resolve().parents[5]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from packages.ai_gateway.router import router as ai_gateway_router

router = APIRouter(prefix="/chat", tags=["ai_gateway"])
router.include_router(ai_gateway_router)
