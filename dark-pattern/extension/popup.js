document.addEventListener("DOMContentLoaded", () => {
  const scanBtn    = document.getElementById("scanBtn");
  const clearBtn   = document.getElementById("clearBtn");
  const llmToggle  = document.getElementById("llmToggle");
  const statusEl   = document.getElementById("status");
  const summaryEl  = document.getElementById("summary");
  const resultsEl  = document.getElementById("results");
  const urlDisplay = document.getElementById("urlDisplay");
  const highCount  = document.getElementById("highCount");
  const medCount   = document.getElementById("medCount");
  const lowCount   = document.getElementById("lowCount");

  // Show current URL
  chrome.tabs.query({ active: true, currentWindow: true }, tabs => {
    if (tabs[0]) {
      const url = new URL(tabs[0].url);
      urlDisplay.textContent = url.hostname;
    }
  });

  // Scan button
  scanBtn.addEventListener("click", async () => {
    const useLLM = false;

    statusEl.className = "status scanning";
    statusEl.textContent = useLLM
      ? "🔍 Scanning with AI analysis... (may take 5–10 seconds)"
      : "🔍 Scanning page...";
    resultsEl.innerHTML = "";
    summaryEl.style.display = "none";
    scanBtn.disabled = true;

    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

    chrome.tabs.sendMessage(
      tab.id,
      { action: "analyze", useLLM },
      (response) => {
        scanBtn.disabled = false;

        if (!response || response.error) {
          statusEl.className = "status error";
          statusEl.textContent = response?.error
            || "❌ Could not connect to backend. Make sure Flask is running on port 5000.";
          return;
        }

        const { total, patterns, severity_counts, llm_used } = response;

        // Update status
        statusEl.className = "status";
        statusEl.textContent = total === 0
          ? "✅ No dark patterns detected on this page."
          : `⚠️ Found ${total} dark pattern${total > 1 ? "s" : ""}${llm_used ? " (AI-enhanced)" : ""}.`;

        // Update summary badges
        summaryEl.style.display = total > 0 ? "flex" : "none";
        highCount.textContent = severity_counts?.high  || 0;
        medCount.textContent  = severity_counts?.medium || 0;
        lowCount.textContent  = severity_counts?.low    || 0;

        // Render results
        if (total === 0) {
          resultsEl.innerHTML = `
            <div class="empty">
              <div class="icon">✅</div>
              <p>No known dark patterns detected on this page.</p>
            </div>`;
          return;
        }

        resultsEl.innerHTML = patterns.map(p => `
          <div class="pattern-item">
            <div class="pattern-header">
              <span class="pattern-name">
                ${p.name}
                <span class="source-badge">${p.source === "llm" ? "AI" : "rule"}</span>
              </span>
              <span class="sev-pill sev-${p.severity}">${p.severity.toUpperCase()}</span>
            </div>
            <div class="pattern-cat">${p.category}</div>
            <div class="pattern-exp">${p.explanation}</div>
            ${p.matched_on
              ? `<div class="pattern-match">Matched: "${p.matched_on.join('", "')}"</div>`
              : p.evidence
              ? `<div class="pattern-match">Evidence: "${p.evidence}"</div>`
              : ""}
          </div>
        `).join("");
      }
    );
  });

  // Clear button
  clearBtn.addEventListener("click", async () => {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    chrome.tabs.sendMessage(tab.id, { action: "clear" }, () => {
      resultsEl.innerHTML = "";
      summaryEl.style.display = "none";
      statusEl.className = "status";
      statusEl.textContent = 'Highlights cleared. Click "Scan This Page" to scan again.';
    });
  });
});