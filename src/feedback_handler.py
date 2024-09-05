import json
from datetime import datetime

class FeedbackHandler:
    def __init__(self, feedback_file):
        self.feedback_file = feedback_file

    def save_feedback(self, code, explanation, rating, comment):
        feedback = {
            'timestamp': datetime.now().isoformat(),
            'code': code,
            'explanation': explanation,
            'rating': rating,
            'comment': comment
        }
        
        with open(self.feedback_file, 'a') as f:
            json.dump(feedback, f)
            f.write('\n')

    def get_all_feedback(self):
        feedback_list = []
        with open(self.feedback_file, 'r') as f:
            for line in f:
                feedback_list.append(json.loads(line))
        return feedback_list