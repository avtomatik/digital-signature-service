const API_URL = "http://127.0.0.1:8000/api";

document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("sign-form");
  const result = document.getElementById("result");
  const status = document.getElementById("status");

  // Ping backend
  fetch(`${API_URL}/sign/ping`)
    .then((r) => r.json())
    .then((data) => {
      status.textContent = `Backend status: ${data.status}`;
    })
    .catch(() => {
      status.textContent = "Backend unreachable!";
    });

  // Submit document for signing
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const docId = document.getElementById("document_id").value;
    const payload = document.getElementById("payload").value;

    const response = await fetch(`${API_URL}/sign`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ document_id: docId, payload }),
    });

    const data = await response.json();
    result.textContent = JSON.stringify(data, null, 2);
  });
});
