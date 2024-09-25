import pandas as pd
import numpy as np

def chapter_one(data_frame) :
    return data_frame['Class']

def chapter_two(data_frame) :
    def count(df, key, value):
        return df[key].value_counts()[value]

    def calculate_prop(df, key, value):
        return count(df, key, value) / len(df)

    recurrence_prop = calculate_prop(data_frame, 'Class', 'recurrence-events')
    no_recurrence_prop = calculate_prop(data_frame, 'Class', 'no-recurrence-events')
    if recurrence_prop > no_recurrence_prop:
        return "recurrence-events", recurrence_prop
    return "no-recurrence-events", no_recurrence_prop

if __name__ == '__main__':
    column_names = ['Class', 'age', 'menopause', 'tumor-size', 'inv-nodes', 'node-caps', 'deg-malig', 'breast', 'breast-quad', 'irradiat']
    df = pd.read_csv('breast-cancer.data', names=column_names)
    print("Chapter 1:")
    print(chapter_one(df))
    print("Chapter 2:")
    result = chapter_two(df)
    print(result[0], " ", result[1])
