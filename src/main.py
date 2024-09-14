from input_handler import parse_code
from ast_analyzer import analyze_ast
from explanation_generator import generate_explanation
from nlp_processor import process_text
# from ml_model import CodeExplanationModel
# from feedback_handler import FeedbackHandler

# model = CodeExplanationModel.load_model('data/model_checkpoints/latest_model.joblib')
# feedback_handler = FeedbackHandler('data/feedback.json')

def explain_code(code: str) -> str:
    try:
        ast_tree = parse_code(code)
        analysis = analyze_ast(ast_tree)
        raw_explanation = generate_explanation(analysis)
        processed_explanation = process_text(raw_explanation)
        
        # Enhance explanation with ML model prediction
        # ml_explanation = model.predict([code])[0]
        # enhanced_explanation = f"{processed_explanation}\n\nAdditional insights: {ml_explanation}"
        
        # return enhanced_explanation
        return processed_explanation
    except ValueError as e:
        return f"Error: {str(e)}"

# def save_feedback(code: str, explanation: str, rating: int, comment: str):
#     feedback_handler.save_feedback(code, explanation, rating, comment)

if __name__ == "__main__":
    # Example usage with nested structures
    sample_code = """
def outer_function(x):
    if x > 0:
        def inner_function(y):
            if y % 2 == 0:
                return y * 2
            else:
                return y + 1
        return inner_function(x)
    else:
        return 0

result = outer_function(5)
print(result)
    """
    
    explanation = explain_code(sample_code)
    print(explanation)
    
    # Simulate user feedback
    # save_feedback(sample_code, explanation, 5, "Great explanation!")