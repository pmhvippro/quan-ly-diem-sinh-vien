# PROJECT THỰC HÀNH PYTHON

#1.Tạo dataframe
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
dulieu = {"Họ và Tên" : ["Phan Minh Hiếu","Đoàn Trần Quỳnh Anh","Phạm Minh Hoàng","Võ Thành An","Nguyễn Thành Đạt", "Nguyễn Tiến Hùng", "Nguyễn Minh Tiến", "Nguyễn Hoàng Long Vỹ", "Nguyễn Quốc Thắng", "Doãn Đức Anh"],
            "Chuyen_can": [9, 10, 7, 10, 6.4, 9, 6, 7, 9, 4],

            "Giua_ky": [8.5, 10, 6, 9, 5, 8, 3.3, 6, 9, 8],

            "Cuoi_ky": [9, 10, 7, 3.6, 4, 9, 2, 5, 9, 9]
}
df = pd.DataFrame(dulieu)


#2.Tính điểm tổng kết
df["Tong_ket"] = df["Chuyen_can"]*0.2+ df["Giua_ky"]*0.3+ df['Cuoi_ky']*0.5

#3.Xếp loại sinh viên
def xeploai (diem):
  if diem >= 8.5:
    return "Giỏi"
  elif diem >=7:
    return "Khá"
  elif diem >= 5:
    return "Trung bình"
  else :
    return "Yếu"
df["Xep_loai"]= df["Tong_ket"].apply(xeploai)
#4. Tiêu đề web 
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

st.write("Bảng điểm của 10 sinh viên")

st.dataframe(df[["Họ và Tên","Chuyen_can","Giua_ky","Cuoi_ky","Tong_ket","Xep_loai"]],use_container_width=True)


#5. Thống kê
diemtrungbinh = df["Tong_ket"].mean()
st.write("Điểm tổng kết trung bình của lớp:" , round(diemtrungbinh, 2))
sinhviencaonhat = df.loc[df["Tong_ket"].idxmax()]
st.write("Sinh viên có điểm tổng kết cao nhất:",sinhviencaonhat["Họ và Tên"])
sinhvienthapnhat= df.loc[df["Tong_ket"].idxmin()]
st.write("Sinh viên có điểm thấp nhất:",sinhvienthapnhat["Họ và Tên"])
sosinhviendat = (df['Tong_ket']>=5).sum()
st.write("Số sinh viên đạt",sosinhviendat )

#6.Tạo biểu đồ
plt.figure(figsize=(10, 5))

plt.barh(df["Họ và Tên" ], df["Tong_ket"])

plt.title("Điểm tổng kết của 10 sinh viên")
plt.xlabel("Điểm tổng kết")
plt.ylabel("Tên sinh viên")

plt.xlim(0, 10)
plt.yticks(rotation=45)

st.pyplot(plt.gcf())

#7.Selectbox
st.subheader("TRA CỨU ĐIỂM SINH VIÊN")

danh_sach_ten = df["Họ và Tên"].tolist()

ten_duoc_chon = st.selectbox(
    "Chọn sinh viên:",
    danh_sach_ten
)

sinh_vien = df[df["Họ và Tên"] == ten_duoc_chon].iloc[0]


st.write(f"### Thông tin của {ten_duoc_chon}")

col1, col2 = st.columns(2)

with col1:
    st.write(f"Chuyên cần: {sinh_vien['Chuyen_can']}")
    st.write(f"Giữa kỳ: {sinh_vien['Giua_ky']}")
    st.write(f"Cuối kỳ: {sinh_vien['Cuoi_ky']}")

with col2:
    st.write(f"Tổng kết: {sinh_vien['Tong_ket']:.2f}")
    st.write(f"Xếp loại: {sinh_vien['Xep_loai']}")

#8.Thông tin người tạo
st.markdown("---")
st.caption("Người tạo: Phan Minh Hiếu | MSSV: 036208000038 ")

