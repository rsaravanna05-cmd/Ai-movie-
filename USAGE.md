# 📖 AI Movie Studio - Complete Usage Guide

## Table of Contents

1. [Getting Started](#getting-started)
2. [Command Line Usage](#command-line-usage)
3. [API Usage](#api-usage)
4. [Web Interface](#web-interface)
5. [Script Format](#script-format)
6. [Examples](#examples)
7. [Troubleshooting](#troubleshooting)

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- FFmpeg installed on your system
- 500MB free disk space minimum

### Installation

```bash
# Clone the repository
git clone https://github.com/rsaravanna05-cmd/Ai-movie-.git
cd Ai-movie-

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env

# Make start script executable
chmod +x start.sh

# Start the application
./start.sh
```

The server will start at: `http://localhost:5000`

---

## Command Line Usage

### Upload Videos

```bash
# Upload a single video
python upload_script.py --file video.mp4 --type video

# Upload audio file
python upload_script.py --file background.mp3 --type audio

# Upload Tamil script
python upload_script.py --file my_script.txt --type script
```

### Generate Movies

```bash
# Generate from script file
python upload_script.py --script scripts/sample_script_1.txt --format mp4 --language tamil

# Check generation status
python upload_script.py --status <job_id>

# Download generated movie
python upload_script.py --download <job_id> --output my_movie.mp4
```

### List Files

```bash
# List all uploaded files
python upload_script.py --list
```

---

## API Usage

### Base URL
```
http://localhost:5000
```

### Endpoints

#### 1. Upload File

**Request:**
```bash
curl -X POST http://localhost:5000/api/upload \
  -F "file=@video.mp4" \
  -F "type=video"
```

**Response:**
```json
{
  "success": true,
  "message": "Video uploaded successfully",
  "filename": "20260828_144532_video.mp4",
  "filepath": "videos/20260828_144532_video.mp4",
  "file_type": "video",
  "timestamp": "2026-08-28T14:45:32"
}
```

#### 2. List Videos

**Request:**
```bash
curl http://localhost:5000/api/list-videos
```

**Response:**
```json
{
  "videos": [
    {
      "filename": "20260828_144532_video.mp4",
      "size": 52428800,
      "type": "video"
    }
  ],
  "scripts": [
    {
      "filename": "20260828_144532_script.txt",
      "size": 1024,
      "type": "script"
    }
  ],
  "total_videos": 1,
  "total_scripts": 1
}
```

#### 3. Generate Movie

**Request:**
```bash
curl -X POST http://localhost:5000/api/generate-movie \
  -d "script=SCENE 1: முதல்ஜன..." \
  -d "output_format=mp4" \
  -d "language=tamil"
```

**Response:**
```json
{
  "success": true,
  "job_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "message": "Movie generation started",
  "status": "processing",
  "language": "tamil",
  "output_format": "mp4"
}
```

#### 4. Check Status

**Request:**
```bash
curl http://localhost:5000/api/status/a1b2c3d4-e5f6-7890-abcd-ef1234567890
```

**Response:**
```json
{
  "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "status": "completed",
  "progress": 100,
  "script_length": 1500,
  "language": "tamil",
  "output_format": "mp4",
  "created_at": "2026-08-28T14:45:00",
  "completed_at": "2026-08-28T14:48:00",
  "output_file": "movie_a1b2c3d4.mp4"
}
```

#### 5. Download Movie

**Request:**
```bash
curl http://localhost:5000/api/download/a1b2c3d4-e5f6-7890-abcd-ef1234567890 \
  -o my_movie.mp4
```

---

## Web Interface

### Home Page

Visit `http://localhost:5000` to access the web interface with features:

- 📤 Upload files (drag & drop)
- ✍️ Write Tamil scripts
- 🎬 Generate movies
- 📊 Track job status
- ⬇️ Download finished movies

---

## Script Format

### Basic Structure

```
SCENE <number>: <title_in_tamil>
DESC: <description>
ACTION: <action_description>
DIALOGUE: <character_name>: "<dialogue_text>"
```

### Tamil Script Example

```
SCENE 1: முதல்ஜன - காலை நேரம்
DESC: வெளி - நகர வீதி - காலை 6:00 மணி
ACTION: பிரதான கதாபாத்திரம் "ராம்" வீதியில் நடக்கிறார்
DIALOGUE: "ராம்: வணக்கம்!"

SCENE 2: வீட்டு உள்ளே
DESC: உள் - பழைய வீடு
ACTION: "ராம்" தனது வீட்டுக்குள் நுழைகிறார்
DIALOGUE: "தாய்: மகனே! நீ வந்துவிட்டாயா?"
```

### Best Practices

- ✅ Use Tamil Unicode characters
- ✅ Keep scenes concise (2-5 minutes each)
- ✅ Include descriptive actions
- ✅ Use character names consistently
- ✅ Add stage directions in parentheses

---

## Examples

### Example 1: Simple Movie Creation

```bash
#!/bin/bash

# Step 1: Upload videos
python upload_script.py --file scene1.mp4 --type video
python upload_script.py --file scene2.mp4 --type video

# Step 2: Upload script
python upload_script.py --file story.txt --type script

# Step 3: Generate movie
RESULT=$(python upload_script.py --script story.txt --format mp4 --language tamil)
JOB_ID=$(echo $RESULT | grep -o '"job_id":"[^"]*"' | cut -d'"' -f4)

# Step 4: Check status
python upload_script.py --status $JOB_ID

# Step 5: Download
python upload_script.py --download $JOB_ID --output final_movie.mp4
```

### Example 2: Python Integration

```python
from upload_script import UploadManager

# Initialize manager
manager = UploadManager('http://localhost:5000')

# Upload files
video_result = manager.upload_video('my_video.mp4')
script_result = manager.upload_script('my_script.txt')

# Generate movie
movie = manager.generate_movie(
    script_file='my_script.txt',
    output_format='mp4',
    language='tamil'
)

job_id = movie['job_id']

# Check status
status = manager.check_status(job_id)
print(f"Status: {status['status']}")

# Download when ready
if status['status'] == 'completed':
    manager.download_movie(job_id, 'output.mp4')
```

### Example 3: Batch Processing

```python
from upload_script import UploadManager

manager = UploadManager()

# List of videos
videos = ['video1.mp4', 'video2.mp4', 'video3.mp4']

# Upload batch
results = manager.upload_batch(videos, file_type='video')

# Generate movie
movie = manager.generate_movie(script_file='script.txt')

print(f"Movie ID: {movie['job_id']}")
```

---

## Troubleshooting

### Server Won't Start

```bash
# Check if port 5000 is in use
lsof -i :5000

# Kill existing process
kill -9 <PID>

# Or use different port
API_PORT=8000 python app.py
```

### Upload Fails

**Error: "File size exceeds limit"**
```bash
# Check file size
ls -lh video.mp4

# Compress video
ffmpeg -i large_video.mp4 -vcodec libx264 -crf 28 small_video.mp4
```

**Error: "File type not allowed"**
```bash
# Check supported formats in config.py
# Supported: mp4, avi, mov, mkv, mp3, wav, txt
```

### Movie Generation Issues

**Generation takes too long**
- Reduce video resolution
- Use lower bitrate
- Split into smaller scenes

**Poor video quality**
```bash
# Use higher bitrate
VIDEO_BITRATE=8000k python app.py
```

### FFmpeg Not Found

```bash
# Install FFmpeg
# On Ubuntu/Debian
sudo apt-get install ffmpeg

# On macOS
brew install ffmpeg

# On Windows
# Download from https://ffmpeg.org/download.html
```

### Tamil Text Not Displaying

```bash
# Install Tamil fonts
sudo apt-get install fonts-noto-cjk

# On macOS
brew install font-noto-sans-tamil
```

---

## Advanced Configuration

### Custom Output Settings

Edit `config.py`:

```python
# Video codec: libx264, libx265, mpeg4
VIDEO_CODEC = 'libx265'

# Resolution: 1920x1080, 1280x720, 854x480
RESOLUTION = '1280x720'

# Frame rate: 24, 30, 60
FRAME_RATE = 24

# Bitrate: 2000k, 5000k, 10000k
VIDEO_BITRATE = '5000k'
```

### Database Setup (Optional)

```bash
# Install database
pip install sqlalchemy

# Initialize database
python -c "from app import db; db.create_all()"
```

---

## Performance Tips

1. **Optimize Videos**
   - Use H.264 codec
   - Resolution: 720p-1080p
   - Bitrate: 5000-8000k

2. **Reduce Processing Time**
   - Split long movies into episodes
   - Use hardware acceleration if available
   - Close other applications

3. **Save Storage**
   - Compress final videos
   - Delete temporary files regularly
   - Archive old movies

4. **Improve Quality**
   - Use 48kHz audio sample rate
   - Add color grading
   - Use professional fonts

---

## Support & Resources

- 📚 [Full Documentation](README.md)
- 📱 [APK Download Guide](APK_GUIDE.md)
- 🐛 [Report Issues](https://github.com/rsaravanna05-cmd/Ai-movie-/issues)
- 💬 [Discussions](https://github.com/rsaravanna05-cmd/Ai-movie-/discussions)

---

**Happy Movie Creating! 🎬✨**
