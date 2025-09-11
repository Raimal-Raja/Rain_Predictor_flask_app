# 🌧️ Rain Predictor Flask App

A comprehensive machine learning web application that predicts whether it will rain tomorrow using the Australian weather dataset. This project implements multiple ML algorithms and deploys the best-performing model through a Flask web interface.

![Rain Predictor App](https://github.com/Raimal-Raja/Rain_Predictor_flask_app/blob/main/first.png)
*Screenshot of the Rain Predictor Web Application*

## 📊 Project Overview

This project addresses the binary classification problem of predicting next-day rainfall using historical weather data from Australia. The application leverages advanced machine learning techniques including data preprocessing, feature engineering, model selection, and hyperparameter optimization to deliver accurate predictions.

**Project Type:** Machine Learning (ML) Classification Project with Web Deployment

## 🎯 Key Features

- **Multiple ML Models:** Implemented and compared various algorithms including CatBoost, XGBoost, Random Forest, SVM, Logistic Regression, KNN, and Naive Bayes
- **Advanced Data Preprocessing:** Handles missing values, categorical encoding, outlier detection, and feature scaling
- **Imbalanced Data Handling:** Uses SMOTE (Synthetic Minority Oversampling Technique) for dataset balancing
- **Model Performance Evaluation:** Comprehensive evaluation using ROC curves, AUC scores, and classification metrics
- **Interactive Web Interface:** User-friendly Flask-based web application for real-time predictions
- **Responsive Design:** Bootstrap-powered frontend with modern UI/UX

## 🛠️ Technologies & Tools

### Machine Learning & Data Science
- **Python 3.6+**
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Scikit-learn** - Machine learning library
- **CatBoost** - Gradient boosting framework
- **XGBoost** - Extreme gradient boosting
- **Matplotlib & Seaborn** - Data visualization
- **SMOTE** - Synthetic data generation for imbalanced datasets

### Web Development
- **Flask** - Backend web framework
- **HTML5 & CSS3** - Frontend markup and styling
- **Bootstrap** - Responsive UI framework
- **JavaScript** - Client-side interactions

### Development Environment
- **Jupyter Notebook** - Interactive development and analysis
- **PyCharm** - Python IDE
- **Git & GitHub** - Version control
- **Heroku** - Cloud deployment platform

## 📈 Model Performance

| Model | AUC Score | Performance |
|-------|-----------|-------------|
| **CatBoost** ⭐ | **~0.89** | Best performing model |
| Random Forest | ~0.85 | Second best |
| Support Vector Classifier | ~0.82 | Third best |
| XGBoost | ~0.80 | Good performance |
| Logistic Regression | ~0.78 | Baseline model |

*CatBoost achieved the highest AUC score of approximately 0.89, making it the selected model for deployment.*

## 🚀 Installation & Setup

### Prerequisites
- Python 3.6 or higher
- pip package manager
- Git (for cloning the repository)

### Step-by-Step Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Raimal-Raja/Rain_Predictor_flask_app.git
   cd Rain_Predictor_flask_app
   ```

2. **Create Virtual Environment**
   ```bash
   conda create -n rain-predictor python=3.6
   # OR using venv
   python -m venv rain-predictor
   ```

3. **Activate Virtual Environment**
   ```bash
   conda activate rain-predictor
   # OR using venv
   # Windows: rain-predictor\Scripts\activate
   # macOS/Linux: source rain-predictor/bin/activate
   ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**
   ```bash
   python app.py
   ```

6. **Access the Application**
   - Open your browser and navigate to `http://localhost:5000`

## 📁 Project Structure

```
Rain_Predictor_flask_app/
│
├── app.py                      # Flask application entry point
├── requirements.txt            # Python dependencies
├── Procfile                   # Heroku deployment configuration
├── runtime.txt                # Python runtime version
│
├── models/                    # Trained ML models
│   └── catboost_model.pkl
│
├── templates/                 # HTML templates
│   ├── index.html            # Home page
│   ├── predict.html          # Prediction form
│   └── result.html           # Results display
│
├── static/                    # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
│
├── notebooks/                 # Jupyter notebooks
│   ├── data_exploration.ipynb
│   ├── model_training.ipynb
│   └── testing_notebook/
│       ├── Prediction.ipynb
│       └── RainPrediction1.ipynb
│
└── data/                     # Dataset files
    └── weatherAUS.csv
```

## 🔬 Data Science Workflow

### 1. Data Preprocessing
- **Missing Values:** Handled using Random Sample Imputation to maintain data variance
- **Categorical Encoding:** Applied Target-Guided Encoding for location and wind direction features
- **Outlier Detection:** Used IQR method and box plots for outlier identification and treatment
- **Feature Scaling:** Applied StandardScaler (optional based on model requirements)

### 2. Feature Engineering
- **Feature Selection:** Explored various feature selection techniques
- **Target Variable:** Binary classification - Will it rain tomorrow? (Yes/No)
- **Feature Importance:** Analyzed using tree-based models

### 3. Model Development
- **Baseline Models:** Logistic Regression, Naive Bayes
- **Ensemble Methods:** Random Forest, XGBoost, CatBoost
- **Support Vector Machines:** Linear and RBF kernels
- **Cross-Validation:** K-fold validation for robust model evaluation

### 4. Model Evaluation
- **Metrics:** Accuracy, Precision, Recall, F1-Score, AUC-ROC
- **Visualization:** ROC curves, confusion matrices, feature importance plots
- **Model Selection:** Based on AUC score and business requirements

## 📊 Dataset Information

**Source:** [Rainfall Prediction in Australia Dataset](https://www.kaggle.com/jsphyg/weather-dataset-rattle-package) from Kaggle

**Dataset Characteristics:**
- **Size:** 145,460 observations with 23 features
- **Target Variable:** RainTomorrow (binary classification)
- **Features Include:** Temperature, humidity, wind speed/direction, pressure, cloud cover, rainfall measurements
- **Challenge:** Imbalanced dataset requiring SMOTE for balancing

## 🌟 Key Insights

1. **Weather Patterns:** Certain combinations of humidity, pressure, and wind patterns are strong predictors of rainfall
2. **Seasonal Variations:** The model captures seasonal rainfall patterns across different Australian locations
3. **Feature Importance:** Humidity, pressure, and previous day rainfall are among the top predictive features
4. **Model Selection:** CatBoost outperformed other algorithms due to its ability to handle categorical features and missing values effectively

## 🔮 Future Enhancements

- [ ] **Hyperparameter Tuning:** Optimize model parameters for better performance
- [ ] **Real-time Data Integration:** Connect with live weather APIs
- [ ] **Mobile Application:** Develop mobile app version
- [ ] **Advanced Visualization:** Add interactive charts and weather maps
- [ ] **Multi-location Predictions:** Expand to global weather prediction
- [ ] **Ensemble Methods:** Implement voting or stacking classifiers

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Raimal Raja**
- GitHub: [@Raimal-Raja](https://github.com/Raimal-Raja)
- LinkedIn: [Connect with me](https://www.linkedin.com/in/raimal-raja-kolhi-860a032bb/)

## 🙏 Acknowledgments

- Kaggle for providing the Australian Weather Dataset
- The open-source community for the amazing libraries and frameworks
- Heroku for free hosting services
- All contributors and users of this project

---

📧 For questions or suggestions, feel free to reach out via GitHub issues or email.

# If you like this project please do give a star. I am also giving my LinkedIn profile. If you want we can connect there too
[https://www.linkedin.com/in/raimal-raja-kolhi-860a032bb/](https://www.linkedin.com/in/raimal-raja-kolhi-860a032bb/)




