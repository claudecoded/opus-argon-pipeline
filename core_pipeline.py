import json
from google import genai
from google.genai import types
from anthropic import Anthropic
from config import Config
from utils import log_step

class BridgePipeline:
    def __init__(self):
        Config.validate()
        self.gemini_client = genai.Client(api_key=Config.GEMINI_API_KEY)
        self.anthropic_client = Anthropic(api_key=Config.ANTHROPIC_API_KEY)

    def execute_argon_prototype(self, prompt: str, legacy_code: str = "") -> str:
        """
        Step 1: Gemini 4 Argon processes the input and builds a fast, high-context prototype.
        """
        log_step("STEP 1", "Invoking Gemini 4 Argon for Rapid Iteration", "amber")
        
        # Configure Argon's reasoning budget
        thinking_budget = 2048 if Config.THINKING_EFFORT == "HIGH" else 1024
        config = types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=thinking_budget),
            temperature=0.2
        )

        system_instruction = (
            "You are an Elite Rapid Prototyping Engineer. Your task is to ingest requirements "
            "and output complete, working, raw structural code blueprints. Do not include markdown "
            "explanations outside the code block."
        )

        user_content = f"Requirement Goal: {prompt}\n\n"
        if legacy_code:
            user_content += f"Legacy Base Material Code:\n```\n{legacy_code}\n```"

        response = self.gemini_client.models.generate_content(
            model='gemini-4-argon',
            contents=user_content,
            config=config
        )
        return response.text

    def execute_opus_refinement(self, prompt: str, raw_blueprint: str) -> str:
        """
        Step 2: Claude Opus 5.5 assumes control to perfect and secure the code.
        """
        log_step("STEP 2", "Invoking Claude Opus 5.5 for Production Refinement", "deep_sky_blue1")

        effort_level = "high" if Config.THINKING_EFFORT == "HIGH" else "medium"

        response = self.anthropic_client.messages.create(
            model="claude-opus-5-5",
            max_tokens=8192,
            thinking={"type": "adaptive"},
            extra_headers={
                "output_config": {"effort": effort_level}
            },
            messages=[
                {
                    "role": "user",
                    "content": (
                        f"Target Architecture Goal: {prompt}\n\n"
                        f"Upstream Engine Raw Blueprint:\n```\n{raw_blueprint}\n```\n\n"
                        f"Refactor and polish the code module above. Fix potential logical bugs, "
                        f"optimize performance parameters, add error handling, and output clean code."
                    )
                }
            ]
        )

        final_code = "".join([block.text for block in response.content if block.type == "text"])
        return final_code
