# UPDATE H1

from product_manager import *

def main():
    products = load_data()

    while True:
        print("\n" + "*"*34)
        print(" HỆ THỐNG QUẢN LÝ LAPTOP POLY-LAP")
        print("*"*34)
        print("1. Hiển thị danh sách sản phẩm")
        print("2. Thêm sản phẩm mới")
        print("3. Tìm kiếm sản phẩm theo tên")
        print("4. Cập nhật thông tin sản phẩm")
        print("5. Xóa sản phẩm theo ID")
        print("6. Lưu dữ liệu & Thoát")
        print("*"*34)

        choice = input("Mời bạn chọn chức năng (1-6): ")

        if choice == "1":
            display_all_products(products)

        elif choice == "2":
            products = add_product(products)

        elif choice == "3":
            search_product_by_name(products)

        elif choice == "4":
            products = update_product(products)

        elif choice == "5":
            products = delete_product(products)

        elif choice == "6":
            save_data(products)
            print("Đã thoát chương trình. Cảm ơn bạn đã sử dụng ❤️ ")
            break

        else:
            print("Lựa chọn không hợp lệ!. Hãy thử lại")

if __name__ == "__main__":
    main()