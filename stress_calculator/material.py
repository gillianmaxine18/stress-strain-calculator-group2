# material.py
from dataclasses import dataclass
from typing import Optional
from .properties import MaterialProperties

class Material:
    """Base class for all materials."""
    
    def __init__(self, name: str, properties: MaterialProperties):
        self.name = name
        self.properties = properties

    def __str__(self) -> str:
        return f"{self.name} (Density: {self.properties.density} kg/m³)"

    def can_withstand_stress(self, stress: float) -> bool:
        """Check if the material can withstand the given stress."""
        return stress < self.properties.yield_strength

class Metal(Material):
    """A metal material subclass."""
    
    def __init__(self, name: str, properties: MaterialProperties, is_ferrous: bool = False):
        super().__init__(name, properties)
        self.is_ferrous = is_ferrous

    def __str__(self) -> str:
        ferrous_text = "Ferrous" if self.is_ferrous else "Non-ferrous"
        return f"{self.name} ({ferrous_text} metal, Density: {self.properties.density} kg/m³)"

class Plastic(Material):
    """A plastic material subclass."""

    def __init__(self, name: str, properties: MaterialProperties, polymer_type: str = "Thermoplastic"):
        super().__init__(name, properties)
        self.polymer_type = polymer_type
    def __str__(self) -> str:
        return f"{self.name} ({self.polymer_type} plastic, Density: {self.properties.density} kg/m³)"

class Composite(Material):
    """A composite material subclass."""

    def __init__(self, name: str, properties: MaterialProperties, reinforcement: str = "Carbon Fiber"):
        super().__init__(name, properties)
        self.reinforcement = reinforcement
        
    def __str__(self) -> str:
        return f"{self.name} (Composite [{self.reinforcement}], Density: {self.properties.density} kg/m³)"


class Ceramic(Material):
    """A ceramic material subclass."""

    pass
