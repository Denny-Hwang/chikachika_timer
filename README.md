# Chikachika Brushing Timer 🦷

An interactive brushing timer app that makes tooth-brushing fun for kids!

---

## Features

### Two Modes
- **Basic Mode** — Character animation with timer and step-by-step guide
- **Mirror Mode (default)** — Front camera shows the user brushing in real-time with AR face effects

### AR Face Effects (Mirror Mode)
Face-tracking effects powered by MediaPipe Face Mesh:
- **🎩 Head** — Crown, top hat, ribbon, flowers, wizard hat, halo
- **👓 Eyes** — Stars, hearts, sunglasses, rainbow, spiral eyes
- **😺 Face** — Clown nose, pig nose, mustache, whiskers, tongue
- **🐾 Animals** — Cat ears, bunny ears, butterfly, sparkles, orbiting stars
- **🎪 Fun** — Balloons, party hat, confetti, fireworks, magic wand, skull, ghosts

Effects are selected before brushing starts so kids stay focused during brushing.

### Selfie & Certificate
- Random selfie capture during brushing (3-second countdown)
- AR effects are included in the captured photo
- Celebration certificate with decorations, message, photo, and date
- Share via SNS (Web Share API) or download as image

### Step-by-Step Brushing Guide
15-stage guide based on dental professional recommendations:
- Upper outer → Upper inner → Lower outer → Lower inner → Chewing surfaces → Tongue
- Each stage includes an emoji indicator and specific brushing instructions

### Multi-language Support
Available in 5 languages:
- Korean (default) | English | Chinese | Spanish | Japanese

### Character Selection
Choose from 6 cute animal characters:
- Bunny | Bear | Cat | Dog | Fox | Frog

### Sound System
- Background music (BGM) with auto-play
- Stage transition sound effects & encouragement sounds
- Volume control & mute toggle
- Automatic audio recovery after mobile app switching

### Germ-Catching Effects
Cavity germs appear periodically during brushing and get caught with burst animations.

### Celebration
Confetti effects and congratulatory messages on brushing completion.

### Other Features
- **Font size control** (A-/A+)
- **Add time** (+10s, +30s)
- **Pause/Resume**
- **Timer selection** — 1 min to 3 min (30-second increments)

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
├── app.py            # Main app (Streamlit + embedded HTML/CSS/JS)
├── LICENSE
├── README.md
└── requirements.txt
```

---

## Tech Stack

| Area | Technology |
|------|-----------|
| Framework | Streamlit |
| Frontend | HTML5, CSS3, JavaScript (vanilla) |
| AR/Face Tracking | MediaPipe Face Mesh |
| Audio | Web Audio API (AudioContext) |
| Camera | getUserMedia API |
| Sharing | Web Share API, Canvas API |
| i18n | Python dict-based multilingual system |

---

## Mobile Compatibility

- Tested on iOS Safari and Android Chrome
- Automatic audio recovery on app switch
- Camera permission handling with graceful fallback

---

## License

Copyright (c) 2026 Denny Hwang. All Rights Reserved.

This software is proprietary. See [LICENSE](LICENSE) for details.
