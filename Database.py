"""database.py"""
import json
import os
import csv

try:
    from properties import MaterialProperties
    from material import Material, Metal, Plastic, Ceramic
except ImportError:
    print("Warning: Missing material or properties modules.")

DB_FILE = "material_database.json"

def create_default_database():
    """Generates the default database based on the OOP specifications."""
    if not os.path.exists(DB_FILE):
        default_data = {
            "Structural Steel": {"category": "Metal", "density": 7850, "yield_strength": 250, "youngs_modulus": 200, "is_ferrous": True},
            "6061-T6 Aluminum": {"category": "Metal", "density": 2700, "yield_strength": 270, "youngs_modulus": 68.9, "is_ferrous": False},
            "PVC Plastic": {"category": "Plastic", "density": 1380, "yield_strength": 45, "youngs_modulus": 3},
            "Standard Concrete": {"category": "Ceramic", "density": 2400, "yield_strength": 30, "youngs_modulus": 30}
        }
        with open(DB_FILE, 'w') as file:
            json.dump(default_data, file, indent=4)

def load_materials() -> dict:
    """Loads JSON data and converts them back into OOP objects."""
    if not os.path.exists(DB_FILE):
        create_default_database()
        
    with open(DB_FILE, 'r') as file:
        data = json.load(file)
        
    materials_db = {}
    for i, (name, props) in enumerate(data.items(), 1):
        mat_props = MaterialProperties(props["density"], props["yield_strength"], props["youngs_modulus"])
        cat = props["category"]
        if cat == "Metal":
            materials_db[str(i)] = Metal(name, mat_props, props.get("is_ferrous", False))
        elif cat == "Plastic":
            materials_db[str(i)] = Plastic(name, mat_props)
        elif cat == "Ceramic":
            materials_db[str(i)] = Ceramic(name, mat_props)
        else:
            materials_db[str(i)] = Material(name, mat_props)
            
    return materials_db

def export_test_results_to_csv(tests_data, filename="test_history.csv"):
    """Exports a list of test dictionaries to a CSV file."""
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Material", "Stress", "Strain", "FoS", "Result"])
            for t in tests_data:
                writer.writerow([t['timestamp'], t['material'], t['stress'], t['strain'], t['fos'], t['result']])
        print(f"\n[Success] Test history exported to {filename}")
    except Exception as e:
        print(f"Error exporting to CSV: {e}")
