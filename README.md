# Fem-Bot <img src="https://media.giphy.com/media/3oge7Ve0gmIOhJkhOg/giphy.gif" width="80" height = "70" >

### Inspiration ⚡ 
<strong>Gender based crimes are highly prevalent in India. Most of the crimes don't get reported and are left unresolved. We wanted to do our part in making sure authorities are held accountable and can't get away with refusing to register or acknowledge cases.
</strong>


<p  align="center"><img height= "400" width = "800" src = "https://github.com/Apurva-tech/Fem-Bot/blob/main/map_images/maps-readme-2.gif"></p>

### What it does 🤖

First it extracts a certain number of tweets having hashtags related to crime against women, and supporting women. Once the tweets are retrieved, it performs sentiment analysis on them to figure out whether the tweets are spreading awareness about women crimes and empowering women or asking for immediate help and classifies them as 'positive' or 'negative', respectively. It retweets tweets and under tweets asking for help (negative), it tags authorities publicly to increase the visibility of the tweets and bring them to their notice.

### How We built it 💡

1. We used the tweepy module and the Twitter API to extract tweets with certain hashtags, and then performed sentiment analysis on them.
2. For training our model we collected tagged twitter data and pre-processed it. The tweets were labelled as either 'positive' or 'negative.'
3. We used spaCy for text classification, which is an open-source python NLP library. Thus, training data was prepared and the model was trained for 10 epochs. The model is tested on the test dataset and it is observed to have a decent accuracy.
4. This model is then used to classify the extracted tweets and also tag appropriate authorities as per the sentiment to bring crimes to their notice for immediate help. 
5. The auto retweet and reply features have been implemented using the twitter API and the Python tweepy library.
6. The website UI/UX was designed using Figma and then developed using HTML, CSS and jQuery. Simplemaps were used to visualize maps with the relevant data and the twitter feed was embedded from publish.twitter.com.


### Challenges we ran into 🧠

- Creating a model to perform sentiment analysis with a good model accuracy. 
- Using the API keeping in mind the rate limit for Twitter API due to which we couldn't deploy the bot. 

### Accomplishments that we are proud of 😌
 We created a completely functional twitter bot, which can make a small difference in society. We successfully embedded all the tweets and created stats for our website.

### What we learned 🤩
We learned how to use the Twitter API and fetch realtime data for the website. 

### What's next for Fem-Bot 📈
#### ➡ Tag authorities based on the geographic location
Currently the bot tags international authorities. It can be made versatile enough to tag authorities based on the geographic location of the twitter user and the crimes.
#### ➡ Improve the sentiment analysis model
The accuracy of the sentiment analysis model can be increased in the future.
#### ➡ Extend the bot to other crime genres
Fembot mainly focuses on gender related crimes and more prominently those against women. This model can be used for other genres of crime and be made more inclusive for other communities.

### Help File 💻
- [x] Clone the repository to your local directory
 - `git clone https://github.com/Apurva-tech/Fem-Bot.git`
 
- [x] Create a twitter developer account and generate API keys and Access keys 
 - Add your keys to the script bot.py
 
```python
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''
```
 
- [x] Now create a virtualenv for your local directory
 - `pip install virtualenv`
 - `virtualenv env`
 - `env\Scripts\activate`
 - `python bot.py`

- [x] Ctrl + C to stop the infinite loop, check your bot account to see the bot in Action!!

### Built With ⚙
- [x] Python 
 - ✔  Virtualenv
 - ✔  Tweepy
 - ✔  SpaCy
- [x] Twitter API 
- [x] HTML/CSS
- [x] Javascript
- [x] Simplemaps
- [x] Deployed on Vercel

### Try it out 👇🏽

- 🤖 [The Fem-Bot](https://twitter.com/_FemBot_)
- 🕸 [The Website](https://fem-bot.vercel.app/#home)
- 🖥 [The Figma Prototype](https://www.figma.com/file/85YouCfOSe4H6J40V2ccaS/TwitterBOT?node-id=0%3A1)

### 3️⃣ Cheers to the team 🥂
- [Gurnehmat Kaur Dhindsa](https://github.com/gkdhindsa) 
- [Vishaka Mohan](https://github.com/vishaka-mohan) 
- [Apurva Sharma](https://github.com/Apurva-tech) 
