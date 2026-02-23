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

    import streamlit.components.v1 as components

    html = f"""
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{
  font-family: 'Segoe UI', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;
  background: linear-gradient(135deg,#e0f7fa,#f3e5f5);
  display:flex; justify-content:center; align-items:flex-start;
  min-height:100vh; overflow-x:hidden;
  padding:8px;
}}
.container {{
  text-align:center; width:100%; max-width:460px; padding:6px;
  position:relative;
}}

/* ---------- top controls ---------- */
.top-bar {{
  display:flex; justify-content:space-between; align-items:center;
  margin-bottom:6px; padding:0 2px;
}}
.top-group {{ display:flex; gap:4px; align-items:center; }}
.font-btn {{
  background:rgba(255,255,255,0.9); border:1px solid #ccc; border-radius:8px;
  padding:4px 10px; font-weight:700; cursor:pointer;
  font-size:15px; min-width:34px; transition:transform .1s;
}}
.font-btn:active {{ transform:scale(.9); }}
.vol-wrap {{
  display:flex; align-items:center; gap:5px;
  background:rgba(255,255,255,0.9); border-radius:12px; padding:4px 10px;
}}
.mute-btn {{
  background:none; border:none; font-size:20px; cursor:pointer; padding:2px;
}}
.vol-slider {{
  -webkit-appearance:none; appearance:none;
  width:70px; height:5px; border-radius:3px;
  background:linear-gradient(90deg,#42a5f5,#ab47bc);
  outline:none; cursor:pointer;
}}
.vol-slider::-webkit-slider-thumb {{
  -webkit-appearance:none; width:16px; height:16px; border-radius:50%;
  background:#fff; border:2px solid #42a5f5; cursor:pointer;
}}
.vol-label {{ font-size:11px; min-width:28px; color:#666; }}

/* ---------- circular timer ---------- */
.timer-ring {{
  position:relative;
  width:min(260px, 58vw); height:min(260px, 58vw);
  margin:0 auto 10px;
}}
.timer-ring svg {{ width:100%; height:100%; transform:rotate(-90deg); }}
.timer-ring .bg  {{ fill:none; stroke:#e0e0e0; stroke-width:12; }}
.timer-ring .fg  {{ fill:none; stroke:url(#grad); stroke-width:12;
  stroke-linecap:round; transition:stroke-dashoffset .4s ease; }}
.timer-text {{
  position:absolute; top:50%; left:50%; transform:translate(-50%,-50%);
  font-size:clamp(34px,9vw,52px); font-weight:700; color:#333;
}}

/* ---------- name header ---------- */
.name-hdr {{ font-size:clamp(17px,4.5vw,22px); margin-bottom:4px; }}

/* ---------- stage badge ---------- */
.stage {{
  font-size:clamp(15px,4vw,20px); min-height:80px;
  margin:6px 0; transition:all .3s ease;
}}
.stage .emoji {{ font-size:clamp(34px,9vw,48px); animation:bounce .6s ease; }}
.stage .guide {{
  background:rgba(255,255,255,0.75); border-radius:12px;
  padding:5px 12px; margin-top:4px; font-weight:500;
  line-height:1.4; color:#333; display:inline-block;
  font-size:clamp(13px,3.5vw,16px);
}}
@keyframes bounce {{
  0%,100% {{ transform:translateY(0); }}
  50% {{ transform:translateY(-12px); }}
}}

/* ---------- buttons ---------- */
.btn-row {{ display:flex; gap:6px; justify-content:center; flex-wrap:wrap; margin:8px 0; }}
.btn {{
  padding:10px 16px; border:none; border-radius:12px;
  font-size:clamp(13px,3.5vw,15px); font-weight:600; cursor:pointer;
  transition:transform .15s;
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
.celebration h2 {{ font-size:clamp(20px,5.5vw,28px); color:#333; }}
.celebration .big-emoji {{ font-size:clamp(60px,16vw,80px); animation:bounce 1s ease infinite; }}

/* confetti */
.confetti-piece {{
  position:fixed; width:10px; height:10px; border-radius:2px;
  animation:confettiFall linear forwards;
}}
@keyframes confettiFall {{
  0%   {{ opacity:1; transform:translateY(-10vh) rotate(0deg); }}
  100% {{ opacity:0; transform:translateY(110vh) rotate(720deg); }}
}}
</style>
</head>
<body>
<div class="container" id="app">

  <!-- Top controls bar -->
  <div class="top-bar">
    <div class="top-group">
      <button class="font-btn" onclick="changeFontSize(-1)">A-</button>
      <button class="font-btn" onclick="changeFontSize(1)">A+</button>
    </div>
    <div class="vol-wrap">
      <button class="mute-btn" id="muteBtn" onclick="toggleMute()">🔊</button>
      <input type="range" class="vol-slider" id="volSlider" min="0" max="100" value="70"
        oninput="changeVolume(this.value)">
      <span class="vol-label" id="volLabel">70%</span>
    </div>
  </div>

  <!-- Timer screen -->
  <div id="timerScreen">
    <div class="name-hdr"><strong>{name}</strong>의 양치 타임!</div>

    <div class="timer-ring" id="timerRing">
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
    <p id="celebSub" style="color:#666;font-size:clamp(14px,3.8vw,16px);"></p>
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
let masterVolume = 0.7;
let muted = false;
let fontStep = 0;

const CIRC = 2 * Math.PI * 88;
const ring = document.getElementById('ring');
const display = document.getElementById('timeDisplay');
const stageArea = document.getElementById('stageArea');

// ========== FONT SIZE CONTROL ==========
function changeFontSize(dir) {{
  fontStep = Math.max(-2, Math.min(3, fontStep + dir));
  const s = 1 + fontStep * 0.13;
  document.body.style.fontSize = (s * 100) + '%';
}}

// ========== BRUSHING GUIDE (양치 교본 기반) ==========
const GUIDE = [
  {{ pct:1.00, emoji:'🪥', msg:NAME+'! 양치 시작!', guide:'칫솔을 잇몸과 45도로 기울여 잡아요' }},
  {{ pct:0.93, emoji:'👋', msg:'준비됐지?', guide:'칫솔에 힘 빼고~ 부드럽게 잡아요' }},
  {{ pct:0.86, emoji:'➡️', msg:'윗니 바깥쪽 오른쪽!', guide:'오른쪽 위 어금니 바깥면을 쓸어주세요' }},
  {{ pct:0.79, emoji:'⬆️', msg:'윗니 바깥쪽 앞니!', guide:'앞니는 칫솔을 세워서 위에서 아래로!' }},
  {{ pct:0.72, emoji:'⬅️', msg:'윗니 바깥쪽 왼쪽!', guide:'왼쪽 위 어금니도 꼼꼼하게~' }},
  {{ pct:0.65, emoji:'💪', msg:'잘하고 있어!', guide:'이제 윗니 안쪽! 혀쪽으로 칫솔을 넣어요' }},
  {{ pct:0.58, emoji:'👅', msg:'윗니 안쪽!', guide:'안쪽은 칫솔을 세워서 살살 닦아요' }},
  {{ pct:0.50, emoji:'🌟', msg:'절반 왔다! '+NAME+' 최고!', guide:'이제 아랫니! 오른쪽 아래 바깥쪽부터!' }},
  {{ pct:0.43, emoji:'⬇️', msg:'아랫니 바깥쪽!', guide:'아래쪽은 아래에서 위로 쓸어올려요' }},
  {{ pct:0.36, emoji:'🦷', msg:'아래 앞니!', guide:'아래 앞니도 칫솔 세워서 닦아요~' }},
  {{ pct:0.29, emoji:'🔥', msg:'거의 다 왔어!', guide:'왼쪽 아래 어금니 바깥면 쓸어주세요' }},
  {{ pct:0.22, emoji:'👅', msg:'아랫니 안쪽!', guide:'아랫니 안쪽도 꼼꼼히! 혀를 살짝 올려요' }},
  {{ pct:0.15, emoji:'🍎', msg:'씹는 면 닦기!', guide:'어금니 윗면을 앞뒤로 왔다갔다~' }},
  {{ pct:0.08, emoji:'👅', msg:'혀도 닦자!', guide:'혀 위를 안쪽에서 바깥으로 쓸어줘요' }},
  {{ pct:0.02, emoji:'🏆', msg:'마지막 마무리!', guide:'전체를 한 번 더 훑어줘요!' }},
];

const CHEERS = [
  NAME+', 충치 세균이 도망가고 있어! 🏃',
  '번쩍번쩍! '+NAME+'의 이가 빛나요! ✨',
  '치카치카~ '+NAME+' 멋져! 😎',
  NAME+' 이가 점점 깨끗해지고 있어! 🧼',
  '세균아 물러가라~ '+NAME+'가 간다! 🦸',
  '와! '+NAME+' 양치 프로급! 👏',
  '깨끗한 이 = 건강한 몸! 💚',
  '잇몸이 좋아하고 있어요! 🥰',
  '치과 선생님이 칭찬할 거야! 👨‍⚕️',
  NAME+' 이빨이 다이아몬드처럼! 💎',
];
let cheerIdx = 0;
let lastStageIdx = -1;
let lastCheerTime = 0;

function getStage(pct) {{
  for (let i = GUIDE.length - 1; i >= 0; i--) {{
    if (pct <= GUIDE[i].pct) return i;
  }}
  return 0;
}}

// ========== AUDIO ==========
let audioCtx = null;
function ensureAudio() {{
  if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
}}
function vol() {{ return muted ? 0 : masterVolume; }}

function playTick() {{
  if (muted) return;
  ensureAudio();
  const v = vol();
  const o = audioCtx.createOscillator();
  const g = audioCtx.createGain();
  o.type = 'sine'; o.frequency.value = 880;
  g.gain.setValueAtTime(0.25 * v, audioCtx.currentTime);
  g.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.1);
  o.connect(g); g.connect(audioCtx.destination);
  o.start(); o.stop(audioCtx.currentTime + 0.1);
}}

function playStageUp() {{
  if (muted) return;
  ensureAudio();
  const v = vol();
  [523,659,784,1047].forEach((f,i) => {{
    const o = audioCtx.createOscillator();
    const g = audioCtx.createGain();
    o.type = 'triangle'; o.frequency.value = f;
    g.gain.setValueAtTime(0.35 * v, audioCtx.currentTime + i*0.1);
    g.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + i*0.1 + 0.3);
    o.connect(g); g.connect(audioCtx.destination);
    o.start(audioCtx.currentTime + i*0.1);
    o.stop(audioCtx.currentTime + i*0.1 + 0.3);
  }});
}}

function playCheer() {{
  if (muted) return;
  ensureAudio();
  const v = vol();
  [784,988].forEach((f,i) => {{
    const o = audioCtx.createOscillator();
    const g = audioCtx.createGain();
    o.type = 'triangle'; o.frequency.value = f;
    g.gain.setValueAtTime(0.2 * v, audioCtx.currentTime + i*0.08);
    g.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + i*0.08 + 0.2);
    o.connect(g); g.connect(audioCtx.destination);
    o.start(audioCtx.currentTime + i*0.08);
    o.stop(audioCtx.currentTime + i*0.08 + 0.2);
  }});
}}

function playCelebration() {{
  if (muted) return;
  ensureAudio();
  const v = vol();
  [523,587,659,698,784,880,988,1047].forEach((f,i) => {{
    const o = audioCtx.createOscillator();
    const g = audioCtx.createGain();
    o.type = 'square'; o.frequency.value = f;
    g.gain.setValueAtTime(0.22 * v, audioCtx.currentTime + i*0.1);
    g.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + i*0.1 + 0.4);
    o.connect(g); g.connect(audioCtx.destination);
    o.start(audioCtx.currentTime + i*0.1);
    o.stop(audioCtx.currentTime + i*0.1 + 0.4);
  }});
}}

// BGM - rhythmical melody + bass beat
let bgmTimer = null;
let bgmBeat = 0;
const MELODY = [
  {{f:523,d:0.18}},{{f:0,d:0.12}},{{f:659,d:0.18}},{{f:0,d:0.12}},
  {{f:784,d:0.18}},{{f:659,d:0.15}},{{f:523,d:0.18}},{{f:0,d:0.12}},
  {{f:440,d:0.18}},{{f:0,d:0.12}},{{f:523,d:0.18}},{{f:659,d:0.18}},
  {{f:784,d:0.25}},{{f:0,d:0.12}},{{f:659,d:0.18}},{{f:523,d:0.18}},
];

function startBgm() {{
  if (bgmTimer) return;
  bgmBeat = 0;
  bgmTimer = setInterval(() => {{
    if (muted || paused || finished) return;
    ensureAudio();
    const v = vol();
    const n = MELODY[bgmBeat % MELODY.length];
    // melody
    if (n.f > 0) {{
      const o = audioCtx.createOscillator();
      const g = audioCtx.createGain();
      o.type = 'sine'; o.frequency.value = n.f;
      g.gain.setValueAtTime(0.14 * v, audioCtx.currentTime);
      g.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + n.d);
      o.connect(g); g.connect(audioCtx.destination);
      o.start(); o.stop(audioCtx.currentTime + n.d);
    }}
    // bass on even beats
    if (bgmBeat % 2 === 0) {{
      const b = audioCtx.createOscillator();
      const bg = audioCtx.createGain();
      b.type = 'sine'; b.frequency.value = 196;
      bg.gain.setValueAtTime(0.1 * v, audioCtx.currentTime);
      bg.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.15);
      b.connect(bg); bg.connect(audioCtx.destination);
      b.start(); b.stop(audioCtx.currentTime + 0.15);
    }}
    // percussion tick
    const p = audioCtx.createOscillator();
    const pg = audioCtx.createGain();
    p.type = 'square';
    p.frequency.value = bgmBeat % 4 === 0 ? 120 : 900;
    pg.gain.setValueAtTime((bgmBeat % 4 === 0 ? 0.07 : 0.025) * v, audioCtx.currentTime);
    pg.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.04);
    p.connect(pg); pg.connect(audioCtx.destination);
    p.start(); p.stop(audioCtx.currentTime + 0.04);
    bgmBeat++;
  }}, 220);
}}
function stopBgm() {{
  clearInterval(bgmTimer); bgmTimer = null;
}}

// ========== VOLUME CONTROLS ==========
function toggleMute() {{
  muted = !muted;
  document.getElementById('muteBtn').textContent = muted ? '🔇' : '🔊';
  if (muted) stopBgm();
  else if (!finished && !paused) startBgm();
}}
function changeVolume(val) {{
  masterVolume = val / 100;
  document.getElementById('volLabel').textContent = val + '%';
  if (val == 0) {{
    muted = true;
    document.getElementById('muteBtn').textContent = '🔇';
  }} else if (muted) {{
    muted = false;
    document.getElementById('muteBtn').textContent = '🔊';
    if (!finished && !paused) startBgm();
  }}
}}

// ========== RENDER ==========
function render() {{
  const pct = remaining / TOTAL;
  ring.style.strokeDashoffset = CIRC * (1 - pct);

  const m = Math.floor(remaining / 60);
  const s = remaining % 60;
  display.textContent = m + ':' + String(s).padStart(2,'0');

  const elapsed = TOTAL - remaining;
  const idx = getStage(pct);

  // Guide stage change
  if (idx !== lastStageIdx) {{
    lastStageIdx = idx;
    const st = GUIDE[idx];
    stageArea.innerHTML =
      '<div class="emoji">' + st.emoji + '</div>' +
      '<div><strong>' + st.msg + '</strong></div>' +
      '<div class="guide">' + st.guide + '</div>';
    if (idx > 0) playStageUp();
    lastCheerTime = elapsed;
  }}
  // Encouragement between stages (every 7 sec)
  else if (elapsed - lastCheerTime >= 7 && remaining > 5) {{
    lastCheerTime = elapsed;
    const c = CHEERS[cheerIdx % CHEERS.length];
    cheerIdx++;
    const g = stageArea.querySelector('.guide');
    if (g) {{
      const orig = g.textContent;
      g.innerHTML = '💬 ' + c;
      g.style.background = 'rgba(255,243,224,0.9)';
      setTimeout(() => {{
        g.textContent = orig;
        g.style.background = '';
      }}, 3000);
    }}
    playCheer();
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
  if (remaining % 3 === 0) playTick();
  render();
  if (remaining <= 0) finish();
}}

function finish() {{
  finished = true;
  clearInterval(interval); stopBgm();
  playCelebration(); spawnConfetti();
  document.getElementById('timerScreen').style.display = 'none';
  const cel = document.getElementById('celebScreen');
  cel.style.display = 'flex';
  const msgs = [
    NAME+'! 양치 완료! 반짝반짝 깨끗한 이! ✨',
    '대단해 '+NAME+'! 충치 걱정 없는 하루! 🦷💎',
    NAME+'의 이가 보석처럼 빛나요! 💎🌟',
    '완벽한 양치! '+NAME+' 치과 선생님도 감동! 👏',
    NAME+'! 세균 퇴치 미션 완료! 🦸✨',
  ];
  document.getElementById('celebMsg').textContent = msgs[Math.floor(Math.random()*msgs.length)];
  document.getElementById('celebSub').textContent = '구석구석 깨끗하게! 오늘도 양치 미션 클리어! 🏅';
  setTimeout(spawnConfetti, 1500);
}}

function togglePause() {{
  paused = !paused;
  document.getElementById('pauseBtn').innerHTML = paused ? '▶️ 계속하기' : '⏸️ 일시정지';
  if (paused) stopBgm(); else startBgm();
}}

function addTime(sec) {{
  if (finished) return;
  remaining += sec; render();
}}

function resetTimer() {{
  finished = false; paused = false;
  remaining = TOTAL; lastStageIdx = -1;
  lastCheerTime = 0; cheerIdx = 0;
  clearInterval(interval); stopBgm();
  document.getElementById('timerScreen').style.display = 'block';
  document.getElementById('celebScreen').style.display = 'none';
  document.getElementById('pauseBtn').innerHTML = '⏸️ 일시정지';
  render();
  interval = setInterval(tick, 1000);
  startBgm();
}}

function restart() {{ resetTimer(); }}

// ========== INIT ==========
render();
interval = setInterval(tick, 1000);
startBgm();
</script>
</body>
</html>
"""
    components.html(html, height=680, scrolling=False)
