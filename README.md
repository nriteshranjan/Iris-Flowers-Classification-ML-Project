# Iris-Flowers-Classification-ML-Project
# Machine Learning Project : Iris-flower-classification
This program applies basic machine learning (classification) concepts on *Fisher's Iris Data* to predict the species of a new sample of Iris flower.

**Software and Libraries**
- Python 3.7.0
- Anaconda 4.8.3 (64 bit)
- scikit-learn 0.22.1
- pandas

**Introduction**  
The dataset for this project originates from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Iris). The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis.
- The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor).
- Four features were measured from each sample (in centimetres): 
  - Length of the sepals
  - Width of the sepals
  - Length of the petals
  - Width of the petals

**Accuracy Scores**
Accuracy obtained = 0.9666666666666667

**Working of the Program**
- The program uses `pandas` module to import the datset
- The program then divides the dataset into training and testing samples in 80:20 ratio randomly using `train_test_split()` function available in `sklearn` module.
- The training sample space is used to train the program and predictions are made on the testing sample space.
- Accuracy score is then calculated by comparing with the correct results of the training dataset.