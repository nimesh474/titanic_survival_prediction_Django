from django.shortcuts import render
import pickle
import numpy as np

# load model
path = r'D:/DeerWalk/titanic_survival_prediction/ml_model/logistic_regression.pkl'
model = pickle.load(open(path, 'rb'))

# titanic prediction
def survival_prediction(request):
    if request.method == 'GET':
        return render(request, 'prediction_form.html')
    else:
        pclass = int(request.POST.get('pclass'))

        gender = request.POST.get('gender')
        return_gender = 0 if gender == 'male' else 1

        age = float(request.POST.get('age'))

        embarked = request.POST.get('embarked')
        if embarked == 'C':
            return_embarked = 0
        elif embarked == 'Q':
            return_embarked = 1
        else:
            return_embarked = 2

        print(pclass, return_gender, age, return_embarked)

        # titanic data
        values = [pclass, return_gender, age, return_embarked]
        # convert 1D to 2D
        reshaped_value = np.array(values).reshape(1, -1)

        # prediction
        prediction = model.predict(reshaped_value)

        context = {
            'age': age,
            'gender': return_gender,
            'embarked': return_embarked,
            'pclass': pclass,
            'prediction': prediction[0]
        }

        return render(request, 'prediction_form.html', context)