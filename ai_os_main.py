from threading import Thread
from ai_services import ai_service, optimize_resources
from ui_components import init_ui

# Start AI services in separate threads
ai_service_thread = Thread(target=ai_service)
optimization_thread = Thread(target=optimize_resources)

# Start threads
ai_service_thread.start()
optimization_thread.start()

# Initialize UI
init_ui()
