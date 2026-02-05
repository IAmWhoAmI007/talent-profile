from __future__ import annotations

from pydantic import BaseModel, Field


class SkillScores(BaseModel):
    technical: float = Field(ge=0, le=100)
    communication: float = Field(ge=0, le=100)
    learning: float = Field(ge=0, le=100)


class Employee(BaseModel):
    id: int
    name: str
    department: str
    title: str
    tenure_months: int = Field(ge=0)
    performance_scores: list[float] = Field(default_factory=list)
    activity_index: float = Field(ge=0, le=100)
    skills: SkillScores


class EmployeeProfile(BaseModel):
    employee: Employee
    capability_score: float
    performance_score: float
    stability_score: float
    potential_label: str
    summary: str
