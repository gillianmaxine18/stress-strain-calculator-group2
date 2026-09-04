
# Part 2: Stress and Strain Calculator with Control Structures
# TODO: Complete this template by filling in the missing code


def main():
    """Main function for Task 2: Control Structures & Safety Analysis."""
    
    # Predefined material yield strengths (in Pa)
    STEEL_YIELD = 250_000_000      # 250 MPa
    ALUMINUM_YIELD = 95_000_000    # 95 MPa
    COPPER_YIELD = 70_000_000      # 70 MPa

    # TODO: Wrap the entire calculator in a loop for repeated calculations
    while True:
        print("\n=== Stress and Strain Calculator (Task 2) ===")
        print()

        # TODO: Get user inputs with exception handling (try-except) and positive-value validation
        # Hint: Use a loop that prompts until valid input (> 0) is entered
        try:
            force = float(input("Enter applied force (N): "))
            area = float(input("Enter cross-sectional area (m^2): "))
            original_length = float(input("Enter original length (m): "))
            change_in_length = float(input("Enter change in length (m): "))

            if force <= 0 or area <= 0 or original_length <= 0:
                print("Error: Force, area, and original length must be greater than zero.")
                continue
        except ValueError:
            print("Error: Invalid numeric input! Please enter valid numbers.")
            continue

        # TODO: Calculate stress and strain
        stress = force / area
        strain = change_in_length / original_length

        # TODO: Material Selection (Predefined or Custom)
        print("\n=== Material Selection ===")
        print("1. Structural Steel")
        print("2. Aluminum")
        print("3. Copper")
        print("4. Custom Material")
        
        choice = input("Select material option (1-4): ")

        if choice == "1":
            material_name = "Structural Steel"
            yield_strength = STEEL_YIELD
        elif choice == "2":
            material_name = "Aluminum"
            yield_strength = ALUMINUM_YIELD
        elif choice == "3":
            material_name = "Copper"
            yield_strength = COPPER_YIELD
        elif choice == "4":
            material_name = "Custom Material"
            try:
                yield_strength = float(input("Enter custom yield strength (Pa): "))
                if yield_strength <= 0:
                    print("Yield strength must be positive!")
                    continue
            except ValueError:
                print("Error: Invalid yield strength input.")
                continue
        else:
            print("Invalid material choice selected.")
            continue

        # TODO: Factor of Safety Calculation & Safety Analysis
        # Hint: Factor of Safety (FOS) = Yield Strength / Calculated Stress
        fos = yield_strength / stress

        print("\n=== RESULTS & SAFETY ANALYSIS ===")
        print(f"Calculated Stress: {stress:.2f} Pa ({stress / 1_000_000:.2f} MPa)")
        print(f"Calculated Strain: {strain:.6f}")
        print(f"Material: {material_name}")
        print(f"Yield Strength: {yield_strength / 1_000_000:.2f} MPa")
        print(f"Factor of Safety (FOS): {fos:.2f}")

        # Safety evaluation using control structures
        if fos >= 1.0:
            print("Status: SAFE — Applied stress is within material yield limits.")
        else:
            print("Status: UNSAFE — Applied stress exceeds material yield limits!")

        # TODO: Repeated Calculations & Graceful Program Termination
        again = input("\nWould you like to perform another calculation? (yes/no): ").strip().lower()
        if again != 'yes' and again != 'y':
            print("\nThank you for using the calculator. Exiting gracefully...")
            break


# TODO: Standard Python execution pattern
if __name__ == "__main__":
    main()



# initial - task 3 

import sys


def main():
    """Main function for the stress and strain calculator with data structures."""

    print("=== Stress and Strain Calculator - Session Manager ===")
    print()

    # TODO: Initialize empty list for calculation history
    calculation_history = []

    # TODO: Initialize empty set for unique materials
    materials_used = set()

    # TODO: Create tuple for measurement units (N, m², m, Pa)
    UNITS = ("N", "m²", "m", "Pa")

    # TODO: Create materials database dictionary with at least 3 materials
    # Each material should have yield_strength and youngs_modulus (values in Pa)
    materials = {
        "1": {"name": "Structural Steel", "yield_strength": 250_000_000, "youngs_modulus": 200_000_000_000},
        "2": {"name": "Aluminum 6061-T6", "yield_strength": 276_000_000, "youngs_modulus": 68_900_000_000},
        "3": {"name": "Titanium", "yield_strength": 880_000_000, "youngs_modulus": 113_800_000_000},
        "4": {"name": "Copper", "yield_strength": 70_000_000, "youngs_modulus": 110_000_000_000}
    }

    # Main calculation loop
    while True:
        # TODO: Display available materials
        print("\nSelect Material for Safety Analysis:")
        for key, props in materials.items():
            print(f"[{key}] {props['name']}")
        print("[Q] Quit & View Summary")

        # TODO: Get material selection from user
        mat_choice = input("Enter choice (1-4 or Q to Quit): ").strip()

        # TODO: Check if user wants to quit
        if mat_choice.lower() in ["q", "quit"]:
            break

        # TODO: Validate material exists in database
        if mat_choice not in materials:
            print("Error: Material not found in database! Please select a valid option.\n")
            continue

        try:
            # TODO: Get input values (force, area, original_length, change_in_length)
            applied_force = float(input(f"Enter applied force ({UNITS[0]}): "))
            cross_sectional_area = float(input(f"Enter cross-sectional area ({UNITS[1]}): "))
            original_length = float(input(f"Enter original length ({UNITS[2]}): "))
            change_in_length = float(input(f"Enter change in length ({UNITS[2]}): "))

            # TODO: Validate inputs (positive values, non-zero where needed)
            if applied_force <= 0 or cross_sectional_area <= 0 or original_length <= 0 or change_in_length <= 0:
                print("Error: Inputs must be positive numbers greater than zero!\n")
                continue

            # TODO: Calculate stress and strain
            stress = applied_force / cross_sectional_area
            strain = change_in_length / original_length

            # TODO: Get material properties from database
            selected_mat = materials[mat_choice]
            mat_name = selected_mat["name"]
            yield_strength = selected_mat["yield_strength"]

            # TODO: Calculate safety factor
            fos = yield_strength / stress
            safety_result = "SAFE" if fos >= 1.0 else "WARNING - MATERIAL WILL FAIL"

            # TODO: Create calculation record dictionary with all data
            record = {
                "material": mat_name,
                "force": applied_force,
                "area": cross_sectional_area,
                "original_length": original_length,
                "change_in_length": change_in_length,
                "stress": stress,
                "strain": strain,
                "factor_of_safety": fos,
                "status": safety_result
            }

            # TODO: Add record to history list
            calculation_history.append(record)

            # TODO: Add material to unique materials set
            materials_used.add(mat_name)

            # TODO: Display results for this calculation
            print("\n" + "-" * 15 + " Results " + "-" * 15)
            print(f"Calculated Stress       : {stress:,.2f} {UNITS[3]}")
            print(f"Calculated Strain       : {strain:.6f}")
            print(f"Selected Material       : {mat_name}")
            print(f"Factor of Safety (FoS)  : {fos:.2f}")
            print(f"Safety Status           : {safety_result}")
            print("-" * 39)

            repeat = input("\nDo you want to calculate again? (yes/no): ").lower().strip()
            if repeat not in ["yes", "y"]:
                break

        except ValueError:
            print("Error: Invalid input. Please enter numeric values.")
        except ZeroDivisionError:
            print("Error: Area and original length cannot be zero!")
        except KeyError:
            print("Error: Material not found in database!")

    # TODO: Display session summary
    # - Total number of calculations
    # - List of unique materials tested
    # - Detailed history of each calculation
    print("\n" + "=" * 45)
    print("              SESSION SUMMARY")
    print("=" * 45)
    print(f"Total calculations performed : {len(calculation_history)}")
    print(f"Unique materials tested      : {len(materials_used)}")

    print("\nMaterials tested:")
    if materials_used:
        for mat in sorted(materials_used):
            print(f" - {mat}")
    else:
        print(" - None")

    if calculation_history:
        print("\nDetailed History:")
        for idx, r in enumerate(calculation_history, start=1):
            print(f"  [{idx}] Material: {r['material']} | Stress: {r['stress']:,.2f} {UNITS[3]} | FoS: {r['factor_of_safety']:.2f} ({r['status']})")

        # TODO: Display statistics (optional)
        # - Highest stress
        # - Lowest safety factor
        # - Average strain
        # - Material test counts
        stresses = [r["stress"] for r in calculation_history]
        foses = [r["factor_of_safety"] for r in calculation_history]
        strains = [r["strain"] for r in calculation_history]

        print("\n=== Session Statistics ===")
        print(f"Highest Stress Observed : {max(stresses):,.2f} {UNITS[3]}")
        print(f"Lowest Safety Factor    : {min(foses):.2f}")
        print(f"Average Strain          : {sum(strains) / len(strains):.6f}")

    print("\nThank you for using the Stress and Strain Calculator!")


# Standard Python execution pattern
if __name__ == "__main__":
    main()
