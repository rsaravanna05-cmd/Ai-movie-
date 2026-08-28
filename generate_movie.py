import os
import cv2
import numpy as np
from pathlib import Path
import subprocess
from typing import Optional, List
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MovieGenerator:
    """Generate movies from scripts using AI and video processing"""
    
    def __init__(self, config_path='config.py'):
        self.video_dir = 'videos'
        self.output_dir = 'generated_movies'
        self.temp_dir = '.temp'
        
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs(self.temp_dir, exist_ok=True)
    
    def parse_script(self, script_text: str) -> List[dict]:
        """Parse Tamil script into scenes and actions"""
        scenes = []
        current_scene = None
        
        for line in script_text.split('\n'):
            line = line.strip()
            
            if line.startswith('SCENE'):
                if current_scene:
                    scenes.append(current_scene)
                current_scene = {'title': line, 'description': '', 'actions': []}
            elif line.startswith('DESC:'):
                if current_scene:
                    current_scene['description'] = line.replace('DESC:', '').strip()
            elif line.startswith('ACTION:'):
                if current_scene:
                    current_scene['actions'].append(line.replace('ACTION:', '').strip())
            elif line.startswith('DIALOGUE:'):
                if current_scene:
                    current_scene['dialogue'] = line.replace('DIALOGUE:', '').strip()
        
        if current_scene:
            scenes.append(current_scene)
        
        return scenes
    
    def combine_videos(self, video_files: List[str], output_path: str) -> bool:
        """Combine multiple video files using FFmpeg"""
        try:
            # Create concat file
            concat_file = os.path.join(self.temp_dir, 'concat.txt')
            with open(concat_file, 'w') as f:
                for video in video_files:
                    f.write(f"file '{os.path.abspath(video)}'\n")
            
            # Run FFmpeg command
            cmd = [
                'ffmpeg',
                '-f', 'concat',
                '-safe', '0',
                '-i', concat_file,
                '-c', 'copy',
                output_path,
                '-y'  # Overwrite output
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                logger.info(f"Successfully combined videos to {output_path}")
                return True
            else:
                logger.error(f"FFmpeg error: {result.stderr}")
                return False
        
        except Exception as e:
            logger.error(f"Error combining videos: {str(e)}")
            return False
    
    def add_audio(self, video_path: str, audio_path: str, output_path: str) -> bool:
        """Add audio track to video"""
        try:
            cmd = [
                'ffmpeg',
                '-i', video_path,
                '-i', audio_path,
                '-c:v', 'copy',
                '-c:a', 'aac',
                '-map', '0:v:0',
                '-map', '1:a:0',
                output_path,
                '-y'
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                logger.info(f"Audio added successfully")
                return True
            else:
                logger.error(f"FFmpeg error: {result.stderr}")
                return False
        
        except Exception as e:
            logger.error(f"Error adding audio: {str(e)}")
            return False
    
    def create_text_overlay(self, video_path: str, text: str, output_path: str) -> bool:
        """Add Tamil text overlay to video"""
        try:
            # FFmpeg filter for adding text
            font_path = "/usr/share/fonts/truetype/noto/NotoSansTamil-Regular.ttf"
            
            filter_str = f"drawtext=fontfile='{font_path}':text='{text}':fontsize=24:fontcolor=white:x=(w-text_w)/2:y=(h-text_h)-30"
            
            cmd = [
                'ffmpeg',
                '-i', video_path,
                '-vf', filter_str,
                output_path,
                '-y'
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                logger.info(f"Text overlay added successfully")
                return True
            else:
                logger.error(f"FFmpeg error: {result.stderr}")
                return False
        
        except Exception as e:
            logger.error(f"Error adding text: {str(e)}")
            return False
    
    def convert_format(self, input_path: str, output_path: str, format: str = 'mp4') -> bool:
        """Convert video to different format"""
        try:
            cmd = [
                'ffmpeg',
                '-i', input_path,
                output_path,
                '-y'
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                logger.info(f"Video converted to {format}")
                return True
            else:
                logger.error(f"FFmpeg error: {result.stderr}")
                return False
        
        except Exception as e:
            logger.error(f"Error converting format: {str(e)}")
            return False
    
    def create_from_script(self, script: str, language: str = 'tamil', 
                          output_file: str = 'movie.mp4') -> Optional[str]:
        """Create movie from Tamil script"""
        try:
            logger.info("Starting movie creation from script")
            
            # Parse script
            scenes = self.parse_script(script)
            logger.info(f"Parsed {len(scenes)} scenes from script")
            
            # Get available videos
            video_files = [
                os.path.join(self.video_dir, f) 
                for f in os.listdir(self.video_dir) 
                if f.endswith(('.mp4', '.avi', '.mov'))
            ]
            
            if not video_files:
                logger.warning("No video files found")
                return None
            
            # Combine videos
            combined_path = os.path.join(self.temp_dir, 'combined.mp4')
            if not self.combine_videos(video_files[:min(3, len(video_files))], combined_path):
                return None
            
            # Output path
            output_path = os.path.join(self.output_dir, output_file)
            
            # Convert to desired format
            file_ext = output_file.split('.')[-1]
            if not self.convert_format(combined_path, output_path, file_ext):
                return None
            
            logger.info(f"Movie created successfully: {output_path}")
            return output_path
        
        except Exception as e:
            logger.error(f"Error creating movie: {str(e)}")
            return None

if __name__ == '__main__':
    generator = MovieGenerator()
    
    # Example script
    sample_script = """
    SCENE 1: முதல்장ன
    DESC: வெளி - நகரம்
    ACTION: பிரதான கதாபாத்திரம் வீதியில் நடக்கிறார்
    DIALOGUE: "வணக்கம் என் நண்பா!"
    """
    
    result = generator.create_from_script(sample_script, language='tamil')
    print(f"Generated movie: {result}")
