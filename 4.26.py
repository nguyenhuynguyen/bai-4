print("NGUYỄN HUY NGUYÊN")
print("MSSV:235752021610019")

# Hàm tính số tiền thực từ nhật ký giao dịch
def tinh_so_tien_tai_khoan():
    # Biến để lưu số dư tài khoản, ban đầu là 0
    so_du = 0

    # Nhập số lượng giao dịch
    n = int(input("Nhập số lượng giao dịch: "))

    # Xử lý từng giao dịch
    for _ in range(n):
        giao_dich = input("Nhập giao dịch (D/W số_tiền): ").split()
        loai_giao_dich = giao_dich[0]
        so_tien = int(giao_dich[1])

        if loai_giao_dich == 'D':
            # Nếu là giao dịch gửi tiền, cộng vào số dư
            so_du += so_tien
        elif loai_giao_dich == 'W':
            # Nếu là giao dịch rút tiền, trừ đi số tiền
            so_du -= so_tien
    
    # In ra số dư tài khoản cuối cùng
    print(f"Số tiền thực của tài khoản là: {so_du}")

# Chạy chương trình
tinh_so_tien_tai_khoan()
