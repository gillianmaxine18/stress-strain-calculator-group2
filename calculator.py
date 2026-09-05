# Part 1: Basic Stress and Strain Calculator Template
# TODO: Complete this template by filling in the missing code


def main():
    """Main function for the stress and strain calculator."""

    # TODO: Print a header for your program
    print("=== Stress and Strain Calculator ===")
    print()

    # TODO: Get user input for the four required values
    # Hint: Use input() to get strings, then convert with float()
    force = float(input("Enter applied force (N): ")) # TODO: Get applied force from user
    area = float(input("Enter cross-sectional area (m²): ")) # TODO: Get cross-sectional area from user
    original_length = float(input("Enter original length (m): ")) # TODO: Get original length from user
    change_in_length = float(input("Enter change in length (m): ")) # TODO: Get change in length from user

    # TODO: Calculate stress and strain
    # Hint: Stress = Force / Area, Strain = Change in Length / Original Length
    stress = force / area # TODO: Calculate stress
    strain = change_in_length / original_length # TODO: Calculate strain


    # TODO: Display the input values using f-string formatting
    print()
    print("=== INPUT VALUES ===")

    # TODO: Print each input value with appropriate formatting
    # Hint: Use {variable:.2f} for 2 decimal places
    print(f"Force: {force:.2f} N")
    print(f"Area: {area:.4f} m²")
    print(f"Original Length: {original_length:.2f} m")
    print(f"Change in Length: {change_in_length:.4f} m")

    print()
    print("=== RESULTS ===")

    # TODO: Display the calculated results
    # TODO: Print stress with 2 decimal places and units (Pa)
    print(f"Stress: {stress:.2f} Pa")

    # TODO: Print strain with 6 decimal places (no units - it's dimensionless)
    print(f"Strain: {strain:.6f}")

    print()

    # BONUS TODO: Convert stress to MPa (divide by 1,000,000)
    stress_mpa = stress / 1_000_000
    print(f"Stress in MPa: {stress_mpa:.2f} MPa")

    # BONUS TODO: Determine if loading is tension or compression
    if change_in_length > 0:
        print("Loading Type: Tension")
    elif change_in_length < 0:
        print("Loading Type: Compression")
    else:
        print("Loading Type: Neutral")

    print()
    print("=== Analysis Complete ===")



if __name__ == "__main__":
    main()
    
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

# TASK 4
# CALCULATION FUNCTIONS
def calculate_stress(force: float, area: float) -> float:
    """Calculate stress based on force and area: σ = F / A."""
    # bawal zero check
    if area <= 0:
        raise ValueError("Cross-sectional area must be strictly greater than zero.")
    return force / area

def calculate_strain(original_length: float, change_in_length: float) -> float:
    """Calculate strain based on original length and change in length: ε = ΔL / L₀."""
    if original_length <= 0:
        raise ValueError("Original length must be strictly greater than zero.")
    return change_in_length / original_length


def calculate_youngs_modulus(stress: float, strain: float) -> float:
    """Calculate Young's modulus from stress and strain: E = σ / ε."""
    # == 0 bcos hindi negative ang strain
    if strain == 0:
        raise ValueError("Strain cannot be zero when calculating Young's Modulus.")
    return stress / strain

def calculate_factor_of_safety(yield_strength: float, stress: float) -> float:
    """Calculate factor of safety: FoS = σ_yield / σ_applied."""
    if stress <= 0:
        raise ValueError("Applied stress must be positive to compute Factor of Safety.")
    return yield_strength / stress

# VALIDATION FUNCS
def validate_positive_number(value: float, parameter_name: str) -> float:
    """Validate that an input value is strictly greater than zero."""
    if not isinstance(value, (int, float)):
        raise TypeError(f"{parameter_name} is invalid. It must be a number.")
    if value <= 0:
        raise ValueError(f"{parameter_name} must be positive, got {value}.")
    return float(value)

def validate_non_zero(value: float, parameter_name: str) -> float:
    """Ensure a denominator or change value is non-zero."""
    if not isinstance(value, (int, float)):
        raise TypeError(f"{parameter_name} is invalid. It must be a number.")
    if value == 0:
        raise ValueError(f"{parameter_name} cannot be zero.")
    return float(value)

def validate_input(force: float, area: float, original_length: float, change_in_length: float) -> bool:
    """Validate that all input values are appropriate for calculations."""

    for name, val in [
        ("Force", force),
        ("Area", area),
        ("Original Length", original_length),
        ("Change in Length", change_in_length),
    ]:
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} is invalid. It must be a number.")

    # validation sa logics ng each parameter
    if area <= 0:
        raise ValueError("Cross-sectional area must be strictly greater than zero.")
    if original_length <= 0:
        raise ValueError("Original length must be strictly greater than zero.")
    if force < 0:
        raise ValueError("Force cannot be negative.")

    return True

def get_validated_input(prompt: str, validator_func, param_name: str) -> float:
    """Prompt user until valid input satisfying validator_func is provided."""
    while True:
        raw_val = input(prompt).strip()
        try:
            num = float(raw_val)
            return validator_func(num, param_name)
        except (ValueError, TypeError) as err:
            print(f"  [Input Error] {err}")

# DATA MANAGEMENT FUNCS
def get_materials_database() -> dict[str, dict[str, float]]:
    """Return default material properties database with yield strengths and Young's modulus."""
    return {
        "Steel": {"yield_strength": 250e6, "youngs_modulus": 200e9},
        "Aluminum": {"yield_strength": 95e6, "youngs_modulus": 69e9},
        "Titanium": {"yield_strength": 880e6, "youngs_modulus": 116e9},
    }

def get_material_properties(material_name: str, database: dict[str, dict[str, float]]) -> dict[str, float] | None:
    """Retrieve material properties by name case-insensitively."""
    for name, props in database.items():
        if name.lower() == material_name.strip().lower():
            return props
    return None

def create_calculation_record(material: str, inputs: dict, results: dict) -> dict:
    """Package test data into a clean dictionary record."""
    # dict to track na mas madali
    return {
        "material": material,
        "inputs": inputs,
        "results": results,
    }


def add_to_history(history_list: list, record: dict) -> None:
    """Append a calculation record to the session history list."""
    history_list.append(record)

# DISPLAY FUNCS
def display_material_menu(database: dict[str, dict[str, float]]) -> None:
    """Display available predefined materials in formatted list."""
    print("\nAvailable Materials:")
    for mat in database:
        print(f"  - {mat}")
    print("  - Custom")

def display_safety_analysis(stress: float, yield_strength: float, safety_factor: float) -> None:
    """Print an engineering safety evaluation based on the Factor of Safety."""
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
    """Format and print complete test results."""
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
    """Print overall summary of tests performed during the session."""
    print("\n" + "=" * 55)
    print("SESSION SUMMARY")
    print(f"Total Tests Recorded    : {len(history)}")
    print(f"Unique Materials Tested : {', '.join(unique_materials) if unique_materials else 'None'}")
    print("-" * 55)
    for idx, item in enumerate(history, 1):
        r = item["results"]
        print(f"[{idx}] {item['material']} | Stress: {r['stress_Pa']:,.0f} Pa | Strain: {r['strain']:.6f}")
    print("=" * 55)

# MAIN - ORCHESTRATION
def main_calculator(
    material: str,
    force: float,
    area: float,
    original_length: float,
    change_in_length: float,
    yield_strength: float | None = None
) -> dict:
    """Main function from template to orchestrate calculation without interactive prompts."""
    # validation muna bago calculations
    validate_input(force, area, original_length, change_in_length)

    # run the calculations
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
    """Coordinate user input prompts, calculation, and packaging for an interactive run."""
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

def main() -> None:
    """Top-level program coordinator."""
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

# TESTS: cases 1, 2, and 3
if __name__ == "__main__":
    # Test Case 1: Modular Testing (Individual calculations)
    assert calculate_stress(50000, 0.01) == 5000000
    assert calculate_strain(10, 0.005) == 0.0005
    assert calculate_youngs_modulus(5000000, 0.0005) == 10000000000

    # Test Case 1b: Validation Testing
    try:
        validate_positive_number(-5, "force")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass  # Expected behavior

    # Test Case 2: Integration Testing (Steel test from specs)
    steel_test = main_calculator(
        material="Steel",
        force=50000,
        area=0.01,
        original_length=10,
        change_in_length=0.005,
        yield_strength=250e6
    )
    assert steel_test["results"]["stress_Pa"] == 5000000
    assert steel_test["results"]["strain"] == 0.0005
    assert steel_test["results"]["youngs_modulus_Pa"] == 10000000000
    assert steel_test["results"]["factor_of_safety"] == 50.0

    print("All unit and integration test assertions passed successfully.")

    main()

import sys
from dataclasses import dataclass
from typing import List

# constants
UNITS = ("N", "m²", "m", "m", "Pa")

# OOP models
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
        return stress < self.properties.yield_strength

class Metal(Material):
    def __init__(self, name: str, properties: MaterialProperties, is_ferrous: bool = False):
        super().__init__(name, properties)
        self.is_ferrous = is_ferrous

    def __str__(self) -> str:
        ferrous_text = "Ferrous" if self.is_ferrous else "Non-ferrous"
        return f"{self.name} ({ferrous_text} metal, Density: {self.properties.density} kg/m³)"

class Plastic(Material): pass
class Ceramic(Material): pass

# database integration
def get_predefined_materials() -> dict:
    return {
        "1": Metal("Structural Steel", MaterialProperties(7850, 250, 200), is_ferrous=True),
        "2": Metal("6061-T6 Aluminum", MaterialProperties(2700, 270, 68.9), is_ferrous=False),
        "3": Plastic("PVC Plastic", MaterialProperties(1380, 45, 3)),
        "4": Ceramic("Standard Concrete", MaterialProperties(2400, 30, 30))
    }

# core stress strain calculations
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
        return (self.stress / self.strain) / 1000

    def will_fail(self) -> bool:
        return not self.material.can_withstand_stress(self.stress)

    @property
    def factor_of_safety(self) -> float:
        if self.stress <= 0:
            return float('inf')
        return self.material.properties.yield_strength / self.stress

    @property
    def safety_result(self) -> str:
        if self.factor_of_safety >= 1.0:
            return "SAFE (Design can handle the load)"
        return "WARNING - MATERIAL WILL FAIL!"

    def __str__(self) -> str:
        return (
            f"Test on {self.material.name}: "
            f"Stress={self.stress:.2f} MPa, "
            f"Strain={self.strain:.6f}, "
            f"Young's Modulus={self.youngs_modulus:.2f} GPa"
        )

# test analysis and session history
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
        print(f"Average Stress: {sum(stresses)/len(stresses):.2e} {UNITS[4]}")
        print(f"Average Strain: {sum(strains)/len(strains):.4f}")
        print(f"Average Young's Modulus: {sum(moduli)/len(moduli):.2e} {UNITS[4]}")
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
            print(f"Force: {test.force:.2f} {UNITS[0]}")
            print(f"Area: {test.area:.6f} {UNITS[1]}")
            print(f"Stress: {test.stress:.2e} {UNITS[4]}")
            print(f"Strain: {test.strain:.4f}")
            print(f"Factor of Safety: {test.factor_of_safety:.2f}")
            print(f"Safety Result: {test.safety_result}")

# utility funcs
def get_valid_number(prompt: str) -> float:
    while True:
        try:
            val = float(input(prompt))
            if val <= 0:
                print("Error: Input must be greater than zero! Try again.\n")
                continue
            return val
        except ValueError:
            print("Invalid input! Please enter a valid number.\n")
        except (KeyboardInterrupt, EOFError):
            print("\nProgram stopped. Goodbye!")
            sys.exit()

# main calc
def main():
    analyzer = TestAnalysisSystem()
    materials_db = get_predefined_materials()

    while True:
        print("\n" + "=" * 45)
        print("       STRESS AND STRAIN CALCULATOR")
        print("=" * 45)

        force = get_valid_number(f"Enter the applied force in {UNITS[0]}: ")
        area = get_valid_number(f"Enter the cross-sectional area in {UNITS[1]}: ")
        length = get_valid_number(f"Enter the original length in {UNITS[2]}: ")
        change = get_valid_number(f"Enter the change in length in {UNITS[3]}: ")

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

        # Process through OOP system
        test = StressStrainTest(selected_material, force, area, length, change)
        analyzer.add_test(test)

        print("\n" + "-" * 15 + " Results " + "-" * 15)
        print(f"Calculated Stress: {test.stress:.2e} {UNITS[4]}")
        print(f"Calculated Strain: {test.strain:.4f}")
        print(f"Young's Modulus: {test.youngs_modulus:.2e} {UNITS[4]}")
        print(f"Selected Material: {test.material.name}")
        print(f"Factor of Safety (FoS): {test.factor_of_safety:.2f}")
        print(f"Safety Status: {test.safety_result}")
        print("-" * 39)

        repeat = input("\nDo you want to calculate again? (yes/no): ").lower().strip()
        if repeat not in ["yes", "y"]:
            break

    # Display final summaries
    analyzer.display_calculation_history()
    analyzer.display_session_summary()
    print("\nThank you for using the Stress and Strain Calculator! Goodbye!")

if __name__ == "__main__":
    main()
