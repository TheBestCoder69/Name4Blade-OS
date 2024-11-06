import time
import random
from datetime import datetime
from collections import defaultdict
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from ui_components import update_recommendations

# Event log for user actions
event_log = []
user_behavior = defaultdict(list)

# Function to log user actions
def log_event(event_type, app_name, duration):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    event = {"timestamp": timestamp, "type": event_type, "details": {"app_name": app_name, "duration": duration}}
    event_log.append(event)
    user_behavior[event_type].append(event)

# Train a basic model for app prediction
def train_model():
    X = np.array([[5], [15], [30], [60], [10]])  # Simulated usage times
    y = np.array(["Browser", "Text Editor", "Media Player", "File Manager", "Terminal"])  # App labels
    model = RandomForestClassifier()
    model.fit(X, y)
    return model

model = train_model()

# Predict next app based on usage
def predict_next_app(duration):
    return model.predict([[duration]])[0]

# Background AI service to log and analyze continuously
def ai_service():
    while True:
        log_event("app_opened", random.choice(["Browser", "File Manager", "Text Editor"]), random.choice([5, 15, 30]))
        
        # Run analysis and update recommendations every few events
        if len(event_log) % 5 == 0:
            recent_duration = random.choice([5, 15, 30])
            recommended_app = predict_next_app(recent_duration)
            update_recommendations(recommended_app)
        
        time.sleep(10)

# Optimize resources based on recent usage patterns
def optimize_resources():
    while True:
        for event in event_log[-10:]:  # Last 10 events
            if event["details"]["app_name"] == "Media Player":
                print("Optimizing for media playback...")

        time.sleep(15)
