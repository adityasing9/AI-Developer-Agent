from fastapi import APIRouter
from agents.debugger import debug_code

router = APIRouter()


@router.post("/debug")
async def debug(data: dict):
    code = data.get("code")
    language = data.get("language", "python")

    result = debug_code(code, language)
    return result


@router.post("/run")
async def run(data: dict):
    from agents.executor import run_code

    code = data.get("code")
    language = data.get("language", "python")

    return run_code(code, language)
