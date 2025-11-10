import streamlit as st
import time
VALID_TOKENS = ["khóm", "khánh"]

# Nhập token
token = st.text_input("Nhập mật khẩu hoặc token để truy cập app:")

if token not in VALID_TOKENS:
    st.warning("⚠️ Không hợp lệ! Bạn không thể vào app.")
    st.stop()  # dừng app nếu token sai
else:
    st.success("✅ Chào mừng bạn!")
    st.write("Nội dung app ở đây...")

is_mobile = st.sidebar.checkbox("Mobile mode")  # if st.button("Gửi", key="send"):

## --- Header ---
st.markdown("### 🧠 Máy tính tuổi thông minh" if not is_mobile else "### máy tính tuổi")
if not is_mobile:
    st.markdown("cre:ditmewibu.com")
st.markdown("---")

## -------------------------------------------------------------------------------
# hàm loading
def loading(message="Đang xử lý...", steps=50, delay=0.05, done_message="✅ Hoàn tất!"):
    if is_mobile:
        st.info("⏳ Đang xử lý...")
        time.sleep(0.5)
    else:
        with st.spinner(message):
            progress = st.progress(0)
            for i in range(steps):
                time.sleep(delay)
                progress.progress(int((i + 1) / steps * 100))
    st.success(done_message)

## -----------------------------------------------------------
# check form-------------
if 'age_input' not in st.session_state:
    st.session_state.age_input = ""

# -------------------------------

age_input = st.text_input("🤨 Nhập tuổi của bạn:", key="age_input").strip()
age = ''.join(c for c in age_input if c.isdigit())
## ------------------------------------------------------------------
# Nút gửi --------------------------------------
if st.button("Gửi"):
    steps = 10 if is_mobile else 50  # số bước progress responsive
    if not age_input:
        st.warning("⚠️ lỗi cmnr, Bạn không nhập gì!")  # Trống hoàn toàn
    elif age_input.isspace() or "\t" in age_input:
        st.warning("⚠️ lỗi cmnr — không hợp lệ!")  # space/tab
    elif not age:  
        st.warning("⚠️ lỗi cmnr, đây là quái gì vậy? 🥀 - không hợp lệ")  # toàn chữ
    else:
        age_int = int(age)
        if age_int == 36:
            loading(steps=steps)
            st.success(f"✅ Tuổi của bạn là {age_int}, Bro, you’re absolutely like someone from Thanh Hoá!☘️☘️☘️")
        elif age_int <= 3**3636:
            loading(steps=steps)
            st.success(f"✅ Tuổi của bạn là: {age_int}")
        else:
            loading(" 😠 bạn bị gì đấy ?", steps=1, delay=1)
            st.error("😭 Đây là tuổi loz gì thế ?!!")
## ------------------------------------------------------------------
# Nút Nhập lại / Thoát-------------
if not is_mobile:
    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔄 Nhập lại"):
            # Nếu người dùng nhập sai (trống, space, tab)
            if not age_input or age_input.isspace() or "\t" in age_input:
                for key in list(st.session_state.keys()):
                    if key not in ["token", "is_mobile"]:  # giữ lại token & chế độ
                        del st.session_state[key]
            # Luôn làm mới giao diện
            st.experimental_rerun()

    with col2:
        if st.button("🚪 Thoát"):
            st.markdown("""
            <iframe width="400" height="300" 
            src="https://www.youtube.com/embed/WNDEUsLKpME?autoplay=1" 
            frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
            </iframe>
            """, unsafe_allow_html=True)
            time.sleep(2)
            st.write("👋 Tạm biệt!☘️")
            st.stop()

else:  # mobile
    if st.button("🔄 Nhập lại"):
        if not age_input or age_input.isspace() or "\t" in age_input:
            for key in list(st.session_state.keys()):
                if key not in ["token", "is_mobile"]:
                    del st.session_state[key]
        st.experimental_rerun()

    if st.button("🚪 Thoát"):
        st.markdown("""
        <iframe width="400" height="300" 
        src="https://www.youtube.com/embed/WNDEUsLKpME?autoplay=1" 
        frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
        </iframe>
        """, unsafe_allow_html=True)
        time.sleep(2)
        st.write("👋 Tạm biệt!☘️")
        st.stop()