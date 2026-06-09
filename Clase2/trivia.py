import requests
import html
import random

def get_trivia_question(category=None, difficulty=None, amount=1, question_type="multiple"):
    base_url = "https://opentdb.com/api.php"
    params = {
        "amount": amount,
        "type": question_type
    }
    if category:
        params["category"] = category
    if difficulty:
        params["difficulty"] = difficulty
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        if data["response_code"] == 0:
            return data["results"]
        else:
            print(f"No questions found for the given parameters.")
            return []
    except requests.RequestException as e:
        print(f"Error fetching trivia questions: {e}")
        return []

def main():
    print("🔹 Trivia API Test 🔹\n")
    questions = get_trivia_question(amount=3)
    for q in questions:
        question = html.unescape(q["question"])
        correct_answer = html.unescape(q["correct_answer"])
        all_answers = q["incorrect_answers"] + [correct_answer]
        random.shuffle(all_answers)
        print(f"❓ Question: {question}")
        print("Options:")
        for i, option in enumerate(all_answers, 1):
            print(f"  {i}. {html.unescape(option)}")
        print(f"✅ Correct Answer: {correct_answer}\n")



class SDKTrivia:
    def __init__(self):
        self.base_url = "https://opentdb.com/"
        self.categoryPath = "api_category.php"

    def getCategories(self):
        """Fetch trivia categories from the Open Trivia Database API."""
        url = self.base_url + self.categoryPath
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data.get("trivia_categories", [])
        except requests.RequestException as e:
            print(f"Error fetching categories: {e}")
            return []
    
    def getQuestions(self, category_id, difficulty="easy", amount=1, type="boolean",):
        """Fetch trivia questions for a given category."""
        url = self.base_url + "api.php"
        params = {
            "amount": amount,
            "category": category_id,
            "type": type,
            "difficulty": difficulty,
            
        }
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            return data.get("results", [])
        except requests.RequestException as e:
            print(f"Error fetching questions: {e}")
            return []
    
    
if __name__ == "__main__":
    sdk = SDKTrivia()
    categories = sdk.getCategories()
    print("Available Trivia Categories:")
    for category in categories:
        print(f"- {category['name']} (ID: {category['id']})")

    input_category = input("Enter a category ID to get a question: \n")
    if input_category.isdigit():
        category_id = int(input_category)

    questions = sdk.getQuestions(category_id=input_category, difficulty="medium")
    if len(questions) > 0:
        question = html.unescape(questions[0]['question'])
        correct_answer = questions[0]['correct_answer']
        answer = input(f"❓ Question: ¿{question}?\n")
        if answer == correct_answer:
            print("✅ Correct!")
        else:
            print(f"❌ Wrong! The correct answer is: {correct_answer}")


