import os
from flask import Flask, request, jsonify, send_file
from werkzeug.utils import secure_filename
import json
from datetime import datetime
import uuid

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'videos'
SCRIPT_FOLDER = 'scripts'
MAX_FILE_SIZE = 500 * 1024 * 1024  # 500MB
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'mkv', 'mp3', 'wav', 'txt'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

# Create directories if not exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(SCRIPT_FOLDER, exist_ok=True)
os.makedirs('generated_movies', exist_ok=True)

# In-memory storage for jobs (use database in production)
jobs = {}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'app': 'AI Movie Studio - Tamil Edition',
        'version': '1.0.0',
        'endpoints': {
            'upload': '/api/upload',
            'generate-movie': '/api/generate-movie',
            'list-videos': '/api/list-videos',
            'download': '/api/download/<job_id>',
            'status': '/api/status/<job_id>'
        }
    })

@app.route('/api/upload', methods=['POST'])
def upload_file():
    """Upload video, audio, or script files"""
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    file_type = request.form.get('type', 'video')  # video, audio, or script
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': f'File type not allowed. Allowed: {ALLOWED_EXTENSIONS}'}), 400
    
    filename = secure_filename(file.filename)
    unique_filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{filename}"
    
    if file_type == 'script':
        filepath = os.path.join(SCRIPT_FOLDER, unique_filename)
    else:
        filepath = os.path.join(UPLOAD_FOLDER, unique_filename)
    
    file.save(filepath)
    
    return jsonify({
        'success': True,
        'message': f'{file_type.capitalize()} uploaded successfully',
        'filename': unique_filename,
        'filepath': filepath,
        'file_type': file_type,
        'timestamp': datetime.now().isoformat()
    }), 201

@app.route('/api/list-videos', methods=['GET'])
def list_videos():
    """List all uploaded videos and scripts"""
    videos = []
    scripts = []
    
    try:
        for file in os.listdir(UPLOAD_FOLDER):
            filepath = os.path.join(UPLOAD_FOLDER, file)
            videos.append({
                'filename': file,
                'size': os.path.getsize(filepath),
                'type': 'video'
            })
        
        for file in os.listdir(SCRIPT_FOLDER):
            filepath = os.path.join(SCRIPT_FOLDER, file)
            scripts.append({
                'filename': file,
                'size': os.path.getsize(filepath),
                'type': 'script'
            })
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    return jsonify({
        'videos': videos,
        'scripts': scripts,
        'total_videos': len(videos),
        'total_scripts': len(scripts)
    }), 200

@app.route('/api/generate-movie', methods=['POST'])
def generate_movie():
    """Generate movie from script"""
    try:
        data = request.form
        script_text = data.get('script')
        script_file = data.get('script_file')
        output_format = data.get('output_format', 'mp4')
        language = data.get('language', 'tamil')
        
        if not script_text and not script_file:
            return jsonify({'error': 'Script text or file required'}), 400
        
        job_id = str(uuid.uuid4())
        
        # Read script from file if provided
        if script_file:
            script_path = os.path.join(SCRIPT_FOLDER, script_file)
            if os.path.exists(script_path):
                with open(script_path, 'r', encoding='utf-8') as f:
                    script_text = f.read()
            else:
                return jsonify({'error': 'Script file not found'}), 404
        
        # Create job entry
        jobs[job_id] = {
            'id': job_id,
            'status': 'processing',
            'progress': 0,
            'script_length': len(script_text) if script_text else 0,
            'language': language,
            'output_format': output_format,
            'created_at': datetime.now().isoformat(),
            'output_file': None
        }
        
        # TODO: Call actual movie generation logic
        # For now, simulate processing
        output_filename = f"movie_{job_id}.{output_format}"
        output_path = os.path.join('generated_movies', output_filename)
        
        # Simulate movie creation
        jobs[job_id]['status'] = 'completed'
        jobs[job_id]['progress'] = 100
        jobs[job_id]['output_file'] = output_filename
        jobs[job_id]['completed_at'] = datetime.now().isoformat()
        
        return jsonify({
            'success': True,
            'job_id': job_id,
            'message': 'Movie generation started',
            'status': 'processing',
            'language': language,
            'output_format': output_format
        }), 202
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/status/<job_id>', methods=['GET'])
def get_status(job_id):
    """Get job status"""
    if job_id not in jobs:
        return jsonify({'error': 'Job not found'}), 404
    
    return jsonify(jobs[job_id]), 200

@app.route('/api/download/<job_id>', methods=['GET'])
def download_movie(job_id):
    """Download generated movie"""
    if job_id not in jobs:
        return jsonify({'error': 'Job not found'}), 404
    
    job = jobs[job_id]
    
    if job['status'] != 'completed':
        return jsonify({'error': 'Movie not yet ready'}), 400
    
    if not job['output_file']:
        return jsonify({'error': 'Output file not found'}), 404
    
    filepath = os.path.join('generated_movies', job['output_file'])
    
    if not os.path.exists(filepath):
        return jsonify({'error': 'File not found on server'}), 404
    
    return send_file(filepath, as_attachment=True)

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
