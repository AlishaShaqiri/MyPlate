from flask import Flask, jsonify, request
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(
api_key= ‘'
)

client = OpenAI(
)

@app.route('/generate-meal-plan', methods=['POST'])
def generate_meal_plan():
    user_informations = {
        'weight': '75',
        'height': '170',
        'age': '22',
    }

    user_preferences = {
        'cuisine': 'Italian',
        'diet': 'Lose weight',
        'favorite_food': ['Brocoli', 'Chicken', 'Eggs' , 'Dark Chocolate'],
        'intolerance_food': ['Potatos', 'Avokado', 'White Bread', 'Milk'],
    }

    prompt = f"Generate a meal plan for a user with these informations {user_informations} with the following preferences: {user_preferences} for a month diet"

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "rol": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )
    sample_meal_plan = chat_completion.choices[0].message.content

    return jsonify({'meal_plan': sample_meal_plan})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
