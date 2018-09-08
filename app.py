# -*- coding: utf-8 -*-
"""
Flask app UI
Created on Sat Sep  8 12:34:46 2018

@author: Roman
"""


from flask import Flask, render_template, request, Response, render_template_string, stream_with_context,  send_file
import webbrowser
import urllib.request
import json
import re
import ssl

CAPITALS = ['Sydney', 'Melbourne', 'Brisbane', 'Darwin', 'Hobart', 'Adelaide', 'Perth', 'Canberra']
ssl._create_default_https_context = ssl._create_unverified_context
gn_key="8a575cb0ec28485bb090447fcae5a402"
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/start_job", methods=["POST"]) 
def start_job():
    #our main module to render a bunch of google charts...
    #query keyword is passed here from the landing page
    key_word = request.form["keyw"]
    key_word=key_word.lower()
    tweeter_string = """
    Cancer, hurricanes, the plague, Hitler, Pol Pot, poverty, floods, bushfires, etc. etc. The irrationality is astounding. If praying to God will stop the drought, then by extension, God is causing the drought at the moment and is just waiting for us to ask him to make it rain.Finding that most blood cancer specialists viewed #Palliativecare as just end of life care or hospice - need to build understanding of value as an additional specialty that can support treatment - #integration #communication #ANZSPM18 #hematology #palloncSteve Jobs' last words ...

He died a billionaire at 56 y.o. of Pancreatic Cancer and here are his last words on the sick bed:

 "I reached the pinnacle of success in the business world. In others’ eyes my life... https://www.facebook.com/124200931526612/posts/279363536010350/ …If this is what it takes to reduce skin cancer rates, and might help mitigate climate change, then really I'm fine with this. https://twitter.com/GuardianAus/status/1038019730324348929 …Distant shores shimmer on the edge of your consciousness. Loca... More for Cancer http://bit.ly/yk3b9m Life on mars? Cure for cancer? Pigs can fly? No, no it is something much more earth shattering I just know it.So full story, had a bit of a cancer scare. We're pretty sure I'm all good, but yeah. I let a few close friends know, mostly just to keep people posted, but also so I wasn't bottling like I tend to do.Discussing the Fear of Cancer Recurrence and Uncertain Prognosis, we have Leah Jane Curran, @drbelindathewes, and Louise Sharpe #ANZSPM18Consumer story: Georgia and breast implant associated cancer https://ift.tt/2oMVfMY Applying the evidence for exercise in #cancer care to #palliativecare with @drbobbycheema #ANZSPM18pic.twitter.com/swJEE0BtzGSomeone near and dear to you is having a change of heart. Thei... More for Cancer http://bit.ly/yk3b9m #Palliative medicine has something really valuable to add to cancer care and especially blood cancer care - @tomleblancMD #ANZSPM18#dyk in 2016 a joint panel from the WHO and the Food and Agriculture Organization of the UN issued a review of glyphosate and concluded it poses no cancer risks when consumed in food? #knowthefacts #factoverfiction
important to let go by without amplification. Complacency is like a cancer. https://twitter.com/profpcdoherty/status/1037461109916065792 …Very concerning when @RACGP lends it's credibility to courses presented by folks claiming to heal cancers with hypnosis - perhaps it is the quantum physics they combine with the hypnosis doing the trick pic.twitter.com/BMvRKlLteCProfessor Jim Pratley told Open House the chemical is safe when used correctly and that banning glyphosate would severely impact world food supply. #glyphosate #GlyphosateAwarenesshttps://hope1032.com.au/stories/open-house/2018/is-a-us-court-decision-linking-weedkiller-and-cancer-fake-news/ …Case study from Power of the #Humanities - 'Enlisting #Shakespeare to help fight cancer' - what #linguistics and bio-informatics have achieved through a remarkable cross-disciplinary collaboration.NOW OPEN! On Sunday 28 October, come and join participants across Australia in the Australian Indoor Rowing Challenge and raise funds for the Cancer Council.#AIRC2018 @Concept2_AU @_776BCpic.twitter.com/IAn1qb8sZenot unusual for respectable rural women to provide green butter and related brownies to friends with cancer https://twitter.com/merryboffin/status/1036772340087095296 …Tweeps, if you are an international leader in medical research (Immunology, Genetics, Cancer, Neuroscience...) & wish to be my boss, please consider applying for Director of @JCSMR at @ourANU highly reputable institute with excellent researchers, 
Yet another study highlighting the importance of metabolism in cancer. Known for a long time but forgotten by the Genomics folks. https://twitter.com/auscancercomp/status/1037949218575601664 …can cancer leave my family the fuck alone pleaseAIDS or cancer? #NRLStormSouths#headandneckcancer 5+YR-survival increased 52.5-64.5% from 1970/1977-2007/2013. Why are some #cancer types going backwards? https://twitter.com/thelancetoncol/status/1035418201193164802 …'Big data' says you're a cancer risk. Do you want your insurer to know? Do you want to know? http://www.abc.net.au/news/science/2018-09-01/health-data-growth-has-privacy-legal-implications/10156396 …OPINION: AS a newspaper editor, I knew Rudd very well. It’s time to inject some truth into his recent statements about media, and remind him of the things he did to destroy Labor, writes @penbo.http://bit.ly/2PVmn90 When I was in bed for 10 months with cancer, I was literally begging friends to bring me food. I was starving.

99% of people wouldn't do it. Everyone was "too busy". I ended up in acute care at RNS Hospital. I almost died.

I can't let it go, I'm still really bitter about it.Yesterday my best friend of 31 years and a fellow SW passed. It’s left a huge hole in my life. She lived 4 doors down from me, so I saw her a few times a day. She still worked up to the age of 80 with her regs of 50 years! RIP #Cancer #maturesexwork #regularclientsLearning about what #Genomics can teach us about #cancer #APOS18 @GarvanInstitutepic.twitter.com/MA5WkgCzMnSigns Of Colon Cancers That You Have Been Ignoring For Years And What You Can Do http://bit.ly/2M8e9Hj Is videoconferencing a good option for doing psych assessments w #AYA #cancer #patients in busy clinical settings? A: Yes! Feasible + no impact on pt/clinician comfort discussing tricky psych topics  thanks to funders @thekca! https://www.researchprotocols.org/2018/8/e168/   @EHEALTH_PSYONCOpic.twitter.com/yBVFw8zi1kPAPER OUT!!! "#Radiation, #Inflammation and the #ImmuneResponse in #Cancer" with @ALHudson2017 on behalf of @BillWalshLab @SydneyNeuroOnc @Sydney_Vital @MarkHughesFdn. Paper at: https://www.ncbi.nlm.nih.gov/pubmed/30178305 pic.twitter.com/N3NnqMUTNqBrilliant talk by Prof Haber on the Zero Childhood Cancer Program and its success at #APOS18 #ChildhoodCancerAwarenessMonth #ChildhoodCancerWe’re underway for #APOS18 @GarvanInstitute. Welcomes by @ProfDMThomas and @GregHuntMP & @Dr_R_Kurzrock has begun her plenary about Precision Cancer Medicine: past, present, future. A great start to an amazing lineup of precision oncology expertise for talks, panels & workshops. pic.twitter.com/yqrQ2XJxkKTo use targeted cancer therapy need to identify the right biomarker for the right patient at the right time @Dr_R_Kurzrock #APOS18 @GarvanInstitutepic.twitter.com/EbZcApBjFFThrilled to be at the Australian Precision Oncology Symposium today at the @GarvanInstitute and looking forward to a fantastic program! #APOS18 #PrecisionMedicine #Genomics #Cancer #clinicaltrialspic.twitter.com/BAbEhXXeOSTargeting Cancer Julie's Story- The Making of the Immobilisation Mask https://youtu.be/5MgidyDEabs  via @YouTube @CCNewSouthWales @throatsurgeon @TargetingCancer @beyondfiveorg @hagsie @HeadNeckNZ @swallowsgroup @CNSA_ORG @SpeechPathAus @JuliaMaclean @FacRadOncology @sasanofpic.twitter.com/i0LBNaLkrzTom LeBlanc speaking about the involvement (or lack of!) palliative care in haematological cancers: “Change is coming, and probably faster than you think” Great session. #ANZSPM18pic.twitter.com/dNrr9il46cKeeping the #TargetingCancer flag flying high over the Vasco De Gama Bridge in beautiful Lisbon! @lucindamorris23 @sandraturner49pic.twitter.com/eX9PXpLcJ4Smart phones, smart homes, smart offices, smart cars... The cumulative radioactive bombardment from so many smart devices makes one thing very clear: smart is the new dumb.

#Cancer #Radiation #Fertility #Pregnancy #SmartMeters #EHS #EMF #Health #Parenting #5G
    """
    
    big_goog_string=''
    bd=[]
    cl=[]    
    for city in CAPITALS:
        gn_path="https://newsapi.org/v2/everything?q=" +key_word+"&q="+ city + "&sources=google-news-au&apiKey="+gn_key
        request1 = urllib.request.Request(gn_path)
        response = urllib.request.urlopen(request1)
        j = json.loads(re.search(r'{.*}',response.read().decode('utf-8')).group())
        bd.append(j)
        cl.append(city)
    for j in bd:
        for item in j['articles']:
            print(item['title']+'\n')
            big_goog_string +=item['title']
    tweeter_string = tweeter_string.replace("\r"," ").replace("\n"," ").lower()
    google_string = big_goog_string.replace("\r"," ").replace("\n"," ").lower()
    print(key_word)
    return render_template('results.html', tweeter_feed = tweeter_string, key_wd = key_word, google_feed = google_string)





if __name__ == "__main__":
    urll='http://127.0.0.1:5000/'
    webbrowser.open(urll, new=2, autoraise=True)
    app.run()
