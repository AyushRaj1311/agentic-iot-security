async function loadData() {
  const res = await fetch("/api/status");
  const data = await res.json();

  document.getElementById("traffic").innerText =
    "📡 Traffic: " + data.traffic;

  document.getElementById("attacks").innerText =
    "🚨 Attacks: " + data.attacks;

  document.getElementById("blocked").innerText =
    "🚫 Blocked IPs: " + data.blocked_ips.length;
}

setInterval(loadData, 2000);
loadData();
let chart;

async function loadChart() {
  const res = await fetch("/api/attack-timeline");
  const data = await res.json();

  const labels = Object.keys(data);
  const values = Object.values(data);

  if (!chart) {
    const ctx = document.getElementById("attackChart").getContext("2d");
    chart = new Chart(ctx, {
      type: "line",
      data: {
        labels,
        datasets: [{
          label: "Attacks Over Time",
          data: values,
          borderColor: "red",
          tension: 0.4
        }]
      }
    });
  } else {
    chart.data.labels = labels;
    chart.data.datasets[0].data = values;
    chart.update();
  }
}

setInterval(loadChart, 4000);
let lastAttackCount = 0;

async function loadData() {
  const res = await fetch("/api/status");
  const data = await res.json();

  document.getElementById("traffic").innerText = "📡 Traffic: " + data.traffic;
  document.getElementById("attacks").innerText = "🚨 Attacks: " + data.attacks;
  document.getElementById("blocked").innerText = "🚫 Blocked IPs: " + data.blocked_ips.length;

  if (data.attacks > lastAttackCount) {
    document.getElementById("attacks").classList.add("alert");
  } else {
    document.getElementById("attacks").classList.remove("alert");
  }

  lastAttackCount = data.attacks;
}

setInterval(loadData, 2000);
