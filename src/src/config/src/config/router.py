"""
Core routing logic for the API Orchestration Layer.
Defines how requests are dispatched to internal modules.
"""

from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok"}
