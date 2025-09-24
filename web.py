from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
 <!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>AgriSathi — Solution Summary</title>
<style>
  :root{
    --bg:#0f1724; --card:#0b1220; --muted:#9aa4b2; --accent:#7dd3fc; --glass: rgba(255,255,255,0.03);
  }
  html,body{height:100%;}
  body{
    margin:0;
    font-family:Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
    background: linear-gradient(180deg,#071028 0%, #071020 60%);
    color: #e6eef6;
    padding:20px;
    -webkit-font-smoothing:antialiased;
  }
  .container{max-width:1100px;margin:0 auto;}
  header{display:flex;gap:16px;align-items:center;margin-bottom:18px;}
  .logo{
    width:56px;height:56px;border-radius:10px;background:linear-gradient(135deg,var(--accent),#60a5fa);
    display:flex;align-items:center;justify-content:center;font-weight:700;color:#04263b;
    box-shadow: 0 6px 18px rgba(13,27,40,0.6);
  }
  h1{font-size:20px;margin:0;}
  p.lead{color:var(--muted);margin:6px 0 0;font-size:14px;}

  .grid{display:grid;grid-template-columns:1fr 340px; gap:18px;align-items:start;}
  @media (max-width:920px){ .grid{grid-template-columns:1fr;} }

  .card{
    background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
    border-radius:12px;padding:16px;border:1px solid rgba(255,255,255,0.03);
    box-shadow: 0 8px 30px rgba(2,6,23,0.6);
  }
  .section-title{display:flex;align-items:center;justify-content:space-between;gap:12px;}
  .section-title h2{font-size:16px;margin:0;}
  .muted{color:var(--muted);font-size:13px;margin-top:6px;}
  ul.features{margin:12px 0 0 18px;color:#dff5ff;}
  ul.features li{margin:8px 0;line-height:1.4;}

  .pill{display:inline-block;padding:6px 10px;border-radius:999px;background:var(--glass);color:var(--muted);font-size:13px;border:1px solid rgba(255,255,255,0.02);}

  .controls{display:flex;gap:8px;align-items:center;}
  button.btn{
    background:linear-gradient(90deg,#0369a1,#7dd3fc);border:none;color:#002233;padding:8px 12px;border-radius:8px;font-weight:600;cursor:pointer;
    box-shadow: 0 6px 18px rgba(13,27,40,0.6);
  }
  button.ghost{background:transparent;border:1px solid rgba(255,255,255,0.04);color:var(--muted);padding:8px 10px;border-radius:8px;cursor:pointer;}
  .small{font-size:13px;padding:6px 10px;border-radius:8px;}

  /* collapsible */
  .collapsible{margin-top:12px;border-radius:10px;overflow:hidden;border:1px solid rgba(255,255,255,0.02);}
  .collapsible summary{list-style:none;padding:12px 16px;cursor:pointer;display:flex;align-items:center;justify-content:space-between;background:linear-gradient(180deg, rgba(255,255,255,0.01), transparent);}
  .collapsible[open] summary{background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));}
  .collapsible p{padding:12px 16px 18px;margin:0;color:#e2f7ff;}
  .note{background:rgba(125,211,252,0.06);border-left:3px solid rgba(125,211,252,0.18);padding:10px;margin-top:10px;color:#c9f1ff;border-radius:6px;}

  /* right column */
  .toc h3{margin:6px 0 8px;}
  .toc ul{padding-left:14px;color:var(--muted);}
  .toc li{margin:8px 0;}
  .kpi{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-top:10px;}
  .kpi .k{background:rgba(255,255,255,0.02);padding:10px;border-radius:8px;text-align:center;}
  .k .v{font-weight:700;font-size:18px;color:#bff0ff;}
  footer{margin-top:18px;color:var(--muted);font-size:13px;}
  .center{display:flex;gap:8px;align-items:center;justify-content:center;}
</style>
</head>
<body>
  <div class="container">
    <header>
      <div class="logo">AS</div>
      <div>
        <h1>AgriSathi — Multilingual AI Advisory for Small & Marginal Farmers</h1>
        <p class="lead">A compact solution summary: what it does, how it works, and the expected impact.</p>
      </div>
      <div style="margin-left:auto" class="controls">
        <button class="btn" id="speakAll">🔊 Listen to page</button>
        <button class="ghost" id="printBtn">🖨 Print</button>
      </div>
    </header>

    <div class="grid">
      <!-- Main content -->
      <main>
        <section class="card">
          <div class="section-title">
            <h2>Proposed Solution</h2>
            <span class="pill">Multilingual · Voice · Offline-first</span>
          </div>
          <p class="muted">A mobile + web advisory platform delivering localized, actionable recommendations (soil, weather, pests, market prices) to small & marginal farmers.</p>

          <details class="collapsible" open>
            <summary>
              <strong>Key features</strong>
              <span class="muted">click to expand/collapse</span>
            </summary>
            <div style="padding:12px 16px 18px;">
              <ul class="features">
                <li><strong>Soil & fertilizer advice</strong> — upload soil reports or enter simple readings; get crop-specific dosing.</li>
                <li><strong>Weather & micro-advisories</strong> — local forecasts with actionable advisories (sowing, irrigation, spray windows).</li>
                <li><strong>Image-based pest/disease detection</strong> — upload photos, receive likely diagnosis + low-toxicity treatment steps.</li>
                <li><strong>Market & price tracker</strong> — mandi prices, sell-location suggestions, simple profit calculator.</li>
                <li><strong>Voice + IVR / USSD fallback</strong> — designed for low-literacy and non-smartphone users.</li>
                <li><strong>Feedback loop</strong> — farmer feedback improves recommendations over time; human escalation to agronomists for complex cases.</li>
              </ul>
              <div class="note">Prototype-first approach: rule-based advisories initially, add ML models after pilot data collection.</div>
            </div>
          </details>
        </section>

        <section class="card" style="margin-top:14px;">
          <div class="section-title">
            <h2>Technical Approach</h2>
            <span class="pill">Simple, scalable stack</span>
          </div>
          <p class="muted">Design decisions to keep the system lightweight, maintainable and regionally deployable.</p>

          <details class="collapsible" >
            <summary><strong>Architecture & components</strong><span class="muted"> (overview)</span></summary>
            <p>
              <strong>Frontend:</strong> React Native (mobile) + PWA for web. Large icons, audio playback for advisories.<br>
              <strong>Backend:</strong> Python (Flask/Django) or Node.js (Express), microservices for model inference, rule engine, and data APIs.<br>
              <strong>Data:</strong> PostgreSQL for structured data, object store for images, message queue for async tasks.<br>
              <strong>AI/ML:</strong> TensorFlow/PyTorch for pest/disease image models, small transformer or retrieval-based NLP for multilingual chat.<br>
              <strong>Integrations:</strong> IMD/OpenWeather for weather, Agmarknet for mandi prices, local labs/KVKs for ground-truth.
            </p>
          </details>

        </section>

        <section class="card" style="margin-top:14px;">
          <div class="section-title">
            <h2>Feasibility & Viability</h2>
            <span class="pill">Pilot-first, low risk</span>
          </div>
          <p class="muted">Why this solution can be implemented and sustained.</p>

          <details class="collapsible" >
            <summary><strong>Feasibility points</strong></summary>
            <p>
              • Start with rule-based agronomy (low ML dependency) and voice/IVR for adoption.<br>
              • Pilot in 1–2 districts and 2 crops to validate impact before scaling.<br>
              • Offline caching & low-bandwidth sync to handle poor connectivity.<br>
              • Partnership with KVKs, state agri departments, and NGOs for trust-building.
            </p>
          </details>

          <details class="collapsible" style="margin-top:8px;">
            <summary><strong>Revenue & sustainability</strong></summary>
            <p>
              • Initial funding via grants / CSR / government schemes.<br>
              • Long-term: B2B analytics, subscription for premium services (market links, lab integration), transaction fees from marketplace.
            </p>
          </details>
        </section>

        <section class="card" style="margin-top:14px;">
          <div class="section-title">
            <h2>Impact & Benefits</h2>
            <span class="pill"> measurable targets</span>
          </div>

          <details class="collapsible" open>
            <summary><strong>Expected outcomes</strong></summary>
            <p>
              • <strong>Yield uplift:</strong> target 15–30% for adopters (pilot estimate).<br>
              • <strong>Cost reduction:</strong> reduced excess fertilizer/pesticide use (15–25%).<br>
              • <strong>Inclusion:</strong> voice + USSD increases reach among low-literacy farmers.<br>
              • <strong>Sustainability:</strong> better soil health and reduced chemical overuse.
            </p>
          </details>

          <div style="margin-top:12px" class="center">
            <button class="btn" onclick="downloadOnePager()">Download One-Page Summary</button>
            <button class="ghost small" onclick="highlight('proposal')">Highlight Key Points</button>
          </div>
        </section>

        <footer class="card" style="margin-top:14px;">
          <strong>Next steps (pilot)</strong>
          <ul style="margin:8px 0 0 18px;color:#dff5ff">
            <li>Select 1–2 districts and 2 priority crops</li>
            <li>Partner with 1 KVK / NGO and run farmer co-design workshops</li>
            <li>Build MVP (mobile + IVR) and recruit ~500 farmers for pilot</li>
            <li>Collect baseline, run pilot 3–6 months, measure KPIs and iterate</li>
          </ul>
        </footer>
      </main>

      <!-- Right column -->
      <aside>
        <div class="card toc">
          <h3>At a glance</h3>
          <p class="muted">Quick navigation & KPIs</p>
          <ul>
            <li>Target users: Small & marginal farmers</li>
            <li>Channels: App, PWA, IVR, USSD</li>
            <li>Core tech: Rule engine + ML (image models)</li>
            <li>Pilot size: 500–1000 farmers</li>
          </ul>

          <h3 style="margin-top:12px">KPIs</h3>
          <div class="kpi">
            <div class="k"><div class="v">15–30%</div><div class="muted">Yield uplift</div></div>
            <div class="k"><div class="v">15–25%</div><div class="muted">Input cost ↓</div></div>
            <div class="k"><div class="v">70%</div><div class="muted">Retention (pilot)</div></div>
          </div>

          <h3 style="margin-top:12px">Stakeholders</h3>
          <ul style="color:var(--muted)">
            <li>Farmers (women & marginalized groups prioritized)</li>
            <li>State Agri Dept & KVKs</li>
            <li>NGOs, agritech startups, input retailers</li>
          </ul>

          <div style="margin-top:14px" class="center">
            <button class="btn small" onclick="speakSection('proposed')">🔊 Speak 'Proposed'</button>
            <button class="ghost small" onclick="speakSection('impact')">🔊 Speak 'Impact'</button>
          </div>
        </div>

        <div class="card" style="margin-top:12px;">
          <h3>Quick resources</h3>
          <p class="muted">Suggested integrations & data sources</p>
          <ul style="color:#dff5ff">
            <li>IMD / OpenWeather for forecasts</li>
            <li>Agmarknet for mandi prices</li>
            <li>ICAR / State agri universities for fertilizer tables</li>
          </ul>
        </div>

      </aside>
    </div>

    <footer style="margin-top:20px;text-align:center;color:var(--muted);font-size:13px;">
      Built for demonstration • Save this page or print for offline sharing
    </footer>
  </div>

<script>
/* Simple text-to-speech utility for sections */
function speak(text){
  if(!('speechSynthesis' in window)){ alert('TTS not supported by your browser'); return; }
  const ut = new SpeechSynthesisUtterance(text);
  ut.lang = 'en-IN';
  ut.rate = 0.95;
  window.speechSynthesis.cancel();
  window.speechSynthesis.speak(ut);
}

/* Read the whole page */
document.getElementById('speakAll').addEventListener('click', ()=>{
  const nodes = [
    "Agri Sathi. Multilingual AI Advisory for small and marginal farmers.",
    "Proposed Solution. A mobile and web advisory platform providing soil and fertilizer advice, weather advisories, pest detection, market price tracking and voice plus IVR support.",
    "Technical Approach. Frontend with React Native and PWA. Backend with Python or Node.js. AI models for image-based pest detection. Integrations with IMD and Agmarknet.",
    "Feasibility. Start pilot with rule-based engine, offline-first design, partnerships with KVKs and NGOs.",
    "Impact. Expected yield uplift of fifteen to thirty percent and reduction in input costs by fifteen to twenty five percent."
  ];
  speak(nodes.join(' '));
});

/* Speak specific named sections */
function speakSection(name){
  if(name==='proposed'){
    speak("Proposed Solution. The system delivers personalized soil and crop advice, weather based micro advisories, image based pest detection and voice support for low literacy users.");
  } else if(name==='impact'){
    speak("Impact and Benefits. Targeted yield uplift of fifteen to thirty percent and reduced input costs, increased inclusion, and improved soil health.");
  }
}

/* Print */
document.getElementById('printBtn').addEventListener('click', ()=> window.print());

/* Download one-pager as text file */
function downloadOnePager(){
  const title = "AgriSathi One-Page Summary";
  const text = [
    "AgriSathi — Multilingual AI Advisory for Small & Marginal Farmers",
    "",
    "Proposed Solution:",
    "- Soil & fertilizer advice, weather micro-advisories, image-based pest detection, market prices, voice & IVR fallback.",
    "",
    "Technical Approach:",
    "- Frontend: React Native + PWA. Backend: Python/Node microservices. AI: TensorFlow/PyTorch for image models.",
    "",
    "Feasibility & Next Steps:",
    "- Pilot in 1-2 districts, partner with KVKs/NGOs, recruit ~500 farmers.",
    "",
    "Expected Impact:",
    "- Yield uplift 15-30%, input cost reduction 15-25%."
  ].join("\\n");
  const blob = new Blob([text], {type:'text/plain'});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a'); a.href = url; a.download = 'agrisathi_onepager.txt';
  document.body.appendChild(a); a.click(); a.remove();
  URL.revokeObjectURL(url);
}

/* small highlight helper (demonstration) */
function highlight(which){
  alert("Highlight function called: " + which + ". Use this to emphasize core points when presenting.");
}
</script>
</body>
</html>
"""

class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())

server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()