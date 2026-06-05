const form = document.querySelector("#aleph-form");
const input = document.querySelector("#aleph-input");
const result = document.querySelector("#aleph-result");

function renderStatus(data) {
  result.hidden = false;

  if (!data.ok) {
    result.className = "result sealed";
    result.innerHTML = `
      <strong>Sealed</strong>
      <p>${data.message}</p>
    `;
    return;
  }

  if (data.mode === "public_aleph_olam") {
    result.className = "result public";
    result.innerHTML = `
      <strong>Public Aleph Olam Opened</strong>
      <p>${data.message}</p>
      <p>Granted: safe parsing, topology viewing, public diagnostics, and safe simulation.</p>
    `;
    return;
  }

  if (data.mode === "secret_aleph_olam") {
    result.className = "result secret";
    result.innerHTML = `
      <strong>Inner Authority Verified</strong>
      <p>${data.message}</p>
      <p>Da'at authority is available server-side. Protected values are not exposed to the browser.</p>
    `;
    return;
  }
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  result.hidden = false;
  result.className = "result";
  result.textContent = "Checking the gate...";

  try {
    const response = await fetch("/.netlify/functions/aleph-olam", {
      method: "POST",
      headers: {
        "content-type": "application/json",
      },
      body: JSON.stringify({
        phrase: input.value,
      }),
    });

    const data = await response.json();
    renderStatus(data);
  } catch (error) {
    result.className = "result sealed";
    result.innerHTML = `
      <strong>Function unavailable</strong>
      <p>The public page loaded, but the Netlify function is not responding yet.</p>
    `;
  }
});
