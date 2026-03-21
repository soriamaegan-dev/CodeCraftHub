from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

COURSES_FILE = 'courses.json'
VALID_STATUSES = ['Not Started', 'In Progress', 'Completed']

def load_courses():
    try:
        if not os.path.exists(COURSES_FILE):
            save_courses([])
            return []
        with open(COURSES_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error reading courses file: {e}")
        return []

def save_courses(courses):
    try:
        with open(COURSES_FILE, 'w') as f:
            json.dump(courses, f, indent=2)
    except IOError as e:
        print(f"Error writing courses file: {e}")
        raise

def get_next_id(courses):
    if not courses:
        return 1
    return max(c['id'] for c in courses) + 1

@app.route('/api/courses', methods=['GET'])
def get_courses():
    try:
        courses = load_courses()
        return jsonify(courses), 200
    except Exception as e:
        return jsonify({'error': f'Failed to retrieve courses: {str(e)}'}), 500


@app.route('/api/courses/stats', methods=['GET'])
def get_stats():
    """Get statistics about all courses."""
    try:
        courses = load_courses()
        stats = {
            'total': len(courses),
            'by_status': {
                'Not Started': len([c for c in courses if c['status'] == 'Not Started']),
                'In Progress': len([c for c in courses if c['status'] == 'In Progress']),
                'Completed': len([c for c in courses if c['status'] == 'Completed'])
            }
        }
        return jsonify(stats), 200
    except Exception as e:
        return jsonify({'error': f'Failed to retrieve stats: {str(e)}'}), 500

@app.route('/api/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    try:
        courses = load_courses()
        course = next((c for c in courses if c['id'] == course_id), None)
        if not course:
            return jsonify({'error': f'Course with ID {course_id} not found'}), 404
        return jsonify(course), 200
    except Exception as e:
        return jsonify({'error': f'Failed to retrieve course: {str(e)}'}), 500

@app.route('/api/courses', methods=['POST'])
def create_course():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Request body is required'}), 400
    if not data.get('name'):
        return jsonify({'error': 'Course name is required'}), 400
    if not data.get('description'):
        return jsonify({'error': 'Description is required'}), 400
    if not data.get('target_date'):
        return jsonify({'error': 'Target date is required (format: YYYY-MM-DD)'}), 400
    if not data.get('status'):
        return jsonify({'error': 'Status is required'}), 400
    try:
        datetime.strptime(data['target_date'], '%Y-%m-%d')
    except ValueError:
        return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD'}), 400
    if data['status'] not in VALID_STATUSES:
        return jsonify({'error': f'Invalid status. Must be one of: {", ".join(VALID_STATUSES)}'}), 400
    try:
        courses = load_courses()
        course = {
            'id': get_next_id(courses),
            'name': data['name'],
            'description': data['description'],
            'target_date': data['target_date'],
            'status': data['status'],
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        courses.append(course)
        save_courses(courses)
        return jsonify(course), 201
    except Exception as e:
        return jsonify({'error': f'Failed to create course: {str(e)}'}), 500

@app.route('/api/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Request body is required'}), 400
    if 'status' in data and data['status'] not in VALID_STATUSES:
        return jsonify({'error': f'Invalid status. Must be one of: {", ".join(VALID_STATUSES)}'}), 400
    if 'target_date' in data:
        try:
            datetime.strptime(data['target_date'], '%Y-%m-%d')
        except ValueError:
            return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD'}), 400
    try:
        courses = load_courses()
        course = next((c for c in courses if c['id'] == course_id), None)
        if not course:
            return jsonify({'error': f'Course with ID {course_id} not found'}), 404
        for field in ['name', 'description', 'target_date', 'status']:
            if field in data:
                course[field] = data[field]
        save_courses(courses)
        return jsonify(course), 200
    except Exception as e:
        return jsonify({'error': f'Failed to update course: {str(e)}'}), 500

@app.route('/api/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    try:
        courses = load_courses()
        course = next((c for c in courses if c['id'] == course_id), None)
        if not course:
            return jsonify({'error': f'Course with ID {course_id} not found'}), 404
        courses = [c for c in courses if c['id'] != course_id]
        save_courses(courses)
        return jsonify({'message': f'Course {course_id} deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': f'Failed to delete course: {str(e)}'}), 500


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "CodeCraftHub API is running!", "version": "1.0"}), 200

if __name__ == "__main__":
    load_courses()
    print("CodeCraftHub API is starting...")
    print(f"Data will be stored in: {os.path.abspath(COURSES_FILE)}")
    print("API will be available at: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=8080)

