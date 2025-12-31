import streamlit as st

# 1. إعداد الصفحة
st.set_page_config(page_title="مستشارك الذكي 2025", layout="centered")

# 2. تشغيل CSS الجمالي (مضمون العمل)
st.markdown("""
    <style>
    .stApp { background-color: #f0f2f6; }
    .car-card {
        background: white;
        padding: 15px;
        border-radius: 15px;
        border-right: 8px solid #1E3A5F;
        box-shadow: 0 4px 10px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }
    .car-header { color: #1E3A5F; font-size: 22px; font-weight: bold; }
    .price-tag { color: #2e7d32; font-size: 18px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚗 منصة اختيار السيارات الذكية")
st.write("استخدم التبويبات أدناه للتنقل بين فئات السيارات المختلفة")

# 3. قاعدة البيانات الموسعة
categories = {
    "سيدان": [
        {"name": "تويوتا كامري 2025", "price": "131,000 ريال", "img": "https://images.unsplash.com/photo-1621007947382-bb3c3994e3fb?w=400", "specs": ["2.5L هايبرد", "225 حصان", "26.2 كم/لتر"]},
        {"name": "هيونداي سوناتا 2025", "price": "118,000 ريال", "img": "https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=400", "specs": ["2.0L توربو", "190 حصان", "18.5 كم/لتر"]}
    ],
    "SUV وعائلية": [
        {"name": "نيسان باترول 2025", "price": "350,000 ريال", "img": "https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?w=400", "specs": ["3.5L توين توربو", "425 حصان", "دفع رباعي"]},
        {"name": "مازدا CX-90", "price": "165,000 ريال", "img": "https://images.unsplash.com/photo-1632243193041-5e0a47a02ba1?w=400", "specs": ["3.3L 6 سلندر", "340 حصان", "فخامة يابانية"]}
    ],
    "كهربائية المستقبل": [
        {"name": "تسلا موديل 3", "price": "190,000 ريال", "img": "https://images.unsplash.com/photo-1560958089-b8a1929cea89?w=400", "specs": ["كهرباء كاملة", "مدى 513 كم", "شاشة 15 بوصة"]},
        {"name": "لوسيد أير", "price": "320,000 ريال", "img": "https://images.unsplash.com/photo-1617788130012-05ba7feee178?w=400", "specs": ["مدى 800 كم", "أسرع شحن في العالم", "صناعة سعودية"]}
    ]
}

# 4. إضافة خاصية التبويب (Tabs)
tab1, tab2, tab3 = st.tabs(["🏙️ سيدان", "🏜️ SUV وعائلية", "⚡ كهربائية"])

def display_cars(category_name, tab_object):
    with tab_object:
        for car in categories[category_name]:
            st.markdown('<div class="car-card">', unsafe_allow_html=True)
            c1, c2 = st.columns([1, 2])
            with c1:
                st.image(car['img'], use_container_width=True)
            with c2:
                st.markdown(f"<div class='car-header'>{car['name']}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='price-tag'>{car['price']}</div>", unsafe_allow_html=True)
                with st.expander("🛠️ عرض المواصفات العميقة"):
                    for s in car['specs']:
                        st.write(f"• {s}")
            st.markdown('</div>', unsafe_allow_html=True)

# تشغيل التبويبات
display_cars("سيدان", tab1)
display_cars("SUV وعائلية", tab2)
display_cars("كهربائية المستقبل", tab3)

st.divider()
st.info("💡 نصيحة الأستاذ: التبويبات تسهل على المستخدم الوصول للمعلومة بسرعة.")
