# Calculator GUI — Development Notes

## Project Overview

A desktop calculator built using Python and CustomTkinter.

The goal is to create a functional calculator with a modern interface while learning GUI development, event handling, application structure, and testing.

## Technology Stack

- **Python** — Application logic
- **CustomTkinter** — Graphical interface
- **pytest** — Automated testing
- **Git / GitHub** — Version control

## Development Approach

Development will begin with the graphical interface before implementing the calculation logic.

The interface and calculation logic will be kept in separate modules to make the application easier to maintain and test.

### 1. Graphical Interface

**First development priority.**

- Create the main application window.
- Apply a modern dark theme.
- Create a display for user input and results.
- Arrange calculator buttons in a four-column grid.
- Use different colors for number, operator, and action buttons.
- Add appropriate spacing, button sizes, and rounded corners.

The initial interface does not need to perform calculations.

### 2. Calculator Logic

Once the interface is established, implement:

- Number input and decimal handling
- Addition, subtraction, multiplication, and division
- Clear and backspace functionality
- Positive/negative toggle
- Percentage calculations
- Error handling, including division by zero

### 3. Connecting the Interface

Connect the buttons to the calculation logic using callbacks.

Update the calculator display based on user input and calculation results.

### 4. Additional Functionality

After the basic calculator works:

- Add keyboard input support.
- Improve input handling and edge cases.
- Refine the interface based on testing.

### 5. Testing and Documentation

- Write automated tests for calculation logic using pytest.
- Test the graphical interface manually.
- Document important implementation decisions as development progresses.
- Update the README with instructions and screenshots when the application is functional.

## Project Structure

| File | Responsibility |
|---|---|
| `main.py` | Application entry point |
| `calculator/app.py` | Main application window and configuration |
| `calculator/ui.py` | Calculator layout and visual components |
| `calculator/logic.py` | Calculator operations and state |
| `tests/test_logic.py` | Automated tests |
| `docs/development.md` | Development notes and decisions |

## Development Notes

This document will be updated as the project progresses. Planned features and implementation details may change during development.