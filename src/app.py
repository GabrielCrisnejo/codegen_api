from fastapi import FastAPI, HTTPException
from .generator import CodeGenerator
from .models import CodeRequest, CodeResponse
from .settings import settings
from .logger import get_logger

logger = get_logger(__name__)

app = FastAPI(
    title="CodeGen API",
    description="Generate code from natural language prompts using CodeGen model",
    version="1.0"
)

generator = CodeGenerator()

@app.post("/generate", response_model=CodeResponse)
async def generate_code(request: CodeRequest):
    try:
        full_prompt = f"# Language: {request.language}\n# Task: {request.prompt}\n"
        generated = generator.generate_code(
            prompt=full_prompt
        )
        return CodeResponse(generated_code=generated)
    except Exception as e:
        logger.error(f"Error generating code: {e}")
        raise HTTPException(status_code=500, detail=str(e))
