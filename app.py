import streamlit as st

st.set_page_config(
    page_title="치카치카 타이머 🦷",
    page_icon="🦷",
    layout="centered",
)

# --- CSS ---
st.markdown(
    """
<style>
    .stApp { background: linear-gradient(135deg, #e0f7fa 0%, #f3e5f5 100%); }
    div[data-testid="stMainBlockContainer"] { max-width: 500px; }
    h1 { text-align: center; }
    .setup-card {
        background: white; border-radius: 20px; padding: 30px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08); margin: 10px 0;
    }
</style>
""",
    unsafe_allow_html=True,
)

st.markdown("# 🦷 치카치카 타이머")
st.markdown(
    "<p style='text-align:center;color:#666;'>양치 시간을 재미있게 관리하세요!</p>",
    unsafe_allow_html=True,
)

# --- Setup UI ---
st.markdown('<div class="setup-card">', unsafe_allow_html=True)

user_name = st.text_input("🧒 양치하는 사람 이름", placeholder="이름을 입력하세요")

TIME_OPTIONS = {
    "1분": 60,
    "1분 30초": 90,
    "2분": 120,
    "2분 30초": 150,
    "3분": 180,
}
selected_label = st.select_slider("⏱️ 양치 시간 선택", options=list(TIME_OPTIONS.keys()), value="2분")
selected_seconds = TIME_OPTIONS[selected_label]

st.markdown("</div>", unsafe_allow_html=True)

start = st.button("🚀 양치 시작!", use_container_width=True, type="primary")

if start:
    name = user_name.strip() or "친구"

    # ---------- inline the whole timer as one HTML component ----------
    import streamlit.components.v1 as components

    html = f"""
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{
  font-family: 'Segoe UI', sans-serif;
  background: linear-gradient(135deg,#e0f7fa,#f3e5f5);
  display:flex; justify-content:center; align-items:center;
  min-height:100vh; overflow:hidden;
}}
.container {{
  text-align:center; width:100%; max-width:420px; padding:20px;
}}

/* ---------- circular timer ---------- */
.timer-ring {{ position:relative; width:260px; height:260px; margin:0 auto 18px; }}
.timer-ring svg {{ width:100%; height:100%; transform:rotate(-90deg); }}
.timer-ring .bg  {{ fill:none; stroke:#e0e0e0; stroke-width:12; }}
.timer-ring .fg  {{ fill:none; stroke:url(#grad); stroke-width:12;
  stroke-linecap:round; transition:stroke-dashoffset .4s ease; }}
.timer-text {{
  position:absolute; top:50%; left:50%; transform:translate(-50%,-50%);
  font-size:52px; font-weight:700; color:#333;
}}

/* ---------- stage badge ---------- */
.stage {{
  font-size:22px; min-height:70px;
  margin:8px 0; transition:all .3s ease;
}}
.stage .emoji {{ font-size:48px; animation:bounce .6s ease; }}
@keyframes bounce {{
  0%,100% {{ transform:translateY(0); }}
  50% {{ transform:translateY(-12px); }}
}}

/* ---------- buttons ---------- */
.btn-row {{ display:flex; gap:8px; justify-content:center; flex-wrap:wrap; margin:10px 0; }}
.btn {{
  padding:10px 18px; border:none; border-radius:12px;
  font-size:15px; font-weight:600; cursor:pointer;
  transition:transform .15s,box-shadow .15s;
}}
.btn:active {{ transform:scale(.95); }}
.btn-add {{ background:#e3f2fd; color:#1565c0; }}
.btn-pause {{ background:#fff3e0; color:#ef6c00; }}
.btn-reset {{ background:#fce4ec; color:#c62828; }}

/* ---------- celebration ---------- */
.celebration {{
  display:none; flex-direction:column; align-items:center; gap:14px;
  animation:fadeIn .5s ease;
}}
@keyframes fadeIn {{ from{{opacity:0;transform:scale(.8)}} to{{opacity:1;transform:scale(1)}} }}
.celebration h2 {{ font-size:28px; color:#333; }}
.celebration .big-emoji {{ font-size:80px; animation:bounce 1s ease infinite; }}

/* confetti */
.confetti-piece {{
  position:fixed; width:10px; height:10px; border-radius:2px;
  animation:confettiFall linear forwards;
}}
@keyframes confettiFall {{
  0%   {{ opacity:1; transform:translateY(-10vh) rotate(0deg); }}
  100% {{ opacity:0; transform:translateY(110vh) rotate(720deg); }}
}}

/* sound toggle */
.sound-toggle {{
  position:absolute; top:10px; right:10px;
  background:none; border:none; font-size:24px; cursor:pointer;
}}
</style>
</head>
<body>
<div class="container" id="app">

  <!-- Sound toggle -->
  <button class="sound-toggle" onclick="toggleSound()" id="soundBtn">🔊</button>

  <!-- Timer screen -->
  <div id="timerScreen">
    <div style="font-size:20px;margin-bottom:6px;">
      <strong>{name}</strong>의 양치 타임!
    </div>

    <div class="timer-ring">
      <svg viewBox="0 0 200 200">
        <defs>
          <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" style="stop-color:#42a5f5"/>
            <stop offset="100%" style="stop-color:#ab47bc"/>
          </linearGradient>
        </defs>
        <circle class="bg" cx="100" cy="100" r="88"/>
        <circle class="fg" id="ring" cx="100" cy="100" r="88"
          stroke-dasharray="553" stroke-dashoffset="0"/>
      </svg>
      <div class="timer-text" id="timeDisplay">0:00</div>
    </div>

    <div class="stage" id="stageArea"></div>

    <div class="btn-row">
      <button class="btn btn-add" onclick="addTime(10)">+10초</button>
      <button class="btn btn-add" onclick="addTime(30)">+30초</button>
      <button class="btn btn-pause" id="pauseBtn" onclick="togglePause()">⏸️ 일시정지</button>
      <button class="btn btn-reset" onclick="resetTimer()">🔄 초기화</button>
    </div>
  </div>

  <!-- Celebration screen -->
  <div class="celebration" id="celebScreen">
    <div class="big-emoji">🎉</div>
    <h2 id="celebMsg"></h2>
    <p id="celebSub" style="color:#666;font-size:16px;"></p>
    <button class="btn btn-add" style="margin-top:10px;font-size:17px;padding:12px 30px;"
      onclick="restart()">🔄 다시 하기</button>
  </div>
</div>

<script>
// ========== CONFIG ==========
const TOTAL = {selected_seconds};
const NAME  = "{name}";
let remaining = TOTAL;
let paused = false;
let finished = false;
let interval = null;
let soundOn = true;

const CIRC = 2 * Math.PI * 88;          // stroke-dasharray
const ring = document.getElementById('ring');
const display = document.getElementById('timeDisplay');
const stageArea = document.getElementById('stageArea');

// ========== STAGES ==========
const STAGES = [
  {{ pct:1.00, emoji:'🦷', msg: NAME+'! 양치 시작이다~ 구석구석 닦자!' }},
  {{ pct:0.75, emoji:'💪', msg: '좋아! 힘차게 닦는 중!' }},
  {{ pct:0.50, emoji:'🌟', msg: '절반 지났어! '+NAME+' 최고!' }},
  {{ pct:0.30, emoji:'🔥', msg: '거의 다 왔어! 파이팅!' }},
  {{ pct:0.15, emoji:'🏆', msg: '마지막 스퍼트! 조금만 더!' }},
];
let lastStageIdx = -1;

function getStage(pct) {{
  for (let i = STAGES.length - 1; i >= 0; i--) {{
    if (pct <= STAGES[i].pct) return i;
  }}
  return 0;
}}

// ========== AUDIO (Web Audio API) ==========
let audioCtx = null;
function ensureAudio() {{
  if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
}}

function playTick() {{
  if (!soundOn) return;
  ensureAudio();
  const o = audioCtx.createOscillator();
  const g = audioCtx.createGain();
  o.type = 'sine'; o.frequency.value = 880;
  g.gain.setValueAtTime(0.08, audioCtx.currentTime);
  g.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.08);
  o.connect(g); g.connect(audioCtx.destination);
  o.start(); o.stop(audioCtx.currentTime + 0.08);
}}

function playStageUp() {{
  if (!soundOn) return;
  ensureAudio();
  [523, 659, 784].forEach((f, i) => {{
    const o = audioCtx.createOscillator();
    const g = audioCtx.createGain();
    o.type = 'triangle'; o.frequency.value = f;
    g.gain.setValueAtTime(0.15, audioCtx.currentTime + i * 0.12);
    g.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + i * 0.12 + 0.25);
    o.connect(g); g.connect(audioCtx.destination);
    o.start(audioCtx.currentTime + i * 0.12);
    o.stop(audioCtx.currentTime + i * 0.12 + 0.25);
  }});
}}

function playCelebration() {{
  if (!soundOn) return;
  ensureAudio();
  const notes = [523,587,659,698,784,880,988,1047];
  notes.forEach((f, i) => {{
    const o = audioCtx.createOscillator();
    const g = audioCtx.createGain();
    o.type = 'square';
    o.frequency.value = f;
    g.gain.setValueAtTime(0.10, audioCtx.currentTime + i*0.1);
    g.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + i*0.1 + 0.35);
    o.connect(g); g.connect(audioCtx.destination);
    o.start(audioCtx.currentTime + i*0.1);
    o.stop(audioCtx.currentTime + i*0.1 + 0.35);
  }});
}}

// BGM - simple looping arpeggio
let bgmInterval = null;
let bgmNoteIdx = 0;
const BGM_NOTES = [262,330,392,523,392,330];
function startBgm() {{
  if (bgmInterval) return;
  bgmNoteIdx = 0;
  bgmInterval = setInterval(() => {{
    if (!soundOn || paused) return;
    ensureAudio();
    const o = audioCtx.createOscillator();
    const g = audioCtx.createGain();
    o.type = 'sine';
    o.frequency.value = BGM_NOTES[bgmNoteIdx % BGM_NOTES.length];
    g.gain.setValueAtTime(0.04, audioCtx.currentTime);
    g.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.3);
    o.connect(g); g.connect(audioCtx.destination);
    o.start(); o.stop(audioCtx.currentTime + 0.3);
    bgmNoteIdx++;
  }}, 400);
}}
function stopBgm() {{
  clearInterval(bgmInterval);
  bgmInterval = null;
}}

function toggleSound() {{
  soundOn = !soundOn;
  document.getElementById('soundBtn').textContent = soundOn ? '🔊' : '🔇';
  if (!soundOn) stopBgm(); else if (!finished && !paused) startBgm();
}}

// ========== RENDER ==========
function render() {{
  const pct = remaining / TOTAL;
  const offset = CIRC * (1 - pct);
  ring.style.strokeDashoffset = offset;

  const m = Math.floor(remaining / 60);
  const s = remaining % 60;
  display.textContent = m + ':' + String(s).padStart(2,'0');

  const idx = getStage(pct);
  if (idx !== lastStageIdx) {{
    lastStageIdx = idx;
    const st = STAGES[idx];
    stageArea.innerHTML = '<div class="emoji">' + st.emoji + '</div><div>' + st.msg + '</div>';
    if (idx > 0) playStageUp();
  }}
}}

// ========== CONFETTI ==========
function spawnConfetti() {{
  const colors = ['#f44336','#e91e63','#9c27b0','#2196f3','#4caf50','#ff9800','#ffeb3b'];
  for (let i = 0; i < 60; i++) {{
    const el = document.createElement('div');
    el.className = 'confetti-piece';
    el.style.left = Math.random()*100 + 'vw';
    el.style.background = colors[Math.floor(Math.random()*colors.length)];
    el.style.animationDuration = (2 + Math.random()*2) + 's';
    el.style.animationDelay = Math.random()*0.5 + 's';
    document.body.appendChild(el);
    setTimeout(() => el.remove(), 4500);
  }}
}}

// ========== TIMER LOGIC ==========
function tick() {{
  if (paused || finished) return;
  remaining--;
  if (remaining % 5 === 0) playTick();
  render();
  if (remaining <= 0) {{
    finish();
  }}
}}

function finish() {{
  finished = true;
  clearInterval(interval);
  stopBgm();
  playCelebration();
  spawnConfetti();
  document.getElementById('timerScreen').style.display = 'none';
  const cel = document.getElementById('celebScreen');
  cel.style.display = 'flex';

  const msgs = [
    NAME + '! 양치 완료! 반짝반짝 깨끗한 이! ✨',
    '대단해 ' + NAME + '! 충치 걱정 없는 하루! 🦷💎',
    NAME + '의 이가 보석처럼 빛나요! 💎🌟',
  ];
  document.getElementById('celebMsg').textContent = msgs[Math.floor(Math.random()*msgs.length)];
  document.getElementById('celebSub').textContent = '오늘도 양치 미션 클리어! 🏅';
  setTimeout(spawnConfetti, 1500);
}}

function togglePause() {{
  paused = !paused;
  document.getElementById('pauseBtn').innerHTML = paused ? '▶️ 계속하기' : '⏸️ 일시정지';
  if (paused) stopBgm(); else startBgm();
}}

function addTime(sec) {{
  if (finished) return;
  remaining += sec;
  render();
}}

function resetTimer() {{
  finished = false; paused = false;
  remaining = TOTAL; lastStageIdx = -1;
  clearInterval(interval); stopBgm();
  document.getElementById('timerScreen').style.display = 'block';
  document.getElementById('celebScreen').style.display = 'none';
  document.getElementById('pauseBtn').innerHTML = '⏸️ 일시정지';
  render();
  interval = setInterval(tick, 1000);
  startBgm();
}}

function restart() {{
  resetTimer();
}}

// ========== INIT ==========
render();
interval = setInterval(tick, 1000);
startBgm();
</script>
</body>
</html>
"""
    components.html(html, height=620, scrolling=False)
