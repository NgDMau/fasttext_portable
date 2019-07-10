import fasttext
import sys

default_data_file = "data"
default_train_method = "cbow"

def train(path_to_data_file):
    model = fasttext.train_unsupervised(path_to_data_file, model=default_train_method)
    model.save_model(path_to_data_file + "_model.bin")

if __name__ == "__main__":
    try:
        train(sys.argv[1])
    except IndexError:
        train(default_data_file)

