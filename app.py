import streamlit as st
import requests
import os
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(
    page_title="AI Post Generator",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI & Tech SMM Post Generatoru")
st.caption("Süni intellekt şirkətləri üçün professional Instagram postları")

st.divider()

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📝 Məlumatları daxil et")
    company = st.text_input("Şirkət adı", placeholder="Məs: TechAz, AILab...")
    product = st.text_input("Məhsul/Xidmət", placeholder="Məs: AI chatbot, data analiz...")
    audience = st.selectbox("Hədəf auditoriya", [
        "Texnologiya həvəskarları",
        "Biznes sahibləri",
        "Gənc mütəxəssislər",
        "Startap qurucuları"
    ])
    topic = st.text_area("Post mövzusu", placeholder="Məs: Yeni məhsul təqdimatı, uğur hekayəsi...")
    generate = st.button("🚀 Post Generasiya Et", use_container_width=True)

with col2:
    st.subheader("✨ Generasiya edilmiş postlar")

    if generate:
        if not company or not topic:
            st.warning("Zəhmət olmasa şirkət adı və mövzunu daxil edin.")
        else:
            with st.spinner("AI postlar hazırlayır..."):
                prompt = f"""Sən peşəkar SMM mütəxəssisisən.
Aşağıdakı məlumatlar əsasında Instagram üçün 3 FƏRQLI post variantı hazırla.

Şirkət: {company}
Məhsul/Xidmət: {product}
Hədəf auditoriya: {audience}
Mövzu: {topic}

Hər variant üçün:
- Cəlbedici başlıq
- 3-4 cümlə mətn
- 5-7 uyğun hashtag
- Azərbaycan dilində yaz
- Emoji istifadə et

Format:
VARIANT 1:
[mətn]

VARIANT 2:
[mətn]

VARIANT 3:
[mətn]"""

                try:
                    response = requests.post(
                        "https://api.groq.com/openai/v1/chat/completions",
                        headers={
                            "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
                            "Content-Type": "application/json"
                        },
                        json={
                            "model": "llama-3.3-70b-versatile",
                            "messages": [
                                {
                                    "role": "system",
                                    "content": "Sən peşəkar Azərbaycan SMM mütəxəssisisən. Həmişə yalnız Azərbaycan dilinin latın əlifbasında yaz."
                                },
                                {
                                    "role": "user",
                                    "content": prompt
                                }
                            ]
                        }
                    )

                    result = response.json()
                    content = result["choices"][0]["message"]["content"]

                    variants = content.split("VARIANT")
                    variants = [v.strip() for v in variants if v.strip()]

                    for i, variant in enumerate(variants, 1):
                        with st.expander(f"📱 Variant {i}", expanded=True):
                            clean = variant.lstrip("123: ").strip()
                            st.write(clean)
                            st.divider()
                            st.text_area(
                                "📋 Kopyala:",
                                value=clean,
                                key=f"text_{i}",
                                height=150
                            )

                except Exception as e:
                    st.error(f"Xəta baş verdi: {str(e)}")
    else:
        st.info("Sol tərəfdəki formu doldurun və 'Post Generasiya Et' düyməsinə basın.")