import json


DB_FILE = "products.json"


def load_data():
    try:
        with open(DB_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(">> Chưa có file dữ liệu. Tạo mới danh sách.")
        return []


def save_data(products):
    try:
        with open(DB_FILE, 'w', encoding='utf-8') as f:
           
            json.dump(products, f)
        print(">> Đã lưu dữ liệu thành công!")
    except Exception as e:
        print(f"Lỗi khi lưu file: {e}")


def display_all_products(products):
    if not products:
        print("\n>> Kho hàng trống.")
        return

    print("\n" + "-"*70)
    print(f"{'ID':<10} {'Tên Sản Phẩm':<25} {'Thương Hiệu':<15} {'Giá':<10} {'SL':<5}")
    print("-"*70)

    for p in products:
       
        print(f"{p['id']:<10} {p['name']:<25} {p['brand']:<15} {p['price']:<10} {p['quantity']:<5}")
    print("-"*70 + "\n")

def add_product(products):
    print("\n--- THÊM SẢN PHẨM MỚI ---")
    name = input("Nhập tên sản phẩm: ") 
    brand = input("Nhập thương hiệu: ")
    

    while True:
        try:
            price = int(input("Nhập giá sản phẩm: "))
            quantity = int(input("Nhập số lượng tồn kho: "))
            break
        except ValueError:
            print(">> Lỗi: Giá và Số lượng phải là số nguyên. Vui lòng nhập lại.")

   
    new_id = f"LT{len(products) + 1:02d}" 
    

    new_product = {
        "id": new_id,
        "name": name,
        "brand": brand,
        "price": price,
        "quantity": quantity
    }
    
    products.append(new_product)
    print(f">> Đã thêm sản phẩm thành công với ID: {new_id}")
    return products

def search_product_by_name(products):
    keyword = input("\nNhập từ khóa tên sản phẩm cần tìm: ").strip().lower()
    found_products = []
    
    for p in products:
        if keyword in p['name'].lower():
            found_products.append(p)
            
    if found_products:
        print(f"\n>> Tìm thấy {len(found_products)} sản phẩm:")
        display_all_products(found_products)
    else:
        print(f">> Không tìm thấy sản phẩm nào chứa từ khóa '{keyword}'")

def delete_product(products):
    id_to_delete = input("\nNhập ID sản phẩm cần xóa: ").strip()
    
    for i, p in enumerate(products):
        if p['id'] == id_to_delete:
            confirm = input(f"Bạn có chắc muốn xóa '{p['name']}'? (y/n): ")
            if confirm.lower() == 'y':
                del products[i]
                print(f">> Đã xóa sản phẩm có ID {id_to_delete}")
            return products
            
    print(f">> Lỗi: Không tìm thấy sản phẩm có ID {id_to_delete}")
    return products

def update_product(products):
    id_to_update = input("\nNhập ID sản phẩm cần cập nhật: ").strip()
    
    found = False
    for p in products:
        if p['id'] == id_to_update:
            found = True
            print(f"Đang cập nhật cho sản phẩm: {p['name']}")

            new_name = input(f"Tên mới (hiện tại: {p['name']}): ")
            new_brand = input(f"Thương hiệu mới (hiện tại: {p['brand']}): ")
            
            if new_name: p['name'] = new_name
            if new_brand: p['brand'] = new_brand
            
            try:
                new_price = input(f"Giá mới (hiện tại: {p['price']}): ")
                if new_price: p['price'] = int(new_price)
                
                new_qty = input(f"Số lượng mới (hiện tại: {p['quantity']}): ")
                if new_qty: p['quantity'] = int(new_qty)
            except Exception:
                print(">> Cảnh báo: Giá/Số lượng nhập sai định dạng, giữ nguyên giá trị cũ.")

            print(">> Cập nhật thành công!")
            break
            
    if not found:
        print(f">> Lỗi: Không tìm thấy sản phẩm có ID {id_to_update}")
    
    return products