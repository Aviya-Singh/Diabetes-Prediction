# Diabetes Prediction Using Machine Learning and Flask

## Project Overview

This project aims to predict the likelihood of a person being diabetic based on a variety of medical parameters. It combines:

* Data preprocessing
* Exploratory data analysis (EDA)
* Model training and evaluation using multiple machine learning algorithms
* Web-based frontend built with HTML and Bootstrap
* Flask-based backend to serve the trained model for real-time predictions

## Technologies Used

* Python 3
* Pandas, NumPy
* Scikit-learn
* Seaborn, Matplotlib, Plotly
* Flask
* HTML/CSS with Bootstrap
* Jupyter Notebook

## Dataset

The dataset used is `diabetes_data_upload.csv`, containing 520 rows and 17 columns.

### Features include:

* Demographics: Age, Gender
* Symptoms: Polyuria, Polydipsia, Sudden Weight Loss, Weakness, etc.
* Target: Class (Positive/Negative for diabetes)

All features are categorical except Age.


## Data Analysis & Visualization

* Histogram and pie plots were created using Plotly to explore relationships between features and the target class.
* Crosstabs and heatmaps (Seaborn) were used to analyze the conditional probabilities and correlations between variables.

Key Insights:

* High correlation of diabetes with Polyuria, Polydipsia, and Sudden Weight Loss.
* Gender and age distribution indicate higher cases in older males.
* Weakness and Partial Paresis also show strong association.

## Model Building

### Preprocessing

* Categorical variables were encoded using `LabelEncoder`
* Age column was scaled using `MinMaxScaler`
* Dataset split into independent features `X` and target `Y`

### Train-Test Split

* Dataset split into training and test sets (80/20 or 70/30 depending on model)
* Stratified sampling was used to preserve class distribution

### Models Implemented

* Logistic Regression
* Decision Tree Classifier
* Support Vector Machine (SVC)
* Random Forest Classifier
* K-Nearest Neighbors (KNN)

All models were evaluated using metrics like Accuracy, Precision, Recall, F1-score, Confusion Matrix, and ROC.

## Model Evaluation

| Model                  | Accuracy | Recall | Precision |
| ---------------------- | -------- | ------ | --------- |
| Random Forest          | 95.51%   | 0.9711 | 0.9619    |
| Decision Tree          | 95.51%   | 0.9551 | 0.9551    |
| Logistic Regression    | 94.87%   | 0.9487 | 0.9487    |
| Support Vector Machine | 91.67%   | 0.9167 | 0.9167    |
| KNN (k=2)              | 83.97%   | 0.7884 | 0.9647    |

The **Random Forest Classifier** achieved the highest accuracy and was saved using Python `pickle` for use in the web application.

## Web Application

A web application was built using Flask.

* Frontend: HTML form styled with Bootstrap for user input
* Backend: Flask receives the input, processes it, feeds it into the model, and returns prediction

### Inputs Collected:

* Age, Gender, Polyuria, Polydipsia, Sudden Weight Loss, Weakness, Polyphagia, Genital Thrush, Visual Blurring, Itching, Irritability, Delayed Healing, Partial Paresis, Muscle Stiffness, Alopecia, Obesity

### Output:

* "Diabetes" or "No Diabetes" message with color-coded feedback

## Installation & Running

### 1. Clone the repository

```bash
git clone <repo-url>
cd <repo-folder>
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Train the model

```bash
python model_training.py
```

### 4. Run the web server

```bash
python app.py
```

Visit `http://127.0.0.1:5000/` in your browser.

## Results

The application correctly classifies diabetic and non-diabetic cases with high accuracy.
The Random Forest classifier, integrated into the backend, showed strong sensitivity and specificity, making it reliable for early screening applications.

## License

This project is licensed under the Modified BSD License - see the [LICENSE](https://opensource.org/licenses/BSD-3-Clause) file for details.

## Acknowledgment

* Dataset from Kaggle or UCI (as applicable)
* Developed using Python, Flask, and ML libraries
* Frontend styling via Bootstrap 5

## References

[1] Y. K. Qawqzeh, , A. S. Bajahzar, M. Jemmali, M. M. Otoom, and A. Thaljaoui, "“Classification of diabetes using photoplethysmogram (PPG) waveform analysis: logistic regression modeling,”," BioMed Research International, p. 6, 2020.
[2] D. K. Choubey, M. Kumar, V. Shukla, S. Tripathi, and V. K. Dhandhania, "“Comparative analysis of classification methods with PCA and LDA for diabetes,”," Current Diabetes Reviews,, vol. 16 no 8, pp. 833-850, 2020.
[3] M. Maniruzzaman, M. J. Rahman, B. Ahammed, and M. M. Abedin, "“Classification and prediction of diabetes disease using machine learning paradigm,”," Health Information Science and Systems, vol. 8 no.1, pp. 7-14, 2020.
[4] R. Ahuja, S. C. Sharma, and M. Ali, "“A diabetic disease prediction model based on classification algorithms,”," Annals of Emerging Technologies in Computing, vol. 3.no.3, pp. 44-52, 2019.