class Logger:
    _instance = None  
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            print("Logger created exactly once")
        else:
            print("Logger already created")
        return cls._instance

    def __init__(self):
        if not hasattr(self, "initialized"):
            self.messages = []
            self.initialized = True  
    def add_message(self, message):
        self.messages.append(message)


def main():
    for i in range(3):
        logger = Logger()
        logger.add_message(f"Adding message number: {i}")
        # Printing messages to check if they're accumulating across instances
        print(logger.messages)

if __name__ == "__main__":
    main()