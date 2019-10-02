from classifier import *
from requests_oauthlib import OAuth1Session

clf = SentimentClassifier()

def getData(topic, ck, cs, rk, rs, quantity=100):
    session = OAuth1Session(ck,
                            client_secret=cs,
                            resource_owner_key=rk,
                            resource_owner_secret=rs)
    url = 'https://api.twitter.com/1.1/search/tweets.json?q=' + topic + '&count=' + str(quantity)
    r = session.get(url)
    return r.json()

def main():
    topic = "MechitaChallenge"
    ck = "DoqLsqxYVx9wA19pa5Ttc2KB3"
    cs = "LYMDbqKaKL8FAzhcG0F08lqQDd8zrBCedGvctQZCFzJp8JYnOq"
    rk = "329999787-JPgY2hgSSHHfqoaOyZxFOJMUVlF292zKVOWElXiQ"
    rs = "VqgsnBsCTn36Y4SksCw6bGYiepy01VgZ6GLVNCVrtL4MG"

    print("Obteniendo opiniones sobre: #" + topic)

    tweets = getData(topic, ck, cs, rk, rs)["statuses"]
    count = 0
    total = 0
    for tweet in tweets:
        x = tweet["text"]
        prediction = clf.predict(x)
        print(x + ' ==> %.5f' % prediction)
        total += 1
        if(prediction) < 0.5:
            count += 1
    count = count * 100 / total
    print("----------------------------------------------------------------")
    print("El " + str(count) + "% tiene opiniones negativas sobre #" + topic)



if __name__ == "__main__":
    main()
