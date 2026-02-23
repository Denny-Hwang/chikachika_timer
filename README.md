# Chikachika Brushing Timer

An interactive brushing timer app that makes tooth-brushing fun for kids!

---

## Features

### Character Selection
Choose from 6 cute animal characters:
- Bunny | Bear | Cat | Dog | Fox | Frog

### Multi-language Support
Available in 5 languages:
- Korean (default) | English | Chinese | Spanish | Japanese

### Step-by-Step Brushing Guide
15-stage guide based on dental professional recommendations:
- Upper outer → Upper inner → Lower outer → Lower inner → Chewing surfaces → Tongue
- Each stage includes an emoji indicator and specific brushing instructions

### Sound System
- Background music (BGM) with auto-play
- Stage transition sound effects & encouragement sounds
- Volume control & mute toggle
- **Automatic audio recovery after mobile app switching** (AudioContext resume with retry)

### Germ-Catching Effects
Cavity germs appear periodically during brushing and get caught with animations.
Particle burst effects with sound play on each catch.

### Celebration
Confetti effects and congratulatory messages on brushing completion.

### Other Features
- **Font size control** (A-/A+) — persistent across stage changes
- **Add time** (+10s, +30s) — for extra brushing
- **Pause/Resume** — take a break mid-brush
- **Timer selection** — 1 min to 3 min (30-second increments)
- **Auto-scroll** — timer centers on screen when started

---

## How to Run

### Prerequisites
- Python 3.8+
- Streamlit

### Install & Run
```bash
pip install streamlit
streamlit run app.py
```

The app opens automatically at `http://localhost:8501`.

### Mobile Usage
Access from a smartphone browser on the same network at `http://<PC_IP>:8501`.

---

## Project Structure

```
chikachika_timer/
├── app.py            # Main app (Streamlit + embedded HTML/JS timer)
├── README.md
└── requirements.txt
```

---

## Tech Stack

| Area | Technology |
|------|-----------|
| Frontend | Streamlit, HTML5, CSS3, JavaScript (vanilla) |
| Audio | Web Audio API (AudioContext) |
| Animation | CSS Keyframes |
| i18n | Python dict-based multilingual system |

---

## Mobile Compatibility

- Tested on iOS Safari and Android Chrome
- Automatic audio recovery on app switch (background → foreground)
- Handles `visibilitychange`, `pageshow`, `focus` events and persistent `touchstart`/`click` unlock

---

## License

MIT License
