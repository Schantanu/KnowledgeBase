import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class EventHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        print('EVENT')
        print(event.event_type)
        print(event.src_path)

class MyEventHandler(PatternMatchingEventHandler):
    def on_modified(self, event):
        super(MyEventHandler, self).on_modified(event)
        logging.info("File %s was just modified" % event.src_path)
        
if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else '.'

    event_handler = EventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()