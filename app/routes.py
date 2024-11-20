from flask import render_template, request
from app import app

@app.route('/', methods=['GET', 'POST'])
def form():
    user_data = None
    if request.method == 'POST':
        name = request.form.get('name')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        age = request.form.get('age')

        user_data = {
            'name': name,
            'city': city,
            'hobby': hobby,
            'age': age
        }

    # Отображаем страницу с формой и текущими данными
    return render_template('form.html', user_data=user_data)
