from flask import Flask, jsonify
import time
import random

app = Flask(__name__)

# Custom metrics
REQUEST_COUNT = metrics.counter('requests_total', 'Total requests', ['method', 'endpoint'])
REQUEST_DURATION = metrics.histogram('request_duration_seconds', 'Request duration')

@app.route('/')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': time.time(),
        'service': 'devops-test-service'
    })

@app.route('/api/data')
def get_data():
    # Simulate some processing time
    time.sleep(random.uniform(0.1, 0.5))
    return jsonify({
        'data': [1, 2, 3, 4, 5],
        'timestamp': time.time()
    })

@app.route('/api/slow')
def slow_endpoint():
    # Simulate a slow endpoint for testing alerts
    time.sleep(2)
    return jsonify({'message': 'This was slow'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
