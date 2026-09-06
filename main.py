"""
main.py - Stress and Strain Analysis System
Entry point for Task 6: Final Modular Application and Integration

"""

import sys

from stress_calculator import (
    get_predefined_materials,
    MaterialProperties,
    Material,
    StressStrainTest,
    TestAnalysisSystem,
)
from stress_calculator.database import (
    save_history_to_json,
    load_history_from_json,
    export_test_results_to_csv,
)

# Task 1: meaningful constant naming + f-string-ready unit labels
UNITS = ("N", "m²", "m", "m", "Pa")


# ==========================================
# TASK 2 CONCEPTS: Control Structures & Input Validation
# (originally Member 2's standalone validation loop; now a reusable function)
# ==========================================
def get_valid_number(prompt: str, allow_negative: bool = False) -> float:
    """Repeatedly prompt until a valid float is entered.

    Demonstrates Task 2 (while loop, try/except, input validation) and
    Task 4 (refactored into a reusable function with parameters).
    """
    while True:
        try:
            value = float(input(prompt))
            if not allow_negative and value <= 0:
                print("Error: Value must be greater than zero. Try again.\n")
                continue
            if allow_negative and value == 0:
                print("Error: Value cannot be exactly zero. Try again.\n")
                continue
            return value
        except ValueError:
            print("Error: Please enter a valid number.\n")
        except (KeyboardInterrupt, EOFError):
            print("\nProgram interrupted. Goodbye!")
            sys.exit()


# ==========================================
# TASK 2 + TASK 5 CONCEPTS: Material Selection Menu & OOP Objects
# ==========================================
def choose_material(materials_db: dict) -> Material:
    """Display material menu and return the chosen Material object.

    Task 2: menu-driven selection with a custom-material branch.
    Task 5: returns an OOP Material instance (or subclass) rather than
    a plain dictionary of properties.
    """
    print("\nSelect a material:")
    for key, mat in materials_db.items():
        print(f"  [{key}] {mat}")
    print("  [C] Custom material")

    choice = input("Enter choice: ").strip()

    if choice in materials_db:
        return materials_db[choice]

    if choice.lower() == "c":
        name = input("Custom material name: ").strip() or "Custom Material"
        density = get_valid_number("  Density (kg/m^3): ")
        yield_strength = get_valid_number("  Yield strength (MPa): ")
        youngs_modulus = get_valid_number("  Young's modulus (GPa): ")
        return Material(name, MaterialProperties(density, yield_strength, youngs_modulus))

    print("Invalid choice, defaulting to the first material in the list.")
    return next(iter(materials_db.values()))


# ==========================================
# TASK 3 + TASK 5 CONCEPTS: Data Structures + OOP Test Objects
# ==========================================
def run_new_test(analyzer: TestAnalysisSystem, materials_db: dict) -> None:
    """Collect inputs, run a stress/strain test, and store it.

    Task 1: force/area/length/change-in-length inputs and formatted output.
    Task 3: the resulting test gets appended into TestAnalysisSystem's
    internal list, and its material name into a set of unique materials
    (see tests.py -> TestAnalysisSystem.add_test).
    Task 5: stress, strain, Young's modulus, and factor of safety are all
    computed via @property methods on the StressStrainTest object.
    """
    force = get_valid_number(f"Enter applied force ({UNITS[0]}): ")
    area = get_valid_number(f"Enter cross-sectional area ({UNITS[1]}): ")
    original_length = get_valid_number(f"Enter original length ({UNITS[2]}): ")
    change_in_length = get_valid_number(
        f"Enter change in length ({UNITS[3]}): ", allow_negative=True
    )
    material = choose_material(materials_db)

    try:
        test = StressStrainTest(material, force, area, original_length, change_in_length)
    except ValueError as err:
        print(f"[ERROR] {err}")
        return

    analyzer.add_test(test)

    # Task 1: formatted output of results
    print("\n" + "-" * 15 + " Results " + "-" * 15)
    print(f"Material         : {test.material.name}")
    print(f"Stress           : {test.stress:,.2f} {UNITS[4]}")
    print(f"Strain           : {test.strain:.6f}")
    print(f"Young's Modulus  : {test.youngs_modulus:.2f} GPa")
    print(f"Factor of Safety : {test.factor_of_safety:.2f}")
    print(f"Safety Status    : {test.safety_result}")
    print("-" * 39)


def print_menu() -> None:
    """Task 2: menu-driven program flow."""
    print("\n" + "=" * 50)
    print("     STRESS & STRAIN ANALYSIS SYSTEM")
    print("=" * 50)
    print("1. Run a new test")
    print("2. View calculation history")          # Task 3: list of past tests
    print("3. View session summary")               # Task 3: set + basic stats
    print("4. Save history to JSON")                # Task 6: json module
    print("5. Load history from JSON")              # Task 6: json module
    print("6. Export history to CSV")               # Task 6: csv module
    print("Q. Quit")
    print("=" * 50)


# ==========================================
# TASK 6: Final Integration - ties every module and every prior
# task's concepts into a single, coordinated application.
# ==========================================
def main() -> None:
    print("=== Stress and Strain Analysis System ===")
    materials_db = get_predefined_materials()   # Task 5: OOP materials database
    analyzer = TestAnalysisSystem()             # Task 3 + 5: history list/set inside an object

    while True:
        print_menu()
        choice = input("Select an option: ").strip().upper()

        if choice == "1":
            run_new_test(analyzer, materials_db)
        elif choice == "2":
            analyzer.display_calculation_history()   # Task 3: iterate list
        elif choice == "3":
            analyzer.display_session_summary()        # Task 3: stats over list/set
        elif choice == "4":
            save_history_to_json(analyzer.get_export_data())   # Task 6: json.dump
        elif choice == "5":
            loaded = load_history_from_json()                  # Task 6: json.load
            if loaded:
                print(f"[INFO] Loaded {len(loaded)} record(s) from file:")
                for record in loaded:
                    print(f"  - {record}")
        elif choice == "6":
            export_test_results_to_csv(analyzer.get_export_data())  # Task 6: csv module
        elif choice == "Q":
            print("\nExiting program. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose a valid menu option.")


if __name__ == "__main__":
    main()
