import streamlit as st
import time

# -------------------------------
st.markdown("## 🧠 Máy tính tuổi thông minh")
st.markdown("---")

# -------------------------------
def loading(message="Đang xử lý...", steps=50, delay=0.05, done_message="✅ Hoàn tất!"):
    with st.spinner(message):
        progress = st.progress(0)
        for i in range(steps):
            time.sleep(delay)
            progress.progress(int((i + 1) / steps * 100))
    st.success(done_message)

# -------------------------------
if 'age_input' not in st.session_state:
    st.session_state.age_input = ""

# -------------------------------
age = st.text_input("🤨 Nhập tuổi của bạn:", key="age_input").strip()

# -------------------------------
if st.button("Gửi", key="send"):
    if not age:
        st.warning("⚠️ Bạn không nhập gì!")
    elif age.isdigit():
        age = int(age)
        if age <= 1000000:
            loading()
            st.success(f"✅ Tuổi của bạn là: {age}")
        else:
            loading(" 😠 bạn bị gì đấy ?", 1, 1)
            st.error("😭 Đây là tuổi loz gì thế ?!!")
    else:
        loading("Đang kiểm tra...", done_message="⚠️ Lỗi cmnr!")
        st.warning("⚠️ Đây không phải tuổi của bạn, đúng không? ĐÚNG KHÔNG?")

# -------------------------------
# Nút Nhập lại / Thoát
col1, col2 = st.columns(2)

with col1:
    if st.button("🔄 Nhập lại", key="retry"):
        st.session_state.clear()
        st.rerun()

with col2:
    if st.button("🚪 Thoát", key="exit"):
        st.balloons()
        st.write("👋🍀x36 Tạm biệt!")
        st.stop()