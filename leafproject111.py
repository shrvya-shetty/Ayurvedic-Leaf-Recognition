import streamlit as st
from PIL import Image
import tensorflow as tf
#from keras.preprocessing.image import load_img,img_to_array
#from keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import streamlit as st
from streamlit_lottie import st_lottie
#import lottie
#from . import mymodule
#from mymodule import load_lottieurl


#from lottie import load_lottieurl

import numpy as np
from keras.models import load_model
import requests
from streamlit_lottie import st_lottie
from bs4 import BeautifulSoup

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")




#import lottie

#lottie_coding = lottie.load_animation("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

#lottie_coding = lottie.load_url("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

lottie_url = "https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json"
# ---- LOAD ASSETS ----
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

#lottie_coding = load_animation("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")


# Load the Lottie animation
#lottie_coding = lottie.load_animation("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")



img_contact_form = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# ---- HEADER SECTION ----
background_css = """
<style>
body {
    background-image: url("C:\\Users\\Shravya Shetty\\Downloads\\Automatic-Identification-Of-Ayurvedic-Leaves-Using-Deep-Learning-main\\Automatic-Identification-Of-Ayurvedic-Leaves-Using-Deep-Learning-main\i1.jpg);
    background-size: cover;
}
</style>
"""
st.markdown(background_css, unsafe_allow_html=True)

with st.container():
    st.markdown(
    """
    <style>
    @keyframes rainbow-animation {
        0% { color: red; }
        14% { color: orange; }
        28% { color: yellow; }
        42% { color: green; }
        57% { color: blue; }
        71% { color: indigo; }
        85% { color: violet; }
        100% { color: red; }
    }
    
    .animated-text {
        animation: text-animation 1s ease-in-out infinite, rainbow-animation 5s linear infinite;
        font-weight: bold;
    }
    </style>
    
    <h2 class="animated-text">HELLO, WELCOME TO OUR SITE 👋</h2>
    """,
    unsafe_allow_html=True
)
#import streamlit as st

st.markdown('<div style="border-radius: 10px; padding: 20px; background-color: #3D9970"><h1 style="color: white;">AYURVEDIC LEAF IDENTIFICATION</h1></div>', unsafe_allow_html=True)

st.write("<span style='color:#0074D9;font-weight:bold;font-style:arial;'>The premier web application designed to assist you in identifying various Ayurvedic leaves and herbs.Unlock the power of nature's remedies with our user-friendly and comprehensive leaf identification tool.</span>", unsafe_allow_html=True)

#st.write("[Learn More >](https://pythonandvba.com)")
    
    

        
        
model = load_model('leaf312.h5')
labels = {0: 'Aam', 1: 'Adulsa', 2: 'Amrud', 3: 'Annar', 4: 'Ashoka', 5: 'Aswagandha', 6: 'Babul', 7: 'Bargad', 8: 'Candan', 9: 'Ghrit Kumari', 10: 'Giloy', 11: 'Gunja', 12: 'Gurhal', 13: 'Jamun', 14: 'Karanda', 15: 'Karanja', 16: 'Karela', 17: 'Katahal', 18: 'Malabar spinach',19: 'Mogra', 20: 'Neem', 21: 'Nimbu', 22: 'Pan', 23: 'Papaya', 24: 'Peepal', 25: 'Phagoora', 26: 'Pudina', 27: 'Rasna', 28: 'Sarso', 29: 'Tindora', 30: 'Tulsi'}         
a={'Aam':'The extract of mango leaves have been used for a long time to cure asthma and it is believed that they are effective in treating diabetes. The leaves contain an abundance of nutrients. These greens are packed with pectin, fiber and vitamin C, which can be beneficial in controlling the blood sugar level.'}
b={'Adulsa':'The medicinal uses of Adulsa leaves are attributed to its antitussive, antimicrobial and anti-inflammatory properties. Its leaf juice is the most common home remedy for cough, respiratory diseases and bleeding disorders. It is also a highly effective natural medicine for respiratory infections.'}
c={'Amrud':'Guava is a traditional remedy for a number of ailments. Preliminary research suggests that compounds in guava leaf extract may have a positive effect on a range of illnesses and symptoms, including menstrual cramps, diarrhea, the flu, type 2 diabetes, and cancer.'}
d={'Annar':'Besides aiding in fat loss, pomegranate leaves are found to be useful in treating a number of disorders and ailments, such as insomnia, abdominal pain, dysentery, cough, jaundice, mouth ulcers, skin ageing, and inflammation of the skin like eczema'}
e={'Ashoka':'Ashoka is useful in controlling internal bleeding, especially in the case of piles due to its Kasaya (astringent) property. It is also beneficial in relieving pain and healing wounds faster due to its Ropan (healing) property. Applying Ashoka bark juice or kwath on the skin helps to get rid of oily and dull skin.'}
f={'Aswagandha':'Practitioners use this herb as a general tonic to boost energy and reduce stress and anxiety. Some also claim that the herb  may be beneficial for certain cancers, Alzheimer’s disease, and anxiety.'}
g={'Babul':'chewing small pieces of fresh Babool bark is good for managing oral health problems. Babool also helps in the management of diarrhea. It also provides relief from cold and cough symptoms as well as sore throat. Consuming Babool gum powder along with water once a day helps in relieving joint pain.'}
h={'Bargad':'It helps manage blood glucose levels by increasing insulin secretion due to its antioxidant properties. The antioxidants present in Banyan also helps to lower bad cholesterol levels. As per Ayurveda, it is useful in diarrhea and female problems like leucorrhea due to its Kashaya (astringent) property.'}
i={'Candan':'Sandalwood is beneficial in treating gastric irritability and other gastric ailments. The wood is used to treat dysentery. Ever since ancient times, Chandan paste has been employed to relieve headache & control the body temperature in case of fevers. Chandan is good against prickly heat.'}
j={'Ghrit Kumari':'Aloe vera gel is often used on the skin to treat sunburn, burns, and eczema. It has a soothing effect that may aid in treating symptoms caused by genital herpes, poison oak, poison ivy, and skin irritation in people treated with radiation.'}
k={'Giloy':'also known as Amrita or Guduchi in Hindi, is an herb that helps improve digestion and boost immunity. It has heart-shaped leaves that resemble betel leaves. All parts of the plant are used in Ayurvedic medicine. However, the stem is thought to have the most beneficial compounds.'}
l={'Gunja':'Abrus precatorius is a poisonous herb used in Ayurvedic medicines after detoxifying process. Its seeds and roots are used in treating hair fall, arthritis pain, as an aphrodisiac and more.'}
m={'Gurhal':'Gurhal is used for treating loss of appetite, colds, heart and nerve diseases, upper respiratory tract pain and swelling (inflammation), fluid retention, stomach irritation, and disorders of circulation; for dissolving phlegm; as a gentle laxative; and as a diuretic to increase urine output.'}
n={'Jamun':'The high alkaloid content present in jamun is effective in controlling hyperglycaemia or high blood sugar. Apart from the fruit, extracts from the seeds, leaves and bark are useful for reducing the high levels of blood sugar in your body.'}
o={'Karanda':'Its fruit is used in the ancient Indian herbal system of medicine, Ayurvedic, to treat acidity, indigestion, fresh and infected wounds, skin diseases, urinary disorders and diabetic ulcer, as well as biliousness, stomach pain, constipation, anemia, skin conditions, anorexia and insanity.'}
ae={'Karanja':'Karanja is medicinal herb mainly used for skin disorders. Karanja is widely used in managing constipation.used for piles due to anti-inflammatory properties.Karanja oil is mainly applied on the skin to manage boils and eczema as well as heal wounds due to its Ropan (healing) and antimicrobial property.'}
ad={'Karela':'Karela is rich in antioxidants and vitamins A and C, which are good for the skin. It reduces ageing and fights acne and skin blemishes. It is useful in treating various skin infections like ringworm, psoriasis, and itching. Karela juice adds lustre to the hair and combats dandruff, hair loss, and split-ends.'}
p={'Katahal':'The several parts of jack tree including fruits, leaves, and barks have been extensively used in traditional medicine due to its anticarcinogenic, antimicrobial, antifungal, anti-inflammatory, wound healing, and hypoglycemic effects.'}
q={'Malabar spinach':' Malabar spinach is a well known nutritious vegetable and a natural coolant. It nourishes, makes the body stout, purifies blood, rejuvenates and acts as aphrodisiac. Including it in regular diet helps to prevent weakness of bones, anemia, cardiovascular diseases and cancers of colon'}
r={'Mogra':'They tend to reduce stress and depression just by being in an area near you. It was also used as a medicine in the earlier days because it can heal wounds. Another way it alleviates pain is by reducing headaches and backaches. Its oils are still used in massage therapies that can help aid arthritis.'}
s={'Neem':'Neem is used for leprosy, eye disorders, bloody nose, intestinal worms, stomach upset, loss of appetite, skin ulcers, diseases of the heart and blood vessels (cardiovascular disease), fever, diabetes, gum disease (gingivitis), and liver problems. The leaf is also used for birth control and to cause abortions.'}
t={'Nimbu':'Lemons contain about 31 grams of Vitamin C, which is nearly double the amount of Vitamin C needed in your daily diet. Along with boosting immunity, this burst of Vitamin C can reduce your risk of stroke and heart disease with regular consumption.'}
u={'Pan':'It is most commonly used to treat chronic bronchitis, asthma, constipation, gonorrhea, paralysis of the tongue, diarrhea, cholera, chronic malaria, viral hepatitis, respiratory infections, stomachache, bronchitis, diseases of the spleen, cough, and tumors.'}
v={'Papaya':'The leaves are used to make medicine. Papaya is used for preventing and treating gastrointestinal tract disorders, intestinal parasite infections, and as a sedative and diuretic. It is also used for nerve pains (neuralgia) and elephantoid growths also useful in treatment of dengue.'}
w={'Peepal':'Leaves have been traditionally used in the treatment of heart ailments, nose bleeding, diabetes, constipation, fever, jaundice, etc. You can take some extract of 2-3 leaves of Peepal tree and mix it with water and little sugar, taking this mix twice a day can help in relieving symptoms of jaundice.'}
x={'Phagoora':'Roasted figs are taken for diarrhea and dysentery. Root latex is used in mumps, cholera, diarrhea and vomiting. Several tribes in Northern eastern India especially in Manipur use the leaf of Ficus auriculata, traditionally for the treatment of diabetes.'} 
y={'Pudina':'Contains menthol that can help relax muscles and ease the pain. Applying pudina juice on your forehead and temples can give you relief from headache. Also, balms of pudina base or mint oil are effective in curing headaches.'}
z={'Rasna':'Rasna is a herb mentioned in Ayurveda for the treatment of pain, indigestion, gout, cough and general debility. Vanda roxburghii and Alpinia galanga is also taken as Rasna in Bengal and South India respectively. Latin name- Pluchea lanceolata C.B Clarke. Family- Asteraceae.'}
aa={'Sarso':'It is a folk remedy for arthritis, foot ache, lumbago and rheumatism. Brassica juncea is grown mainly for its seed used in the fabrication of brown mustard or for the extraction of vegetable oil. Brown mustard oil is used against skin eruptions and ulcers.'}
ab={'Tindora':'Ivy gourd is most often used for diabetes. People also use ivy gourd for gonorrhea, constipation, wounds, and other conditions, but there is no good scientific evidence to support these uses. Ivy gourd fruit and leaves are also used as a vegetable in India and other Asian countries.'}
ac={'Tulsi':'Tulsi most popularly known as Tulsi has been used for thousands of years in Ayurveda for its diverse healing properties. Healing Power: The Basil or Tulsi plant has many medicinal properties. The leaves strengthen the stomach and help in respiratory diseases.'}

def fetch_name(prediction):
    try:
        URL = "https://www.google.com/search?q=scientific+name of"  + prediction
        headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
    }
        page = requests.get(URL,headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        name = soup.find(class_='Z0LcW').get_text()
        return name
    except Exception as e: 
        st.error("Can't able to fetch the Scientific Name")
        print(e)

def processed_img(img_path):
    img=load_img(img_path,target_size=(100,100,3))
    img=img_to_array(img)
    img=img/255
    img=np.expand_dims(img,[0])
    answer=model.predict(img)
    y_class = answer.argmax(axis=-1)
    print(y_class)
    y = " ".join(str(x) for x in y_class)
    y = int(y)
    res = labels[y]
    print(res)
    return res.capitalize()

def run():
    st.title("Ayurvedic Leaves And Their Benefits")
    img_file = st.file_uploader("Choose an Image", type=["jpg", "png"])
    if img_file is not None:
        img = Image.open(img_file).resize((250,250))
        st.image(img,use_column_width=False)
        save_image_path = 'D:/project-image'+img_file.name
        with open(save_image_path, "wb") as f:
            f.write(img_file.getbuffer())


        # if st.button("Predict"):
        if img_file is not None:
            result= processed_img(save_image_path)
            st.success("**Predicted : "+result+'**')
        na = fetch_name(result)
        if na:
            st.warning('**Scientific Name:' +na+'**')
        if result in a:
            st.info('**Benifits : '+ a.get('Aam')+'**')
        elif result in b:
            st.info('**Benifits : '+ b.get('Adulsa')+'**')
        elif result in c:
            st.info('**Benifits : '+ c.get('Amrud')+'**')
        elif result in d:
            st.info('**Benifits : '+ d.get('Annar')+'**')
        elif result in e:
            st.info('**Benifits : '+ e.get('Ashoka')+'**')
       # elif result in f:
       #     st.info('**Benifits : '+ f.get('Aswagandha')+'**')
        elif result in g:
            st.info('**Benifits : '+ g.get('Babul')+'**')
        elif result in h:
            st.info('**Benifits : '+ h.get('Bargad')+'**')    
        elif result in i:
            st.info('**Benifits : '+ i.get('Candan')+'**')
        elif result in j:
            st.info('**Benifits : '+ j.get('Ghrit Kumari')+'**')
        elif result in k:
            st.info('**Benifits : '+ k.get('Giloy')+'**')
        elif result in l:
            st.info('**Benifits : '+ l.get('Gunja')+'**')
        elif result in m:
            st.info('**Benifits : '+ m.get('Gurhal')+'**')
        elif result in n:
            st.info('**Benifits : '+ n.get('Jamun')+'**')
        elif result in o:
            st.info('**Benifits : '+ o.get('Karanda')+'**')
        elif result in ae:
            st.info('**Benifits : '+ ae.get('Karanja')+'**')
        elif result in ad:
            st.info('**Benifits : '+ ad.get('Karela')+'**')
        elif result in p:
            st.info('**Benifits : '+ p.get('Katahal')+'**')
        elif result in q:
            st.info('**Benifits : '+ q.get('Malabar spinach')+'**')
        elif result in r:
            st.info('**Benifits : '+ r.get('Mogra')+'**')
        elif result in s:
            st.info('**Benifits : '+ s.get('Neem')+'**')
        elif result in t:
            st.info('**Benifits : '+ t.get('Nimbu')+'**')
        elif result in u:
            st.info('**Benifits : '+ u.get('Pan')+'**')
        elif result in v:
            st.info('**Benifits : '+ v.get('Papaya')+'**')
        elif result in w:
            st.info('**Benifits : '+ w.get('Peepal')+'**')
        elif result in x:
            st.info('**Benifits : '+ x.get('Phagoora ')+'**')
        elif result in y:
            st.info('**Benifits : '+ y.get('Pudina')+'**')
        elif result in z:
            st.info('**Benifits : '+ z.get('Rasna')+'**')
        elif result in aa:
            st.info('**Benifits : '+ aa.get('Sarso')+'**')
        elif result in ab:
            st.info('**Benifits : '+ ab.get('Tindora')+'**')
        elif result in ac:
            st.info('**Benifits : '+ ac.get('Tulsi')+'**')
run()



        
