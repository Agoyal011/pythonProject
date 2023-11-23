import pandas as pd
import numpy as np
import os

data_root = "C:/Users/Aniket/AI_datasets"


# url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/robotfailure-mld/lp1.data'


def my_function(dataframe, proportion_tr, proportion_test, target_name, file_name):
    print(dataframe)
    popped_col = dataframe.pop(target_name)
    new = dataframe.copy()
    new[target_name] = popped_col
    print(new)

    filepath = os.path.join(data_root, file_name)
    new.to_csv(filepath, index=False)
    train = new.sample(frac=proportion_tr, random_state=200)  # random state is a seed value
    test = new.drop(train.index)
    print(train)
    print(test)


paths = [
    "C:/Users/Aniket/Desktop/ecoli.csv",
    "C:/Users/Aniket/AI_datasets/Letter Recognition_data.csv",
    "C:/Users/Aniket/AI_datasets/breast_cancer_data.csv",
    "C:/Users/Aniket/AI_datasets/Ecoli_dataset.csv"
]

new_paths = [
    {
        "file_path": "C:/Users/Aniket/Desktop/ecoli.csv",
        "columns": ['Sequence', 'Name', 'mcg', 'gvh', 'lip', 'chg', 'aac', 'alm1', 'alm2'],
        "target_name": 'Sequence',
        "new_file_name": "Ecoli_dataset_new.csv"
    },
    {
        "file_path": "C:/Users/Aniket/AI_datasets/Letter Recognition_data.csv",
        "columns": ['', '', 'High', 'Lettr', 'Onpix', 'Width', 'X-bar', 'X-box', 'X-ege', 'X2bar', 'X2ybr', 'XegvyXy2br',
                    'Xybar', 'Y-bar', 'Y-box', 'Y-ege', 'Y2bar', 'Yegvx'],
        "target_name": 'Lettr',
        "new_file_name": "new_lr_data.csv"
    },
    {
        "file_path": "C:/Users/Aniket/AI_datasets/breast_cancer_data.csv",
        "columns": ['', 'ID', 'Diagnosis', 'Area1', 'Area2', 'Area3', 'Compactness1', 'Compactness2', 'Compactness3',
                    'Concave_points1', 'Concave_points2',
                    'Concave_points3', 'Concavity1', 'Concavity2', 'Concavity3', 'Fractal_dimension1',
                    'Fractal_dimension2',
                    'Fractal_dimension3', 'Perimeter1', 'Perimeter2', 'Perimeter3',
                    'Radius1', 'Radius2', 'Radius3', 'Smoothness1', 'Smoothness2', 'Smoothness3', 'Symmetry1',
                    'Symmetry2',
                    'Symmetry3', 'Texture1',
                    'Texture2', 'Texture'],
        "target_name": 'Diagnosis',
        "new_file_name": "new_bc_data.csv"
    },
    {
        "file_path": "C:/Users/Aniket/AI_datasets/Ecoli_dataset.csv",
        "columns": ['Name', 'mcg', 'gvh', 'lip', 'chg', 'aac', 'alm1', 'alm2'],
        "target_name": 'mcg',
        "new_file_name": "new_ecoli_data1.csv"
    }
]

for path in new_paths:
    df = pd.read_csv(path['file_path'])
    df.columns = path['columns']
    my_function(df, 0.7, 0.3, path['target_name'], path['new_file_name'])
    print()









