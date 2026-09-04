# Stress and Strain Analysis System

## Group Members
| Member | Primary Responsibility | GitHub Username | Task 6 Contribution |
| :--- | :--- | :--- | :--- |
| Hans Adrian Laudato | Task 1 – Basic Calculations | @hansadrianlaudato | Tested calculation modules |
| Gillian Maxine Estilloso | Task 2 – Control Structures  | @gillianmaxine18 | Integrated validation |
| Giana Elisha Tuplano | Task 3 – Data Structures | @gianaelishatuplano-jpg | Implemented CSV export |
| Kaycelyn Tigas | Task 4 – Functions| @kaycelyntigas | Refactored utility functions |
| Kate Robyn Alday | Task 5 – OOP | @katerobynalday | Integrated class architecture |

*Note: Task 6 – Modular Integration was completed collaboratively by all members.*

---

## Project Description
A Python-based engineering tool designed to calculate, analyze, and manage stress and strain test data for various materials. The application demonstrates the evolution of a simple script into a fully modular, object-oriented software system.

---

## Program Features
- **Calculations:** Stress, Strain, Young's Modulus, and Factor of Safety.
- **Input Validation:** Error handling for invalid inputs, zero-area prevention, and material limits.
- **Material Selection:** Predefined material properties and custom inputs.
- **Test Management:** Class-based structures to store test history and generate session summaries.
- **Data Persistence:** Save/load test records using JSON and export datasets via CSV.

---

## Repository Structure
stress_calculator/
│
├── material.py     # Material class hierarchy (Metal, Plastic, Composite)
├── properties.py   # Data-oriented material properties and dataclasses
├── tests.py        # StressStrainTest classes and test collection managers
├── utils.py        # Reusable math, validation, and conversion helpers
├── database.py     # Predefined materials and data persistence (JSON/CSV)
└── main.py         # Primary entry point coordinating application flow

---

## Requirements & How to Run

### Requirements
- Python 3.8 or higher

### How to Run
Run the application from the root directory:
```bash
python main.py==

