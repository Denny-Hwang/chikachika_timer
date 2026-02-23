# 🦷 치카치카 타이머 (Chikachika Brushing Timer)

아이들이 양치를 재미있게 할 수 있도록 도와주는 인터랙티브 타이머 앱입니다.

An interactive brushing timer app that makes tooth-brushing fun for kids!

---

## ✨ 주요 기능 / Features

### 🐾 캐릭터 선택 / Character Selection
6종의 귀여운 동물 캐릭터 중 선택할 수 있습니다.
- 🐰 토끼 Bunny | 🐻 곰 Bear | 🐱 고양이 Cat
- 🐶 강아지 Dog | 🦊 여우 Fox | 🐸 개구리 Frog

### 🌐 다국어 지원 / Multi-language Support
5개 언어를 지원합니다:
- 🇰🇷 한국어 (기본) | 🇺🇸 English | 🇨🇳 中文 | 🇪🇸 Español | 🇯🇵 日本語

### ⏱️ 양치 가이드 / Brushing Guide
치과 전문가의 양치 교본에 기반한 15단계 가이드:
- 윗니 바깥 → 윗니 안쪽 → 아랫니 바깥 → 아랫니 안쪽 → 씹는 면 → 혀
- 각 단계마다 연관 이모티콘과 구체적인 안내 제공

### 🎵 사운드 시스템 / Sound System
- 배경 음악 (BGM) 자동 재생
- 단계 전환 효과음 & 응원 사운드
- 볼륨 조절 & 음소거 지원
- **모바일 앱 전환 후 자동 오디오 복구** (AudioContext resume)

### 🦠 충치균 잡기 효과 / Germ-Catching Effects
양치 중 주기적으로 충치균(🦠)이 나타나고 잡히는 애니메이션이 재생됩니다.
격파 시 파티클 효과(✨💥⚡💫)와 함께 사운드가 출력됩니다.

### 🎉 양치 완료 축하 / Celebration
양치 완료 시 컨페티 효과와 축하 메시지가 표시됩니다.

### 🔤 기타 기능
- **글꼴 크기 조절** (A-/A+) — 아이 눈높이에 맞게 조절 가능
- **시간 추가** (+10초, +30초) — 더 닦고 싶을 때
- **일시정지/재개** — 중간에 잠시 멈출 수 있음
- **타이머 선택** — 1분 ~ 3분 (30초 단위)

---

## 🚀 실행 방법 / How to Run

### 필요 조건 / Prerequisites
- Python 3.8+
- Streamlit

### 설치 및 실행 / Install & Run
```bash
pip install streamlit
streamlit run app.py
```

브라우저에서 자동으로 `http://localhost:8501` 이 열립니다.

### 모바일 사용 / Mobile Usage
같은 네트워크의 스마트폰 브라우저에서 `http://<PC_IP>:8501` 로 접속하면 됩니다.

---

## 📁 프로젝트 구조 / Project Structure

```
chikachika_timer/
├── app.py          # 메인 앱 (Streamlit + embedded HTML/JS timer)
├── README.md       # 이 문서
└── requirements.txt
```

---

## 🛠️ 기술 스택 / Tech Stack

| 영역 | 기술 |
|------|------|
| Frontend | Streamlit, HTML5, CSS3, JavaScript (vanilla) |
| Audio | Web Audio API (AudioContext) |
| Animation | CSS Keyframes |
| i18n | Python dict 기반 다국어 시스템 |

---

## 📱 모바일 호환성 / Mobile Compatibility

- iOS Safari, Android Chrome 에서 테스트됨
- 앱 전환(백그라운드 → 포그라운드) 시 오디오 자동 복구
- `visibilitychange`, `pageshow` 이벤트, `touchstart` unlock 처리

---

## 📄 License

MIT License
