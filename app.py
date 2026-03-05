import streamlit as st

st.set_page_config(
    page_title="치카치카 타이머 🦷",
    page_icon="🦷",
    layout="centered",
)

# --- i18n ---
LANGS = {
    "한국어": "ko",
    "English": "en",
    "中文": "zh",
    "Español": "es",
    "日本語": "ja",
}

TEXTS = {
    "ko": {
        "title": "🦷 치카치카 타이머",
        "subtitle": "양치 시간을 재미있게 관리하세요!",
        "name_label": "🧒 양치하는 사람 이름",
        "name_placeholder": "이름을 입력하세요",
        "time_label": "⏱️ 양치 시간 선택",
        "char_label": "🐾 캐릭터 선택",
        "char_toggle": "🐾 캐릭터 사용",
        "char_cat_label": "📂 캐릭터 종류",
        "cancel": "❌ 취소",
        "cancel_confirm": "정말 양치를 취소할까요?",
        "mode_label": "📱 모드",
        "mode_basic": "기본",
        "mode_mirror": "🪞 거울",
        "cam_unavail": "📷 카메라를 사용할 수 없어요",
        "selfie_toggle": "📸 인증샷 촬영",
        "effect_prompt": "✨ 효과를 골라보세요!",
        "cat_labels": ["없음", "머리", "눈", "얼굴", "동물", "파티"],
        "pick_prompt": "👇 하나 골라요!",
        "start_btn": "🚀 양치 시작!",
        "time_opts": {"1분": 60, "1분 30초": 90, "2분": 120, "2분 30초": 150, "3분": 180},
        "default_time": "2분",
        "default_name": "친구",
        "timer_title": "의 양치 타임!",
        "add10": "+10초",
        "add30": "+30초",
        "pause": "⏸️ 일시정지",
        "resume": "▶️ 계속하기",
        "reset": "🔄 초기화",
        "restart": "🔄 다시 하기",
        "share_btn": "📤 공유하기",
        "save_btn": "💾 사진 저장",
        "photo_msg": "📸 찰칵! 양치 중 인증샷!",
        "celeb_sub": "구석구석 깨끗하게! 오늘도 양치 미션 클리어! 🏅",
        "guide": [
            {"pct":1.00,"emoji":"🪥","msg":"{name}! 양치 시작!","guide":"칫솔을 잇몸과 45도로 기울여 잡아요"},
            {"pct":0.93,"emoji":"👋","msg":"준비됐지?","guide":"칫솔에 힘 빼고~ 부드럽게 잡아요"},
            {"pct":0.86,"emoji":"➡️","msg":"윗니 바깥쪽 오른쪽!","guide":"오른쪽 위 어금니 바깥면을 쓸어주세요"},
            {"pct":0.79,"emoji":"⬆️","msg":"윗니 바깥쪽 앞니!","guide":"앞니는 칫솔을 세워서 위에서 아래로!"},
            {"pct":0.72,"emoji":"⬅️","msg":"윗니 바깥쪽 왼쪽!","guide":"왼쪽 위 어금니도 꼼꼼하게~"},
            {"pct":0.65,"emoji":"💪","msg":"잘하고 있어!","guide":"이제 윗니 안쪽! 혀쪽으로 칫솔을 넣어요"},
            {"pct":0.58,"emoji":"👅","msg":"윗니 안쪽!","guide":"안쪽은 칫솔을 세워서 살살 닦아요"},
            {"pct":0.50,"emoji":"🌟","msg":"절반 왔다! {name} 최고!","guide":"이제 아랫니! 오른쪽 아래 바깥쪽부터!"},
            {"pct":0.43,"emoji":"⬇️","msg":"아랫니 바깥쪽!","guide":"아래쪽은 아래에서 위로 쓸어올려요"},
            {"pct":0.36,"emoji":"🦷","msg":"아래 앞니!","guide":"아래 앞니도 칫솔 세워서 닦아요~"},
            {"pct":0.29,"emoji":"🔥","msg":"거의 다 왔어!","guide":"왼쪽 아래 어금니 바깥면 쓸어주세요"},
            {"pct":0.22,"emoji":"👅","msg":"아랫니 안쪽!","guide":"아랫니 안쪽도 꼼꼼히! 혀를 살짝 올려요"},
            {"pct":0.15,"emoji":"🍎","msg":"씹는 면 닦기!","guide":"어금니 윗면을 앞뒤로 왔다갔다~"},
            {"pct":0.08,"emoji":"👅","msg":"혀도 닦자!","guide":"혀 위를 안쪽에서 바깥으로 쓸어줘요"},
            {"pct":0.02,"emoji":"🏆","msg":"마지막 마무리!","guide":"전체를 한 번 더 훑어줘요!"},
        ],
        "cheers": [
            "{name}, 충치 세균이 도망가고 있어! 🏃",
            "번쩍번쩍! {name}의 이가 빛나요! ✨",
            "치카치카~ {name} 멋져! 😎",
            "{name} 이가 점점 깨끗해지고 있어! 🧼",
            "세균아 물러가라~ {name}가 간다! 🦸",
            "와! {name} 양치 프로급! 👏",
            "깨끗한 이 = 건강한 몸! 💚",
            "잇몸이 좋아하고 있어요! 🥰",
            "치과 선생님이 칭찬할 거야! 👨‍⚕️",
            "{name} 이빨이 다이아몬드처럼! 💎",
        ],
        "celeb_msgs": [
            "{name}! 양치 완료! 반짝반짝 깨끗한 이! ✨",
            "대단해 {name}! 충치 걱정 없는 하루! 🦷💎",
            "{name}의 이가 보석처럼 빛나요! 💎🌟",
            "완벽한 양치! {name} 치과 선생님도 감동! 👏",
            "{name}! 세균 퇴치 미션 완료! 🦸✨",
        ],
    },
    "en": {
        "title": "🦷 Brushing Timer",
        "subtitle": "Make brushing fun!",
        "name_label": "🧒 Who's brushing?",
        "name_placeholder": "Enter your name",
        "time_label": "⏱️ Brushing time",
        "char_label": "🐾 Choose character",
        "char_toggle": "🐾 Use character",
        "char_cat_label": "📂 Character type",
        "cancel": "❌ Cancel",
        "cancel_confirm": "Really stop brushing?",
        "mode_label": "📱 Mode",
        "mode_basic": "Basic",
        "mode_mirror": "🪞 Mirror",
        "cam_unavail": "📷 Camera unavailable",
        "selfie_toggle": "📸 Take selfie",
        "effect_prompt": "✨ Choose your effect!",
        "cat_labels": ["None", "Head", "Eyes", "Face", "Animal", "Fun"],
        "pick_prompt": "👇 Pick one!",
        "start_btn": "🚀 Start Brushing!",
        "time_opts": {"1 min": 60, "1m 30s": 90, "2 min": 120, "2m 30s": 150, "3 min": 180},
        "default_time": "2 min",
        "default_name": "Friend",
        "timer_title": "'s Brushing Time!",
        "add10": "+10s",
        "add30": "+30s",
        "pause": "⏸️ Pause",
        "resume": "▶️ Resume",
        "reset": "🔄 Reset",
        "restart": "🔄 Again",
        "share_btn": "📤 Share",
        "save_btn": "💾 Save Photo",
        "photo_msg": "📸 Snap! Brushing selfie!",
        "celeb_sub": "Every corner is clean! Brushing mission complete! 🏅",
        "guide": [
            {"pct":1.00,"emoji":"🪥","msg":"{name}! Let's brush!","guide":"Tilt the brush 45° against the gums"},
            {"pct":0.93,"emoji":"👋","msg":"Ready?","guide":"Hold the brush gently, no pressure~"},
            {"pct":0.86,"emoji":"➡️","msg":"Upper right outside!","guide":"Sweep the outer surface of upper right molars"},
            {"pct":0.79,"emoji":"⬆️","msg":"Upper front outside!","guide":"Hold brush vertical for front teeth, top to bottom!"},
            {"pct":0.72,"emoji":"⬅️","msg":"Upper left outside!","guide":"Upper left molars – nice and thorough~"},
            {"pct":0.65,"emoji":"💪","msg":"Doing great!","guide":"Now upper inside! Slide the brush toward the tongue"},
            {"pct":0.58,"emoji":"👅","msg":"Upper inside!","guide":"Stand the brush up and brush gently inside"},
            {"pct":0.50,"emoji":"🌟","msg":"Halfway! {name} rocks!","guide":"Now lower teeth! Start from lower right outside!"},
            {"pct":0.43,"emoji":"⬇️","msg":"Lower outside!","guide":"Sweep from bottom to top on the lower teeth"},
            {"pct":0.36,"emoji":"🦷","msg":"Lower front!","guide":"Stand the brush up for lower front teeth~"},
            {"pct":0.29,"emoji":"🔥","msg":"Almost there!","guide":"Sweep the outer surface of lower left molars"},
            {"pct":0.22,"emoji":"👅","msg":"Lower inside!","guide":"Lower inside too! Lift your tongue a little"},
            {"pct":0.15,"emoji":"🍎","msg":"Chewing surfaces!","guide":"Scrub the top of molars back and forth~"},
            {"pct":0.08,"emoji":"👅","msg":"Brush your tongue!","guide":"Sweep tongue from back to front"},
            {"pct":0.02,"emoji":"🏆","msg":"Final touch!","guide":"One more pass over everything!"},
        ],
        "cheers": [
            "{name}, cavity germs are running away! 🏃",
            "Sparkling! {name}'s teeth are shining! ✨",
            "Brush brush~ {name} is awesome! 😎",
            "{name}'s teeth are getting cleaner! 🧼",
            "Germs, retreat~ {name} is coming! 🦸",
            "Wow! {name} brushes like a pro! 👏",
            "Clean teeth = healthy body! 💚",
            "Your gums are happy! 🥰",
            "The dentist would be proud! 👨‍⚕️",
            "{name}'s teeth shine like diamonds! 💎",
        ],
        "celeb_msgs": [
            "{name}! Brushing done! Sparkling clean teeth! ✨",
            "Amazing {name}! No cavities today! 🦷💎",
            "{name}'s teeth shine like jewels! 💎🌟",
            "Perfect brushing! The dentist is impressed! 👏",
            "{name}! Germ-busting mission complete! 🦸✨",
        ],
    },
    "zh": {
        "title": "🦷 刷牙计时器",
        "subtitle": "让刷牙变得有趣！",
        "name_label": "🧒 谁在刷牙？",
        "name_placeholder": "请输入名字",
        "time_label": "⏱️ 刷牙时间",
        "char_label": "🐾 选择角色",
        "char_toggle": "🐾 使用角色",
        "char_cat_label": "📂 角色种类",
        "cancel": "❌ 取消",
        "cancel_confirm": "真的要停止刷牙吗？",
        "mode_label": "📱 模式",
        "mode_basic": "基本",
        "mode_mirror": "🪞 镜子",
        "cam_unavail": "📷 无法使用相机",
        "selfie_toggle": "📸 拍照认证",
        "effect_prompt": "✨ 选一个效果吧！",
        "cat_labels": ["无", "头饰", "眼睛", "脸部", "动物", "派对"],
        "pick_prompt": "👇 选一个！",
        "start_btn": "🚀 开始刷牙！",
        "time_opts": {"1分钟": 60, "1分30秒": 90, "2分钟": 120, "2分30秒": 150, "3分钟": 180},
        "default_time": "2分钟",
        "default_name": "小朋友",
        "timer_title": "的刷牙时间！",
        "add10": "+10秒",
        "add30": "+30秒",
        "pause": "⏸️ 暂停",
        "resume": "▶️ 继续",
        "reset": "🔄 重置",
        "restart": "🔄 再来一次",
        "share_btn": "📤 分享",
        "save_btn": "💾 保存照片",
        "photo_msg": "📸 咔嚓！刷牙自拍！",
        "celeb_sub": "每个角落都干净了！今天的刷牙任务完成！🏅",
        "guide": [
            {"pct":1.00,"emoji":"🪥","msg":"{name}！开始刷牙！","guide":"把牙刷倾斜45度对着牙龈"},
            {"pct":0.93,"emoji":"👋","msg":"准备好了吗？","guide":"轻轻握住牙刷，不要用力~"},
            {"pct":0.86,"emoji":"➡️","msg":"上牙外侧右边！","guide":"刷右上方臼齿的外表面"},
            {"pct":0.79,"emoji":"⬆️","msg":"上牙外侧门牙！","guide":"门牙要竖着刷，从上到下！"},
            {"pct":0.72,"emoji":"⬅️","msg":"上牙外侧左边！","guide":"左上方臼齿也要仔细刷~"},
            {"pct":0.65,"emoji":"💪","msg":"做得好！","guide":"现在刷上牙内侧！把牙刷伸向舌头那边"},
            {"pct":0.58,"emoji":"👅","msg":"上牙内侧！","guide":"内侧要竖起牙刷轻轻刷"},
            {"pct":0.50,"emoji":"🌟","msg":"一半了！{name}最棒！","guide":"现在刷下牙！从右下方外侧开始！"},
            {"pct":0.43,"emoji":"⬇️","msg":"下牙外侧！","guide":"下面的牙齿从下往上刷"},
            {"pct":0.36,"emoji":"🦷","msg":"下门牙！","guide":"下门牙也要竖着刷哦~"},
            {"pct":0.29,"emoji":"🔥","msg":"快完成了！","guide":"刷左下方臼齿的外表面"},
            {"pct":0.22,"emoji":"👅","msg":"下牙内侧！","guide":"下牙内侧也要仔细！稍微抬起舌头"},
            {"pct":0.15,"emoji":"🍎","msg":"刷咬合面！","guide":"臼齿上面前后来回刷~"},
            {"pct":0.08,"emoji":"👅","msg":"刷舌头！","guide":"从里到外轻轻刷舌面"},
            {"pct":0.02,"emoji":"🏆","msg":"最后收尾！","guide":"再整体刷一遍！"},
        ],
        "cheers": [
            "{name}，蛀牙细菌在逃跑！🏃",
            "闪闪发光！{name}的牙齿在发亮！✨",
            "刷刷刷~ {name}真棒！😎",
            "{name}的牙齿越来越干净了！🧼",
            "细菌快跑~ {name}来了！🦸",
            "哇！{name}刷牙像专业的！👏",
            "干净的牙齿 = 健康的身体！💚",
            "牙龈很开心！🥰",
            "牙医会表扬你的！👨‍⚕️",
            "{name}的牙齿像钻石一样！💎",
        ],
        "celeb_msgs": [
            "{name}！刷牙完成！牙齿闪闪发亮！✨",
            "太棒了{name}！今天不用担心蛀牙！🦷💎",
            "{name}的牙齿像宝石一样闪亮！💎🌟",
            "完美刷牙！牙医也会感动！👏",
            "{name}！消灭细菌任务完成！🦸✨",
        ],
    },
    "es": {
        "title": "🦷 Temporizador de Cepillado",
        "subtitle": "¡Haz que cepillarte sea divertido!",
        "name_label": "🧒 ¿Quién se cepilla?",
        "name_placeholder": "Escribe tu nombre",
        "time_label": "⏱️ Tiempo de cepillado",
        "char_label": "🐾 Elige personaje",
        "char_toggle": "🐾 Usar personaje",
        "char_cat_label": "📂 Tipo de personaje",
        "cancel": "❌ Cancelar",
        "cancel_confirm": "Realmente quieres dejar de cepillarte?",
        "mode_label": "📱 Modo",
        "mode_basic": "Básico",
        "mode_mirror": "🪞 Espejo",
        "cam_unavail": "📷 Cámara no disponible",
        "selfie_toggle": "📸 Tomar selfie",
        "effect_prompt": "✨ ¡Elige un efecto!",
        "cat_labels": ["Ninguno", "Cabeza", "Ojos", "Cara", "Animal", "Fiesta"],
        "pick_prompt": "👇 ¡Elige uno!",
        "start_btn": "🚀 ¡A cepillarse!",
        "time_opts": {"1 min": 60, "1m 30s": 90, "2 min": 120, "2m 30s": 150, "3 min": 180},
        "default_time": "2 min",
        "default_name": "Amigo",
        "timer_title": " ¡Hora de cepillarse!",
        "add10": "+10s",
        "add30": "+30s",
        "pause": "⏸️ Pausa",
        "resume": "▶️ Continuar",
        "reset": "🔄 Reiniciar",
        "restart": "🔄 Otra vez",
        "share_btn": "📤 Compartir",
        "save_btn": "💾 Guardar foto",
        "photo_msg": "📸 ¡Clic! ¡Selfie cepillándose!",
        "celeb_sub": "¡Cada rincón está limpio! ¡Misión de cepillado completada! 🏅",
        "guide": [
            {"pct":1.00,"emoji":"🪥","msg":"¡{name}! ¡A cepillarse!","guide":"Inclina el cepillo 45° contra las encías"},
            {"pct":0.93,"emoji":"👋","msg":"¿Listo?","guide":"Sujeta el cepillo suavemente, sin presionar~"},
            {"pct":0.86,"emoji":"➡️","msg":"¡Arriba derecha afuera!","guide":"Cepilla la superficie exterior de las muelas superiores derechas"},
            {"pct":0.79,"emoji":"⬆️","msg":"¡Dientes delanteros!","guide":"¡Pon el cepillo vertical para los dientes delanteros!"},
            {"pct":0.72,"emoji":"⬅️","msg":"¡Arriba izquierda afuera!","guide":"Las muelas superiores izquierdas también~"},
            {"pct":0.65,"emoji":"💪","msg":"¡Muy bien!","guide":"¡Ahora la parte interior! Desliza el cepillo hacia la lengua"},
            {"pct":0.58,"emoji":"👅","msg":"¡Interior superior!","guide":"Pon el cepillo vertical y cepilla suavemente"},
            {"pct":0.50,"emoji":"🌟","msg":"¡Mitad! ¡{name} es genial!","guide":"¡Ahora los dientes de abajo! ¡Desde la derecha!"},
            {"pct":0.43,"emoji":"⬇️","msg":"¡Abajo afuera!","guide":"Cepilla de abajo hacia arriba"},
            {"pct":0.36,"emoji":"🦷","msg":"¡Dientes delanteros abajo!","guide":"Pon el cepillo vertical para los de abajo~"},
            {"pct":0.29,"emoji":"🔥","msg":"¡Casi terminamos!","guide":"Cepilla las muelas inferiores izquierdas"},
            {"pct":0.22,"emoji":"👅","msg":"¡Interior inferior!","guide":"¡Levanta un poco la lengua!"},
            {"pct":0.15,"emoji":"🍎","msg":"¡Superficies de masticar!","guide":"Frota la parte superior de las muelas~"},
            {"pct":0.08,"emoji":"👅","msg":"¡Cepilla la lengua!","guide":"Pasa el cepillo de atrás hacia adelante"},
            {"pct":0.02,"emoji":"🏆","msg":"¡Último toque!","guide":"¡Una pasada más por todo!"},
        ],
        "cheers": [
            "¡{name}, los gérmenes de caries están huyendo! 🏃",
            "¡Brillante! ¡Los dientes de {name} brillan! ✨",
            "¡Cepilla cepilla~ {name} es genial! 😎",
            "¡Los dientes de {name} están cada vez más limpios! 🧼",
            "¡Gérmenes, retrocedan~ {name} viene! 🦸",
            "¡Wow! ¡{name} cepilla como un pro! 👏",
            "¡Dientes limpios = cuerpo sano! 💚",
            "¡Tus encías están felices! 🥰",
            "¡El dentista estaría orgulloso! 👨‍⚕️",
            "¡Los dientes de {name} brillan como diamantes! 💎",
        ],
        "celeb_msgs": [
            "¡{name}! ¡Cepillado completo! ¡Dientes relucientes! ✨",
            "¡Increíble {name}! ¡Sin caries hoy! 🦷💎",
            "¡Los dientes de {name} brillan como joyas! 💎🌟",
            "¡Cepillado perfecto! ¡El dentista está impresionado! 👏",
            "¡{name}! ¡Misión anti-gérmenes completada! 🦸✨",
        ],
    },
    "ja": {
        "title": "🦷 歯みがきタイマー",
        "subtitle": "楽しく歯みがきしよう！",
        "name_label": "🧒 歯みがきする人の名前",
        "name_placeholder": "名前を入れてね",
        "time_label": "⏱️ 歯みがき時間",
        "char_label": "🐾 キャラクターを選ぼう",
        "char_toggle": "🐾 キャラクターを使う",
        "char_cat_label": "📂 キャラクターの種類",
        "cancel": "❌ キャンセル",
        "cancel_confirm": "本当に歯みがきをやめますか？",
        "mode_label": "📱 モード",
        "mode_basic": "きほん",
        "mode_mirror": "🪞 ミラー",
        "cam_unavail": "📷 カメラが使えません",
        "selfie_toggle": "📸 セルフィー撮影",
        "effect_prompt": "✨ エフェクトを選んでね！",
        "cat_labels": ["なし", "頭", "目", "顔", "動物", "パーティ"],
        "pick_prompt": "👇 一つ選んでね！",
        "start_btn": "🚀 歯みがきスタート！",
        "time_opts": {"1分": 60, "1分30秒": 90, "2分": 120, "2分30秒": 150, "3分": 180},
        "default_time": "2分",
        "default_name": "おともだち",
        "timer_title": "の歯みがきタイム！",
        "add10": "+10秒",
        "add30": "+30秒",
        "pause": "⏸️ 一時停止",
        "resume": "▶️ つづき",
        "reset": "🔄 リセット",
        "restart": "🔄 もういちど",
        "share_btn": "📤 シェア",
        "save_btn": "💾 写真を保存",
        "photo_msg": "📸 パシャ！歯みがきセルフィー！",
        "celeb_sub": "すみずみまでピカピカ！今日の歯みがきミッションクリア！🏅",
        "guide": [
            {"pct":1.00,"emoji":"🪥","msg":"{name}！歯みがきスタート！","guide":"歯ブラシを歯ぐきに45度に当てよう"},
            {"pct":0.93,"emoji":"👋","msg":"じゅんびはいい？","guide":"歯ブラシを軽く持って、やさしくね~"},
            {"pct":0.86,"emoji":"➡️","msg":"上の歯の外側みぎ！","guide":"右上の奥歯の外側をみがこう"},
            {"pct":0.79,"emoji":"⬆️","msg":"上の前歯の外側！","guide":"前歯は歯ブラシを立てて上から下へ！"},
            {"pct":0.72,"emoji":"⬅️","msg":"上の歯の外側ひだり！","guide":"左上の奥歯もていねいに~"},
            {"pct":0.65,"emoji":"💪","msg":"がんばってるね！","guide":"つぎは上の歯の内側！舌のほうへブラシを入れよう"},
            {"pct":0.58,"emoji":"👅","msg":"上の歯の内側！","guide":"内側は歯ブラシを立ててそっとみがこう"},
            {"pct":0.50,"emoji":"🌟","msg":"半分きた！{name}すごい！","guide":"つぎは下の歯！右下の外側から！"},
            {"pct":0.43,"emoji":"⬇️","msg":"下の歯の外側！","guide":"下の歯は下から上にかきあげよう"},
            {"pct":0.36,"emoji":"🦷","msg":"下の前歯！","guide":"下の前歯も歯ブラシを立ててね~"},
            {"pct":0.29,"emoji":"🔥","msg":"あとちょっと！","guide":"左下の奥歯の外側をみがこう"},
            {"pct":0.22,"emoji":"👅","msg":"下の歯の内側！","guide":"下の内側もていねいに！舌をちょっと上げてね"},
            {"pct":0.15,"emoji":"🍎","msg":"かむ面をみがこう！","guide":"奥歯の上を前後にゴシゴシ~"},
            {"pct":0.08,"emoji":"👅","msg":"舌もみがこう！","guide":"舌の上を奥から手前にすーっと"},
            {"pct":0.02,"emoji":"🏆","msg":"ラストスパート！","guide":"全体をもう一回みがこう！"},
        ],
        "cheers": [
            "{name}、虫歯バイキンが逃げてるよ！🏃",
            "ピッカピカ！{name}の歯が光ってる！✨",
            "シャカシャカ~ {name}かっこいい！😎",
            "{name}の歯がどんどんきれいに！🧼",
            "バイキンたいさん~ {name}がきたぞ！🦸",
            "わぁ！{name}はみがきプロ級！👏",
            "きれいな歯 = 元気なからだ！💚",
            "歯ぐきがよろこんでるよ！🥰",
            "歯医者さんがほめてくれるよ！👨‍⚕️",
            "{name}の歯がダイヤモンドみたい！💎",
        ],
        "celeb_msgs": [
            "{name}！歯みがき完了！ピッカピカの歯！✨",
            "すごい{name}！虫歯の心配なし！🦷💎",
            "{name}の歯が宝石みたいにキラキラ！💎🌟",
            "完璧な歯みがき！歯医者さんも感動！👏",
            "{name}！バイキン退治ミッション完了！🦸✨",
        ],
    },
}

# --- Characters (categorized) ---
CHAR_CATEGORIES = {
    "ko": {
        "기본": {
            "🐰 토끼": "🐰", "🐻 곰": "🐻", "🐱 고양이": "🐱",
            "🐶 강아지": "🐶", "🦊 여우": "🦊", "🐸 개구리": "🐸",
            "🐼 판다": "🐼", "🦁 사자": "🦁", "🐯 호랑이": "🐯",
        },
        "공룡": {
            "🦕 브라키오사우르스": "🦕", "🦖 티라노사우르스": "🦖",
            "🔰 트리케라톱스": "🛡️", "🪨 안킬로사우르스": "🪨",
            "🌿 스테고사우르스": "🌿", "🏃 오르니토미무스": "🏃",
            "🪶 아르카이옵테릭스": "🪶", "🌋 스피노사우르스": "🌋",
            "🥚 파라사우롤로푸스": "🥚", "🦴 벨로키랍토르": "🦴",
        },
        "새": {
            "🦅 독수리": "🦅", "🦜 앵무새": "🦜", "🐧 펭귄": "🐧",
            "🦉 올빼미": "🦉", "🦢 백조": "🦢", "🦩 플라밍고": "🦩",
            "🐦 참새": "🐦", "🦚 공작": "🦚",
        },
        "바다": {
            "🐬 돌고래": "🐬", "🐙 문어": "🐙", "🦈 상어": "🦈",
            "🐢 거북이": "🐢", "🐠 열대어": "🐠", "🦑 오징어": "🦑",
            "🐳 고래": "🐳", "🦀 게": "🦀",
        },
        "곤충": {
            "🦋 나비": "🦋", "🐞 무당벌레": "🐞", "🐝 꿀벌": "🐝",
            "🐛 애벌레": "🐛", "🦗 귀뚜라미": "🦗", "🐜 개미": "🐜",
        },
    },
    "en": {
        "Basic": {
            "🐰 Bunny": "🐰", "🐻 Bear": "🐻", "🐱 Cat": "🐱",
            "🐶 Dog": "🐶", "🦊 Fox": "🦊", "🐸 Frog": "🐸",
            "🐼 Panda": "🐼", "🦁 Lion": "🦁", "🐯 Tiger": "🐯",
        },
        "Dinosaurs": {
            "🦕 Brachiosaurus": "🦕", "🦖 T-Rex": "🦖",
            "🛡️ Triceratops": "🛡️", "🪨 Ankylosaurus": "🪨",
            "🌿 Stegosaurus": "🌿", "🏃 Ornithomimus": "🏃",
            "🪶 Archaeopteryx": "🪶", "🌋 Spinosaurus": "🌋",
            "🥚 Parasaurolophus": "🥚", "🦴 Velociraptor": "🦴",
        },
        "Birds": {
            "🦅 Eagle": "🦅", "🦜 Parrot": "🦜", "🐧 Penguin": "🐧",
            "🦉 Owl": "🦉", "🦢 Swan": "🦢", "🦩 Flamingo": "🦩",
            "🐦 Sparrow": "🐦", "🦚 Peacock": "🦚",
        },
        "Sea": {
            "🐬 Dolphin": "🐬", "🐙 Octopus": "🐙", "🦈 Shark": "🦈",
            "🐢 Turtle": "🐢", "🐠 Tropical Fish": "🐠", "🦑 Squid": "🦑",
            "🐳 Whale": "🐳", "🦀 Crab": "🦀",
        },
        "Insects": {
            "🦋 Butterfly": "🦋", "🐞 Ladybug": "🐞", "🐝 Bee": "🐝",
            "🐛 Caterpillar": "🐛", "🦗 Cricket": "🦗", "🐜 Ant": "🐜",
        },
    },
    "zh": {
        "基本": {
            "🐰 兔子": "🐰", "🐻 熊": "🐻", "🐱 猫": "🐱",
            "🐶 狗": "🐶", "🦊 狐狸": "🦊", "🐸 青蛙": "🐸",
            "🐼 熊猫": "🐼", "🦁 狮子": "🦁", "🐯 老虎": "🐯",
        },
        "恐龙": {
            "🦕 腕龙": "🦕", "🦖 霸王龙": "🦖",
            "🛡️ 三角龙": "🛡️", "🪨 甲龙": "🪨",
            "🌿 剑龙": "🌿", "🏃 似鸟龙": "🏃",
            "🪶 始祖鸟": "🪶", "🌋 棘龙": "🌋",
            "🥚 副栉龙": "🥚", "🦴 迅猛龙": "🦴",
        },
        "鸟类": {
            "🦅 鹰": "🦅", "🦜 鹦鹉": "🦜", "🐧 企鹅": "🐧",
            "🦉 猫头鹰": "🦉", "🦢 天鹅": "🦢", "🦩 火烈鸟": "🦩",
            "🐦 麻雀": "🐦", "🦚 孔雀": "🦚",
        },
        "海洋": {
            "🐬 海豚": "🐬", "🐙 章鱼": "🐙", "🦈 鲨鱼": "🦈",
            "🐢 海龟": "🐢", "🐠 热带鱼": "🐠", "🦑 鱿鱼": "🦑",
            "🐳 鲸鱼": "🐳", "🦀 螃蟹": "🦀",
        },
        "昆虫": {
            "🦋 蝴蝶": "🦋", "🐞 瓢虫": "🐞", "🐝 蜜蜂": "🐝",
            "🐛 毛毛虫": "🐛", "🦗 蟋蟀": "🦗", "🐜 蚂蚁": "🐜",
        },
    },
    "es": {
        "Basico": {
            "🐰 Conejo": "🐰", "🐻 Oso": "🐻", "🐱 Gato": "🐱",
            "🐶 Perro": "🐶", "🦊 Zorro": "🦊", "🐸 Rana": "🐸",
            "🐼 Panda": "🐼", "🦁 Leon": "🦁", "🐯 Tigre": "🐯",
        },
        "Dinosaurios": {
            "🦕 Braquiosaurio": "🦕", "🦖 T-Rex": "🦖",
            "🛡️ Triceratops": "🛡️", "🪨 Anquilosaurio": "🪨",
            "🌿 Estegosaurio": "🌿", "🏃 Ornitomimo": "🏃",
            "🪶 Archaeopteryx": "🪶", "🌋 Espinosaurio": "🌋",
            "🥚 Parasaurolophus": "🥚", "🦴 Velociraptor": "🦴",
        },
        "Aves": {
            "🦅 Aguila": "🦅", "🦜 Loro": "🦜", "🐧 Pinguino": "🐧",
            "🦉 Buho": "🦉", "🦢 Cisne": "🦢", "🦩 Flamenco": "🦩",
            "🐦 Gorrion": "🐦", "🦚 Pavo Real": "🦚",
        },
        "Mar": {
            "🐬 Delfin": "🐬", "🐙 Pulpo": "🐙", "🦈 Tiburon": "🦈",
            "🐢 Tortuga": "🐢", "🐠 Pez Tropical": "🐠", "🦑 Calamar": "🦑",
            "🐳 Ballena": "🐳", "🦀 Cangrejo": "🦀",
        },
        "Insectos": {
            "🦋 Mariposa": "🦋", "🐞 Mariquita": "🐞", "🐝 Abeja": "🐝",
            "🐛 Oruga": "🐛", "🦗 Grillo": "🦗", "🐜 Hormiga": "🐜",
        },
    },
    "ja": {
        "きほん": {
            "🐰 うさぎ": "🐰", "🐻 くま": "🐻", "🐱 ねこ": "🐱",
            "🐶 いぬ": "🐶", "🦊 きつね": "🦊", "🐸 かえる": "🐸",
            "🐼 パンダ": "🐼", "🦁 ライオン": "🦁", "🐯 とら": "🐯",
        },
        "きょうりゅう": {
            "🦕 ブラキオサウルス": "🦕", "🦖 ティラノサウルス": "🦖",
            "🛡️ トリケラトプス": "🛡️", "🪨 アンキロサウルス": "🪨",
            "🌿 ステゴサウルス": "🌿", "🏃 オルニトミムス": "🏃",
            "🪶 アーケオプテリクス": "🪶", "🌋 スピノサウルス": "🌋",
            "🥚 パラサウロロフス": "🥚", "🦴 ヴェロキラプトル": "🦴",
        },
        "とり": {
            "🦅 わし": "🦅", "🦜 おうむ": "🦜", "🐧 ペンギン": "🐧",
            "🦉 ふくろう": "🦉", "🦢 はくちょう": "🦢", "🦩 フラミンゴ": "🦩",
            "🐦 すずめ": "🐦", "🦚 くじゃく": "🦚",
        },
        "うみ": {
            "🐬 イルカ": "🐬", "🐙 たこ": "🐙", "🦈 サメ": "🦈",
            "🐢 かめ": "🐢", "🐠 ねったいぎょ": "🐠", "🦑 いか": "🦑",
            "🐳 くじら": "🐳", "🦀 かに": "🦀",
        },
        "むし": {
            "🦋 ちょうちょ": "🦋", "🐞 てんとうむし": "🐞", "🐝 みつばち": "🐝",
            "🐛 いもむし": "🐛", "🦗 こおろぎ": "🦗", "🐜 あり": "🐜",
        },
    },
}

# --- CSS ---
st.markdown(
    """
<style>
    /* ===== 전체 배경 ===== */
    .stApp { background: linear-gradient(135deg, #e0f7fa 0%, #f3e5f5 100%) !important; }
    div[data-testid="stMainBlockContainer"] { max-width: 500px; }

    /* ===== 타이틀 / 서브타이틀 ===== */
    h1 { text-align: center; color: #222 !important; font-size: 1.8rem !important; }

    /* ===== 위젯 라벨 (다크 모드에서도 진한 색 강제) ===== */
    [data-testid="stWidgetLabel"] p,
    [data-testid="stWidgetLabel"] label {
        font-size: 1.15rem !important;
        font-weight: 600 !important;
        color: #2c2c2c !important;
    }

    /* ===== 입력 필드 ===== */
    .stTextInput input {
        font-size: 1.1rem !important;
        color: #222 !important;
        background: #fafafa !important;
        border: 1.5px solid #ccc !important;
    }
    .stTextInput input::placeholder { color: #999 !important; }

    /* ===== Selectbox / 드롭다운 (선택 전·후 모두) ===== */
    [data-baseweb="select"] * {
        color: #222 !important;
        font-size: 1.05rem !important;
    }
    [data-baseweb="select"] > div:first-child {
        background: #fafafa !important;
        border: 1.5px solid #bbb !important;
    }
    [data-baseweb="select"] svg {
        fill: #555 !important;
    }

    /* ===== 슬라이더 ===== */
    [data-testid="stTickBarMin"] p,
    [data-testid="stTickBarMax"] p {
        font-size: 1rem !important;
        color: #444 !important;
        font-weight: 500 !important;
    }
    .stSlider [data-testid="stThumbValue"] {
        color: #222 !important;
        font-size: 0.95rem !important;
    }

    /* ===== 라디오 버튼 (모드 선택) ===== */
    .stRadio [role="radiogroup"] label p {
        font-size: 1.1rem !important;
        color: #333 !important;
        font-weight: 500 !important;
    }

    /* ===== 시작 버튼 ===== */
    .stButton button[kind="primary"],
    .stButton button[data-testid="stBaseButton-primary"] {
        font-size: 1.2rem !important;
        padding: 0.6rem 1.2rem !important;
        font-weight: 700 !important;
    }

    /* ===== 드롭다운 메뉴 옵션 ===== */
    [data-baseweb="menu"] li {
        font-size: 1.05rem !important;
        color: #222 !important;
    }
</style>
""",
    unsafe_allow_html=True,
)

# --- Language selection ---
lang_choice = st.selectbox("🌐 Language / 언어", list(LANGS.keys()), index=0)
lang = LANGS[lang_choice]
T = TEXTS[lang]

st.markdown(f"# {T['title']}")
st.markdown(
    f"<p style='text-align:center;color:#444;font-size:1.1rem;font-weight:500;'>{T['subtitle']}</p>",
    unsafe_allow_html=True,
)

# --- Setup UI ---
user_name = st.text_input(T["name_label"], placeholder=T["name_placeholder"])

time_opts = T["time_opts"]
selected_label = st.select_slider(T["time_label"], options=list(time_opts.keys()), value=T["default_time"])
selected_seconds = time_opts[selected_label]

char_enabled = st.checkbox(T["char_toggle"], value=True)
if char_enabled:
    char_cats = CHAR_CATEGORIES[lang]
    cat_names = list(char_cats.keys())
    selected_cat = st.selectbox(T["char_cat_label"], cat_names, index=0)
    chars_in_cat = char_cats[selected_cat]
    char_choice = st.selectbox(T["char_label"], list(chars_in_cat.keys()), index=0)
    char_emoji = chars_in_cat[char_choice]
else:
    char_emoji = "🦷"

mode = st.radio(T["mode_label"], [T["mode_basic"], T["mode_mirror"]], horizontal=True, index=1)
mirror_mode = mode == T["mode_mirror"]
selfie_enabled = st.checkbox(T["selfie_toggle"], value=True) if mirror_mode else False

start = st.button(T["start_btn"], use_container_width=True, type="primary")

if start:
    import json
    name = user_name.strip() or T["default_name"]

    guide_json = json.dumps(T["guide"], ensure_ascii=False)
    cheers_json = json.dumps(T["cheers"], ensure_ascii=False)
    celeb_msgs_json = json.dumps(T["celeb_msgs"], ensure_ascii=False)
    cat_labels = T.get("cat_labels", ["None", "Head", "Eyes", "Face", "Animal", "Fun"])
    pick_prompt = T.get("pick_prompt", "👇 Pick one!")

    import streamlit.components.v1 as components

    html = f"""
<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{
  font-family: 'Segoe UI', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;
  color: #333;
  background: linear-gradient(135deg,#e0f7fa,#f3e5f5);
  display:flex; justify-content:center; align-items:flex-start;
  min-height:100vh; overflow-x:hidden;
  padding:8px;
}}
.container {{
  text-align:center; width:100%; max-width:460px; padding:6px;
  position:relative; overflow:hidden;
}}

/* ---------- scalable root ---------- */
.scalable {{
  transition: font-size 0.2s ease;
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

/* ---------- character ---------- */
.char-face {{
  font-size:clamp(38px,10vw,52px);
  margin-bottom:2px;
  animation: charBounce 2s ease-in-out infinite;
}}
@keyframes charBounce {{
  0%,100% {{ transform:translateY(0); }}
  50% {{ transform:translateY(-6px); }}
}}

/* ---------- circular timer (smaller) ---------- */
.timer-ring {{
  position:relative;
  width:min(180px, 42vw); height:min(180px, 42vw);
  margin:0 auto 6px;
}}
.timer-ring svg {{ width:100%; height:100%; transform:rotate(-90deg); }}
.timer-ring .bg  {{ fill:none; stroke:#e0e0e0; stroke-width:12; }}
.timer-ring .fg  {{ fill:none; stroke:url(#grad); stroke-width:12;
  stroke-linecap:round; transition:stroke-dashoffset .4s ease; }}
.timer-text {{
  position:absolute; top:50%; left:50%; transform:translate(-50%,-50%);
  font-size:clamp(26px,7vw,38px); font-weight:700; color:#333;
}}

/* ---------- name header ---------- */
.name-hdr {{ font-size:clamp(15px,4vw,19px); margin-bottom:2px; color:#2e2e2e; text-shadow:0 1px 2px rgba(255,255,255,0.8); }}

/* ---------- stage badge (larger text) ---------- */
.stage {{
  font-size:clamp(16px,4.5vw,22px); min-height:100px;
  margin:8px 0; transition:all .3s ease;
  color:#2e2e2e; text-shadow:0 1px 2px rgba(255,255,255,0.8);
}}
.stage .emoji {{ font-size:clamp(36px,10vw,50px); animation:bounce .6s ease; }}
.stage .guide {{
  background:rgba(255,255,255,0.92); border-radius:14px;
  padding:8px 16px; margin-top:6px; font-weight:600;
  line-height:1.5; color:#1a1a1a; display:inline-block;
  text-shadow:none;
  font-size:clamp(15px,4vw,19px);
  max-width:95%;
}}
@keyframes bounce {{
  0%,100% {{ transform:translateY(0); }}
  50% {{ transform:translateY(-12px); }}
}}

/* ---------- germ effect ---------- */
.germ {{
  position:absolute; font-size:28px; pointer-events:none;
  z-index:50; animation: germCatch 1.2s ease forwards;
}}
@keyframes germCatch {{
  0% {{ opacity:1; transform:scale(1) rotate(0deg); }}
  40% {{ opacity:1; transform:scale(1.3) rotate(180deg); }}
  70% {{ opacity:0.6; transform:scale(0.5) rotate(360deg); }}
  100% {{ opacity:0; transform:scale(0) rotate(540deg); }}
}}
.germ-burst {{
  position:absolute; font-size:22px; pointer-events:none;
  z-index:49; animation: burstOut 0.8s ease forwards;
}}
@keyframes burstOut {{
  0% {{ opacity:1; transform:translate(0,0) scale(1); }}
  100% {{ opacity:0; transform:translate(var(--dx),var(--dy)) scale(0.3); }}
}}

/* ---------- mirror mode ---------- */
.mirror-container {{
  display:none; position:relative;
  width:min(300px, 78vw); aspect-ratio:4/3;
  margin:0 auto 8px; border-radius:20px;
  overflow:hidden; background:#111;
  border:3px solid rgba(255,255,255,0.5);
  box-shadow:0 4px 15px rgba(0,0,0,0.15);
}}
.mirror-video {{
  width:100%; height:100%; object-fit:cover;
  transform:scaleX(-1);
}}
.mirror-char-badge {{
  position:absolute; bottom:8px; left:10px;
  font-size:30px; filter:drop-shadow(0 2px 3px rgba(0,0,0,0.4));
  animation:charBounce 2s ease-in-out infinite;
}}
.mirror-no-cam {{
  color:#aaa; font-size:14px;
  position:absolute; top:50%; left:50%;
  transform:translate(-50%,-50%); text-align:center;
}}

/* ---------- photo capture ---------- */
.photo-countdown {{
  position:absolute; inset:0;
  background:rgba(0,0,0,0.35);
  font-size:clamp(60px,18vw,90px); font-weight:900;
  color:#fff; z-index:10;
  display:none; justify-content:center; align-items:center;
  text-shadow:0 4px 12px rgba(0,0,0,0.5);
}}
.photo-flash {{
  display:none; position:absolute; inset:0;
  background:#fff; z-index:11; pointer-events:none;
}}
.celeb-photo-wrap {{
  display:none; position:relative;
  border-radius:16px; overflow:hidden;
  border:4px solid #ffd54f;
  box-shadow:0 4px 20px rgba(0,0,0,0.15);
  max-width:min(260px, 65vw);
  animation:fadeIn .5s ease;
}}
.celeb-photo-wrap img {{ width:100%; display:block; }}
.celeb-photo-label {{
  position:absolute; bottom:0; left:0; right:0;
  background:linear-gradient(transparent, rgba(0,0,0,0.6));
  color:#fff; padding:10px 8px 8px; text-align:center;
  font-size:clamp(12px,3.5vw,15px); font-weight:600;
}}
.share-row {{
  display:none; gap:8px; justify-content:center; flex-wrap:wrap;
}}
.btn-share {{ background:#e8f5e9; color:#2e7d32; }}
.btn-save {{ background:#e3f2fd; color:#1565c0; }}

/* ---------- face effects ---------- */
.effect-canvas {{
  position:absolute; top:0; left:0;
  width:100%; height:100%; pointer-events:none;
}}
.effect-cats {{
  display:flex; gap:4px; justify-content:center; flex-wrap:wrap;
  padding:4px 6px;
}}
.effect-cat-btn {{
  display:flex; flex-direction:column; align-items:center; gap:1px;
  padding:4px 8px 3px; border:2px solid rgba(0,0,0,0.08);
  border-radius:10px; background:rgba(255,255,255,0.9);
  cursor:pointer; transition:transform .1s, background .15s;
}}
.cat-icon {{ font-size:18px; line-height:1.2; }}
.cat-label {{ font-size:10px; color:#888; line-height:1; white-space:nowrap; }}
.effect-cat-btn:active {{ transform:scale(.9); }}
.effect-cat-btn.active {{ border-color:#42a5f5; background:#bbdefb; }}
.effect-cat-btn.active .cat-label {{ color:#1565c0; font-weight:600; }}
.effect-items-wrap {{
  width:100%;
}}
.pick-prompt {{
  font-size:11px; color:#888; text-align:center; margin-bottom:2px;
}}
.effect-items {{
  display:flex; gap:4px; justify-content:center; flex-wrap:wrap;
  padding:5px 8px;
  background:rgba(255,243,224,0.5); border:1.5px dashed #ffcc80;
  border-radius:10px;
}}
.effect-item-btn {{
  font-size:18px; padding:2px; border:2px solid transparent;
  border-radius:50%; background:rgba(255,255,255,0.8);
  cursor:pointer; transition:transform .1s;
  width:36px; height:36px; display:flex; align-items:center; justify-content:center;
}}
.effect-item-btn:active {{ transform:scale(.9); }}
.effect-item-btn.active {{ border-color:#ff9800; background:#fff3e0; }}
.effect-loading {{
  display:none; position:absolute; bottom:6px; right:6px;
  font-size:11px; color:#fff; background:rgba(0,0,0,0.5);
  padding:2px 8px; border-radius:8px;
}}
/* ---------- pre-start ---------- */
.pre-start {{
  display:none; flex-direction:column; align-items:center;
  gap:6px; margin:6px 0; padding:8px;
  background:rgba(255,255,255,0.6); border-radius:14px;
}}
.pre-start-prompt {{
  font-size:clamp(14px,4vw,17px); font-weight:600; color:#333;
}}
.btn-start {{
  padding:12px 32px; border:none; border-radius:14px;
  font-size:clamp(15px,4vw,18px); font-weight:700; cursor:pointer;
  background:linear-gradient(135deg,#42a5f5,#ab47bc); color:#fff;
  box-shadow:0 3px 10px rgba(66,165,245,0.3);
  transition:transform .15s;
}}
.btn-start:active {{ transform:scale(.95); }}

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
.btn-cancel {{ background:#f5f5f5; color:#616161; border:1.5px solid #bbb; }}

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
  <div id="timerScreen" class="scalable">
    <div class="char-face" id="charFace">{char_emoji}</div>

    <!-- Timer elements (hidden during pre-start in mirror mode) -->
    <div id="timerElements">
      <div class="name-hdr"><strong>{name}</strong>{T['timer_title']}</div>
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
    </div>

    <!-- Mirror (visible in mirror mode, below timer during brushing) -->
    <div class="mirror-container" id="mirrorContainer">
      <video id="mirrorVideo" class="mirror-video" autoplay playsinline muted></video>
      <canvas id="effectCanvas" class="effect-canvas"></canvas>
      <div class="mirror-char-badge">{char_emoji}</div>
      <div class="effect-loading" id="effectLoading">Loading...</div>
      <div class="mirror-no-cam" id="mirrorNoCam" style="display:none;">{T['cam_unavail']}</div>
      <div class="photo-countdown" id="photoCountdown"></div>
      <div class="photo-flash" id="photoFlash"></div>
    </div>

    <!-- Pre-start: effect selector + start (mirror mode only) -->
    <div class="pre-start" id="preStart">
      <div class="pre-start-prompt">{T['effect_prompt']}</div>
      <div class="effect-cats">
        <button class="effect-cat-btn" onclick="selectCat(-1)"><span class="cat-icon">🚫</span><span class="cat-label">{cat_labels[0]}</span></button>
        <button class="effect-cat-btn" onclick="selectCat(0)"><span class="cat-icon">🎩</span><span class="cat-label">{cat_labels[1]}</span></button>
        <button class="effect-cat-btn" onclick="selectCat(1)"><span class="cat-icon">👓</span><span class="cat-label">{cat_labels[2]}</span></button>
        <button class="effect-cat-btn" onclick="selectCat(2)"><span class="cat-icon">😺</span><span class="cat-label">{cat_labels[3]}</span></button>
        <button class="effect-cat-btn" onclick="selectCat(3)"><span class="cat-icon">🐾</span><span class="cat-label">{cat_labels[4]}</span></button>
        <button class="effect-cat-btn" onclick="selectCat(4)"><span class="cat-icon">🎪</span><span class="cat-label">{cat_labels[5]}</span></button>
      </div>
      <div class="effect-items-wrap" id="effectItemsWrap" style="display:none;">
        <div class="pick-prompt">{pick_prompt}</div>
        <div class="effect-items" id="effectItems"></div>
      </div>
      <button class="btn-start" onclick="startBrushing()">{T['start_btn']}</button>
    </div>

    <div class="btn-row" id="btnRow">
      <button class="btn btn-add" onclick="addTime(10)">{T['add10']}</button>
      <button class="btn btn-add" onclick="addTime(30)">{T['add30']}</button>
      <button class="btn btn-pause" id="pauseBtn" onclick="togglePause()">{T['pause']}</button>
      <button class="btn btn-reset" onclick="resetTimer()">{T['reset']}</button>
      <button class="btn btn-cancel" onclick="cancelTimer()">{T['cancel']}</button>
    </div>
  </div>

  <!-- Celebration screen -->
  <div class="celebration" id="celebScreen">
    <div class="big-emoji">{char_emoji}</div>
    <h2 id="celebMsg"></h2>
    <div class="celeb-photo-wrap" id="celebPhotoWrap">
      <img id="celebPhoto" src="" alt="">
      <div class="celeb-photo-label" id="celebPhotoLabel"></div>
    </div>
    <p id="celebSub" style="color:#444;font-size:clamp(14px,3.8vw,16px);"></p>
    <div class="share-row" id="shareRow">
      <button class="btn btn-share" onclick="sharePhoto()">{T['share_btn']}</button>
      <button class="btn btn-save" onclick="downloadPhoto()">{T['save_btn']}</button>
    </div>
    <button class="btn btn-add" style="margin-top:10px;font-size:17px;padding:12px 30px;"
      onclick="restart()">{T['restart']}</button>
  </div>
</div>

<script>
// ========== CONFIG ==========
const TOTAL = {selected_seconds};
const NAME  = "{name}";
const CHAR_EMOJI = "{char_emoji}";
const PAUSE_LABEL = `{T['pause']}`;
const RESUME_LABEL = `{T['resume']}`;
const CELEB_SUB = `{T['celeb_sub']}`;
const CANCEL_CONFIRM = `{T['cancel_confirm']}`;
const PHOTO_MSG = `{T['photo_msg']}`;
const APP_TITLE = `{T['title']}`;
let celebMsgText = '';
let remaining = TOTAL;
let paused = false;
let finished = false;
let interval = null;
let masterVolume = 0.7;
let muted = false;
let fontStep = 0;
const MIRROR_MODE = {'true' if mirror_mode else 'false'};
let photoDataUrl = null;
let photoTaken = false;
let photoTime = 0;
const SELFIE_ENABLED = {'true' if selfie_enabled else 'false'};
const EFFECT_CATS = [
  {{emoji:'🎩',items:['👑','🎩','🎀','🌸','🧙','😇']}},
  {{emoji:'👓',items:['⭐','💖','🕶️','🌈','🤪']}},
  {{emoji:'😺',items:['🤡','🐽','🥸','😺','👅']}},
  {{emoji:'🐾',items:['🐱','🐰','🦋','✨','💫']}},
  {{emoji:'🎪',items:['🎈','🎉','🪅','🎆','🪄','💀','👻']}},
];
let activeEffect=null, activeCat=-1;
let faceLandmarks=null, fmInstance=null;
let efxCanvas=null, efxCtx=null;
let animFr=0, fmReady=false;

const CIRC = 2 * Math.PI * 88;
const ring = document.getElementById('ring');
const display = document.getElementById('timeDisplay');
const stageArea = document.getElementById('stageArea');
const scalable = document.querySelector('.scalable');

// ========== i18n DATA ==========
const GUIDE_RAW = {guide_json};
const GUIDE = GUIDE_RAW.map(g => ({{
  ...g,
  msg: g.msg.replace(/\\{{name\\}}/g, NAME),
  guide: g.guide.replace(/\\{{name\\}}/g, NAME),
}}));

const CHEERS_RAW = {cheers_json};
const CHEERS = CHEERS_RAW.map(c => c.replace(/\\{{name\\}}/g, NAME));

const CELEB_MSGS_RAW = {celeb_msgs_json};
const CELEB_MSGS = CELEB_MSGS_RAW.map(c => c.replace(/\\{{name\\}}/g, NAME));

let cheerIdx = 0;
let lastStageIdx = -1;
let lastCheerTime = 0;

// ========== FONT SIZE CONTROL (px-based, persistent) ==========
const BASE_FONT_SIZE = 16;
function applyFontSize() {{
  const newSize = BASE_FONT_SIZE + fontStep * 2;
  scalable.style.fontSize = newSize + 'px';
  document.querySelectorAll('.guide').forEach(g => {{
    g.style.fontSize = (newSize + 1) + 'px';
  }});
  document.querySelectorAll('.stage > div > strong').forEach(el => {{
    el.style.fontSize = (newSize + 2) + 'px';
  }});
  const nameHdr = document.querySelector('.name-hdr');
  if (nameHdr) nameHdr.style.fontSize = (newSize + 3) + 'px';
}}
function changeFontSize(dir) {{
  fontStep = Math.max(-2, Math.min(4, fontStep + dir));
  applyFontSize();
}}

function getStage(pct) {{
  for (let i = GUIDE.length - 1; i >= 0; i--) {{
    if (pct <= GUIDE[i].pct) return i;
  }}
  return 0;
}}

// ========== AUDIO (with mobile resume fix) ==========
let audioCtx = null;
function ensureAudio() {{
  if (!audioCtx) {{
    audioCtx = new (window.AudioContext || window.webkitAudioContext)();
  }}
  if (audioCtx.state === 'suspended') {{
    audioCtx.resume();
  }}
}}
function vol() {{ return muted ? 0 : masterVolume; }}

// Robust audio recovery for mobile app switching
function tryResumeAudio() {{
  if (audioCtx && audioCtx.state === 'suspended') {{
    audioCtx.resume().catch(() => {{}});
  }}
}}
function restartBgmIfNeeded() {{
  if (!finished && !paused && !muted) {{
    stopBgm();
    setTimeout(() => {{
      if (!bgmTimer && !muted && !paused && !finished) startBgm();
    }}, 150);
  }}
}}

document.addEventListener('visibilitychange', () => {{
  if (document.visibilityState === 'visible') {{
    tryResumeAudio();
    setTimeout(tryResumeAudio, 100);
    setTimeout(tryResumeAudio, 300);
    setTimeout(tryResumeAudio, 1000);
    restartBgmIfNeeded();
  }}
}});

window.addEventListener('pageshow', (e) => {{
  tryResumeAudio();
  setTimeout(tryResumeAudio, 100);
  setTimeout(tryResumeAudio, 500);
  if (e.persisted) restartBgmIfNeeded();
}});

window.addEventListener('focus', () => {{
  tryResumeAudio();
  if (!finished && !paused && !muted && !bgmTimer) startBgm();
}});

// Persistent touch/click handler to unlock audio on mobile
function resumeAudioOnInteraction() {{
  if (audioCtx && audioCtx.state === 'suspended') {{
    audioCtx.resume().then(() => {{
      if (!finished && !paused && !muted && !bgmTimer) startBgm();
    }}).catch(() => {{}});
  }}
}}
document.addEventListener('touchstart', resumeAudioOnInteraction);
document.addEventListener('click', resumeAudioOnInteraction);

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

function playGermCatch() {{
  if (muted) return;
  ensureAudio();
  const v = vol();
  const o = audioCtx.createOscillator();
  const g = audioCtx.createGain();
  o.type = 'square'; o.frequency.value = 300;
  o.frequency.exponentialRampToValueAtTime(80, audioCtx.currentTime + 0.3);
  g.gain.setValueAtTime(0.15 * v, audioCtx.currentTime);
  g.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.3);
  o.connect(g); g.connect(audioCtx.destination);
  o.start(); o.stop(audioCtx.currentTime + 0.3);
}}

// BGM
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
    if (n.f > 0) {{
      const o = audioCtx.createOscillator();
      const g = audioCtx.createGain();
      o.type = 'sine'; o.frequency.value = n.f;
      g.gain.setValueAtTime(0.14 * v, audioCtx.currentTime);
      g.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + n.d);
      o.connect(g); g.connect(audioCtx.destination);
      o.start(); o.stop(audioCtx.currentTime + n.d);
    }}
    if (bgmBeat % 2 === 0) {{
      const b = audioCtx.createOscillator();
      const bg = audioCtx.createGain();
      b.type = 'sine'; b.frequency.value = 196;
      bg.gain.setValueAtTime(0.1 * v, audioCtx.currentTime);
      bg.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.15);
      b.connect(bg); bg.connect(audioCtx.destination);
      b.start(); b.stop(audioCtx.currentTime + 0.15);
    }}
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

// ========== GERM CATCHING EFFECT ==========
const GERM_EMOJIS = ['🦠','🦠','🦠','💀','👾','🧫'];
let lastGermTime = 0;

function spawnGerm() {{
  const now = Date.now();
  if (now - lastGermTime < 4000) return;
  lastGermTime = now;

  const container = document.getElementById('app');
  const germ = document.createElement('div');
  germ.className = 'germ';
  germ.textContent = GERM_EMOJIS[Math.floor(Math.random()*GERM_EMOJIS.length)];
  // Position only in the character/timer ring area (top portion)
  const x = 10 + Math.random() * 80;
  const timerRing = document.getElementById('timerRing');
  const ringRect = timerRing.getBoundingClientRect();
  const contRect = container.getBoundingClientRect();
  const yMin = Math.max(0, ringRect.top - contRect.top - 20);
  const yMax = ringRect.bottom - contRect.top + 10;
  const y = yMin + Math.random() * (yMax - yMin);
  germ.style.left = x + '%';
  germ.style.top = y + 'px';
  container.appendChild(germ);

  setTimeout(() => {{
    const sparks = ['✨','💥','⚡','💫'];
    for (let i = 0; i < 4; i++) {{
      const burst = document.createElement('div');
      burst.className = 'germ-burst';
      burst.textContent = sparks[i];
      burst.style.left = x + '%';
      burst.style.top = y + 'px';
      const angle = (Math.PI * 2 * i) / 4;
      burst.style.setProperty('--dx', Math.cos(angle) * 40 + 'px');
      burst.style.setProperty('--dy', Math.sin(angle) * 40 + 'px');
      container.appendChild(burst);
      setTimeout(() => burst.remove(), 800);
    }}
    playGermCatch();
  }}, 500);

  setTimeout(() => germ.remove(), 1200);
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

  if (idx !== lastStageIdx) {{
    lastStageIdx = idx;
    const st = GUIDE[idx];
    stageArea.innerHTML =
      '<div class="emoji">' + st.emoji + '</div>' +
      '<div><strong>' + st.msg + '</strong></div>' +
      '<div class="guide">' + st.guide + '</div>';
    applyFontSize();
    if (idx > 0) playStageUp();
    lastCheerTime = elapsed;
  }}
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
        applyFontSize();
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
  if (remaining > 5 && remaining % 8 === 0) spawnGerm();
  render();
  if (MIRROR_MODE && SELFIE_ENABLED && !photoTaken && remaining > 0 && remaining === photoTime) {{
    startPhotoCountdown();
  }}
  if (remaining <= 0) finish();
}}

function finish() {{
  finished = true;
  clearInterval(interval); stopBgm();
  if (MIRROR_MODE) stopCamera();
  playCelebration(); spawnConfetti();
  document.getElementById('timerScreen').style.display = 'none';
  const cel = document.getElementById('celebScreen');
  cel.style.display = 'flex';
  celebMsgText = CELEB_MSGS[Math.floor(Math.random()*CELEB_MSGS.length)];
  document.getElementById('celebMsg').textContent = celebMsgText;
  document.getElementById('celebSub').textContent = CELEB_SUB;
  if (photoDataUrl) {{
    document.getElementById('celebPhotoWrap').style.display = 'block';
    document.getElementById('celebPhoto').src = photoDataUrl;
    document.getElementById('celebPhotoLabel').textContent = PHOTO_MSG;
    document.getElementById('shareRow').style.display = 'flex';
  }}
  setTimeout(spawnConfetti, 1500);
}}

function togglePause() {{
  paused = !paused;
  document.getElementById('pauseBtn').innerHTML = paused ? RESUME_LABEL : PAUSE_LABEL;
  if (paused) stopBgm(); else startBgm();
}}

function cancelTimer() {{
  if (!confirm(CANCEL_CONFIRM)) return;
  clearInterval(interval); stopBgm();
  finished = false; paused = false;
  remaining = TOTAL; lastStageIdx = -1;
  lastCheerTime = 0; cheerIdx = 0;
  // Send message to Streamlit to reload
  try {{ window.parent.location.reload(); }} catch(e) {{
    // fallback: hide timer, show nothing
    document.getElementById('timerScreen').style.display = 'none';
  }}
}}

function addTime(sec) {{
  if (finished) return;
  remaining += sec; render();
}}

function startBrushing() {{
  // Transition from pre-start to timer
  document.getElementById('preStart').style.display = 'none';
  document.getElementById('timerElements').style.display = 'block';
  document.getElementById('btnRow').style.display = 'flex';
  initPhotoTime();
  render();
  interval = setInterval(tick, 1000);
  startBgm();
}}

function resetTimer() {{
  finished = false; paused = false;
  remaining = TOTAL; lastStageIdx = -1;
  document.getElementById('celebPhotoWrap').style.display = 'none';
  document.getElementById('shareRow').style.display = 'none';
  lastCheerTime = 0; cheerIdx = 0;
  clearInterval(interval); stopBgm();
  document.getElementById('timerScreen').style.display = 'block';
  document.getElementById('celebScreen').style.display = 'none';
  document.getElementById('pauseBtn').innerHTML = PAUSE_LABEL;
  if (MIRROR_MODE) {{
    startCamera(); if(fmReady) efxLoop();
    document.getElementById('preStart').style.display = 'flex';
    document.getElementById('timerElements').style.display = 'none';
    document.getElementById('btnRow').style.display = 'none';
  }} else {{
    initPhotoTime();
    render();
    interval = setInterval(tick, 1000);
    startBgm();
  }}
}}

function restart() {{ resetTimer(); }}

// ========== FACE EFFECTS ==========
function selectCat(idx) {{
  activeCat=idx; activeEffect=null;
  const items=document.getElementById('effectItems');
  const wrap=document.getElementById('effectItemsWrap');
  document.querySelectorAll('.effect-cat-btn').forEach((b,i)=>b.classList.toggle('active',i===idx+1));
  if(idx<0){{items.innerHTML='';wrap.style.display='none';return;}}
  wrap.style.display='block';
  items.innerHTML=EFFECT_CATS[idx].items.map(e=>
    `<button class="effect-item-btn" onclick="selectEffect('${{e}}')">${{e}}</button>`
  ).join('');
}}
function selectEffect(e){{
  activeEffect=(activeEffect===e)?null:e;
  document.querySelectorAll('.effect-item-btn').forEach(b=>
    b.classList.toggle('active',b.textContent===activeEffect));
}}

async function loadFaceMesh(){{
  const el=document.getElementById('effectLoading');
  if(el)el.style.display='block';
  try{{
    await new Promise((res,rej)=>{{
      const s=document.createElement('script');
      s.src='https://cdn.jsdelivr.net/npm/@mediapipe/face_mesh@0.4/face_mesh.js';
      s.onload=res;s.onerror=rej;document.head.appendChild(s);
    }});
    fmInstance=new FaceMesh({{
      locateFile:f=>`https://cdn.jsdelivr.net/npm/@mediapipe/face_mesh@0.4/${{f}}`
    }});
    fmInstance.setOptions({{
      maxNumFaces:1,refineLandmarks:false,
      minDetectionConfidence:0.5,minTrackingConfidence:0.5
    }});
    fmInstance.onResults(r=>{{
      faceLandmarks=(r.multiFaceLandmarks&&r.multiFaceLandmarks.length>0)
        ?r.multiFaceLandmarks[0]:null;
    }});
    await fmInstance.initialize();
    fmReady=true;
    if(el)el.style.display='none';
    efxLoop();
  }}catch(e){{
    console.log('FaceMesh failed:',e);
    if(el){{el.textContent='⚠️';}}
  }}
}}

function initEfxCanvas(){{
  efxCanvas=document.getElementById('effectCanvas');
  if(!efxCanvas)return;
  const mc=document.getElementById('mirrorContainer');
  efxCanvas.width=mc.clientWidth;
  efxCanvas.height=mc.clientHeight;
  efxCtx=efxCanvas.getContext('2d');
}}

async function efxLoop(){{
  if(finished||!fmReady)return;
  const v=document.getElementById('mirrorVideo');
  if(v&&v.readyState>=2&&fmInstance){{
    try{{await fmInstance.send({{image:v}});}}catch(e){{}}
  }}
  renderEfx();
  animFr++;
  requestAnimationFrame(efxLoop);
}}

function _d(a,b){{return Math.hypot(a.x-b.x,a.y-b.y);}}

function mapPts(lm,w,h,objFit){{
  if(objFit){{
    const v=document.getElementById('mirrorVideo');
    const vw=v.videoWidth||640,vh=v.videoHeight||480;
    const sc=Math.max(w/vw,h/vh);
    const dw=vw*sc,dh=vh*sc,ox=(w-dw)/2,oy=(h-dh)/2;
    return lm.map(l=>({{x:w-(l.x*dw+ox),y:l.y*dh+oy}}));
  }}
  return lm.map(l=>({{x:(1-l.x)*w,y:l.y*h}}));
}}

function renderEfx(){{
  if(!efxCtx)return;
  efxCtx.clearRect(0,0,efxCanvas.width,efxCanvas.height);
  if(!activeEffect||!faceLandmarks)return;
  const pts=mapPts(faceLandmarks,efxCanvas.width,efxCanvas.height,true);
  drawEfx(efxCtx,activeEffect,pts,animFr);
}}

function renderEfxCapture(ctx,w,h){{
  if(!activeEffect||!faceLandmarks)return;
  const pts=mapPts(faceLandmarks,w,h,false);
  drawEfx(ctx,activeEffect,pts,animFr);
}}

function drawEfx(ctx,eff,p,fr){{
  const top=p[10],chin=p[152],nose=p[1],lE=p[33],rE=p[263];
  const mth=p[0],lEar=p[234],rEar=p[454];
  const s=_d(top,chin);
  const eyeC={{x:(lE.x+rE.x)/2,y:(lE.y+rE.y)/2}};
  ctx.textAlign='center';ctx.textBaseline='middle';
  switch(eff){{
  /* ===== HEAD ===== */
  case '👑':ctx.font=`${{s*.55}}px sans-serif`;ctx.fillText('👑',top.x,top.y-s*.15);break;
  case '🎩':ctx.font=`${{s*.6}}px sans-serif`;ctx.fillText('🎩',top.x,top.y-s*.22);break;
  case '🎀':ctx.font=`${{s*.35}}px sans-serif`;ctx.fillText('🎀',top.x+s*.3,top.y-s*.05);break;
  case '🌸':{{
    ctx.font=`${{s*.2}}px sans-serif`;
    for(let i=0;i<5;i++){{
      const a=-Math.PI*.8+i*Math.PI*.4,r=s*.35;
      ctx.fillText('🌸',top.x+Math.cos(a)*r,top.y+Math.sin(a)*r*.5-s*.08);
    }}break;
  }}
  /* ===== GLASSES ===== */
  case '⭐':{{
    ctx.font=`${{s*.28}}px sans-serif`;
    ctx.fillText('⭐',lE.x,lE.y);ctx.fillText('⭐',rE.x,rE.y);break;
  }}
  case '💖':{{
    ctx.font=`${{s*.28}}px sans-serif`;
    ctx.fillText('💖',lE.x,lE.y);ctx.fillText('💖',rE.x,rE.y);break;
  }}
  case '🕶️':ctx.font=`${{s*.5}}px sans-serif`;ctx.fillText('🕶️',eyeC.x,eyeC.y);break;
  case '🌈':{{
    ctx.lineWidth=s*.03;
    const cols=['#ff0000','#ff7700','#ffff00','#00ff00','#0077ff','#8b00ff'];
    for(let i=0;i<cols.length;i++){{
      ctx.strokeStyle=cols[i];ctx.beginPath();
      ctx.arc(top.x,top.y+s*.05,s*.38+i*s*.025,Math.PI,0);ctx.stroke();
    }}break;
  }}
  /* ===== FACE ===== */
  case '🤡':{{
    ctx.fillStyle='#ff1744';ctx.beginPath();
    ctx.arc(nose.x,nose.y,s*.08,0,Math.PI*2);ctx.fill();
    ctx.fillStyle='rgba(255,100,100,0.3)';ctx.beginPath();
    ctx.arc(nose.x,nose.y,s*.12,0,Math.PI*2);ctx.fill();break;
  }}
  case '🐽':ctx.font=`${{s*.3}}px sans-serif`;ctx.fillText('🐽',nose.x,nose.y);break;
  case '🥸':{{
    ctx.strokeStyle='#5d4037';ctx.lineWidth=s*.03;ctx.lineCap='round';
    [-1,1].forEach(d=>{{
      ctx.beginPath();ctx.moveTo(nose.x+d*s*.02,mth.y-s*.05);
      ctx.quadraticCurveTo(nose.x+d*s*.15,mth.y-s*.1,nose.x+d*s*.2,mth.y-s*.02);
      ctx.quadraticCurveTo(nose.x+d*s*.22,mth.y+s*.02,nose.x+d*s*.18,mth.y-s*.06);
      ctx.stroke();
    }});break;
  }}
  case '😺':{{
    ctx.strokeStyle='#555';ctx.lineWidth=s*.015;ctx.lineCap='round';
    [-1,1].forEach(d=>{{
      for(let i=-1;i<=1;i++){{
        ctx.beginPath();ctx.moveTo(nose.x+d*s*.04,nose.y+s*.02);
        ctx.lineTo(nose.x+d*s*.25,nose.y+i*s*.06);ctx.stroke();
      }}
    }});
    ctx.fillStyle='#ff69b4';ctx.beginPath();
    ctx.arc(nose.x,nose.y+s*.01,s*.035,0,Math.PI*2);ctx.fill();break;
  }}
  /* ===== ANIMALS ===== */
  case '🐱':{{
    const es=s*.22;
    [-1,1].forEach(d=>{{
      const ex=top.x+d*s*.28,ey=top.y-s*.05;
      ctx.fillStyle='#ff9800';ctx.beginPath();
      ctx.moveTo(ex-es*.5*d,ey);ctx.lineTo(ex,ey-es);ctx.lineTo(ex+es*.5*d,ey);ctx.fill();
      ctx.fillStyle='#ffe0b2';ctx.beginPath();
      ctx.moveTo(ex-es*.3*d,ey-es*.1);ctx.lineTo(ex,ey-es*.7);
      ctx.lineTo(ex+es*.3*d,ey-es*.1);ctx.fill();
    }});
    ctx.fillStyle='#ff69b4';ctx.beginPath();
    ctx.arc(nose.x,nose.y,s*.03,0,Math.PI*2);ctx.fill();break;
  }}
  case '🐰':{{
    [-1,1].forEach(d=>{{
      const ex=top.x+d*s*.18,ey=top.y-s*.1;
      ctx.fillStyle='#fff';ctx.beginPath();
      ctx.ellipse(ex,ey-s*.22,s*.08,s*.22,d*.15,0,Math.PI*2);ctx.fill();
      ctx.strokeStyle='#eee';ctx.lineWidth=1;ctx.stroke();
      ctx.fillStyle='#ffb6c1';ctx.beginPath();
      ctx.ellipse(ex,ey-s*.2,s*.045,s*.15,d*.15,0,Math.PI*2);ctx.fill();
    }});break;
  }}
  case '🦋':{{
    const bx=nose.x+Math.sin(fr*.06)*s*.5;
    const by=eyeC.y-s*.2+Math.cos(fr*.04)*s*.15;
    ctx.font=`${{s*.3}}px sans-serif`;ctx.fillText('🦋',bx,by);
    for(let i=1;i<=3;i++){{
      ctx.globalAlpha=1-i*.25;
      ctx.font=`${{s*(.12-i*.02)}}px sans-serif`;
      ctx.fillText('✨',bx-Math.sin((fr-i*5)*.06)*s*.1*i,by+i*s*.06);
    }}ctx.globalAlpha=1;break;
  }}
  case '✨':{{
    for(let i=0;i<6;i++){{
      const a=fr*.04+i*Math.PI*2/6;
      const r=s*.5+Math.sin(fr*.06+i)*s*.08;
      const sz=s*(.12+Math.sin(fr*.08+i*2)*.04);
      ctx.font=`${{sz}}px sans-serif`;
      ctx.fillText('✨',nose.x+Math.cos(a)*r,nose.y+Math.sin(a)*r*.7);
    }}break;
  }}
  /* ===== PARTY ===== */
  case '🎈':{{
    [-1,1].forEach((d,i)=>{{
      const bx=lEar.x*(1-i)+rEar.x*i;
      const by=top.y-s*.4+Math.sin(fr*.05+i*2)*s*.06;
      ctx.font=`${{s*.35}}px sans-serif`;
      ctx.fillText(i?'🎈':'🎈',bx+d*s*.1,by);
      ctx.strokeStyle='rgba(200,200,200,0.6)';ctx.lineWidth=1;
      ctx.beginPath();ctx.moveTo(bx+d*s*.1,by+s*.15);
      ctx.lineTo(bx+d*s*.05,top.y+s*.1);ctx.stroke();
    }});break;
  }}
  case '🎉':{{
    ctx.font=`${{s*.5}}px sans-serif`;ctx.fillText('🥳',top.x,top.y-s*.25);
    for(let i=0;i<8;i++){{
      const a=fr*.08+i*Math.PI/4;
      const r=s*.4+Math.sin(fr*.1+i)*s*.1;
      const cols=['#ff1744','#ffea00','#00e676','#2979ff','#d500f9','#ff9100'];
      ctx.fillStyle=cols[i%cols.length];
      ctx.globalAlpha=0.7+Math.sin(fr*.1+i)*.3;
      ctx.beginPath();
      ctx.arc(top.x+Math.cos(a)*r,top.y-s*.1+Math.sin(a)*r*.5,s*.025,0,Math.PI*2);
      ctx.fill();
    }}ctx.globalAlpha=1;break;
  }}
  case '🪅':{{
    for(let i=0;i<12;i++){{
      const x=nose.x+(Math.sin(i*73+fr*.02)-.5)*s*1.2;
      const y=top.y-s*.5+((fr*1.5+i*60)%(s*2));
      const cols=['#ff1744','#ffea00','#00e676','#2979ff','#d500f9','#ff9100','#00bcd4','#e91e63'];
      ctx.fillStyle=cols[i%cols.length];
      ctx.globalAlpha=0.8;
      const sz=s*.02+Math.sin(i+fr*.05)*s*.01;
      ctx.save();ctx.translate(x,y);ctx.rotate(fr*.1+i);
      ctx.fillRect(-sz,-sz*.5,sz*2,sz);ctx.restore();
    }}ctx.globalAlpha=1;break;
  }}
  case '🎆':{{
    for(let b=0;b<3;b++){{
      const cx=nose.x+Math.sin(b*2.5)*s*.4;
      const cy=top.y-s*.2+Math.cos(b*3.7)*s*.15;
      const phase=(fr*.06+b*2.1)%6.28;
      const burst=Math.sin(phase)*.5+.5;
      const cols=['#ff1744','#ffea00','#00e5ff','#d500f9','#ff9100','#76ff03'];
      for(let r=0;r<8;r++){{
        const a=r*Math.PI/4+b;
        const dist=burst*s*.3;
        ctx.fillStyle=cols[(r+b)%cols.length];
        ctx.globalAlpha=burst*.8;
        ctx.beginPath();
        ctx.arc(cx+Math.cos(a)*dist,cy+Math.sin(a)*dist,s*.02*burst,0,Math.PI*2);
        ctx.fill();
      }}
    }}ctx.globalAlpha=1;break;
  }}
  /* ===== MAGIC ===== */
  case '🧙':{{
    const hw=s*.45,hh=s*.55;
    ctx.fillStyle='#3f51b5';ctx.beginPath();
    ctx.moveTo(top.x,top.y-hh-s*.1);
    ctx.lineTo(top.x-hw,top.y);ctx.lineTo(top.x+hw,top.y);ctx.closePath();ctx.fill();
    ctx.fillStyle='#ffd54f';ctx.beginPath();
    ctx.arc(top.x,top.y-hh-s*.05,s*.06,0,Math.PI*2);ctx.fill();
    ctx.fillStyle='#ffd54f';
    const stars=['✦','✦','✦'];
    ctx.font=`${{s*.08}}px sans-serif`;
    stars.forEach((_,i)=>{{
      ctx.fillText('✦',top.x+(-1+i)*s*.15,top.y-s*.15-i*s*.12);
    }});break;
  }}
  case '😇':{{
    ctx.strokeStyle='#ffd54f';ctx.lineWidth=s*.035;
    ctx.shadowColor='#ffd54f';ctx.shadowBlur=s*.1;
    ctx.beginPath();
    ctx.ellipse(top.x,top.y-s*.2,s*.2,s*.06,0,0,Math.PI*2);
    ctx.stroke();ctx.shadowBlur=0;
    const glow=0.3+Math.sin(fr*.08)*.2;
    ctx.strokeStyle=`rgba(255,213,79,${{glow}})`;ctx.lineWidth=s*.06;
    ctx.beginPath();
    ctx.ellipse(top.x,top.y-s*.2,s*.22,s*.07,0,0,Math.PI*2);
    ctx.stroke();break;
  }}
  case '🪄':{{
    const wx=rEar.x+s*.1,wy=eyeC.y;
    ctx.save();ctx.translate(wx,wy);ctx.rotate(-0.5+Math.sin(fr*.06)*.2);
    ctx.fillStyle='#5d4037';ctx.fillRect(-s*.02,-s*.35,s*.04,s*.35);
    ctx.fillStyle='#fff';ctx.fillRect(-s*.03,-s*.38,s*.06,s*.06);
    ctx.restore();
    for(let i=0;i<5;i++){{
      const a=fr*.1+i*1.26;
      const r2=s*.15+i*s*.04;
      ctx.globalAlpha=1-i*.18;
      ctx.font=`${{s*(.08-i*.01)}}px sans-serif`;
      ctx.fillText('✨',wx+Math.cos(a)*r2,wy-s*.35+Math.sin(a)*r2);
    }}ctx.globalAlpha=1;break;
  }}
  case '💫':{{
    for(let i=0;i<5;i++){{
      const a=fr*.05+i*Math.PI*2/5;
      const r2=s*.45;
      const x=nose.x+Math.cos(a)*r2;
      const y=nose.y+Math.sin(a)*r2*.7;
      const twinkle=0.5+Math.sin(fr*.12+i*1.5)*.5;
      ctx.globalAlpha=twinkle;
      ctx.font=`${{s*.15}}px sans-serif`;
      ctx.fillText('💫',x,y);
    }}
    ctx.globalAlpha=0.4+Math.sin(fr*.06)*.2;
    ctx.strokeStyle='#ffd54f';ctx.lineWidth=s*.01;
    ctx.beginPath();
    ctx.ellipse(nose.x,nose.y,s*.48,s*.35,fr*.01,0,Math.PI*2);
    ctx.stroke();ctx.globalAlpha=1;break;
  }}
  /* ===== FUNNY ===== */
  case '👅':{{
    ctx.font=`${{s*.3}}px sans-serif`;
    const ty=mth.y+s*.05+Math.sin(fr*.1)*s*.02;
    ctx.fillText('👅',mth.x,ty);break;
  }}
  case '🤪':{{
    const er=s*.09;
    [-1,1].forEach((d,i)=>{{
      const ex=d<0?lE.x:rE.x,ey=d<0?lE.y:rE.y;
      ctx.strokeStyle=i?'#ff1744':'#2979ff';ctx.lineWidth=s*.025;
      ctx.beginPath();
      for(let t=0;t<4*Math.PI;t+=.2){{
        const sr=er*(t/(4*Math.PI));
        const sx=ex+Math.cos(t+fr*.15*d)*sr;
        const sy=ey+Math.sin(t+fr*.15*d)*sr;
        t===0?ctx.moveTo(sx,sy):ctx.lineTo(sx,sy);
      }}ctx.stroke();
    }});break;
  }}
  case '💀':{{
    ctx.font=`${{s*.7}}px sans-serif`;
    ctx.globalAlpha=0.5+Math.sin(fr*.08)*.15;
    ctx.fillText('💀',nose.x,nose.y);
    ctx.globalAlpha=1;break;
  }}
  case '👻':{{
    for(let i=0;i<4;i++){{
      const a=fr*.04+i*Math.PI/2;
      const r2=s*.55+Math.sin(fr*.06+i)*s*.08;
      const gy=Math.sin(fr*.05+i*1.5)*s*.1;
      ctx.font=`${{s*.2}}px sans-serif`;
      ctx.globalAlpha=0.6+Math.sin(fr*.08+i)*.3;
      ctx.fillText('👻',nose.x+Math.cos(a)*r2,nose.y+Math.sin(a)*r2*.6+gy);
    }}ctx.globalAlpha=1;break;
  }}
  }}
}}

// ========== PHOTO CAPTURE ==========
function initPhotoTime() {{
  photoDataUrl = null; photoTaken = false;
  if (MIRROR_MODE && SELFIE_ENABLED && TOTAL >= 30) {{
    const minR = Math.floor(TOTAL * 0.3);
    const maxR = Math.floor(TOTAL * 0.7);
    photoTime = minR + Math.floor(Math.random() * (maxR - minR));
  }}
}}

function startPhotoCountdown() {{
  photoTaken = true;
  const overlay = document.getElementById('photoCountdown');
  overlay.style.display = 'flex';
  let count = 3;
  overlay.textContent = count;
  playTick();
  const cdInterval = setInterval(() => {{
    count--;
    if (count > 0) {{
      overlay.textContent = count;
      playTick();
    }} else {{
      clearInterval(cdInterval);
      overlay.textContent = '📸';
      capturePhoto();
      setTimeout(() => {{ overlay.style.display = 'none'; }}, 600);
    }}
  }}, 1000);
}}

function capturePhoto() {{
  const video = document.getElementById('mirrorVideo');
  if (!video || !video.srcObject) return;
  const canvas = document.createElement('canvas');
  canvas.width = video.videoWidth || 640;
  canvas.height = video.videoHeight || 480;
  const ctx = canvas.getContext('2d');
  ctx.translate(canvas.width, 0);
  ctx.scale(-1, 1);
  ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
  ctx.setTransform(1,0,0,1,0,0);
  renderEfxCapture(ctx, canvas.width, canvas.height);
  photoDataUrl = canvas.toDataURL('image/jpeg', 0.85);
  // flash
  const flash = document.getElementById('photoFlash');
  flash.style.display = 'block';
  setTimeout(() => {{ flash.style.display = 'none'; }}, 200);
}}

// ========== CERTIFICATE CANVAS ==========
function rrect(ctx, x, y, w, h, r) {{
  ctx.beginPath();
  ctx.moveTo(x+r,y);
  ctx.lineTo(x+w-r,y); ctx.quadraticCurveTo(x+w,y,x+w,y+r);
  ctx.lineTo(x+w,y+h-r); ctx.quadraticCurveTo(x+w,y+h,x+w-r,y+h);
  ctx.lineTo(x+r,y+h); ctx.quadraticCurveTo(x,y+h,x,y+h-r);
  ctx.lineTo(x,y+r); ctx.quadraticCurveTo(x,y,x+r,y);
  ctx.closePath();
}}
function certWrap(ctx, text, x, y, maxW, lh) {{
  let line = '', curY = y;
  for (let i = 0; i < text.length; i++) {{
    const t = line + text[i];
    if (ctx.measureText(t).width > maxW && line) {{
      ctx.fillText(line, x, curY); line = text[i]; curY += lh;
    }} else {{ line = t; }}
  }}
  if (line) ctx.fillText(line, x, curY);
  return curY;
}}

function generateCertificate() {{
  return new Promise((resolve) => {{
    const W = 600, H = 880;
    const cv = document.createElement('canvas');
    cv.width = W; cv.height = H;
    const c = cv.getContext('2d');
    const font = '"Segoe UI","Apple SD Gothic Neo","Malgun Gothic",sans-serif';

    // background gradient
    const bg = c.createLinearGradient(0,0,W,H);
    bg.addColorStop(0,'#e0f7fa'); bg.addColorStop(1,'#f3e5f5');
    c.fillStyle = bg; c.fillRect(0,0,W,H);

    // gold double border
    c.strokeStyle = '#ffd54f'; c.lineWidth = 6;
    rrect(c,18,18,W-36,H-36,22); c.stroke();
    c.strokeStyle = 'rgba(255,213,79,0.35)'; c.lineWidth = 2;
    rrect(c,30,30,W-60,H-60,18); c.stroke();

    // star decorations (corners)
    c.font = '22px sans-serif'; c.textAlign = 'center';
    c.fillText('⭐',52,56); c.fillText('⭐',W-52,56);
    c.fillText('⭐',52,H-36); c.fillText('⭐',W-52,H-36);

    // title
    c.font = `bold 30px ${{font}}`; c.fillStyle = '#333'; c.textAlign = 'center';
    c.fillText(APP_TITLE, W/2, 82);

    // divider line
    c.strokeStyle = '#e0e0e0'; c.lineWidth = 1;
    c.beginPath(); c.moveTo(80,98); c.lineTo(W-80,98); c.stroke();

    // character emoji
    c.font = '68px sans-serif';
    c.fillText(CHAR_EMOJI, W/2, 175);

    // celebration message
    c.font = `bold 26px ${{font}}`; c.fillStyle = '#2e2e2e';
    const msgY = certWrap(c, celebMsgText, W/2, 220, W-100, 34);

    const drawBottom = (startY) => {{
      // sub message
      c.font = `17px ${{font}}`; c.fillStyle = '#555';
      const subY = certWrap(c, CELEB_SUB, W/2, startY, W-90, 24);

      // date
      const d = new Date();
      const ds = d.getFullYear()+'.' +
        String(d.getMonth()+1).padStart(2,'0')+'.' +
        String(d.getDate()).padStart(2,'0');
      c.font = `15px ${{font}}`; c.fillStyle = '#aaa';
      c.fillText(ds, W/2, subY + 42);

      // medal
      c.font = '48px sans-serif';
      c.fillText('🏅', W/2, subY + 98);

      resolve(cv.toDataURL('image/jpeg', 0.92));
    }};

    if (photoDataUrl) {{
      const img = new Image();
      img.onload = () => {{
        const maxPW = 320, maxPH = 280;
        const imgR = img.naturalWidth / img.naturalHeight;
        let pw, ph;
        if (imgR > maxPW / maxPH) {{ pw = maxPW; ph = Math.round(maxPW / imgR); }}
        else {{ ph = maxPH; pw = Math.round(maxPH * imgR); }}
        const px = (W-pw)/2, py = msgY + 32;

        // gold frame
        c.fillStyle = '#ffd54f';
        rrect(c, px-5, py-5, pw+10, ph+10, 14); c.fill();

        // photo clipped to rounded rect
        c.save();
        rrect(c, px, py, pw, ph, 10); c.clip();
        c.drawImage(img, px, py, pw, ph);

        // label overlay at bottom of photo
        c.fillStyle = 'rgba(0,0,0,0.45)';
        c.fillRect(px, py+ph-34, pw, 34);
        c.font = `bold 15px ${{font}}`; c.fillStyle = '#fff';
        c.textAlign = 'center';
        c.fillText(PHOTO_MSG, W/2, py+ph-12);
        c.restore();

        drawBottom(py + ph + 36);
      }};
      img.src = photoDataUrl;
    }} else {{
      drawBottom(msgY + 32);
    }}
  }});
}}

async function sharePhoto() {{
  try {{
    const certUrl = await generateCertificate();
    const blob = await (await fetch(certUrl)).blob();
    const file = new File([blob], 'brushing_cert_' + Date.now() + '.jpg', {{ type: 'image/jpeg' }});
    if (navigator.canShare && navigator.canShare({{ files: [file] }})) {{
      await navigator.share({{
        title: celebMsgText,
        text: PHOTO_MSG,
        files: [file]
      }});
    }} else if (navigator.share) {{
      await navigator.share({{ title: celebMsgText, text: PHOTO_MSG }});
    }} else {{
      downloadPhoto();
    }}
  }} catch(e) {{
    if (e.name !== 'AbortError') downloadPhoto();
  }}
}}

async function downloadPhoto() {{
  const certUrl = await generateCertificate();
  const a = document.createElement('a');
  a.href = certUrl;
  a.download = 'brushing_cert_' + Date.now() + '.jpg';
  a.click();
}}

// ========== MIRROR MODE CAMERA ==========
async function startCamera() {{
  try {{
    const stream = await navigator.mediaDevices.getUserMedia({{
      video: {{ facingMode: 'user', width: {{ ideal: 640 }}, height: {{ ideal: 480 }} }},
      audio: false
    }});
    document.getElementById('mirrorVideo').srcObject = stream;
  }} catch(err) {{
    document.getElementById('mirrorNoCam').style.display = 'block';
    document.getElementById('mirrorVideo').style.display = 'none';
  }}
}}
function stopCamera() {{
  const video = document.getElementById('mirrorVideo');
  if (video && video.srcObject) {{
    video.srcObject.getTracks().forEach(t => t.stop());
    video.srcObject = null;
  }}
}}

// ========== INIT ==========
if (MIRROR_MODE) {{
  // Mirror mode: show pre-start screen, don't start timer yet
  document.getElementById('mirrorContainer').style.display = 'block';
  document.querySelector('.char-face').style.display = 'none';
  document.getElementById('preStart').style.display = 'flex';
  document.getElementById('timerElements').style.display = 'none';
  document.getElementById('btnRow').style.display = 'none';
  startCamera();
  setTimeout(() => {{ initEfxCanvas(); loadFaceMesh(); }}, 200);
}} else {{
  // Basic mode: start timer immediately
  initPhotoTime();
  render();
  interval = setInterval(tick, 1000);
  startBgm();
}}

// Auto-scroll timer into view on start
setTimeout(() => {{
  try {{
    if (window.frameElement) {{
      window.frameElement.scrollIntoView({{behavior:'smooth', block:'center'}});
    }}
  }} catch(e) {{}}
}}, 300);
</script>
</body>
</html>
"""
    components.html(html, height=880 if mirror_mode else 700, scrolling=False)
