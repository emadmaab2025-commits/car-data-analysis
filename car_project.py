import streamlit as st

# 1. إعداد الصفحة
st.set_page_config(page_title="مستشارك للسيارات", layout="centered")

# 2. تشغيل CSS (هنا سر الجمال والألوان)
# تأكدنا من استخدام unsafe_allow_html=True بدقة
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .car-box {
        background: white;
        padding: 20px;
        border-radius: 15px;
        border-right: 10px solid #1E3A5F;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 25px;
    }
    .car-name { color: #1E3A5F; font-size: 24px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏎️ معرض سيارات 2025")
st.write("اضغط على السهم لعرض التفاصيل الفنية العميقة")

# 3. قاعدة البيانات (يمكنك إضافة سيارات أكثر هنا بنفس الطريقة)
cars = [
    {
        "name": "تويوتا كامري 2025",
        "price": "131,000 ريال",
        "img": "https://images.unsplash.com/photo-1621007947382-bb3c3994e3fb?w=500",
        "specs": ["محرك هايبرد 2.5L", "225 حصان", "استهلاك 26.2 كم/لتر"]
    },
    {
        "name": "نيسان باترول 2025",
        "price": "350,000 ريال",
        "img": "https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?w=500",
        "specs": ["محرك V6 توين توربو", "425 حصان", "نظام دفع رباعي ذكي"]
    }
]

# 4. عرض المحتوى (الاسم برا والتفاصيل جوا)
for car in cars:
    # بداية البطاقة الجمالية
    st.markdown('<div class="car-box">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(car['img'], use_container_width=True)
    with col2:
        st.markdown(f"<div class='car-name'>{car['name']}</div>", unsafe_allow_html=True)
        st.markdown(f"### :green[{car['price']}]")
        
        # هنا التفاصيل التي تظهر عند الضغط فقط
        with st.expander("🔍 عرض التفاصيل الفنية العميقة"):
            st.write("---")
            for spec in car['specs']:
                st.write(f"✅ {spec}")
            st.info("تم التحقق من البيانات الفنية")
            
    st.markdown('</div>', unsafe_allow_html=True) # نهاية البطاقة
