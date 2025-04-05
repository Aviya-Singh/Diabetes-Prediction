# Diabetes Prediction

## Overview
This project focuses on predicting diabetes using machine learning algorithms. By analyzing various health metrics, the system can identify individuals at risk of developing diabetes, enabling early intervention and prevention.

## Table of Contents
- [Dataset](#dataset)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Architecture](#model-architecture)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Dataset
The project uses the PIMA Indians Diabetes dataset, which includes health metrics from individuals with and without diabetes. The dataset contains the following attributes:
- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI (Body Mass Index)
- Diabetes Pedigree Function
- Age
- Outcome (Target variable: 1 for diabetes, 0 for no diabetes)

## Features
- Data preprocessing and cleaning
- Exploratory data analysis with visualizations
- Feature selection and engineering
- Implementation of various classification algorithms
- Model evaluation and comparison
- User-friendly prediction interface

## Installation
```bash
# Clone the repository
git clone https://github.com/Aviya-Singh/Diabetes-Prediction.git
cd Diabetes-Prediction

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage
To train and evaluate the model:
```bash
python train_model.py
```

To make predictions using the trained model:
```bash
python predict.py --input path/to/input_data.csv
```

For the web interface (if available):
```bash
python app.py
```
Then navigate to `http://localhost:5000` in your web browser.

## Model Architecture
This project implements several machine learning algorithms including:
- Logistic Regression
- Random Forest
- Support Vector Machines (SVM)
- K-Nearest Neighbors (KNN)
- Neural Networks

The best-performing model was selected based on metrics such as accuracy, precision, recall, and F1-score.

## Results
Our best model achieved:
- Accuracy: ~85%
- Precision: ~80%
- Recall: ~82%
- F1-score: ~81%

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.