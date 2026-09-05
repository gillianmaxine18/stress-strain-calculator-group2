"""
properties.py - Material properties data class & interactive session manager.
"""

from dataclasses import dataclass
import sys
from .database import load_materials, export_test_results_to_csv


# 1. CLASS DEFINITION FOR MATERIAL PROPERTIES
@dataclass
class MaterialProperties:
    density: float         # kg/m³
    yield_strength: float  # MPa
    youngs_modulus: float  # GPa


# 2. INTERACTIVE SESSION MANAGER (TASK 3)
def main():
    """Main session manager function for Task 3."""

    print("=== Stress and Strain Calculator - Session Manager ===")
    print()

    # Task 3 Requirement 1: Tuple for measurement units
    UNITS = ("N", "m²", "m", "Pa")

    # Task 3 Requirement 2: Load dictionary of Material objects from database.py
    materials_db = load_materials()

    # Task 3 Requirement 3 & 4: List for calculation history, Set for unique materials
    calculation_history = []
    materials_used = set()

    # Interactive calculation loop
    while True:
        print("\nSelect Material for Safety Analysis:")
        for key, mat_obj in materials_db.items():
            print(f"[{key}] {mat_obj.name}")
        print("[Q] Quit & View Session Summary")

        mat_choice = input("Enter choice (1-4 or Q to Quit): ").strip()

        if mat_choice.lower() in ["q", "quit"]:
            break

        if mat_choice not in materials_db:
            print("Error: Invalid option! Please select a valid material key.\n")
            continue

        selected_material = materials_db[mat_choice]
        # Yield strength in database is in MPa; convert to Pa for calculation (1 MPa = 1,000,000 Pa)
        yield_strength_pa = selected_material.properties.yield_strength * 1_000_000

        try:
            applied_force = float(input(f"Enter the applied force in newtons ({UNITS[0]}): "))
            cross_sectional_area = float(input(f"Enter the cross-sectional area in square metres ({UNITS[1]}): "))
            original_length = float(input(f"Enter the original length in metres ({UNITS[2]}): "))
            change_in_length = float(input(f"Enter the change in length in metres ({UNITS[2]}): "))

            if applied_force <= 0 or cross_sectional_area <= 0 or original_length <= 0 or change_in_length <= 0:
                print("Error: All inputs must be positive numbers greater than zero!\n")
                continue

            # Core Calculations
            stress = applied_force / cross_sectional_area
            strain = change_in_length / original_length

            # Check safety using the Material object method
            is_safe = selected_material.can_withstand_stress(stress)
            fos = yield_strength_pa / stress if stress > 0 else 0.0
            safety_result = "SAFE (Design can handle load)" if is_safe else "WARNING - MATERIAL WILL FAIL!"

            # Task 3: Store record in dictionary (Keys matched to database.py export requirements)
            record = {
                "material": selected_material.name,
                "force": applied_force,
                "area": cross_sectional_area,
                "original_length": original_length,
                "change_in_length": change_in_length,
                "stress": stress,
                "strain": strain,
                "yield_strength": yield_strength_pa,
                "factor_of_safety": fos,
                "safety_result": safety_result,  # Key required by export_test_results_to_csv()
            }

            # Task 3: Append to list and add to set
            calculation_history.append(record)
            materials_used.add(selected_material.name)

            print("\n" + "-" * 15 + " Results " + "-" * 15)
            print(f"Calculated Stress       : {stress:,.2f} {UNITS[3]}")
            print(f"Calculated Strain       : {strain:.6f}")
            print(f"Selected Material       : {selected_material.name}")
            print(f"Yield Strength          : {yield_strength_pa:,.2f} {UNITS[3]}")
            print(f"Factor of Safety (FoS)  : {fos:.2f}")
            print(f"Safety Status           : {safety_result}")
            print("-" * 39)

            repeat = input("\nDo you want to calculate again? (yes/no): ").lower().strip()
            if repeat not in ["yes", "y"]:
                break

        except ValueError:
            print("Error: Invalid numeric entry! Please enter numbers only.")
        except ZeroDivisionError:
            print("Error: Area and original length cannot be zero!")

    # Task 3: Session Summary Output
    print("\n" + "=" * 45)
    print("              SESSION SUMMARY")
    print("=" * 45)
    print(f"Total calculations performed : {len(calculation_history)}")
    print(f"Unique materials tested      : {len(materials_used)}")

    print("\nMaterials tested in this session:")
    if materials_used:
        for mat in sorted(materials_used):
            print(f" - {mat}")
    else:
        print(" - None")

    if calculation_history:
        print("\nDetailed Calculation History:")
        for idx, r in enumerate(calculation_history, start=1):
            print(f"\n  [Test {idx}] - {r['material']}")
            print(f"   Force: {r['force']:,.2f} {UNITS[0]} | Area: {r['area']:.6f} {UNITS[1]}")
            print(f"   Stress: {r['stress']:,.2f} {UNITS[3]} | Strain: {r['strain']:.6f}")
            print(f"   FoS: {r['factor_of_safety']:.2f} | Status: {r['safety_result']}")

        stresses = [r["stress"] for r in calculation_history]
        foses = [r["factor_of_safety"] for r in calculation_history]
        strains = [r["strain"] for r in calculation_history]

        print("\n" + "=" * 45)
        print("            SESSION STATISTICS")
        print("=" * 45)
        print(f"Highest Stress Observed : {max(stresses):,.2f} {UNITS[3]}")
        print(f"Lowest Safety Factor    : {min(foses):.2f}")
        print(f"Average Strain          : {sum(strains) / len(strains):.6f}")

        # Export test results to CSV
        export_test_results_to_csv(calculation_history)

    print("\nThank you for using the Stress and Strain Calculator!")


if __name__ == "__main__":
    main()
