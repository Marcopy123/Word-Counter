from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

text = input("Enter your text here : \n")

counter = Counter(text.split())
most_common = counter.most_common(5)
most_common_values = []
most_common_words = []

for word, times_appeared in most_common:
    most_common_words.append(word)
    most_common_values.append(times_appeared)


def count_words(text):
    """ Function that counts the number of words in the text """
    total_words= 0
    for word in text.split():
        total_words += 1
    
    return f"The total number of words in the text is : {total_words}"


def draw_plot(x,y):
    sns.barplot(x,y)
    plt.title('Most Common Words')
    plt.xlabel("Words")
    plt.ylabel("Count")
    plt.show()

if __name__ == "__main__":
    print(count_words(text))
    draw_plot(most_common_words,most_common_values)
