__Quick guide__:  
1. Install fasttext:  
```bash
cd fastText
sudo python setup.py install
```  
2. Train data by running train_data.py:  
```bash
python train_data <data_train_file>
```  
After the process is done, you will see a file .bin, that is the *model_file_path*.  
Note: default *data_train_file = "data"*.  

3. To get vector represents a word:  
```python
import fasttext
model = fasttext.load_model(model_file_path)
print(model['king']) # get the vector of the word 'king'
```  