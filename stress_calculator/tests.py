# tests.py
from typing import List
from .material import Material, Metal, Plastic, Composite
from .properties import MaterialProperties
from .database import get_predefined_materials
from .utils import calculate_stress, calculate_strain
from . import utils

UNITS = ("N", "m²", "m", "m", "Pa")


class StressStrainTest:

    def __init__(
        self,
        material: Material,
        force: float,
        area: float,
        original_length: float,
        change_in_length: float,
    ):
        utils.validate_input(force, area, original_length, change_in_length)

        self.material = material
        self._force = force
        self._area = area
        self._original_length = original_length
        self._change_in_length = change_in_length

    @property
    def stress(self) -> float:
        return utils.calculate_stress(self._force, self._area)

    @property
    def strain(self) -> float:
        return utils.calculate_strain(
            self._original_length, self._change_in_length
        )

    @property
    def youngs_modulus(self) -> float:
        if self.strain == 0:
            return 0
        raw_modulus = utils.calculate_youngs_modulus(self.stress, self.strain)
        return raw_modulus / 1e9

    def will_fail(self) -> bool:
        return not self.material.can_withstand_stress(self.stress)
    
    @property
    def factor_of_safety(self) -> float:
        if self.stress <= 0:
            return float("inf")
        return utils.calculate_factor_of_safety(self.material.properties.yield_strength * 1_000_000, self.stress)

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


class TestAnalysisSystem:

    def __init__(self):
        self.tests: List[StressStrainTest] = []
        self.materials_used = set()

    def add_test(self, test: StressStrainTest):
        self.tests.append(test)
        self.materials_used.add(test.material.name)

    def get_export_data(self) -> list:
        """Helper to structure test history for database CSV export."""
        return [
            {
                "material": test.material.name,
                "stress": test.stress,
                "strain": test.strain,
                "factor_of_safety": test.factor_of_safety,
                "safety_result": test.safety_result,
            }
            for test in self.tests
        ]

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
        print(
            f"Average Stress: {sum(stresses)/len(stresses):.2e} {UNITS[4]}"
        )
        print(f"Average Strain: {sum(strains)/len(strains):.4f}")
        print(
            f"Average Young's Modulus: {sum(moduli)/len(moduli):.2e} {UNITS[4]}"
        )
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
            print(f"Force: {test._force:.2f} {UNITS[0]}")
            print(f"Area: {test._area:.6f} {UNITS[1]}")
            print(f"Stress: {test.stress:.2e} {UNITS[4]}")
            print(f"Strain: {test.strain:.4f}")
            print(f"Factor of Safety: {test.factor_of_safety:.2f}")
            print(f"Safety Result: {test.safety_result}")
