from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
import pandas as pd
import joblib
import os

def predict_accident_risk(request):
    if request.method == 'POST':
        try:
            # Get form data
            road_type = request.POST.get('road_type')
            num_lanes = int(request.POST.get('num_lanes'))
            curvature = float(request.POST.get('curvature'))
            speed_limit = int(request.POST.get('speed_limit'))
            lighting = request.POST.get('lighting')
            weather = request.POST.get('weather')
            road_signs_present = request.POST.get('road_signs_present') == 'on'
            public_road = request.POST.get('public_road') == 'on'
            time_of_day = request.POST.get('time_of_day')
            holiday = request.POST.get('holiday') == 'on'
            school_season = request.POST.get('school_season') == 'on'
            num_reported_accidents = int(request.POST.get('num_reported_accidents'))

            # Load the model and preprocessors
            model_path = os.path.join(settings.BASE_DIR, 'linear_regression_model.pkl')
            scaler_path = os.path.join(settings.BASE_DIR, 'scaler.pkl')
            label_encoders_path = os.path.join(settings.BASE_DIR, 'label_encoders.pkl')

            model = joblib.load(model_path)
            scaler = joblib.load(scaler_path)
            label_encoders = joblib.load(label_encoders_path)

            # Prepare input data
            input_data = pd.DataFrame({
                'road_type': [road_type],
                'num_lanes': [num_lanes],
                'curvature': [curvature],
                'speed_limit': [speed_limit],
                'lighting': [lighting],
                'weather': [weather],
                'road_signs_present': [road_signs_present],
                'public_road': [public_road],
                'time_of_day': [time_of_day],
                'holiday': [holiday],
                'school_season': [school_season],
                'num_reported_accidents': [num_reported_accidents]
            })

            # Encode categorical variables
            categorical_cols = ['road_type', 'lighting', 'weather', 'time_of_day']
            for col in categorical_cols:
                input_data[col] = label_encoders[col].transform(input_data[col])

            # Scale numerical features
            numerical_cols = ['num_lanes', 'curvature', 'speed_limit', 'num_reported_accidents']
            input_data[numerical_cols] = scaler.transform(input_data[numerical_cols])

            # Make prediction
            prediction = model.predict(input_data)[0]

            return JsonResponse({'accident_risk': round(prediction, 4)})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return render(request, 'accident_risk/predict.html')
