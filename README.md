# CS168 Final Project: Evaluating Different Classifiers performance on Categorizing Dementia of MRI Brain Images

Diagnosing Dementia and Classifying Stages of Dementia using SciKit's AdaBoost-SAMME, Decision Trees, Gausian Process Classification, K-Neighbors, Multi-Layer Perceptron, Random Forest, and Linear Support Vector Classification on medical MRI scans of patient's brains. Data was provided by [OASIS Cross-Sectional](https://www.oasis-brains.org).

The objective of the project is to identify the effectiveness of different classifiers at identifying if a brain MRI depicts someone with dementia or not. We use nibabel to handle the loading of the images as well as handle the preprocessing. Then, we use SciKit to create a classifier pipeline, applying a variance threshold, removing low variance features, and using ANOVA to select the best features from the images, before running our classifier on the extracted features. 



## Prerequisites

Python3

## Installing


Install required dependencies:

```
$ pip install nilearn matplotlib jupyter sklearn
```

Launch appropriate notebook:

```
$ jupyter notebook <notebook name>
```
For example, if you want to launch the SVC notebook, you would run:

``` 
$ jupyter notebook src/variance_anova_svc.ipynb 
```

## Plotting Images

If want to plot an image, below is an example:
```
%matplotlib inline

from nilearn import plotting

plotting.plot_img("<path_to_file>")
plotting.plot_glass_brain("<path_to_file>")  

```
## How to Use
Simply open a notebook as described in Installing and run Kernal -> Restart All. 
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details
