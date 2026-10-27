// Required for Manifest V3 — handles extension lifecycle
chrome.runtime.onInstalled.addListener(() => {
  console.log("Dark Pattern Detector installed.");
});