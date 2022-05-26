import os
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.metrics import auc
import shap
import pandas as pd
import pickle
this_file = os.path.basename(__file__)


def average_shap_values(dir_name,data, num_trials,num_splits):
	"""
	Takes shap values from .pkl files computed for different folds and trials and makes a mathematical average, and plots the final results.
	--------------------------
	Parameters:
	
	- dir_name : <string>, path in which there is the directory "Shap_values/"
	- data : <pandas dataframe>, data used to compute SHAP values
	- num_trials : <int>, number of repetitions
	- num_splits: <int>, number of splits for the nested cross-validation  
	
	"""
	shaps = []
	for name in ["train", "test"]:
		final_shap_values = None
		for num_trial in range(num_trials):
			for num_split in range(num_splits):
				file = open(dir_name+"/Shap_values/"+name+str(num_trial)+"fold"+str(num_split)+".pkl","rb")
				shap_values = pickle.load(file)
				if final_shap_values is None:
					final_shap_values = shap_values
				else:
					final_shap_values = final_shap_values.append(shap_values)
			
		features = list(shap_values.columns)
		features.remove("index")

		
		df = pd.DataFrame(columns=features)
		for i in range(len(data)):
			filt = final_shap_values['index'] == i
			
			df = df.append(final_shap_values[filt].sum(axis=0, numeric_only=True),ignore_index=True)
		del df["index"]
		
		
		if "train" in name:
			df = df/num_trials/(num_splits-1)
		else:
			df = df/num_trials
			
		shaps.append(df)

	return shaps


def mean_std(x):
	"""
	Returns a tuple with the mean and standard deviation of an array
	----------------------
	Parameters:
	x : np.array
	---------------------
	Returns:
	the mean and standard deviation of the array
	"""
	return np.mean(x), np.std(x)


def roc_plot(mean_fpr,tprs,dir_name,model_name,num_trials,num_splits):
	plt.figure()
	import matplotlib as mpl

	mpl.rcParams['axes.spines.right'] = False
	mpl.rcParams['axes.spines.top'] = False
	plt.plot([0, 1], [0, 1], '--', color='r', label='Random classifier', lw=2, alpha=0.8)
	mean_tpr = np.mean(tprs, axis=0)
	mean_tpr[-1] = 1.0
	mean_auc = auc(mean_fpr, mean_tpr)
	#plt.title(experiment_name + ' AUC=%0.3f' % mean_auc)
	plt.plot(mean_fpr, mean_tpr, color='b', label='Mean ROC', lw=2, alpha=0.8)

	# Youden index
	#youden, dist = youden_index(mean_fpr, mean_tpr, title = dir_name + "/roc_coords/" + "average_ROC_coords.csv")
	## Standard deviation computation
	std_tpr = np.std(tprs, axis=0)
	tprs_upper_std = np.minimum(mean_tpr + std_tpr, 1)
	tprs_lower_std = np.maximum(mean_tpr - std_tpr, 0)
	plt.fill_between(mean_fpr, tprs_lower_std, tprs_upper_std, color='green', alpha=.2,label=r'$\pm$ 1 SD')

	## 99.9% CI computation
	z = 3.291
	SE = std_tpr / np.sqrt(num_trials * num_splits)
	tprs_upper_95CI = mean_tpr + (z * SE)
	tprs_lower_95CI = mean_tpr - (z * SE)
	plt.fill_between(mean_fpr, tprs_lower_95CI, tprs_upper_95CI, color='grey', alpha=.5,label=r'$\pm$ 99.9% CI')
	#plt.scatter(youden[0],youden[1], label="Youden index")
	#plt.scatter(dist[0],dist[1], label="min distance from (0,1)")
	plt.xlim([-0.05, 1.05])
	plt.ylim([-0.05, 1.05])
	plt.xlabel('False Positive Rate')
	plt.ylabel('True Positive Rate')
	plt.legend(loc="lower right")
	#plt.axis('square')
	plt.savefig(dir_name + "average_plots/"+ model_name+"_ROCcurve.png", dpi=600)
