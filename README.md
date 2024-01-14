# Heart Disease Prediction

![Heart Disease Prediction](https://www.emergencyphysicians.org/siteassets/emphysicians/all-images/kwtg/heart-attack.jpg)

## Overview

This repository contains a comprehensive Heart Disease Prediction system that leverages machine learning to predict the likelihood of an individual having a heart problem based on various input parameters. The project achieves an impressive accuracy of 94% and employs a combination of data analysis, visualization, and optimal algorithm selection.

## Tools, Libraries, and Frameworks Used

- **Flask**: For building the web application and serving predictions.
- **Numpy**: Fundamental package for scientific computing with Python.
- **Pandas**: Data manipulation and analysis library.
- **HTML, CSS**: Front-end development for the user interface.
- **Machine Learning**: Core technology for training predictive models.
- **Data Analysis**: Techniques to extract meaningful insights from the dataset.
- **Visualization**: Matplotlib and Seaborn for creating insightful charts and plots.
- **Validation Techniques**: Ensuring model robustness and reliability.
- **Optimal Algorithm Selection**: Choosing the most suitable algorithm for accurate predictions.

## Project Structure

- **/Dataset**: Contains datasets used for training and testing the model.
- **/models**: Stores the trained machine learning models.
- **/static**: Holds static files like CSS for the web application.
- **/templates**: HTML templates for the web application.
- **/Model.ipynb and heart-disease.ipynb**: Python Notebook for EDA and Model Building
- **/Demo_Model.sav and Final Model.sav**: Demo Machine Learning Model & Final Machine Learning Model

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/John-Alex07/Heart-Disease-Prediction.git
   cd Heart-Disease-Prediction
2. Install the dependencies
   ```bash
   pip install -r requirements.txt
3. Run the application
   ```bash
   run App.py
4. Open the app
   Open your browser and go to http://localhost:5000 to use the Heart Disease Prediction system.

## Result
   # Confusion Matrix for the final model with the considered features
   ![Confusion Matrix](https://github.com/John-Alex07/Heart-Disease-Prediction/blob/master/Confusion%20Matrix.png)

   # Final Perfomance Metric Values of the Explored Models
   ![Perfomance Metric Values](https://github.com/John-Alex07/Heart-Disease-Prediction/blob/master/Result.png)

   # Conclusion
   By comparing different machine learning models based on accuracy score, it is found that **Random Forest** classifier works best for this dataset.
