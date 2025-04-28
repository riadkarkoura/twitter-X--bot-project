import random

# مجموعة مواضيع الذكاء الاصطناعي في الإعلام
topics = [
    "تحرير الفيديو باستخدام الذكاء الاصطناعي",
    "تصميم الصور الإبداعية مع Midjourney",
    "كتابة المحتوى باستخدام ChatGPT",
    "تحليل بيانات الجمهور عبر أدوات AI",
    "إنشاء عروض تقديمية ذكية مع Beautiful.ai",
    "تسريع التحرير الصحفي بأدوات الذكاء الاصطناعي"
]

# جمل افتتاحية لجذب الانتباه
openers = [
    "هل تبحث عن طريقة مبتكرة لتطوير عملك الإعلامي؟",
    "اكتشف كيف يمكنك استخدام الذكاء الاصطناعي لصناعة محتوى مذهل!",
    "اليوم نقدم لك أداة ستغير طريقة عملك الإعلامي!",
    "دع الذكاء الاصطناعي يساعدك في إنشاء محتوى أسرع وأقوى!"
]

# جمل ختامية لتحفيز القارئ
closers = [
    "جربها اليوم وشاركنا تجربتك!",
    "لا تتردد بالبدء اليوم واستمتع بالفرق!",
    "اجعل عملك الإعلامي أذكى وأسهل مع هذه الأدوات!",
    "ابدأ باستخدام الذكاء الاصطناعي الآن واكتشف الإمكانيات!"
]

# وظيفة لإنشاء منشور كامل
def generate_post():
    topic = random.choice(topics)
    opener = random.choice(openers)
    closer = random.choice(closers)
    
    post = f"{opener}\n\nموضوع اليوم: {topic}\n\n{closer}"
    return post

# إنشاء منشور جديد وعرضه
new_post = generate_post()
print("🔵 منشور الذكاء الاصطناعي الجديد:\n")
print(new_post)

import tweepy

# إدخال المفاتيح التي حصلت عليها من تويتر
API_KEY = 'W3Qs0cHwtPnDj0qrMrYI19tAt'
API_SECRET_KEY = 'cqAAMplaaBP2caphM4qxo91PcsOcyoO0AOK7OcRb1DjKErcjIo'
ACCESS_TOKEN = '970986310155501568-m7esi4aMBt9araKz2ZZJhZHToy7IjMT'
ACCESS_TOKEN_SECRET = 'VkgZBm0iXczci4f1WA8mlswbTUbPWCogQcVmvwXcsxNjK'

# توثيق الدخول باستخدام مفاتيح تويتر
auth = tweepy.OAuth1UserHandler(consumer_key=API_KEY, consumer_secret=API_SECRET_KEY,
                                access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)

# إنشاء API باستخدام التوثيق
api = tweepy.API(auth)

# النص الذي تريد نشره
tweet_text = "hallo with python project"

# نشر التغريدة
api.update_status(status=tweet_text)

print("تم نشر التغريدة بنجاح!")

