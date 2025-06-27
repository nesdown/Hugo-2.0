# Hugo 2.0 - AI Personal Assistant

<div align="center">

![Hugo 2.0](https://img.shields.io/badge/Hugo-2.0-blue.svg)
![Python](https://img.shields.io/badge/Python-3.7+-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

*An advanced AI-powered personal assistant with voice interaction, face recognition, and multi-modal capabilities*

</div>

## 🚀 Overview

Hugo 2.0 is a sophisticated AI personal assistant that combines voice recognition, text-to-speech synthesis, computer vision, and web technologies to create an interactive, intelligent companion. Built with Python and featuring a modern web interface, Hugo can recognize faces, analyze objects, provide weather updates, parse deals and events, and engage in natural conversations.

## ✨ Key Features

### 🎤 Voice Interaction
- **Speech Recognition**: Real-time speech-to-text conversion using Google's API
- **Text-to-Speech**: Cross-platform synthesis with Windows SAPI and Linux Speech Dispatcher
- **Natural Conversations**: Context-aware dialog management with online and offline response modes

### 👥 Face Recognition & Friendship System
- **Smart Recognition**: Advanced face detection and identification using OpenCV
- **User Database**: Automatic user registration and personalized greetings
- **Memory System**: Remembers users and builds lasting relationships

### 🔍 Computer Vision
- **Object Analysis**: Real-time object detection and scene analysis
- **Environmental Awareness**: Describes surroundings using AI-powered vision
- **Camera Integration**: Seamless integration with system cameras

### 🌐 Information Services
- **Weather Updates**: Real-time weather information with voice reports
- **Deal Parsing**: Shopping deals aggregation and notifications
- **Event Tracking**: Event information collection and reminders

### 💻 Modern Web Interface
- **Responsive Design**: Beautiful, animated web interface built with HTML5/CSS3
- **Real-time Feedback**: Dynamic facial expressions and visual feedback
- **Cross-platform**: Works on Windows and Linux systems

## 🏗️ Architecture

Hugo 2.0 follows a layered architecture design:

```
┌─────────────────────────────────────┐
│          Web Interface              │
│        (HTML/CSS/JavaScript)        │
├─────────────────────────────────────┤
│       Request Processing            │
│         (Python/Eel)               │
├─────────────────────────────────────┤
│      Artificial Intelligence       │
│    (Speech, Vision, NLP)           │
├─────────────────────────────────────┤
│       Network Analysis             │
│    (APIs, Data Parsing)            │
├─────────────────────────────────────┤
│      Hardware Interface            │
│   (Camera, Microphone, Speakers)   │
└─────────────────────────────────────┘
```

## 📋 Prerequisites

- Python 3.7 or higher
- System microphone and speakers
- Camera (for face recognition and object analysis)
- Internet connection (for online features)

### System-Specific Requirements

**Windows:**
- Windows 10 or later
- Windows Speech API (SAPI)
- Visual C++ Redistributables

**Linux:**
- Ubuntu 18.04+ or equivalent
- Speech Dispatcher
- RHVoice TTS engine
- ALSA/PulseAudio

## 🔧 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/Hugo-2.0.git
cd Hugo-2.0
```

2. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

3. **Create necessary directories:**
```bash
mkdir database
mkdir execs
```

4. **Configure the system:**
   - Edit `config.cfg` to set your preferred language and settings
   - Add API keys for weather services if needed

5. **Install system-specific dependencies:**

**For Windows:**
```bash
# Install Windows-specific TTS components
pip install pyttsx3
```

**For Linux:**
```bash
# Install Speech Dispatcher and RHVoice
sudo apt-get install speech-dispatcher espeak rhvoice
```

## 🚀 Quick Start

1. **Launch Hugo 2.0:**
```bash
python main.py
```

2. **Web Interface:**
   - The application will open in fullscreen mode
   - Click on Hugo's face to start voice interaction
   - Speak your commands and questions

3. **Available Commands:**
   - "Анализ" - Object analysis mode
   - "Дружить" - Friendship/face recognition mode
   - "Погода" - Weather information
   - "События" - Events information
   - "Скидки" - Deals and offers
   - General questions - AI-powered responses

## 📁 Project Structure

```
Hugo-2.0/
├── main.py                 # Main application entry point
├── config.cfg              # Configuration settings
├── requirements.txt        # Python dependencies
├── 
├── Core Modules/
│   ├── audio_recognition.py    # Speech-to-text conversion
│   ├── speech_generation.py   # Text-to-speech synthesis
│   ├── dialog_launcher.py     # Main dialog controller
│   ├── friendship.py          # Face recognition system
│   ├── object_analyzis.py     # Computer vision analysis
│   ├── weather_parser.py      # Weather information
│   ├── deals_parser.py        # Shopping deals parsing
│   ├── events_parser.py       # Events information
│   ├── online_answers.py      # AI-powered responses
│   ├── offline_answers.py     # Offline response system
│   └── get_system.py          # System detection
│
├── interface/              # Web interface files
│   ├── main.html          # Main interface
│   ├── loader.html        # Loading screen
│   ├── style/             # CSS stylesheets
│   ├── js/                # JavaScript files
│   └── img/               # Interface images
│
├── database/              # User face database
├── execs/                 # Executable files
└── demo/                  # Demo files and examples
```

## ⚙️ Configuration

### Basic Configuration (`config.cfg`)

```json
{
  "settings": {
    "recognition_language": "ru-RU",
    "speech_language": "ru",
    "online_mode": "True"
  }
}
```

**Settings Explanation:**
- `recognition_language`: Language for speech recognition (ISO format)
- `speech_language`: Language for text-to-speech synthesis
- `online_mode`: Enable/disable online AI responses

### Advanced Configuration

For advanced users, you can modify:
- Camera settings in face recognition modules
- API endpoints for weather and data services
- Voice recognition sensitivity
- Response generation parameters

## 🔌 API Integration

Hugo 2.0 integrates with several external services:

- **Google Speech Recognition API**: For accurate speech-to-text conversion
- **Weather APIs**: For real-time weather information
- **AI Services**: For intelligent response generation

## 🧪 Development & Testing

### Running in Development Mode

```bash
# Enable debug mode
export HUGO_DEBUG=1
python main.py
```

### Testing Components

```bash
# Test speech recognition
python -c "from audio_recognition import audio_recognition; print(audio_recognition())"

# Test speech synthesis
python -c "from speech_generation import global_speech; global_speech('Hello World')"

# Test face recognition
python -c "from friendship import load_known_people; load_known_people()"
```

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit your changes**: `git commit -m 'Add amazing feature'`
4. **Push to the branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 style guidelines
- Add comprehensive comments and docstrings
- Test on both Windows and Linux
- Update documentation for new features

## 🐛 Troubleshooting

### Common Issues

**"No module named 'speech_recognition'"**
```bash
pip install SpeechRecognition pyaudio
```

**Camera not working**
- Check camera permissions
- Try different camera index (0, 1, 2...)
- Ensure camera is not being used by other applications

**Speech synthesis not working**
- **Windows**: Install SAPI voices
- **Linux**: Install speech-dispatcher and rhvoice
- Check audio output settings

**Face recognition errors**
- Ensure good lighting conditions
- Check if database directory exists
- Verify OpenCV installation

### Getting Help

1. Check the [Issues](https://github.com/yourusername/Hugo-2.0/issues) page
2. Review the troubleshooting section
3. Create a new issue with detailed information

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **OpenCV** - Computer vision library
- **SpeechRecognition** - Speech-to-text conversion
- **Eel** - Web app framework for Python
- **face_recognition** - Face recognition library
- **pyttsx3** - Text-to-speech synthesis
- **Speech Dispatcher** - Linux TTS system

## 🔮 Future Roadmap

- [ ] Multi-language support expansion
- [ ] Mobile app integration
- [ ] Advanced AI conversation models
- [ ] Smart home integration
- [ ] Voice command customization
- [ ] Cloud synchronization
- [ ] Plugin system for extensions

## 📊 Performance & Requirements

### System Requirements
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 2GB free space
- **CPU**: Multi-core processor recommended
- **GPU**: Optional, improves computer vision performance

### Performance Metrics
- **Speech Recognition**: ~1-2 seconds response time
- **Face Recognition**: ~0.5-1 second processing
- **Object Analysis**: ~2-3 seconds processing
- **Memory Usage**: ~200-500MB typical

---

<div align="center">

**Hugo 2.0** - *Your Intelligent Companion*

Made with ❤️ by the Hugo Development Team

[⭐ Star this project](https://github.com/yourusername/Hugo-2.0/stargazers) | [🐛 Report Bug](https://github.com/yourusername/Hugo-2.0/issues) | [💡 Request Feature](https://github.com/yourusername/Hugo-2.0/issues)

</div> 