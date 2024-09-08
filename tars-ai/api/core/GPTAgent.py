from logger import TarsLogger


class GPTAgent:
    def __init__(self, logging: TarsLogger):
        self.logging = logging
        pass

    def get_response(self, prompt):
        self.logging.info("GPTAgent: " + prompt)
        return "Hello Paola"
