# Adult Income Census Prediction

## 📄 Description
The Adult Income Census Prediction project is a machine learning challenge that predicts whether or not an individual's income exceeds a given level based on a variety of variables or traits. This sort of project is frequently related with the dataset from the 1994 Census Bureau database, generally known as the "Census Income" dataset.
The objective is to create a prediction model that can categorize people into two income groups: Those who earn more than a certain amount (often $50,000 per year) and those who earn less.

The following are the essential components and steps involved in such a project:

1. **Dataset**: A dataset often comprises information about individuals, such as age, education level, marital status, employment, work class, and other characteristics. For model construction and assessment, the dataset is separated into training and testing sets.

2. **Target Variable**: The target variable is the one you want to forecast, in this example whether an individual's salary is above or below a given level.

3. **Data Exploration and Preprocessing**: EDA is used to understand the distribution of features, discover missing values, and deal with outliers. Handling categorical variables, encoding, and scaling numerical characteristics are examples of preprocessing procedures.

4. **Feature Engineering**: The creation of new features or the transformation of existing ones in order to improve the model's performance. This might entail collecting useful information from certain traits or combining them in a meaningful way.

5. **Model Selection**: Choosing a machine learning algorithm that is appropriate for the classification problem. Decision Trees, Random Forests, Support Vector Machines, and Logistic Regression are common methods for this sort of project.

6. **Model Training**: The chosen model is trained on the training dataset, learning patterns and correlations between features and the target variable.

7. **Model Evaluation**: To analyze the trained model's performance, it is tested on a separate testing dataset. Accuracy, precision, recall, F1-score, and the area under the Receiver Operating Characteristic (ROC) curve are all common assessment criteria.

8. **Hyperparameter Tuning**: Optimizing the model's performance by fine-tuning its hyperparameters. This might include strategies such as grid search or random search.

9. **Model Deployment**: Once the model's performance has been validated, it may be used to generate predictions on previously unknown data.

10. **Interpretability and Explanation**: Understanding and interpreting the model's predictions, particularly in sectors where interpretability is critical, such as finance or law.

The Adult Income Census Prediction project is a typical example of a binary classification issue, and its success is dependent on data quality, feature engineering, and the machine learning model employed. It is a real-world application of machine learning for making predictions about socioeconomic aspects in the actual world.

## 📂 Required file(s)
- Initial dataset(Optional to explore):
- - https://github.com/tirumaleshn2458/adult-income-prediction/blob/be09061d37b8bd31c5d866f485a558077741e1e2/data/adult.csv
- Machine Learning model to predict the values:
- - https://github.com/tirumaleshn2458/adult-income-prediction/blob/be09061d37b8bd31c5d866f485a558077741e1e2/data/hist_grad_bc.pkl
- And the remaining files in data folder

## 🖥️ Installation

### Requirements
- Python 3.5+
- Scikit-learn
- Pandas
- Numpy

## 🛠️ Setup
<ol>
<li> Install pandas : `pip3 install pandas` </li>
Markup :  `pip3 install pandas`
<li> Install scikit-learn : `pip3 install scikit-learn` </li>
<li> Install Numpy : `pip3 install numpy` </li>
<li> Download the repository</li>
- Using git command : `git clone "https://github.com/tirumaleshn2458/adult-income-prediction.git"`
- Or directly download the zip file by clicking the below link and extract
https://github.com/tirumaleshn2458/adult-income-prediction/archive/refs/heads/main.zip
</ol>

## Running
<ol>
<li>Open terminal</li>
<li>Go to the downloaded or cloned repository : `cd adult-census-prediction` </li>
<li>Run the main file : `python3 main.py` </li>

</ol>
