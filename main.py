import sys
from dataclasses import dataclass
from typing import List

# ==========================================
# PART 1: Basic Stress and Strain Calculator
# ==========================================
def main_part1():
    """Main function for the basic stress and strain calculator."""
    print("=== Stress and Strain Calculator ===")
    print()

    # Wrap inputs in a validation loop to prevent crashes
    while True:
        try:
            force = float(input("Enter applied force (N): "))
            area = float(input("Enter cross-sectional area (m²): "))
            original_length = float(input("Enter original length (m): "))
            change_in_length = float(input("Enter change in length (m): "))
            
            # Prevent negative/zero values for physical properties, but allow negative change_in_length
            if force <= 0 or area <= 0 or original_length <= 0:
                print("Error: Force, area, and original length must be strictly positive.\n")
                continue
            break # Exit the loop if all inputs are valid
        except ValueError:
            print("Error: Invalid input! Please enter valid numbers.\n")

    stress = force / area
    strain = change_in_length / original_length

    print("\n=== INPUT VALUES ===")
    print(f"Force: {force:.2f} N")
    print(f"Area: {area:.4f} m²")
    print(f"Original Length: {original_length:.2f} m")
    print(f"Change in Length: {change_in_length:.4f} m")

    print("\n=== RESULTS ===")
    print(f"Stress: {stress:.2f} Pa")
    print(f"Strain: {strain:.6f}")
    print()

    stress_mpa = stress / 1_000_000
    print(f"Stress in MPa: {stress_mpa:.2f} MPa")

    if change_in_length > 0:
        print("Loading Type: Tension")
    elif change_in_length < 0:
        print("Loading Type: Compression")
    else:
        print("Loading Type: Neutral")

    print("\n=== Analysis Complete ===")


# ==========================================
# PART 2: Control Structures
# ==========================================
def main_part2():
    """Main function for Task 2: Control Structures & Safety Analysis."""
    STEEL_YIELD = 250_000_000      # 250 MPa
    ALUMINUM_YIELD = 95_000_000    # 95 MPa
    COPPER_YIELD = 70_000_000      # 70 MPa

    while True:
        print("\n=== Stress and Strain Calculator (Task 2) ===")
        print()

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

        stress = force / area
        strain = change_in_length / original_length

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

        fos = yield_strength / stress

        print("\n=== RESULTS & SAFETY ANALYSIS ===")
        print(f"Calculated Stress: {stress:.2f} Pa ({stress / 1_000_000:.2f} MPa)")
        print(f"Calculated Strain: {strain:.6f}")
        print(f"Material: {material_name}")
        print(f"Yield Strength: {yield_strength / 1_000_000:.2f} MPa")
        print(f"Factor of Safety (FOS): {fos:.2f}")

        if fos >= 1.0:
            print("Status: SAFE — Applied stress is within material yield limits.")
        else:
            print("Status: UNSAFE — Applied stress exceeds material yield limits!")

        again = input("\nWould you like to perform another calculation? (yes/no): ").strip().lower()
        if again != 'yes' and again != 'y':
            print("\nThank you for using the calculator. Exiting gracefully...")
            break


# ==========================================
# PART 3: Data Structures (Session Manager)
# ==========================================
def main_part3():
    """Main function for the stress and strain calculator with data structures."""
    print("=== Stress and Strain Calculator - Session Manager ===")
    print()

    calculation_history = []
    materials_used = set()
    UNITS_P3 = ("N", "m²", "m", "Pa")

    materials = {
        "1": {"name": "Structural Steel", "yield_strength": 250_000_000, "youngs_modulus": 200_000_000_000},
        "2": {"name": "Aluminum 6061-T6", "yield_strength": 276_000_000, "youngs_modulus": 68_900_000_000},
        "3": {"name": "Titanium", "yield_strength": 880_000_000, "youngs_modulus": 113_800_000_000},
        "4": {"name": "Copper", "yield_strength": 70_000_000, "youngs_modulus": 110_000_000_000}
    }

    while True:
        print("\nSelect Material for Safety Analysis:")
        for key, props in materials.items():
            print(f"[{key}] {props['name']}")
        print("[Q] Quit & View Summary")

        mat_choice = input("Enter choice (1-4 or Q to Quit): ").strip()

        if mat_choice.lower() in ["q", "quit"]:
            break

        if mat_choice not in materials:
            print("Error: Material not found in database! Please select a valid option.\n")
            continue

        try:
            applied_force = float(input(f"Enter applied force ({UNITS_P3[0]}): "))
            cross_sectional_area = float(input(f"Enter cross-sectional area ({UNITS_P3[1]}): "))
            original_length = float(input(f"Enter original length ({UNITS_P3[2]}): "))
            change_in_length = float(input(f"Enter change in length ({UNITS_P3[2]}): "))

            # Removed change_in_length from strictly positive requirement to allow compression
            if applied_force <= 0 or cross_sectional_area <= 0 or original_length <= 0:
                print("Error: Force, area, and original length must be positive numbers greater than zero!\n")
                continue

            stress = applied_force / cross_sectional_area
            strain = change_in_length / original_length

            selected_mat = materials[mat_choice]
            mat_name = selected_mat["name"]
            yield_strength = selected_mat["yield_strength"]

            fos = yield_strength / stress
            safety_result = "SAFE" if fos >= 1.0 else "WARNING - MATERIAL WILL FAIL"

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

            calculation_history.append(record)
            materials_used.add(mat_name)

            print("\n" + "-" * 15 + " Results " + "-" * 15)
            print(f"Calculated Stress       : {stress:,.2f} {UNITS_P3[3]}")
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
            print(f"  [{idx}] Material: {r['material']} | Stress: {r['stress']:,.2f} {UNITS_P3[3]} | FoS: {r['factor_of_safety']:.2f} ({r['status']})")

        stresses = [r["stress"] for r in calculation_history]
        foses = [r["factor_of_safety"] for r in calculation_history]
        strains = [r["strain"] for r in calculation_history]

        print("\n=== Session Statistics ===")
        print(f"Highest Stress Observed : {max(stresses):,.2f} {UNITS_P3[3]}")
        print(f"Lowest Safety Factor    : {min(foses):.2f}")
        print(f"Average Strain          : {sum(strains) / len(strains):.6f}")

    print("\nThank you for using the Stress and Strain Calculator!")


# ==========================================
# PART 4: Calculation Functions
# ==========================================
def calculate_stress(force: float, area: float) -> float:
    if area <= 0:
        raise ValueError("Cross-sectional area must be strictly greater than zero.")
    return force / area

def calculate_strain(original_length: float, change_in_length: float) -> float:
    if original_length <= 0:
        raise ValueError("Original length must be strictly greater than zero.")
    return change_in_length / original_length

def calculate_youngs_modulus(stress: float, strain: float) -> float:
    if strain == 0:
        raise ValueError("Strain cannot be zero when calculating Young's Modulus.")
    return stress / strain

def calculate_factor_of_safety(yield_strength: float, stress: float) -> float:
    if stress <= 0:
        raise ValueError("Applied stress must be positive to compute Factor of Safety.")
    return yield_strength / stress

def validate_positive_number(value: float, parameter_name: str) -> float:
    if not isinstance(value, (int, float)):
        raise TypeError(f"{parameter_name} is invalid. It must be a number.")
    if value <= 0:
        raise ValueError(f"{parameter_name} must be positive, got {value}.")
    return float(value)

def validate_non_zero(value: float, parameter_name: str) -> float:
    if not isinstance(value, (int, float)):
        raise TypeError(f"{parameter_name} is invalid. It must be a number.")
    if value == 0:
        raise ValueError(f"{parameter_name} cannot be zero.")
    return float(value)

def validate_input(force: float, area: float, original_length: float, change_in_length: float) -> bool:
    for name, val in [
        ("Force", force),
        ("Area", area),
        ("Original Length", original_length),
        ("Change in Length", change_in_length),
    ]:
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} is invalid. It must be a number.")

    if area <= 0:
        raise ValueError("Cross-sectional area must be strictly greater than zero.")
    if original_length <= 0:
        raise ValueError("Original length must be strictly greater than zero.")
    if force < 0:
        raise ValueError("Force cannot be negative.")

    return True

def get_validated_input(prompt: str, validator_func, param_name: str) -> float:
    while True:
        raw_val = input(prompt).strip()
        try:
            num = float(raw_val)
            return validator_func(num, param_name)
        except (ValueError, TypeError) as err:
            print(f"  [Input Error] {err}")

def get_materials_database() -> dict[str, dict[str, float]]:
    return {
        "Steel": {"yield_strength": 250e6, "youngs_modulus": 200e9},
        "Aluminum": {"yield_strength": 95e6, "youngs_modulus": 69e9},
        "Titanium": {"yield_strength": 880e6, "youngs_modulus": 116e9},
    }

def get_material_properties(material_name: str, database: dict[str, dict[str, float]]) -> dict[str, float] | None:
    for name, props in database.items():
        if name.lower() == material_name.strip().lower():
            return props
    return None

def create_calculation_record(material: str, inputs: dict, results: dict) -> dict:
    return {
        "material": material,
        "inputs": inputs,
        "results": results,
    }

def add_to_history(history_list: list, record: dict) -> None:
    history_list.append(record)

def display_material_menu(database: dict[str, dict[str, float]]) -> None:
    print("\nAvailable Materials:")
    for mat in database:
        print(f"  - {mat}")
    print("  - Custom")

def display_safety_analysis(stress: float, yield_strength: float, safety_factor: float) -> None:
    print("\n--- Safety Analysis ---")
    print(f"  Applied Stress   : {stress:,.2f} Pa")
    print(f"  Yield Strength   : {yield_strength:,.2f} Pa")
    print(f"  Factor of Safety : {safety_factor:.2f}")
    if safety_factor >= 1.5:
        print("  Status           : SAFE (Meets typical structural safety factor of 1.5+)")
    elif safety_factor >= 1.0:
        print("  Status           : MARGINAL (Within yield limits, but low safety margin)")
    else:
        print("  Status           : FAILURE / YIELDING (Applied stress exceeds yield strength)")

def display_calculation_results(record: dict) -> None:
    res = record["results"]
    print("\n" + "=" * 50)
    print(f"TEST RESULTS: {record['material']}")
    print("-" * 50)
    print(f"Stress           : {res['stress_Pa']:,.2f} Pa")
    print(f"Strain           : {res['strain']:.6f}")
    if res.get("youngs_modulus_Pa") is not None:
        print(f"Young's Modulus  : {res['youngs_modulus_Pa']:,.2f} Pa")

    if res.get("factor_of_safety") is not None and res.get("yield_strength_Pa") is not None:
        display_safety_analysis(
            res["stress_Pa"],
            res["yield_strength_Pa"],
            res["factor_of_safety"]
        )
    print("=" * 50)

def display_session_summary(history: list[dict], unique_materials: set[str]) -> None:
    print("\n" + "=" * 55)
    print("SESSION SUMMARY")
    print(f"Total Tests Recorded    : {len(history)}")
    print(f"Unique Materials Tested : {', '.join(unique_materials) if unique_materials else 'None'}")
    print("-" * 55)
    for idx, item in enumerate(history, 1):
        r = item["results"]
        print(f"[{idx}] {item['material']} | Stress: {r['stress_Pa']:,.0f} Pa | Strain: {r['strain']:.6f}")
    print("=" * 55)

def main_calculator(
    material: str,
    force: float,
    area: float,
    original_length: float,
    change_in_length: float,
    yield_strength: float | None = None
) -> dict:
    validate_input(force, area, original_length, change_in_length)
    stress = calculate_stress(force, area)
    strain = calculate_strain(original_length, change_in_length)
    youngs_modulus = calculate_youngs_modulus(stress, strain) if strain != 0 else None

    fos = None
    if yield_strength is not None and yield_strength > 0:
        fos = calculate_factor_of_safety(yield_strength, stress)

    inputs = {
        "force_N": force,
        "area_m2": area,
        "original_length_m": original_length,
        "change_in_length_m": change_in_length,
    }
    results = {
        "stress_Pa": stress,
        "strain": strain,
        "youngs_modulus_Pa": youngs_modulus,
        "yield_strength_Pa": yield_strength,
        "factor_of_safety": fos,
    }
    return create_calculation_record(material, inputs, results)

def execute_single_calculation(database: dict[str, dict[str, float]]) -> tuple[dict, str]:
    display_material_menu(database)
    mat_choice = input("Select a material: ").strip()
    mat_props = get_material_properties(mat_choice, database)

    yield_strength = None
    if mat_props:
        material_name = mat_choice.capitalize()
        yield_strength = mat_props["yield_strength"]
    else:
        material_name = "Custom"

    force = get_validated_input("Enter force (N): ", validate_positive_number, "Force")
    area = get_validated_input("Enter cross-sectional area (m²): ", validate_positive_number, "Area")
    orig_l = get_validated_input("Enter original length (m): ", validate_positive_number, "Original Length")
    delta_l = get_validated_input("Enter change in length (m): ", validate_non_zero, "Change in Length")

    return main_calculator(material_name, force, area, orig_l, delta_l, yield_strength), material_name

def main_part4() -> None:
    """Top-level program coordinator for Part 4."""
    # Test Cases run silently before initialization to verify logic
    assert calculate_stress(50000, 0.01) == 5000000
    assert calculate_strain(10, 0.005) == 0.0005
    assert calculate_youngs_modulus(5000000, 0.0005) == 10000000000

    try:
        validate_positive_number(-5, "force")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass  # Expected behavior

    steel_test = main_calculator(
        material="Steel", force=50000, area=0.01, original_length=10,
        change_in_length=0.005, yield_strength=250e6
    )
    assert steel_test["results"]["stress_Pa"] == 5000000
    assert steel_test["results"]["strain"] == 0.0005
    assert steel_test["results"]["youngs_modulus_Pa"] == 10000000000
    assert steel_test["results"]["factor_of_safety"] == 50.0
    print("[INFO] All modular tests passed successfully.\n")

    database = get_materials_database()
    history: list[dict] = []
    unique_materials: set[str] = set()

    print("=== Stress and Strain Analysis System (Part 4: Modular) ===")

    while True:
        record, mat_name = execute_single_calculation(database)
        add_to_history(history, record)
        unique_materials.add(mat_name)
        display_calculation_results(record)

        run_again = input("\nRun another calculation? (y/n): ").strip().lower()
        if run_again != "y":
            break

    display_session_summary(history, unique_materials)
    print("Program exited successfully.")


# ==========================================
# PART 5: OOP Models
# ==========================================
UNITS_P5 = ("N", "m²", "m", "m", "Pa")

@dataclass
class MaterialProperties:
    density: float  # kg/m³
    yield_strength: float  # MPa
    typical_youngs_modulus: float  # GPa

    def __post_init__(self):
        if self.density <= 0:
            raise ValueError("Density must be positive")
        if self.yield_strength <= 0:
            raise ValueError("Yield strength must be positive")
        if self.typical_youngs_modulus <= 0:
            raise ValueError("Young's modulus must be positive")

class Material:
    def __init__(self, name: str, properties: MaterialProperties):
        self.name = name
        self.properties = properties

    def __str__(self) -> str:
        return f"{self.name} (Density: {self.properties.density} kg/m³)"

    def can_withstand_stress(self, stress: float) -> bool:
        return stress < (self.properties.yield_strength * 1_000_000)

class Metal(Material):
    def __init__(self, name: str, properties: MaterialProperties, is_ferrous: bool = False):
        super().__init__(name, properties)
        self.is_ferrous = is_ferrous

    def __str__(self) -> str:
        ferrous_text = "Ferrous" if self.is_ferrous else "Non-ferrous"
        return f"{self.name} ({ferrous_text} metal, Density: {self.properties.density} kg/m³)"

class Plastic(Material): pass
class Ceramic(Material): pass

def get_predefined_materials() -> dict:
    return {
        "1": Metal("Structural Steel", MaterialProperties(7850, 250, 200), is_ferrous=True),
        "2": Metal("6061-T6 Aluminum", MaterialProperties(2700, 270, 68.9), is_ferrous=False),
        "3": Plastic("PVC Plastic", MaterialProperties(1380, 45, 3)),
        "4": Ceramic("Standard Concrete", MaterialProperties(2400, 30, 30))
    }

class StressStrainTest:
    def __init__(self, material: Material, force: float, area: float, original_length: float, change_in_length: float):
        self.material = material
        self._force = force
        self._area = area
        self._original_length = original_length
        self._change_in_length = change_in_length

        if force <= 0:
            raise ValueError("Force must be positive")
        if area <= 0:
            raise ValueError("Area must be positive")
        if original_length <= 0:
            raise ValueError("Original length must be positive")
        if change_in_length == 0:
            raise ValueError("Change in length cannot be zero")

    @property
    def stress(self) -> float:
        return self._force / self._area

    @property
    def strain(self) -> float:
        return self._change_in_length / self._original_length

    @property
    def youngs_modulus(self) -> float:
        if self.strain == 0:
            return 0
        return (self.stress / self.strain) / 1e9

    def will_fail(self) -> bool:
        return not self.material.can_withstand_stress(self.stress)

    @property
    def factor_of_safety(self) -> float:
        if self.stress <= 0:
            return float('inf')
        return (self.material.properties.yield_strength * 1_000_000) / self.stress

    @property
    def safety_result(self) -> str:
        if self.factor_of_safety >= 1.0:
            return "SAFE (Design can handle the load)"
        return "WARNING - MATERIAL WILL FAIL!"

    def __str__(self) -> str:
        return (
            f"Test on {self.material.name}: "
            f"Stress={self.stress:.2f} Pa, "
            f"Strain={self.strain:.6f}, "
            f"Young's Modulus={self.youngs_modulus:.2f} GPa"
        )

class TestAnalysisSystem:
    def __init__(self):
        self.tests: List[StressStrainTest] = []
        self.materials_used = set()

    def add_test(self, test: StressStrainTest):
        self.tests.append(test)
        self.materials_used.add(test.material.name)

    def display_session_summary(self):
        print("\n" + "=" * 45)
        print("             SESSION SUMMARY")
        print("=" * 45)

        print(f"Total tests performed: {len(self.tests)}")
        print(f"Unique materials used: {len(self.materials_used)}")

        print("\nMaterials used:")
        if self.materials_used:
            for mat in sorted(self.materials_used):
                print(f"- {mat}")
        else:
            print("- None")

        if not self.tests:
            print("\nNo calculations were performed.")
            return

        stresses = [t.stress for t in self.tests]
        strains = [t.strain for t in self.tests]
        moduli = [t.youngs_modulus for t in self.tests]
        factors = [t.factor_of_safety for t in self.tests]

        print("\nBasic Statistics:")
        print(f"Average Stress: {sum(stresses)/len(stresses):.2e} {UNITS_P5[4]}")
        print(f"Average Strain: {sum(strains)/len(strains):.4f}")
        print(f"Average Young's Modulus: {sum(moduli)/len(moduli):.2e} GPa")
        print(f"Average Factor of Safety: {sum(factors)/len(factors):.2f}")

    def display_calculation_history(self):
        if not self.tests:
            return

        print("\n" + "=" * 45)
        print("          CALCULATION HISTORY")
        print("=" * 45)

        for i, test in enumerate(self.tests, start=1):
            print(f"\nTest {i}")
            print("-" * 30)
            print(f"Material: {test.material.name}")
            print(f"Force: {test._force:.2f} {UNITS_P5[0]}")
            print(f"Area: {test._area:.6f} {UNITS_P5[1]}")
            print(f"Stress: {test.stress:.2e} {UNITS_P5[4]}")
            print(f"Strain: {test.strain:.4f}")
            print(f"Factor of Safety: {test.factor_of_safety:.2f}")
            print(f"Safety Result: {test.safety_result}")

def get_valid_number(prompt: str, allow_negative: bool = False) -> float:
    while True:
        try:
            val = float(input(prompt))
            
            # If negatives are not allowed, block <= 0
            if not allow_negative and val <= 0:
                print("Error: Input must be greater than zero! Try again.\n")
                continue
            
            # If negatives are allowed (for compression), just block exactly 0
            if allow_negative and val == 0:
                print("Error: Change in length cannot be exactly zero! Try again.\n")
                continue
                
            return val
        except ValueError:
            print("Invalid input! Please enter a valid number.\n")
        except (KeyboardInterrupt, EOFError):
            print("\nProgram stopped. Goodbye!")
            sys.exit()

def main_part5():
    """Main execution function for Part 5 (OOP Models)"""
    analyzer = TestAnalysisSystem()
    materials_db = get_predefined_materials()

    while True:
        print("\n" + "=" * 45)
        print("       STRESS AND STRAIN CALCULATOR (OOP)")
        print("=" * 45)

        force = get_valid_number(f"Enter the applied force in {UNITS_P5[0]}: ")
        area = get_valid_number(f"Enter the cross-sectional area in {UNITS_P5[1]}: ")
        length = get_valid_number(f"Enter the original length in {UNITS_P5[2]}: ")
        
        # Set allow_negative to True so compression tests can be performed
        change = get_valid_number(f"Enter the change in length in {UNITS_P5[3]}: ", allow_negative=True)

        print("\nSelect Material for Safety Analysis:")
        for key, mat in materials_db.items():
            print(f"[{key}] {mat.name}")
        print("[5] Custom Material")

        choice = input("Enter choice (1-5): ").strip()

        if choice in materials_db:
            selected_material = materials_db[choice]
        elif choice == "5":
            mat_name = input("Enter custom material name: ").strip() or "Custom Material"
            density = get_valid_number("Enter custom Density (kg/m³): ")
            yield_strength = get_valid_number("Enter custom Yield Strength (MPa): ")
            youngs_modulus = get_valid_number("Enter custom Young's Modulus (GPa): ")
            selected_material = Material(mat_name, MaterialProperties(density, yield_strength, youngs_modulus))
        else:
            print("Invalid choice! Defaulting to Structural Steel.")
            selected_material = materials_db["1"]

        test = StressStrainTest(selected_material, force, area, length, change)
        analyzer.add_test(test)

        print("\n" + "-" * 15 + " Results " + "-" * 15)
        print(f"Calculated Stress: {test.stress:.2e} {UNITS_P5[4]}")
        print(f"Calculated Strain: {test.strain:.4f}")
        print(f"Young's Modulus: {test.youngs_modulus:.2f} GPa")
        print(f"Selected Material: {test.material.name}")
        print(f"Factor of Safety (FoS): {test.factor_of_safety:.2f}")
        print(f"Safety Status: {test.safety_result}")
        print("-" * 39)

        repeat = input("\nDo you want to calculate again? (yes/no): ").lower().strip()
        if repeat not in ["yes", "y"]:
            break

    analyzer.display_calculation_history()
    analyzer.display_session_summary()
    print("\nThank you for using the Stress and Strain Calculator! Goodbye!")


# ==========================================
# MASTER PROGRAM COORDINATOR
# ==========================================
if __name__ == "__main__":
    while True:
        print("\n" + "=" * 50)
        print("  STRESS & STRAIN CALCULATOR - MASTER MENU")
        print("=" * 50)
        print("1. Run Part 1: Basic Calculator")
        print("2. Run Part 2: Control Structures")
        print("3. Run Part 3: Data Structures (Session Manager)")
        print("4. Run Part 4: Modular Functions")
        print("5. Run Part 5: OOP Models")
        print("Q. Quit")
        print("=" * 50)
        
        menu_choice = input("Select a programme to run (1-5 or Q): ").strip().upper()
        
        if menu_choice == '1':
            main_part1()
        elif menu_choice == '2':
            main_part2()
        elif menu_choice == '3':
            main_part3()
        elif menu_choice == '4':
            main_part4()
        elif menu_choice == '5':
            main_part5()
        elif menu_choice == 'Q':
            print("Exiting Master Program. Goodbye!")
            sys.exit()
        else:
            print("Invalid selection. Please enter a number between 1 and 5, or 'Q' to quit.")