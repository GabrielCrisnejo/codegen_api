import os
import uuid
from transformers import pipeline
from .settings import settings
import logging

logger = logging.getLogger(__name__)

class CodeGenerator:
    def __init__(self):
        self.generator = pipeline(
            "text-generation", 
            model=settings.MODEL_NAME, 
            torch_dtype="auto", 
            device_map="auto"
        )
        logger.info(f"Loaded model {settings.MODEL_NAME}")

    def generate_code(self, prompt: str) -> str:
        logger.info(f"Generating code for prompt: {prompt}")
        result = self.generator(
            prompt, 
            max_length=settings.MAX_LENGTH, 
            num_return_sequences=1,
            truncation=True
        )[0]["generated_text"]

        return result
