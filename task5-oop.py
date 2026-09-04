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
