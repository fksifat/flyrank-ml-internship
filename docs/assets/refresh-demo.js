const controls = Array.from(document.querySelectorAll("[data-control]"));
const demandValue = document.getElementById("demand-value");
const freshnessValue = document.getElementById("freshness-value");
const engagementValue = document.getElementById("engagement-value");
const positionValue = document.getElementById("position-value");
const scorePill = document.getElementById("score-pill");
const scoreText = document.getElementById("score-text");
const scoreDetail = document.getElementById("score-detail");

function computeScore(values) {
  const demand = values[0] / 100;
  const freshness = values[1] / 100;
  const decline = values[2] / 100;
  const position = values[3];

  const weighted =
    demand * 0.35 +
    (1 - freshness) * 0.25 +
    decline * 0.25 +
    ((11 - position) / 10) * 0.15;

  return Math.round(weighted * 100);
}

function describeScore(score) {
  if (score >= 80) {
    return {
      text: "High priority: this page is a strong refresh candidate right now.",
      detail:
        "The signal is strong because demand remains healthy while freshness and engagement are weakening.",
    };
  }
  if (score >= 60) {
    return {
      text: "Medium priority: this page still shows demand, but it needs a review soon.",
      detail:
        "The score blends demand, freshness, engagement decline, and search position into a transparent priority signal.",
    };
  }
  return {
    text: "Low priority: the page is not urgent yet, but it is worth watching.",
    detail:
      "The signal suggests that the page may be stable for now, though it could still drift over time.",
  };
}

function updateDemo() {
  const values = controls.map((input) => Number(input.value));
  const score = computeScore(values);
  const description = describeScore(score);

  demandValue.textContent = values[0];
  freshnessValue.textContent = values[1];
  engagementValue.textContent = values[2];
  positionValue.textContent = values[3];
  scorePill.textContent = score;
  scoreText.textContent = description.text;
  scoreDetail.textContent = description.detail;
}

controls.forEach((control) => control.addEventListener("input", updateDemo));
updateDemo();
