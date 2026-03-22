import subprocess
import tempfile
import os

print("🔥 EXECUTOR FILE LOADED")


def run_code(code, language="python"):
    print("🔥 LANGUAGE RECEIVED:", language)

    try:
        # ================= PYTHON =================
        if language == "python":
            print("👉 Running Python")

            with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as f:
                f.write(code.encode())
                file = f.name

            result = subprocess.run(
                ["python", file], capture_output=True, text=True, timeout=5
            )

        # ================= C =================
        elif language == "c":
            print("👉 Running C")

            with tempfile.NamedTemporaryFile(delete=False, suffix=".c") as f:
                f.write(code.encode())
                c_file = f.name

            exe_file = c_file.replace(".c", ".exe")

            # compile
            compile = subprocess.run(
                ["gcc", c_file, "-o", exe_file], capture_output=True, text=True
            )

            if compile.returncode != 0:
                return {"error": compile.stderr}

            # run
            result = subprocess.run(
                [exe_file], capture_output=True, text=True, timeout=5
            )

        else:
            return {"error": "Unsupported language"}

        return {"output": result.stdout, "error": result.stderr}

    except Exception as e:
        return {"error": str(e)}
