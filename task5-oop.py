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
