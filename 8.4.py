print("NGUYỄN HUY NGUYÊN")
print("MSSV:235752021610019")

import tkinter as tk

# Hàm xử lý sự kiện khi phím được bấm
def on_key_press(event):
    print(f"Bạn đã bấm phím: {event.char}")

# Hàm thay đổi màu button khi nhấn
def change_button_color():
    button.config(bg="pink",fg="black")
    
# Tạo một cửa sổ chính
window = tk.Tk()
window.title("Ứng dụng Tkinter")


# Thêm một button vào cửa sổ
button = tk.Button(window, text="Nhấn vào đây", command=change_button_color)
button.pack(pady=20)  

# Đăng ký sự kiện bàn phím
window.bind("<KeyPress>", on_key_press)

# thiết lập màu nền cho cửa sổ
window.config(bg="lightyellow")

#chạy vòng lặp chính 
window.mainloop()
