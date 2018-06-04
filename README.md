


# CS168 Final Project: Evaluating/Using a CNN and LSTM Model's performance on Diagnosing and categorizing different stages of Dementia.

Diagnosing Dementia and Classifying Stages of Dementia using CNN and LSTM on .nii medical images. The objective is to create and properly train and test on a huge dataset of medical images of patients, given a lot of data, figure out which data may be relevant to improving our predictions and classification of the patient's stages of Dementia. We will be using (some amount) of images as our test data, and (some amount) of images as our train data. The objective is to first train from a big set of data with the model proposed above, and then evaluate the performance of the model on a big set of test data. The readme should also consist of how to open these .nii files and how we are setting up the training and testing for the datasets.



### Prerequisites

Python and Anaconda/Jupyter Notebook (as already done from the first 2 homework assignments)


### Installing



First step is to open terminal and run:

```
pip install nibabel
```

Then install nilearn by running:


```
pip install -U --user nilearn

```
Then open IPython or choice of VirtualEnv or Jupyter Notebook etc (to quit Ipython just type exit in command prompt window) If you choose to use anaconda for example, you would run pythonw train.py instead of python3 train.py


Other note: May need to update conda by typing conda update conda if applicable.

## Running the tests

Explain how to run the automated tests for this system


### Break down into end to end tests

Run the below to execute script if using anaconda

```
pythonw train.py

```
If want to plot an image, below is an example:

```
%matplotlib inline

from nilearn import image


plotting.plot_img("../files/OAS30001_MR_d0129/anat4/test.nii")
plotting.plot_glass_brain("../files/OAS30001_MR_d0129/anat4/test.nii")  


```

## Built With

* 
* 
* 

## Sources

https://docs.python.org/3/installing/index.html

https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
