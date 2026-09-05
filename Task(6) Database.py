"""main.py"""
import sys
try:
    from properties import MaterialProperties
    from material import Material
    from tests import StressStrainTest, TestAnalysisSystem
    import database
    import utils
except ImportError as e:
    print(f"CRITICAL ERROR: Missing module - {e}")
    sys.exit(1)

def main():
    analyzer = TestAnalysisSystem()
    # Load materials from JSON DB instead of standard dict
    materials_db = database.load_materials()

    while True:
        print("\n" + "=" * 45)
        print("       STRESS AND STRAIN CALCULATOR")
        print("=" * 45)

        force = utils.get_valid_number(f"Enter the applied force in {utils.UNITS[0]}: ")
        area = utils.get_valid_number(f"Enter the cross-sectional area in {utils.UNITS[1]}: ")
        length = utils.get_valid_number(f"Enter the original length in {utils.UNITS[2]}: ")
        change = utils.get_valid_number(f"Enter the change in length in {utils.UNITS[3]}: ")

        print("\nSelect Material for Safety Analysis:")
        for key, mat in materials_db.items():
            print(f"[{key}] {mat.name}")
        print("[5] Custom Material")

        choice = input("Enter choice (1-5): ").strip()

        if choice in materials_db:
            selected_material = materials_db[choice]
        elif choice == "5":
            mat_name = input("Enter custom material name: ").strip() or "Custom Material"
            density = utils.get_valid_number("Enter custom Density (kg/m³): ")
            yield_strength = utils.get_valid_number("Enter custom Yield Strength (MPa): ")
            youngs_modulus = utils.get_valid_number("Enter custom Young's Modulus (GPa): ")
            selected_material = Material(mat_name, MaterialProperties(density, yield_strength, youngs_modulus))
        else:
            print("Invalid choice! Defaulting to Structural Steel.")
            selected_material = materials_db["1"]

        # Process through OOP system
        test = StressStrainTest(selected_material, force, area, length, change)
        analyzer.add_test(test)

        print("\n" + "-" * 15 + " Results " + "-" * 15)
        print(f"Calculated Stress: {test.stress:.2e} {utils.UNITS[4]}")
        print(f"Calculated Strain: {test.strain:.4f}")
        print(f"Factor of Safety (FoS): {test.factor_of_safety:.2f}")
        print(f"Safety Status: {test.safety_result}")
        print("-" * 39)

        repeat = input("\nDo you want to calculate again? (yes/no): ").lower().strip()
        if repeat not in ["yes", "y"]:
            break

    # Display final summaries and export
    analyzer.display_session_summary()
    
    # New CSV Export feature
    if analyzer.tests:
        database.export_test_results_to_csv(analyzer.get_export_data())
        
    print("\nThank you for using the Stress and Strain Calculator! Goodbye!")

if __name__ == "__main__":
    main()