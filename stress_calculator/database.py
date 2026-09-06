# database.py

"""
database.py - Predefined Materials & File Export Management
Part of Task 6 Package Integration
"""

import json
import csv
from pathlib import Path
from datetime import datetime
from .material import Material, Metal, Plastic, Composite

BASE_DIR = Path(__file__).resolve().parent
JSON_PATH = BASE_DIR / "materials_db.json"
CSV_PATH = BASE_DIR / "test_results.csv"

def get_predefined_materials() -> dict:
    """Default fallback materials."""
    from .properties import MaterialProperties  # <--- MUST BE HERE TOO
    return {
        "1": Metal("Structural Steel", MaterialProperties(7850, 250, 200), is_ferrous=True),
        "2": Metal("Aluminum 6061", MaterialProperties(2700, 276, 68.9), is_ferrous=False),
        "3": Plastic("ABS Plastic", MaterialProperties(1040, 40, 2.3)),
        "4": Composite("Carbon Fiber", MaterialProperties(1600, 600, 150)),
    }

def load_materials():
    """Loads material database (JSON fallback to default dict)."""
    from .properties import MaterialProperties
    if not JSON_PATH.exists():
        return get_predefined_materials()

    try:
        with open(JSON_PATH, "r", encoding="utf-8") as f:
            raw = json.load(f)
            return {
                k: Material(v["name"], MaterialProperties(v["density"], v["yield_strength"], v["youngs_modulus"]))
                for k, v in raw.items()
            }
    except Exception:
        return get_predefined_materials()

def export_test_results_to_csv(test_data: list) -> None:
    """Exports test history to a CSV file."""
    if not test_data:
        return

    fieldnames = ["Timestamp", "Material", "Stress (Pa)", "Strain", "Factor of Safety", "Status"]
    file_exists = CSV_PATH.exists()

    try:
        with open(CSV_PATH, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()

            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            for item in test_data:
                writer.writerow({
                    "Timestamp": now,
                    "Material": item.get("material", "N/A"),
                    "Stress (Pa)": f"{item.get('stress', 0):.2e}",
                    "Strain": f"{item.get('strain', 0):.6f}",
                    "Factor of Safety": f"{item.get('factor_of_safety', 0):.2f}",
                    "Status": item.get("safety_result", "N/A")
                })
        print(f"\n[INFO] Results exported to {CSV_PATH.name}")
    except Exception as e:
        print(f"[ERROR] Export failed: {e}")

HISTORY_PATH = BASE_DIR / "test_history.json"


def save_history_to_json(test_data: list) -> None:
    """Saves the current session's test history to a JSON file."""
    if not test_data:
        print("[INFO] No test history to save.")
        return

    try:
        with open(HISTORY_PATH, "w", encoding="utf-8") as f:
            json.dump(test_data, f, indent=4)
        print(f"[INFO] Test history saved to {HISTORY_PATH.name}")
    except Exception as e:
        print(f"[ERROR] Save failed: {e}")


def load_history_from_json() -> list:
    """Loads previously saved test history from a JSON file. Returns [] if none exists."""
    if not HISTORY_PATH.exists():
        print("[INFO] No saved history file found.")
        return []

    try:
        with open(HISTORY_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[ERROR] Load failed: {e}")
        return []
