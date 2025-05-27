# Keywords-to-text Generator
Welcome to the GitHub repository for the keywords-to-text generator web app. In this application, still under development, we help users by generating syntactically correct text from keywords. In the current version of the app, users can input 2-5 keywords to generate conversational style text. The app isn't currently well suited to generate longer sentences. This issue will be addressed in the future.

# Files and Codes
[requirements.txt](https://github.com/burning-river/text_generator/blob/main/requirements.txt): List of dependencies for the development of the app. Use `pip install -r requirements.txt` to install.

[scrape_web.ipynb](https://github.com/burning-river/text_generator/blob/main/scrape_web.ipynb): Contains code that creates the dataset for the app. We download human entered posts on Reddit using the Reddit API. They are then split into sentences. In total, there are 1.84 million sentences. 

[preprocess_dataset.ipynb](https://github.com/burning-river/text_generator/blob/main/preprocess_dataset.ipynb): Code that cleans up the text data. It removes any non-ascii characters in the text and prepares the dataset for LLM fine-tuning.

[model_dev.ipynb](https://github.com/burning-river/text_generator/blob/main/model_dev.ipynb): Extracts keywords from sentences which form the features for the dataset. The sentences form the ground truth. The features and the ground truth are then tokenized using the `t5-small` tokenizer.

[train_text_generator.ipynb](https://github.com/burning-river/text_generator/blob/main/train_text_generator.ipynb): Contains code to fine-tune the T5-small LLM model (60.5 million parameters) using 126,000 short sentences (containing 3 to 7 words). The trained model is pushed to the Hugging Face feature store. We evaluate the model on the test set using the BERT scores. We obtain a median F1 score of 0.89. 

[app/app.py](https://github.com/burning-river/text_generator/blob/main/app/app.py): Code for the Flask App. 

[app/requirements.txt](https://github.com/burning-river/text_generator/blob/main/app/requirements.txt): List of dependencies to run the application code. 

[app/Dockerfile](https://github.com/burning-river/text_generator/blob/main/app/Dockerfile): Dockerfile for containerized deployment.

[app/heroku.yml](https://github.com/burning-river/text_generator/blob/main/app/heroku.yml): Creates Docker image on Heroku.

[app/templates/index.html](https://github.com/burning-river/text_generator/blob/main/app/templates/index.html): HTML code for website.
