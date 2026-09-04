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
