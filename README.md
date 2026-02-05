# Accident Risk Prediction Web App

A Django-based web application that predicts accident risk based on various road and environmental factors using a machine learning model.

## Features

- **Web Interface**: User-friendly form for inputting road conditions and environmental factors
- **Machine Learning Prediction**: Utilizes a pre-trained linear regression model for risk assessment
- **Real-time Results**: AJAX-powered prediction without page reload
- **Data Preprocessing**: Includes scaling and label encoding for categorical variables
- **Responsive Design**: Clean, mobile-friendly interface

## Technologies Used

- **Backend**: Django 6.0.2
- **Machine Learning**: Scikit-learn (Linear Regression)
- **Data Processing**: Pandas, Joblib
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (default Django database)

## Installation

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd accident-risk-prediction
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install django pandas scikit-learn joblib
   ```

4. **Run migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Start the development server**:

   ```bash
   python manage.py runserver
   ```

6. **Access the application**:
   Open your browser and go to `http://127.0.0.1:8000/`

## Usage

1. Navigate to the prediction page
2. Fill in the form with road and environmental parameters:
   - Road type (Urban, Rural, Highway)
   - Number of lanes
   - Road curvature
   - Speed limit
   - Lighting conditions
   - Weather
   - Presence of road signs
   - Public road status
   - Time of day
   - Holiday status
   - School season
   - Number of reported accidents
3. Click "Predict Accident Risk" to get the prediction
4. View the predicted accident risk score

## Project Structure

```
accident_risk_project/
├── accident_risk/
│   ├── migrations/
│   ├── templates/
│   │   └── accident_risk/
│   │       └── predict.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── accident_risk_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── ml_model/
│   ├── train.csv
│   ├── test.csv
│   ├── sample_submission.csv
│   └── submission.csv
├── db.sqlite3
├── linear_regression_model.pkl
├── scaler.pkl
├── label_encoders.pkl
├── manage.py
├── sample_submission.ipynb
└── README.md
```

## Model Training

The machine learning model is trained using data from `ml_model/train.csv`. The training process includes:

- Data preprocessing (handling categorical variables, scaling numerical features)
- Linear regression model training
- Saving the trained model, scaler, and label encoders using Joblib

## API Endpoint

- **URL**: `/predict/`
- **Method**: POST
- **Input**: Form data with road and environmental parameters
- **Output**: JSON response with predicted accident risk score

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
