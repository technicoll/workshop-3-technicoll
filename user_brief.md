# User Brief — Hotdog Upsell Predictor

## Project Title
**Upsell Like an Engineer**

## Background
Busy food outlets often want to know whether to offer customers a drink with their order.  
This workshop reframes that simple logic as an engineering exercise to teach:
- Test-Driven Development  
- Refactoring and readability  
- Safe logging with MLflow  

The exercise demonstrates how small, clear tests and defensive coding habits reduce risk in AI projects.

## Objectives
- Implement a minimal decision logic function (`will_buy_drink`) using **TDD**.  
- Record experiments using **MLflow**.  
- Refactor safely using tests as a safety net.  
- Extend logic through a **policy override** in the Curveball task.

## Deliverables
1. Completed master notebook (`Workshop3W_Master.ipynb`)  
2. Source module (`src/hotdog/rules.py`)  
3. Test suite (`tests/test_rules.py`)  
4. Logged experiment (`./mlruns/`)  
5. Optional Curveball extension with policy flag.

## Success Criteria
- All tests pass locally (`pytest`).  
- Code follows refactor rules (readable, modular, documented).  
- MLflow logging runs without error or fails gracefully.  
- Learner can explain each rule and its precedence.

## Timeframe
- **Main Workshop:** 1 day (6 hours)  
- **Curveball Extension:** 45–60 minutes  
