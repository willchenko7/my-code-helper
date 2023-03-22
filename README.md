# my-code-helper

This repo was created to quickly ask an openai gpt model any coding question. This simple project can easily be modified to meet your needs. For example, you can easily change the temperature settings, max token length, and model. You can also set a base prompt that will be attached prior to any prompt fed by the user.

## Setup 
1. Create your openai api keys
2. Save your keys in a json file called: "gpt3-keys.json"
3. Edit CONFIG_PATH in src/config.py to point to your config file.
4. Optionally, save this path in your bashrc file so that it can be called from anywhere on your computer.

# Example

Prompt:
```
my-code-helper.sh "how can I filter a pandas dataframe on a particular column?"
```

text-davinci-003 Answer:
```
To filter a pandas dataframe on a particular column, you can use the pandas.DataFrame.loc indexer method. This method allows you to access a subset of the dataframe based on a specific column value. For example, if you wanted to filter a dataframe df based on column 'A' having a value of 5, you could use the following line of code: df.loc[df['A'] == 5]. This will return a new dataframe with only the rows where column 'A' has a value of 5.
```