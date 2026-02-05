from __future__ import annotations

from app.models.employee import Employee, EmployeeProfile


def _avg(nums: list[float]) -> float:
    if not nums:
        return 0.0
    return round(sum(nums) / len(nums), 2)


def compute_profile(employee: Employee) -> EmployeeProfile:
    capability_score = round(
        employee.skills.technical * 0.5
        + employee.skills.communication * 0.3
        + employee.skills.learning * 0.2,
        2,
    )

    performance_score = _avg(employee.performance_scores)

    tenure_component = min(employee.tenure_months / 36 * 100, 100)
    stability_score = round(tenure_component * 0.6 + employee.activity_index * 0.4, 2)

    if capability_score >= 85 and performance_score >= 85:
        potential_label = "高潜人才"
    elif capability_score >= 70 and performance_score >= 70:
        potential_label = "稳定骨干"
    else:
        potential_label = "待提升"

    summary = (
        f"{employee.name}（{employee.department}/{employee.title}）"
        f"能力分 {capability_score}，绩效分 {performance_score}，"
        f"稳定性 {stability_score}，当前标签：{potential_label}。"
    )

    return EmployeeProfile(
        employee=employee,
        capability_score=capability_score,
        performance_score=performance_score,
        stability_score=stability_score,
        potential_label=potential_label,
        summary=summary,
    )
