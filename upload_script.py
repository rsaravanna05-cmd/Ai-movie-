import requests
import os
import argparse
from pathlib import Path
import json

class UploadManager:
    """Handle file uploads to AI Movie Studio"""
    
    def __init__(self, api_url='http://localhost:5000'):
        self.api_url = api_url
        self.upload_endpoint = f"{api_url}/api/upload"
    
    def upload_video(self, filepath: str) -> dict:
        """Upload video file"""
        return self._upload(filepath, 'video')
    
    def upload_audio(self, filepath: str) -> dict:
        """Upload audio file"""
        return self._upload(filepath, 'audio')
    
    def upload_script(self, filepath: str) -> dict:
        """Upload Tamil script"""
        return self._upload(filepath, 'script')
    
    def _upload(self, filepath: str, file_type: str) -> dict:
        """Generic upload function"""
        if not os.path.exists(filepath):
            return {'success': False, 'error': f'File not found: {filepath}'}
        
        try:
            with open(filepath, 'rb') as f:
                files = {'file': f}
                data = {'type': file_type}
                
                response = requests.post(
                    self.upload_endpoint,
                    files=files,
                    data=data,
                    timeout=300
                )
            
            if response.status_code in [200, 201]:
                return response.json()
            else:
                return {
                    'success': False,
                    'error': f'Upload failed: {response.status_code}',
                    'response': response.text
                }
        
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def upload_batch(self, files: list, file_type: str = 'video') -> list:
        """Upload multiple files"""
        results = []
        for filepath in files:
            print(f"Uploading {filepath}...")
            result = self._upload(filepath, file_type)
            results.append(result)
            
            if result.get('success'):
                print(f"✓ Uploaded: {result.get('filename')}")
            else:
                print(f"✗ Failed: {result.get('error')}")
        
        return results
    
    def list_files(self) -> dict:
        """List all uploaded files"""
        try:
            response = requests.get(f"{self.api_url}/api/list-videos")
            if response.status_code == 200:
                return response.json()
            else:
                return {'error': 'Failed to list files'}
        except Exception as e:
            return {'error': str(e)}
    
    def generate_movie(self, script_file: str = None, script_text: str = None, 
                      output_format: str = 'mp4', language: str = 'tamil') -> dict:
        """Generate movie from script"""
        try:
            if script_file and not script_text:
                # Read script from file
                if not os.path.exists(script_file):
                    return {'error': f'Script file not found: {script_file}'}
                
                with open(script_file, 'r', encoding='utf-8') as f:
                    script_text = f.read()
            
            if not script_text:
                return {'error': 'Script text or file required'}
            
            data = {
                'script': script_text,
                'output_format': output_format,
                'language': language
            }
            
            response = requests.post(
                f"{self.api_url}/api/generate-movie",
                data=data,
                timeout=600
            )
            
            if response.status_code == 202:
                return response.json()
            else:
                return {
                    'error': f'Generation failed: {response.status_code}',
                    'response': response.text
                }
        
        except Exception as e:
            return {'error': str(e)}
    
    def check_status(self, job_id: str) -> dict:
        """Check movie generation status"""
        try:
            response = requests.get(f"{self.api_url}/api/status/{job_id}")
            if response.status_code == 200:
                return response.json()
            else:
                return {'error': f'Job not found: {job_id}'}
        except Exception as e:
            return {'error': str(e)}
    
    def download_movie(self, job_id: str, output_path: str = None) -> bool:
        """Download generated movie"""
        try:
            response = requests.get(
                f"{self.api_url}/api/download/{job_id}",
                stream=True
            )
            
            if response.status_code == 200:
                if not output_path:
                    output_path = f"movie_{job_id}.mp4"
                
                with open(output_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                
                print(f"✓ Downloaded: {output_path}")
                return True
            else:
                print(f"✗ Download failed: {response.status_code}")
                return False
        
        except Exception as e:
            print(f"✗ Error: {str(e)}")
            return False

def main():
    parser = argparse.ArgumentParser(description='Upload files to AI Movie Studio')
    
    parser.add_argument('--file', '-f', type=str, help='File to upload')
    parser.add_argument('--type', '-t', type=str, choices=['video', 'audio', 'script'], 
                       default='video', help='File type')
    parser.add_argument('--script', '-s', type=str, help='Script file for movie generation')
    parser.add_argument('--format', type=str, default='mp4', help='Output format')
    parser.add_argument('--language', '-l', type=str, default='tamil', help='Language')
    parser.add_argument('--list', '-ls', action='store_true', help='List all files')
    parser.add_argument('--status', type=str, help='Check job status')
    parser.add_argument('--download', '-d', type=str, help='Download movie by job_id')
    parser.add_argument('--api', type=str, default='http://localhost:5000', help='API URL')

    args = parser.parse_args()
    manager = UploadManager(args.api)
    
    if args.list:
        files = manager.list_files()
        print(json.dumps(files, indent=2, ensure_ascii=False))
    
    elif args.status:
        status = manager.check_status(args.status)
        print(json.dumps(status, indent=2, ensure_ascii=False))
    
    elif args.download:
        manager.download_movie(args.download)
    
    elif args.script:
        print(f"Generating movie from {args.script}...")
        result = manager.generate_movie(
            script_file=args.script,
            output_format=args.format,
            language=args.language
        )
        print(json.dumps(result, indent=2, ensure_ascii=False))
    
    elif args.file:
        print(f"Uploading {args.file} as {args.type}...")
        result = manager._upload(args.file, args.type)
        print(json.dumps(result, indent=2, ensure_ascii=False))
    
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
