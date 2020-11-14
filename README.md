# Fem-Bot 

# Inspiration ⚡ 
Worldwide, 1 in 3 women have experienced physical or sexual violence — mostly by an intimate partner. When accounting for sexual harassment, this figure is even higher. Worldwide, almost 3 in 5 women killed were killed by their partners or family in 2017. 
In order to be considered violence against women, the act must be committed solely because the victim is female.
Sexual harassment includes non-contact forms, like sexual comments about a person’s body parts or appearance, whistling, demands for sexual favors, 
sexually suggestive staring, stalking, and exposing one’s sexual organs at someone. It also includes physical contact forms, like grabbing, pinching, slapping, or 
rubbing against another person in a sexual way.

<strong>Most of the crimes don't even get reported and are left unresolved. Approximately 15 million adolescent girls (aged 15 to 19) worldwide have experienced forced 
sex at some point in their life. And India ranks 133 in the women, peace and security index rating. 
</strong>

<p  align="center"><img height= "400" width = "800" src = "https://github.com/Apurva-tech/Fem-Bot/blob/main/map_images/maps-readme-2.gif"></p>


# What it does 🤖

## FemBot is a twitter bot that helps get tweets related to gender related crimes more traction on twitter and increase their reach. Our project aims to contribute towards making sure incidents don’t go unnoticed by authorities and get more attention because of being in the public domain.

# How We built it 💡

First we extracted a certain number of tweets(latest first) having hashtags related to crime against women. Once the tweets are retrieved, we perform sentiment analysis on them to figure out whether the tweets are positive – spreading awareness about women crimes or empowering women, negative – victims asking for immediate help and tweets having neutral tone as well.  
For training our model we collected tagged twitter data and performed cleansing by removing URLs, usernames, numbers, special characters, etc. after which the text was processed and tokenized. The data is then transformed into a bag of words representation. Naïve Bayes Classifier is used for classification. The model was about x% accurate.
This model is used for classifying the tweets which we extracted earlier(with respect to certain hashtags) and then retweets it. It also tags the authorities to bring crimes to their notice so that they can reach out to the victim and offer immediate help. <strong>The auto retweet and reply features have been implemented using the twitter API and the Python tweepy library. </strong> 


# Challenges we ran into 🧠

- 1. Creating a model to perform sentiment analysis with a good model accuracy. 
- 2. Using the API keeping in mind the rate limit for Twitter API.
- 3. Creating Statistics data for the website. 
- 4. Deploying the bot. 

# Accomplishments that we are proud of 😌
## We created a completely functional bot , which can make a small in society. We successfully embeded all the tweets and created stats for our website.

# What we learned 🤩
We learned how to use the Twitter API and fetch realtime data for the website. 

# What's next for Fem-Bot 📈
## ➡ Tag authorities based on the geographic location
Currently the bot tags international authorities. It can be made versatile enough to tag authorities based on the geographic location of the twitter user and the crimes.
## ➡ Improve the sentiment analysis model
The accuracy of the sentiment analysis model can be increased in the future.
## ➡ Extend the bot to other crime genres
Fembot mainly focuses on gender related crimes and more prominently those against women. This model can be used for other genres of crime and be made more inclusive for other communities.

# Built With ⚙
- [x] Python 
 - ✔  Virtualenv
 - ✔  Tweepy
- [x] Twitter API 
- [x] HTML/CSS
- [x] Javascript
- [x] Simplemaps
- [x] Deployed on Vercel
