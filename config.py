import os
from dotenv import load_dotenv

load_dotenv()

# Application Settings
APP_NAME = "AI Movie Studio - Tamil Edition"
APP_VERSION = "1.0.0"
DEBUG = os.getenv('DEBUG', 'False') == 'True'
SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')

# File Upload Settings
UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'videos')
SCRIPT_FOLDER = os.getenv('SCRIPT_FOLDER', 'scripts')
OUTPUT_FOLDER = os.getenv('OUTPUT_FOLDER', 'generated_movies')
TEMP_FOLDER = os.getenv('TEMP_FOLDER', '.temp')

# File size limits (in bytes)
MAX_VIDEO_SIZE = 500 * 1024 * 1024  # 500MB
MAX_AUDIO_SIZE = 100 * 1024 * 1024  # 100MB
MAX_SCRIPT_SIZE = 10 * 1024 * 1024  # 10MB

# Supported file formats
ALLOWED_VIDEO_FORMATS = {'mp4', 'avi', 'mov', 'mkv', 'flv', 'wmv'}
ALLOWED_AUDIO_FORMATS = {'mp3', 'wav', 'aac', 'flac', 'm4a'}
ALLOWED_SCRIPT_FORMATS = {'txt', 'md'}

# Language Settings
SUPPORTED_LANGUAGES = ['tamil', 'english', 'hindi']
DEFAULT_LANGUAGE = 'tamil'

# Video Processing Settings
VIDEO_CODEC = os.getenv('VIDEO_CODEC', 'libx264')
AUDIO_CODEC = os.getenv('AUDIO_CODEC', 'aac')
VIDEO_BITRATE = os.getenv('VIDEO_BITRATE', '5000k')
AUDIO_BITRATE = os.getenv('AUDIO_BITRATE', '192k')
FRAME_RATE = int(os.getenv('FRAME_RATE', '30'))
RESOLUTION = os.getenv('RESOLUTION', '1920x1080')

# API Settings
API_PORT = int(os.getenv('API_PORT', 5000))
API_HOST = os.getenv('API_HOST', '0.0.0.0')
API_TIMEOUT = int(os.getenv('API_TIMEOUT', 600))

# Database Settings (if using)
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///movies.db')

# Font paths for Tamil text rendering
TAMIL_FONT_PATHS = [
    "/usr/share/fonts/truetype/noto/NotoSansTamil-Regular.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
]

# FFmpeg paths
FFMPEG_PATH = os.getenv('FFMPEG_PATH', 'ffmpeg')
FFPROBE_PATH = os.getenv('FFPROBE_PATH', 'ffprobe')

# Logging Settings
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_FILE = os.getenv('LOG_FILE', 'app.log')

# Create necessary directories
for directory in [UPLOAD_FOLDER, SCRIPT_FOLDER, OUTPUT_FOLDER, TEMP_FOLDER]:
    os.makedirs(directory, exist_ok=True)
