import re
from agents.executor import run_code
from agents.llm import call_ollama


def extract_code(text):
    code = re.findall(r"```(?:\w+)?\n(.*?)```", text, re.DOTALL)
    if code:
        return code[0].strip()
    return text.strip()


def debug_code(code, language="python"):
    history = []

    for step in range(3):
        result = run_code(code, language)

        # ✅ SUCCESS
        if not result.get("error"):
            return {
                "fixed_code": code,
                "output": result.get("output", ""),
                "steps": history,
            }

        # ✅ PROMPT (VERY IMPORTANT)
        prompt = f"""
You are an expert programmer.

Fix the following {language} code.

ONLY return corrected code.
NO explanation.
NO markdown.

Code:
{code}

Error:
{result["error"]}
"""

        raw_output = call_ollama(prompt)
        fixed_code = extract_code(raw_output)

        # ✅ SAFETY CHECK
        if not fixed_code or fixed_code == code:
            return {"error": "AI could not improve code", "steps": history}

        history.append({"step": step, "error": result["error"], "fix": fixed_code})

        code = fixed_code

    return {"error": "Could not fix code", "steps": history}
