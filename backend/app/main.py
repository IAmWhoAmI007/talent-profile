from __future__ import annotations

from fastapi import FastAPI, HTTPException

from app.models.employee import Employee, SkillScores
from app.services.profiling import compute_profile

app = FastAPI(title="Talent Profile API", version="0.1.0")

EMPLOYEES: list[Employee] = [
    Employee(
        id=1,
        name="张三",
        department="研发中心",
        title="后端工程师",
        tenure_months=28,
        performance_scores=[88, 90, 86],
        activity_index=82,
        skills=SkillScores(technical=90, communication=75, learning=84),
    ),
    Employee(
        id=2,
        name="李四",
        department="产品部",
        title="产品经理",
        tenure_months=16,
        performance_scores=[80, 77, 83],
        activity_index=88,
        skills=SkillScores(technical=70, communication=89, learning=81),
    ),
    Employee(
        id=3,
        name="王五",
        department="市场部",
        title="运营专员",
        tenure_months=8,
        performance_scores=[68, 72, 70],
        activity_index=73,
        skills=SkillScores(technical=62, communication=74, learning=76),
    ),
]


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/employees")
def list_profiles() -> list[dict]:
    return [compute_profile(emp).model_dump() for emp in EMPLOYEES]


@app.get("/employees/{employee_id}")
def get_profile(employee_id: int) -> dict:
    for employee in EMPLOYEES:
        if employee.id == employee_id:
            return compute_profile(employee).model_dump()
    raise HTTPException(status_code=404, detail="Employee not found")
