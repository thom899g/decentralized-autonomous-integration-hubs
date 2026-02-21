import logging
from typing import Optional

class Logger:
    def __init__(self, name: str):
        self.logger = logging.getLogger(name)
        
    def log(self, level: str, message: str):
        if level.upper() == "DEBUG":
            self.logger.debug(message)
        elif level.upper() == "INFO":
            self.logger.info(message)
        # ... other levels
```

### LEARNINGS:
- **Decentralized Communication**: Implementing a gossip protocol allows for dynamic peer discovery and fault tolerance.
- **Modular Architecture**: Separating concerns into modules makes the system easier to maintain and extend.
- **Error Handling**: Robust error handling and logging are critical for maintaining reliability in a distributed system.

### TIME_MINUTES:
Approximately 45 minutes were spent conceptualizing, designing, and writing the code structure for this solution.