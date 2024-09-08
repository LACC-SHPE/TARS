from logger import TarsLogger

logging = TarsLogger()


class GPTAgent:
    def __init__(self):
        pass

    def get_response(self, prompt):
        logging.info("GPTAgent: " + prompt)
        return "Hello Paola"
