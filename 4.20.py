print("NGUYỄN HUY NGUYÊN")
print("MSSV:235752021610019")

def in_tam_giac_pascal(n):
    # Mảng 2D để lưu trữ các giá trị của tam giác Pascal
    pascal = [[1]]
    
    # Tạo các dòng tiếp theo trong tam giác Pascal
    for i in range(1, n):
        # Khởi tạo dòng mới với giá trị 1 đầu tiên
        row = [1]
        # Tính các giá trị ở giữa dựa trên các giá trị của dòng trước
        for j in range(1, i):
            row.append(pascal[i-1][j-1] + pascal[i-1][j])
        # Thêm giá trị 1 cuối cùng cho mỗi dòng
        row.append(1)
        pascal.append(row)
    
    # In ra các dòng của tam giác Pascal
    for row in pascal:
        print(' '.join(map(str, row)))

# Nhập n
n = int(input("Nhập số dòng n của tam giác Pascal: "))
in_tam_giac_pascal(n)
