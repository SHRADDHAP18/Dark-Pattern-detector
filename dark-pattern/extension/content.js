// Extracts page text and sends to backend
async function analyzeCurrentPage(useLLM = false) {
  const pageText = document.body.innerText;
  const pageUrl  = window.location.href;

  try {
    const response = await fetch("http://127.0.0.1:5000/analyze", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: pageText, url: pageUrl, use_llm: useLLM })
    });
    return await response.json();
  } catch (err) {
    console.error("Dark Pattern Detector: API error", err);
    return { error: "Backend not reachable. Is Flask running?" };
  }
}

// Highlight suspicious text on the page
function highlightPatterns(patterns) {
  // Remove existing highlights first
  document.querySelectorAll(".dpd-highlight").forEach(el => {
    el.classList.remove("dpd-highlight", "dpd-high", "dpd-medium", "dpd-low");
  });

  patterns.forEach(pattern => {
    if (!pattern.matched_on) return;

    pattern.matched_on.forEach(keyword => {
      // Walk all text nodes and wrap matches
      const walker = document.createTreeWalker(
        document.body,
        NodeFilter.SHOW_TEXT,
        null
      );

      let node;
      while ((node = walker.nextNode())) {
        const text = node.textContent.toLowerCase();
        if (text.includes(keyword.toLowerCase()) && node.parentElement) {
          const parent = node.parentElement;
          if (!parent.classList.contains("dpd-highlight")) {
            parent.classList.add("dpd-highlight", `dpd-${pattern.severity}`);
            parent.title = `⚠️ Dark Pattern: ${pattern.name}\n${pattern.explanation}`;
          }
        }
      }
    });
  });
}

// Listen for messages from popup
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "analyze") {
    analyzeCurrentPage(request.useLLM).then(result => {
      if (result.patterns) highlightPatterns(result.patterns);
      sendResponse(result);
    });
    return true; // Keep async channel open
  }

  if (request.action === "clear") {
    document.querySelectorAll(".dpd-highlight").forEach(el => {
      el.classList.remove("dpd-highlight", "dpd-high", "dpd-medium", "dpd-low");
    });
    sendResponse({ cleared: true });
    return true;
  }
});