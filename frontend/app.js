const API_BASE = "http://localhost:8000";

function scoreLine(label, score) {
  return `<p><strong>${label}：</strong>${Number(score).toFixed(2)}</p>`;
}

function renderCards(profiles) {
  const container = document.getElementById("cards");
  container.innerHTML = profiles
    .map(
      (profile) => `
      <article class="card">
        <h3>${profile.employee.name}</h3>
        <p>${profile.employee.department} · ${profile.employee.title}</p>
        ${scoreLine("能力分", profile.capability_score)}
        ${scoreLine("绩效分", profile.performance_score)}
        ${scoreLine("稳定性", profile.stability_score)}
        <span class="tag">${profile.potential_label}</span>
      </article>
    `,
    )
    .join("");
}

async function init() {
  const resp = await fetch(`${API_BASE}/employees`);
  if (!resp.ok) {
    throw new Error("加载员工画像失败");
  }
  const data = await resp.json();
  renderCards(data);
}

init().catch((err) => {
  const container = document.getElementById("cards");
  container.innerHTML = `<p>加载失败：${err.message}</p>`;
});
