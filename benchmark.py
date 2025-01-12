import csv
from commit_classification import classify_commit_message
from more_itertools import ilen
from pycm import ConfusionMatrix

LABELS = ['bug fix', 'refactoring', 'new feature']

def run_becnhmark():
    labels_index = {
        label:index for index, label in enumerate(LABELS, start=1)
    }
    actual_labels_indices = []
    predict_labels_indices = []
    with open('dataset.csv', 'r', newline='') as dataset_file:
        dataset = csv.DictReader(dataset_file, delimiter='#')
        for row in dataset:
            message = row['comment']
            actual_label = row['label']
            actual_label_index = labels_index[actual_label]
            predict_label = classify_commit_message(message)
            predict_label_index = labels_index[predict_label]
            actual_labels_indices.append(actual_label_index)
            predict_labels_indices.append(predict_label_index)
    correct_predictions = ilen(filter(lambda pair: pair[0] == pair[1], zip(actual_labels_indices, predict_labels_indices)))
    total_predictions = len(predict_labels_indices)
    wrong_predictions = total_predictions - correct_predictions
    print(f'Correct predictions: {correct_predictions}/{total_predictions} ({round(correct_predictions/total_predictions, 2)*100}%)')
    print(f'Wrong predictions: {wrong_predictions}/{total_predictions} ({round(wrong_predictions/total_predictions, 2)*100}%)')
    for label, index in labels_index.items():
        print(f'{index}. {label}')
    cm = ConfusionMatrix(predict_vector=predict_labels_indices, actual_vector=actual_labels_indices)
    print(cm)

if __name__ == '__main__':
    run_benchmark()
