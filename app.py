import json
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="치카치카 타이머 🦷", page_icon="🦷", layout="centered")

# ──────────────────────── i18n ────────────────────────
LANGS = {"한국어": "ko", "English": "en", "中文": "zh", "Español": "es", "日本語": "ja"}

TEXTS = {
  "ko": {
    "title":"🦷 치카치카 타이머","subtitle":"양치 시간을 재미있게 관리하세요!",
    "name_label":"🧒 양치하는 사람 이름","name_ph":"이름을 입력하세요",
    "time_label":"⏱️ 양치 시간 선택","char_label":"🐾 캐릭터 선택",
    "start":"🚀 양치 시작!",
    "time_opts":{"1분":60,"1분 30초":90,"2분":120,"2분 30초":150,"3분":180},"default_time":"2분",
    "default_name":"친구","timer_title":"의 양치 타임!",
    "add10":"+10초","add30":"+30초","pause":"⏸️ 일시정지","resume":"▶️ 계속하기",
    "reset":"🔄 초기화","restart":"🔄 다시 하기",
    "celeb_sub":"구석구석 깨끗하게! 오늘도 양치 미션 클리어! 🏅",
    "guide":[
      {"p":1.00,"e":"🪥","m":"{N}! 양치 시작!","g":"칫솔을 잇몸과 45도로 기울여 잡아요"},
      {"p":0.93,"e":"👋","m":"준비됐지?","g":"칫솔에 힘 빼고~ 부드럽게 잡아요"},
      {"p":0.86,"e":"➡️","m":"윗니 바깥쪽 오른쪽!","g":"오른쪽 위 어금니 바깥면을 쓸어주세요"},
      {"p":0.79,"e":"⬆️","m":"윗니 바깥쪽 앞니!","g":"앞니는 칫솔을 세워서 위에서 아래로!"},
      {"p":0.72,"e":"⬅️","m":"윗니 바깥쪽 왼쪽!","g":"왼쪽 위 어금니도 꼼꼼하게~"},
      {"p":0.65,"e":"💪","m":"잘하고 있어!","g":"이제 윗니 안쪽! 혀쪽으로 칫솔을 넣어요"},
      {"p":0.58,"e":"👅","m":"윗니 안쪽!","g":"안쪽은 칫솔을 세워서 살살 닦아요"},
      {"p":0.50,"e":"🌟","m":"절반 왔다! {N} 최고!","g":"이제 아랫니! 오른쪽 아래 바깥쪽부터!"},
      {"p":0.43,"e":"⬇️","m":"아랫니 바깥쪽!","g":"아래쪽은 아래에서 위로 쓸어올려요"},
      {"p":0.36,"e":"🦷","m":"아래 앞니!","g":"아래 앞니도 칫솔 세워서 닦아요~"},
      {"p":0.29,"e":"🔥","m":"거의 다 왔어!","g":"왼쪽 아래 어금니 바깥면 쓸어주세요"},
      {"p":0.22,"e":"👅","m":"아랫니 안쪽!","g":"아랫니 안쪽도 꼼꼼히! 혀를 살짝 올려요"},
      {"p":0.15,"e":"🍎","m":"씹는 면 닦기!","g":"어금니 윗면을 앞뒤로 왔다갔다~"},
      {"p":0.08,"e":"👅","m":"혀도 닦자!","g":"혀 위를 안쪽에서 바깥으로 쓸어줘요"},
      {"p":0.02,"e":"🏆","m":"마지막 마무리!","g":"전체를 한 번 더 훑어줘요!"}],
    "cheers":["{N}, 충치 세균이 도망가고 있어! 🏃","번쩍번쩍! {N}의 이가 빛나요! ✨",
      "치카치카~ {N} 멋져! 😎","{N} 이가 점점 깨끗해지고 있어! 🧼",
      "세균아 물러가라~ {N}가 간다! 🦸","와! {N} 양치 프로급! 👏",
      "깨끗한 이 = 건강한 몸! 💚","잇몸이 좋아하고 있어요! 🥰",
      "치과 선생님이 칭찬할 거야! 👨‍⚕️","{N} 이빨이 다이아몬드처럼! 💎"],
    "celeb":["{N}! 양치 완료! 반짝반짝 깨끗한 이! ✨","대단해 {N}! 충치 걱정 없는 하루! 🦷💎",
      "{N}의 이가 보석처럼 빛나요! 💎🌟","완벽한 양치! {N} 치과 선생님도 감동! 👏",
      "{N}! 세균 퇴치 미션 완료! 🦸✨"]},
  "en": {
    "title":"🦷 Brushing Timer","subtitle":"Make brushing time fun!",
    "name_label":"🧒 Who's brushing?","name_ph":"Enter your name",
    "time_label":"⏱️ Brushing time","char_label":"🐾 Choose character",
    "start":"🚀 Start Brushing!",
    "time_opts":{"1 min":60,"1m 30s":90,"2 min":120,"2m 30s":150,"3 min":180},"default_time":"2 min",
    "default_name":"Friend","timer_title":"'s Brushing Time!",
    "add10":"+10s","add30":"+30s","pause":"⏸️ Pause","resume":"▶️ Resume",
    "reset":"🔄 Reset","restart":"🔄 Again",
    "celeb_sub":"Every corner sparkling! Brushing mission complete! 🏅",
    "guide":[
      {"p":1.00,"e":"🪥","m":"{N}! Let's brush!","g":"Tilt the brush 45° against the gums"},
      {"p":0.93,"e":"👋","m":"Ready?","g":"Hold the brush gently~"},
      {"p":0.86,"e":"➡️","m":"Upper right outside!","g":"Sweep outer surface of upper‑right molars"},
      {"p":0.79,"e":"⬆️","m":"Upper front teeth!","g":"Hold brush upright, top to bottom!"},
      {"p":0.72,"e":"⬅️","m":"Upper left outside!","g":"Upper left molars too, nice & thorough~"},
      {"p":0.65,"e":"💪","m":"Doing great!","g":"Now upper inside! Slide brush toward tongue"},
      {"p":0.58,"e":"👅","m":"Upper inside!","g":"Stand the brush up and brush gently"},
      {"p":0.50,"e":"🌟","m":"Halfway! {N} rocks!","g":"Now lower teeth! Start lower‑right outside!"},
      {"p":0.43,"e":"⬇️","m":"Lower outside!","g":"Sweep bottom to top on lower teeth"},
      {"p":0.36,"e":"🦷","m":"Lower front!","g":"Stand brush up for lower front teeth~"},
      {"p":0.29,"e":"🔥","m":"Almost there!","g":"Sweep lower left molars outside"},
      {"p":0.22,"e":"👅","m":"Lower inside!","g":"Lower inside too! Lift tongue slightly"},
      {"p":0.15,"e":"🍎","m":"Chewing surfaces!","g":"Scrub molar tops back and forth~"},
      {"p":0.08,"e":"👅","m":"Brush your tongue!","g":"Sweep tongue from back to front"},
      {"p":0.02,"e":"🏆","m":"Final touch!","g":"One more pass over everything!"}],
    "cheers":["{N}, cavity germs are running away! 🏃","Sparkling! {N}'s teeth are shining! ✨",
      "Brush brush~ {N} is awesome! 😎","{N}'s teeth getting cleaner! 🧼",
      "Germs retreat~ {N} is coming! 🦸","Wow! {N} brushes like a pro! 👏",
      "Clean teeth = healthy body! 💚","Your gums are happy! 🥰",
      "The dentist would be proud! 👨‍⚕️","{N}'s teeth shine like diamonds! 💎"],
    "celeb":["{N}! Brushing done! Sparkling clean! ✨","Amazing {N}! No cavities today! 🦷💎",
      "{N}'s teeth shine like jewels! 💎🌟","Perfect brushing! Dentist impressed! 👏",
      "{N}! Germ‑busting mission complete! 🦸✨"]},
  "zh": {
    "title":"🦷 刷牙计时器","subtitle":"让刷牙变得有趣！",
    "name_label":"🧒 谁在刷牙？","name_ph":"请输入名字",
    "time_label":"⏱️ 刷牙时间","char_label":"🐾 选择角色",
    "start":"🚀 开始刷牙！",
    "time_opts":{"1分钟":60,"1分30秒":90,"2分钟":120,"2分30秒":150,"3分钟":180},"default_time":"2分钟",
    "default_name":"小朋友","timer_title":"的刷牙时间！",
    "add10":"+10秒","add30":"+30秒","pause":"⏸️ 暂停","resume":"▶️ 继续",
    "reset":"🔄 重置","restart":"🔄 再来一次",
    "celeb_sub":"每个角落都干净了！刷牙任务完成！🏅",
    "guide":[
      {"p":1.00,"e":"🪥","m":"{N}！开始刷牙！","g":"把牙刷倾斜45度对着牙龈"},
      {"p":0.93,"e":"👋","m":"准备好了吗？","g":"轻轻握住牙刷~"},
      {"p":0.86,"e":"➡️","m":"上牙外侧右边！","g":"刷右上方臼齿的外表面"},
      {"p":0.79,"e":"⬆️","m":"上牙外侧门牙！","g":"门牙要竖着刷，从上到下！"},
      {"p":0.72,"e":"⬅️","m":"上牙外侧左边！","g":"左上方臼齿也要仔细刷~"},
      {"p":0.65,"e":"💪","m":"做得好！","g":"现在刷上牙内侧！"},
      {"p":0.58,"e":"👅","m":"上牙内侧！","g":"内侧要竖起牙刷轻轻刷"},
      {"p":0.50,"e":"🌟","m":"一半了！{N}最棒！","g":"现在刷下牙！从右下方外侧开始！"},
      {"p":0.43,"e":"⬇️","m":"下牙外侧！","g":"下面的牙齿从下往上刷"},
      {"p":0.36,"e":"🦷","m":"下门牙！","g":"下门牙也要竖着刷哦~"},
      {"p":0.29,"e":"🔥","m":"快完成了！","g":"刷左下方臼齿的外表面"},
      {"p":0.22,"e":"👅","m":"下牙内侧！","g":"下牙内侧也要仔细！"},
      {"p":0.15,"e":"🍎","m":"刷咬合面！","g":"臼齿上面前后来回刷~"},
      {"p":0.08,"e":"👅","m":"刷舌头！","g":"从里到外轻轻刷舌面"},
      {"p":0.02,"e":"🏆","m":"最后收尾！","g":"再整体刷一遍！"}],
    "cheers":["{N}，蛀牙细菌在逃跑！🏃","闪闪发光！{N}的牙齿在发亮！✨",
      "刷刷刷~ {N}真棒！😎","{N}的牙齿越来越干净了！🧼",
      "细菌快跑~ {N}来了！🦸","哇！{N}刷牙像专业的！👏",
      "干净的牙齿 = 健康的身体！💚","牙龈很开心！🥰",
      "牙医会表扬你的！👨‍⚕️","{N}的牙齿像钻石一样！💎"],
    "celeb":["{N}！刷牙完成！牙齿闪闪发亮！✨","太棒了{N}！今天不用担心蛀牙！🦷💎",
      "{N}的牙齿像宝石一样闪亮！💎🌟","完美刷牙！牙医也会感动！👏",
      "{N}！消灭细菌任务完成！🦸✨"]},
  "es": {
    "title":"🦷 Temporizador de Cepillado","subtitle":"¡Haz que cepillarte sea divertido!",
    "name_label":"🧒 ¿Quién se cepilla?","name_ph":"Escribe tu nombre",
    "time_label":"⏱️ Tiempo de cepillado","char_label":"🐾 Elige personaje",
    "start":"🚀 ¡A cepillarse!",
    "time_opts":{"1 min":60,"1m 30s":90,"2 min":120,"2m 30s":150,"3 min":180},"default_time":"2 min",
    "default_name":"Amigo","timer_title":" ¡Hora de cepillarse!",
    "add10":"+10s","add30":"+30s","pause":"⏸️ Pausa","resume":"▶️ Continuar",
    "reset":"🔄 Reiniciar","restart":"🔄 Otra vez",
    "celeb_sub":"¡Cada rincón limpio! ¡Misión completada! 🏅",
    "guide":[
      {"p":1.00,"e":"🪥","m":"¡{N}! ¡A cepillarse!","g":"Inclina el cepillo 45° contra las encías"},
      {"p":0.93,"e":"👋","m":"¿Listo?","g":"Sujeta el cepillo suavemente~"},
      {"p":0.86,"e":"➡️","m":"¡Arriba derecha afuera!","g":"Cepilla la superficie exterior de muelas superiores derechas"},
      {"p":0.79,"e":"⬆️","m":"¡Dientes delanteros!","g":"¡Pon el cepillo vertical, de arriba a abajo!"},
      {"p":0.72,"e":"⬅️","m":"¡Arriba izquierda!","g":"Las muelas superiores izquierdas también~"},
      {"p":0.65,"e":"💪","m":"¡Muy bien!","g":"¡Ahora la parte interior superior!"},
      {"p":0.58,"e":"👅","m":"¡Interior superior!","g":"Pon el cepillo vertical y cepilla suavemente"},
      {"p":0.50,"e":"🌟","m":"¡Mitad! ¡{N} es genial!","g":"¡Ahora los dientes de abajo!"},
      {"p":0.43,"e":"⬇️","m":"¡Abajo afuera!","g":"Cepilla de abajo hacia arriba"},
      {"p":0.36,"e":"🦷","m":"¡Dientes delanteros abajo!","g":"Pon el cepillo vertical~"},
      {"p":0.29,"e":"🔥","m":"¡Casi terminamos!","g":"Cepilla las muelas inferiores izquierdas"},
      {"p":0.22,"e":"👅","m":"¡Interior inferior!","g":"¡Levanta un poco la lengua!"},
      {"p":0.15,"e":"🍎","m":"¡Superficies de masticar!","g":"Frota la parte superior de las muelas~"},
      {"p":0.08,"e":"👅","m":"¡Cepilla la lengua!","g":"Pasa el cepillo de atrás hacia adelante"},
      {"p":0.02,"e":"🏆","m":"¡Último toque!","g":"¡Una pasada más por todo!"}],
    "cheers":["¡{N}, los gérmenes huyen! 🏃","¡Brillante! ¡Los dientes de {N} brillan! ✨",
      "¡Cepilla~ {N} es genial! 😎","¡Los dientes de {N} cada vez más limpios! 🧼",
      "¡Gérmenes, retrocedan~ {N} viene! 🦸","¡Wow! ¡{N} cepilla como pro! 👏",
      "¡Dientes limpios = cuerpo sano! 💚","¡Tus encías están felices! 🥰",
      "¡El dentista estaría orgulloso! 👨‍⚕️","¡Los dientes de {N} como diamantes! 💎"],
    "celeb":["¡{N}! ¡Cepillado completo! ¡Dientes relucientes! ✨",
      "¡Increíble {N}! ¡Sin caries hoy! 🦷💎",
      "¡Los dientes de {N} brillan como joyas! 💎🌟",
      "¡Cepillado perfecto! ¡El dentista impresionado! 👏",
      "¡{N}! ¡Misión anti-gérmenes completada! 🦸✨"]},
  "ja": {
    "title":"🦷 歯みがきタイマー","subtitle":"楽しく歯みがきしよう！",
    "name_label":"🧒 歯みがきする人の名前","name_ph":"名前を入れてね",
    "time_label":"⏱️ 歯みがき時間","char_label":"🐾 キャラクターを選ぼう",
    "start":"🚀 歯みがきスタート！",
    "time_opts":{"1分":60,"1分30秒":90,"2分":120,"2分30秒":150,"3分":180},"default_time":"2分",
    "default_name":"おともだち","timer_title":"の歯みがきタイム！",
    "add10":"+10秒","add30":"+30秒","pause":"⏸️ 一時停止","resume":"▶️ つづき",
    "reset":"🔄 リセット","restart":"🔄 もういちど",
    "celeb_sub":"すみずみまでピカピカ！歯みがきミッションクリア！🏅",
    "guide":[
      {"p":1.00,"e":"🪥","m":"{N}！歯みがきスタート！","g":"歯ブラシを歯ぐきに45度に当てよう"},
      {"p":0.93,"e":"👋","m":"じゅんびはいい？","g":"歯ブラシを軽く持って~"},
      {"p":0.86,"e":"➡️","m":"上の歯の外側みぎ！","g":"右上の奥歯の外側をみがこう"},
      {"p":0.79,"e":"⬆️","m":"上の前歯の外側！","g":"前歯は歯ブラシを立てて上から下へ！"},
      {"p":0.72,"e":"⬅️","m":"上の歯の外側ひだり！","g":"左上の奥歯もていねいに~"},
      {"p":0.65,"e":"💪","m":"がんばってるね！","g":"つぎは上の歯の内側！"},
      {"p":0.58,"e":"👅","m":"上の歯の内側！","g":"内側は歯ブラシを立ててそっとみがこう"},
      {"p":0.50,"e":"🌟","m":"半分きた！{N}すごい！","g":"つぎは下の歯！右下の外側から！"},
      {"p":0.43,"e":"⬇️","m":"下の歯の外側！","g":"下の歯は下から上にかきあげよう"},
      {"p":0.36,"e":"🦷","m":"下の前歯！","g":"下の前歯も歯ブラシを立ててね~"},
      {"p":0.29,"e":"🔥","m":"あとちょっと！","g":"左下の奥歯の外側をみがこう"},
      {"p":0.22,"e":"👅","m":"下の歯の内側！","g":"下の内側もていねいに！"},
      {"p":0.15,"e":"🍎","m":"かむ面をみがこう！","g":"奥歯の上を前後にゴシゴシ~"},
      {"p":0.08,"e":"👅","m":"舌もみがこう！","g":"舌の上を奥から手前にすーっと"},
      {"p":0.02,"e":"🏆","m":"ラストスパート！","g":"全体をもう一回みがこう！"}],
    "cheers":["{N}、虫歯バイキンが逃げてるよ！🏃","ピッカピカ！{N}の歯が光ってる！✨",
      "シャカシャカ~ {N}かっこいい！😎","{N}の歯がどんどんきれいに！🧼",
      "バイキンたいさん~ {N}がきたぞ！🦸","わぁ！{N}はみがきプロ級！👏",
      "きれいな歯 = 元気なからだ！💚","歯ぐきがよろこんでるよ！🥰",
      "歯医者さんがほめてくれるよ！👨‍⚕️","{N}の歯がダイヤモンドみたい！💎"],
    "celeb":["{N}！歯みがき完了！ピッカピカの歯！✨","すごい{N}！虫歯の心配なし！🦷💎",
      "{N}の歯が宝石みたいにキラキラ！💎🌟","完璧な歯みがき！歯医者さんも感動！👏",
      "{N}！バイキン退治ミッション完了！🦸✨"]},
}

# ──────────────────────── Characters ────────────────────────
CHARACTERS = {
    "🐰 토끼 Bunny":  "🐰",
    "🐻 곰 Bear":     "🐻",
    "🐱 고양이 Cat":   "🐱",
    "🐶 강아지 Dog":   "🐶",
    "🦊 여우 Fox":     "🦊",
    "🐸 개구리 Frog":  "🐸",
}

# ──────────────────────── CSS ────────────────────────
st.markdown("""<style>
.stApp{background:linear-gradient(135deg,#e0f7fa 0%,#f3e5f5 100%)}
div[data-testid="stMainBlockContainer"]{max-width:500px}
h1{text-align:center}
.setup-card{background:white;border-radius:20px;padding:30px;
  box-shadow:0 4px 20px rgba(0,0,0,.08);margin:10px 0}
</style>""", unsafe_allow_html=True)

# ──────────────────────── Setup UI ────────────────────────
lang_choice = st.selectbox("🌐 Language / 언어", list(LANGS.keys()), index=0)
lang = LANGS[lang_choice]
T = TEXTS[lang]

st.markdown(f"# {T['title']}")
st.markdown(f"<p style='text-align:center;color:#666'>{T['subtitle']}</p>", unsafe_allow_html=True)
st.markdown('<div class="setup-card">', unsafe_allow_html=True)

user_name = st.text_input(T["name_label"], placeholder=T["name_ph"])
time_opts = T["time_opts"]
sel_label = st.select_slider(T["time_label"], options=list(time_opts.keys()), value=T["default_time"])
sel_sec = time_opts[sel_label]
char_choice = st.selectbox(T["char_label"], list(CHARACTERS.keys()), index=0)
char_emoji = CHARACTERS[char_choice]

st.markdown("</div>", unsafe_allow_html=True)
start = st.button(T["start"], use_container_width=True, type="primary")

# ──────────────────────── Timer HTML ────────────────────────
if start:
    name = user_name.strip() or T["default_name"]
    gj = json.dumps(T["guide"], ensure_ascii=False)
    cj = json.dumps(T["cheers"], ensure_ascii=False)
    mj = json.dumps(T["celeb"], ensure_ascii=False)

    html = f"""<!DOCTYPE html><html lang="{lang}"><head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:'Segoe UI','Apple SD Gothic Neo','Malgun Gothic',sans-serif;
  background:linear-gradient(135deg,#e0f7fa,#f3e5f5);display:flex;justify-content:center;
  align-items:flex-start;min-height:100vh;overflow-x:hidden;padding:8px}}
.c{{text-align:center;width:100%;max-width:460px;padding:6px;position:relative}}
.scalable{{transition:font-size .2s ease}}
/* top bar */
.tb{{display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;padding:0 2px}}
.tg{{display:flex;gap:4px;align-items:center}}
.fb{{background:rgba(255,255,255,.9);border:1px solid #ccc;border-radius:8px;
  padding:4px 10px;font-weight:700;cursor:pointer;font-size:15px;min-width:34px;transition:transform .1s}}
.fb:active{{transform:scale(.9)}}
.vw{{display:flex;align-items:center;gap:5px;background:rgba(255,255,255,.9);border-radius:12px;padding:4px 10px}}
.mb{{background:none;border:none;font-size:20px;cursor:pointer;padding:2px}}
.vs{{-webkit-appearance:none;appearance:none;width:70px;height:5px;border-radius:3px;
  background:linear-gradient(90deg,#42a5f5,#ab47bc);outline:none;cursor:pointer}}
.vs::-webkit-slider-thumb{{-webkit-appearance:none;width:16px;height:16px;border-radius:50%;
  background:#fff;border:2px solid #42a5f5;cursor:pointer}}
.vl{{font-size:11px;min-width:28px;color:#666}}
/* character */
.cf{{font-size:clamp(36px,9vw,48px);margin-bottom:2px;animation:cb 2s ease-in-out infinite}}
@keyframes cb{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-6px)}}}}
/* timer ring — smaller */
.tr{{position:relative;width:min(170px,40vw);height:min(170px,40vw);margin:0 auto 6px}}
.tr svg{{width:100%;height:100%;transform:rotate(-90deg)}}
.tr .bg{{fill:none;stroke:#e0e0e0;stroke-width:12}}
.tr .fg{{fill:none;stroke:url(#gr);stroke-width:12;stroke-linecap:round;transition:stroke-dashoffset .4s ease}}
.tt{{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);
  font-size:clamp(24px,6.5vw,36px);font-weight:700;color:#333}}
/* name */
.nh{{font-size:clamp(15px,4vw,19px);margin-bottom:2px}}
/* stage — bigger */
.st{{font-size:clamp(16px,4.5vw,22px);min-height:110px;margin:8px 0;transition:all .3s ease}}
.st .em{{font-size:clamp(36px,10vw,50px);animation:bn .6s ease}}
.st .gd{{background:rgba(255,255,255,.85);border-radius:14px;padding:10px 16px;margin-top:6px;
  font-weight:600;line-height:1.5;color:#333;display:inline-block;
  font-size:clamp(15px,4.2vw,20px);max-width:95%}}
@keyframes bn{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-12px)}}}}
/* germ */
.germ{{position:fixed;font-size:30px;pointer-events:none;z-index:9999;animation:gc 1.2s ease forwards}}
@keyframes gc{{0%{{opacity:1;transform:scale(1) rotate(0)}}
  40%{{opacity:1;transform:scale(1.3) rotate(180deg)}}
  70%{{opacity:.6;transform:scale(.5) rotate(360deg)}}
  100%{{opacity:0;transform:scale(0) rotate(540deg)}}}}
.gburst{{position:fixed;font-size:22px;pointer-events:none;z-index:9998;animation:gb .8s ease forwards}}
@keyframes gb{{0%{{opacity:1;transform:translate(0,0) scale(1)}}
  100%{{opacity:0;transform:translate(var(--dx),var(--dy)) scale(.3)}}}}
/* buttons */
.br{{display:flex;gap:6px;justify-content:center;flex-wrap:wrap;margin:8px 0}}
.bt{{padding:10px 16px;border:none;border-radius:12px;font-size:clamp(13px,3.5vw,15px);
  font-weight:600;cursor:pointer;transition:transform .15s}}
.bt:active{{transform:scale(.95)}}
.ba{{background:#e3f2fd;color:#1565c0}}
.bp{{background:#fff3e0;color:#ef6c00}}
.bx{{background:#fce4ec;color:#c62828}}
/* celebration */
.cel{{display:none;flex-direction:column;align-items:center;gap:14px;animation:fi .5s ease}}
@keyframes fi{{from{{opacity:0;transform:scale(.8)}}to{{opacity:1;transform:scale(1)}}}}
.cel h2{{font-size:clamp(20px,5.5vw,28px);color:#333}}
.cel .be{{font-size:clamp(60px,16vw,80px);animation:bn 1s ease infinite}}
/* confetti */
.cp{{position:fixed;width:10px;height:10px;border-radius:2px;animation:cf linear forwards}}
@keyframes cf{{0%{{opacity:1;transform:translateY(-10vh) rotate(0)}}
  100%{{opacity:0;transform:translateY(110vh) rotate(720deg)}}}}
</style></head><body>
<div class="c" id="app">
  <div class="tb">
    <div class="tg">
      <button class="fb" onclick="cfs(-1)">A-</button>
      <button class="fb" onclick="cfs(1)">A+</button>
    </div>
    <div class="vw">
      <button class="mb" id="muB" onclick="tgM()">🔊</button>
      <input type="range" class="vs" id="vS" min="0" max="100" value="70" oninput="chV(this.value)">
      <span class="vl" id="vL">70%</span>
    </div>
  </div>
  <div id="tS" class="scalable">
    <div class="cf" id="cF">{char_emoji}</div>
    <div class="nh"><strong>{name}</strong>{T['timer_title']}</div>
    <div class="tr">
      <svg viewBox="0 0 200 200">
        <defs><linearGradient id="gr" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" style="stop-color:#42a5f5"/>
          <stop offset="100%" style="stop-color:#ab47bc"/>
        </linearGradient></defs>
        <circle class="bg" cx="100" cy="100" r="88"/>
        <circle class="fg" id="ring" cx="100" cy="100" r="88" stroke-dasharray="553" stroke-dashoffset="0"/>
      </svg>
      <div class="tt" id="tD">0:00</div>
    </div>
    <div class="st" id="sA"></div>
    <div class="br">
      <button class="bt ba" onclick="addT(10)">{T['add10']}</button>
      <button class="bt ba" onclick="addT(30)">{T['add30']}</button>
      <button class="bt bp" id="pB" onclick="tgP()">{T['pause']}</button>
      <button class="bt bx" onclick="rsT()">{T['reset']}</button>
    </div>
  </div>
  <div class="cel" id="cS">
    <div class="be">{char_emoji}</div>
    <h2 id="cM"></h2>
    <p id="cU" style="color:#666;font-size:clamp(14px,3.8vw,16px)"></p>
    <button class="bt ba" style="margin-top:10px;font-size:17px;padding:12px 30px" onclick="rsT()">{T['restart']}</button>
  </div>
</div>
<script>
const TOTAL={sel_sec},NAME="{name}",CE="{char_emoji}";
const PL=`{T['pause']}`,RL=`{T['resume']}`,CSB=`{T['celeb_sub']}`;
let rem=TOTAL,pau=false,fin=false,iv=null,mVol=.7,mut=false,fs=0;
const CI=2*Math.PI*88;
const ring=document.getElementById('ring'),disp=document.getElementById('tD'),
  sA=document.getElementById('sA'),sc=document.querySelector('.scalable');

// i18n data
const GR={gj};
const G=GR.map(x=>({{...x,m:x.m.replace(/\\{{N\\}}/g,NAME),g:x.g.replace(/\\{{N\\}}/g,NAME)}}));
const CR={cj};
const CH=CR.map(x=>x.replace(/\\{{N\\}}/g,NAME));
const MR={mj};
const CM=MR.map(x=>x.replace(/\\{{N\\}}/g,NAME));

let ci=0,lsi=-1,lct=0;

/* ===== Font size (fixed) ===== */
const BFS=16;
function cfs(d){{
  fs=Math.max(-2,Math.min(4,fs+d));
  const n=BFS+fs*2;
  sc.style.fontSize=n+'px';
  document.querySelectorAll('.gd').forEach(e=>e.style.fontSize=(n+2)+'px');
  const h=document.querySelector('.nh');
  if(h)h.style.fontSize=(n+3)+'px';
}}

function gS(p){{for(let i=G.length-1;i>=0;i--)if(p<=G[i].p)return i;return 0}}

/* ===== Audio with mobile-resume fix ===== */
let ac=null;
function eA(){{
  if(!ac)ac=new(window.AudioContext||window.webkitAudioContext)();
  if(ac.state==='suspended')ac.resume();
}}
function vl(){{return mut?0:mVol}}

// Visibility change — resume audio after app switch on mobile
document.addEventListener('visibilitychange',()=>{{
  if(document.visibilityState==='visible'){{
    if(ac&&ac.state==='suspended')ac.resume();
    if(!fin&&!pau&&!mut){{stopB();startB()}}
  }}
}});
window.addEventListener('pageshow',e=>{{
  if(e.persisted){{
    if(ac&&ac.state==='suspended')ac.resume();
    if(!fin&&!pau&&!mut){{stopB();startB()}}
  }}
}});
document.addEventListener('touchstart',function _r(){{
  if(ac&&ac.state==='suspended')ac.resume();
  document.removeEventListener('touchstart',_r);
}},{{once:true}});

function pTk(){{
  if(mut)return;eA();const v=vl();
  const o=ac.createOscillator(),g=ac.createGain();
  o.type='sine';o.frequency.value=880;
  g.gain.setValueAtTime(.25*v,ac.currentTime);
  g.gain.exponentialRampToValueAtTime(.001,ac.currentTime+.1);
  o.connect(g);g.connect(ac.destination);o.start();o.stop(ac.currentTime+.1);
}}
function pSU(){{
  if(mut)return;eA();const v=vl();
  [523,659,784,1047].forEach((f,i)=>{{
    const o=ac.createOscillator(),g=ac.createGain();
    o.type='triangle';o.frequency.value=f;
    g.gain.setValueAtTime(.35*v,ac.currentTime+i*.1);
    g.gain.exponentialRampToValueAtTime(.001,ac.currentTime+i*.1+.3);
    o.connect(g);g.connect(ac.destination);
    o.start(ac.currentTime+i*.1);o.stop(ac.currentTime+i*.1+.3);
  }});
}}
function pCh(){{
  if(mut)return;eA();const v=vl();
  [784,988].forEach((f,i)=>{{
    const o=ac.createOscillator(),g=ac.createGain();
    o.type='triangle';o.frequency.value=f;
    g.gain.setValueAtTime(.2*v,ac.currentTime+i*.08);
    g.gain.exponentialRampToValueAtTime(.001,ac.currentTime+i*.08+.2);
    o.connect(g);g.connect(ac.destination);
    o.start(ac.currentTime+i*.08);o.stop(ac.currentTime+i*.08+.2);
  }});
}}
function pCe(){{
  if(mut)return;eA();const v=vl();
  [523,587,659,698,784,880,988,1047].forEach((f,i)=>{{
    const o=ac.createOscillator(),g=ac.createGain();
    o.type='square';o.frequency.value=f;
    g.gain.setValueAtTime(.22*v,ac.currentTime+i*.1);
    g.gain.exponentialRampToValueAtTime(.001,ac.currentTime+i*.1+.4);
    o.connect(g);g.connect(ac.destination);
    o.start(ac.currentTime+i*.1);o.stop(ac.currentTime+i*.1+.4);
  }});
}}
function pGC(){{
  if(mut)return;eA();const v=vl();
  const o=ac.createOscillator(),g=ac.createGain();
  o.type='square';o.frequency.value=300;
  o.frequency.exponentialRampToValueAtTime(80,ac.currentTime+.3);
  g.gain.setValueAtTime(.15*v,ac.currentTime);
  g.gain.exponentialRampToValueAtTime(.001,ac.currentTime+.3);
  o.connect(g);g.connect(ac.destination);o.start();o.stop(ac.currentTime+.3);
}}

/* BGM */
let bgT=null,bgB=0;
const ML=[
  {{f:523,d:.18}},{{f:0,d:.12}},{{f:659,d:.18}},{{f:0,d:.12}},
  {{f:784,d:.18}},{{f:659,d:.15}},{{f:523,d:.18}},{{f:0,d:.12}},
  {{f:440,d:.18}},{{f:0,d:.12}},{{f:523,d:.18}},{{f:659,d:.18}},
  {{f:784,d:.25}},{{f:0,d:.12}},{{f:659,d:.18}},{{f:523,d:.18}}];
function startB(){{
  if(bgT)return;bgB=0;
  bgT=setInterval(()=>{{
    if(mut||pau||fin)return;eA();const v=vl();
    const n=ML[bgB%ML.length];
    if(n.f>0){{const o=ac.createOscillator(),g=ac.createGain();
      o.type='sine';o.frequency.value=n.f;
      g.gain.setValueAtTime(.14*v,ac.currentTime);
      g.gain.exponentialRampToValueAtTime(.001,ac.currentTime+n.d);
      o.connect(g);g.connect(ac.destination);o.start();o.stop(ac.currentTime+n.d);}}
    if(bgB%2===0){{const b=ac.createOscillator(),bg=ac.createGain();
      b.type='sine';b.frequency.value=196;
      bg.gain.setValueAtTime(.1*v,ac.currentTime);
      bg.gain.exponentialRampToValueAtTime(.001,ac.currentTime+.15);
      b.connect(bg);bg.connect(ac.destination);b.start();b.stop(ac.currentTime+.15);}}
    const p=ac.createOscillator(),pg=ac.createGain();
    p.type='square';p.frequency.value=bgB%4===0?120:900;
    pg.gain.setValueAtTime((bgB%4===0?.07:.025)*v,ac.currentTime);
    pg.gain.exponentialRampToValueAtTime(.001,ac.currentTime+.04);
    p.connect(pg);pg.connect(ac.destination);p.start();p.stop(ac.currentTime+.04);
    bgB++;
  }},220);
}}
function stopB(){{clearInterval(bgT);bgT=null}}

/* Volume */
function tgM(){{
  mut=!mut;document.getElementById('muB').textContent=mut?'🔇':'🔊';
  if(mut)stopB();else if(!fin&&!pau)startB();
}}
function chV(v){{
  mVol=v/100;document.getElementById('vL').textContent=v+'%';
  if(v==0){{mut=true;document.getElementById('muB').textContent='🔇'}}
  else if(mut){{mut=false;document.getElementById('muB').textContent='🔊';if(!fin&&!pau)startB()}}
}}

/* ===== Germ catching ===== */
const GE=['🦠','🦠','🦠','💀','👾','🧫'];
let lgT=0;
function spG(){{
  const now=Date.now();if(now-lgT<4000)return;lgT=now;
  const el=document.createElement('div');el.className='germ';
  el.textContent=GE[Math.floor(Math.random()*GE.length)];
  const x=15+Math.random()*70,y=20+Math.random()*50;
  el.style.left=x+'vw';el.style.top=y+'vh';
  document.body.appendChild(el);
  setTimeout(()=>{{
    const sp=['✨','💥','⚡','💫'];
    for(let i=0;i<4;i++){{
      const b=document.createElement('div');b.className='gburst';b.textContent=sp[i];
      b.style.left=x+'vw';b.style.top=y+'vh';
      const a=(Math.PI*2*i)/4;
      b.style.setProperty('--dx',Math.cos(a)*40+'px');
      b.style.setProperty('--dy',Math.sin(a)*40+'px');
      document.body.appendChild(b);setTimeout(()=>b.remove(),800);
    }}
    pGC();
  }},500);
  setTimeout(()=>el.remove(),1200);
}}

/* ===== Render ===== */
function render(){{
  const p=rem/TOTAL;
  ring.style.strokeDashoffset=CI*(1-p);
  const m=Math.floor(rem/60),s=rem%60;
  disp.textContent=m+':'+String(s).padStart(2,'0');
  const el=TOTAL-rem,idx=gS(p);
  if(idx!==lsi){{
    lsi=idx;const st=G[idx];
    sA.innerHTML='<div class="em">'+st.e+'</div><div><strong>'+st.m+'</strong></div><div class="gd">'+st.g+'</div>';
    if(idx>0)pSU();lct=el;
  }} else if(el-lct>=7&&rem>5){{
    lct=el;const c=CH[ci%CH.length];ci++;
    const g=sA.querySelector('.gd');
    if(g){{const orig=g.textContent;g.innerHTML='💬 '+c;g.style.background='rgba(255,243,224,.9)';
      setTimeout(()=>{{g.textContent=orig;g.style.background=''}},3000)}}
    pCh();
  }}
}}

/* Confetti */
function spC(){{
  const co=['#f44336','#e91e63','#9c27b0','#2196f3','#4caf50','#ff9800','#ffeb3b'];
  for(let i=0;i<60;i++){{const e=document.createElement('div');e.className='cp';
    e.style.left=Math.random()*100+'vw';
    e.style.background=co[Math.floor(Math.random()*co.length)];
    e.style.animationDuration=(2+Math.random()*2)+'s';
    e.style.animationDelay=Math.random()*.5+'s';
    document.body.appendChild(e);setTimeout(()=>e.remove(),4500)}}
}}

/* Timer */
function tick(){{
  if(pau||fin)return;rem--;
  if(rem%3===0)pTk();
  if(rem>5&&rem%8===0)spG();
  render();if(rem<=0)finish();
}}
function finish(){{
  fin=true;clearInterval(iv);stopB();pCe();spC();
  document.getElementById('tS').style.display='none';
  const c=document.getElementById('cS');c.style.display='flex';
  document.getElementById('cM').textContent=CM[Math.floor(Math.random()*CM.length)];
  document.getElementById('cU').textContent=CSB;
  setTimeout(spC,1500);
}}
function tgP(){{
  pau=!pau;document.getElementById('pB').innerHTML=pau?RL:PL;
  if(pau)stopB();else startB();
}}
function addT(s){{if(fin)return;rem+=s;render()}}
function rsT(){{
  fin=false;pau=false;rem=TOTAL;lsi=-1;lct=0;ci=0;
  clearInterval(iv);stopB();
  document.getElementById('tS').style.display='block';
  document.getElementById('cS').style.display='none';
  document.getElementById('pB').innerHTML=PL;
  render();iv=setInterval(tick,1000);startB();
}}

render();iv=setInterval(tick,1000);startB();
</script></body></html>"""
    components.html(html, height=700, scrolling=False)
