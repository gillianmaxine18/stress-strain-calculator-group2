
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
