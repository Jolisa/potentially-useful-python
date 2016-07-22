from flask import Flask, render_template 

app = Flask(__name__) 

@app.route('/')

def home():
import random

adjective_list=["A stupefying","An edifying","An austere","A treacherous","An unforeseeable","A fickle",
"A dubious","An epic","A bewildering","Auspicious"]
noun_list=["surprise","hand shake", "elbow rub", "turn of luck","foot rub",
"elevator ride","timing","kiss","epiphany","truck ride"]
feeling_list=["constipated","down in the dumps","paranoid","anxious","hopeful",
"like it's time to leave the city","surveilled","like a winner","sleepy","daring"]
random_adj=random.randint(0,len(adjective_list)-1)
random_noun=random.randint(0,len(noun_list)-1)
random_feeling=random.randint(0,len(feeling_list)-1)
print (adjective_list[random_adj])
the_noun=noun_list[random_noun]
print(the_noun)
the_feeling =  feeling_list[random_feeling]
print("will leave you feeling "+the_feeling)

return render_template("my_portfolio.css")

if __name__ == '__main__':

    app.run(debug=True)

