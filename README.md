# 🎬 AI Movie Studio - Tamil Edition

Create stunning AI-generated movies with Tamil language support. Upload scripts, generate videos, and download your complete movies.

## 🚀 Features

- **AI Video Generation** - Create full-length movies with AI
- **Tamil Script Support** - Write scripts in Tamil language
- **Upload Manager** - Easy video and audio uploads
- **Video Processing** - Combine, edit, and render videos
- **Download Support** - Get your finished movies in multiple formats

## 📋 Requirements

- Python 3.8+
- FFmpeg
- OpenCV
- PyTorch or TensorFlow (for AI models)
- Flask (API server)

## 📦 Installation

```bash
git clone https://github.com/rsaravanna05-cmd/Ai-movie-.git
cd Ai-movie-
pip install -r requirements.txt
```

## 🎯 Quick Start

### 1. Start the Server
```bash
python app.py
```

### 2. Upload Script
```bash
python upload_script.py --file movie_script.txt --language tamil
```

### 3. Generate Movie
```bash
curl -X POST http://localhost:5000/api/generate-movie \
  -F "script=@script.txt" \
  -F "output_format=mp4"
```

## 📁 Project Structure

```
Ai-movie-/
├── app.py                 # Flask main application
├── upload_script.py       # Video upload handler
├── generate_movie.py      # Movie generation logic
├── config.py             # Configuration settings
├── requirements.txt      # Python dependencies
├── models/               # AI models
├── videos/               # Video storage
├── scripts/              # Tamil script templates
└── README.md            # This file
```

## 🎨 Usage Examples

### Example 1: Simple Movie Creation
```python
from generate_movie import MovieGenerator

generator = MovieGenerator()
movie = generator.create_from_script(
    script="Your Tamil script here",
    language="tamil",
    output_file="my_movie.mp4"
)
```

### Example 2: Upload and Generate
```bash
# Upload video clips
python upload_script.py --type video --file clip1.mp4
python upload_script.py --type audio --file background_music.mp3

# Generate movie
python generate_movie.py --combine --output final_movie.mp4
```

## 📝 Tamil Script Format

```
SCENE 1: முதல்장면
DESC: வெளி - நகரம் (EXTERIOR - CITY)
ACTION: பிரதான கதாபாத்திரம் வீதியில் நடக்கிறார்
DIALOGUE: "வணக்கம் என் நண்பா!" (Hello my friend!)
```

## 🔧 Configuration

Edit `config.py`:
```python
VIDEO_UPLOAD_DIR = "videos/"
MAX_FILE_SIZE = 500 * 1024 * 1024  # 500MB
SUPPORTED_FORMATS = ['mp4', 'avi', 'mov', 'mkv']
LANGUAGE = 'tamil'
```

## 🚀 API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/upload` | POST | Upload video/audio |
| `/api/generate-movie` | POST | Generate movie from script |
| `/api/list-videos` | GET | List uploaded videos |
| `/api/download/:id` | GET | Download generated movie |
| `/api/status/:id` | GET | Check generation status |

## 🎓 Learning Resources

- [FFmpeg Documentation](https://ffmpeg.org/documentation.html)
- [OpenCV Tutorials](https://docs.opencv.org/)
- [Flask API Guide](https://flask.palletsprojects.com/)

## 📄 License

MIT License - Feel free to use and modify

## 👨‍💻 Author

Created by rsaravanna05-cmd

## 📞 Support

For issues and feature requests, please open a GitHub issue.

---

**Happy Movie Creating! 🎬✨**
