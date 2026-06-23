class DeliveryOrder:
    def __init__(self, order_id, receiver_name, base_fee, distance, surcharge):
        self.order_id = order_id
        self.receiver_name = receiver_name
        self.base_fee = base_fee
        self.distance = distance
        self.surcharge = surcharge
        self.total_delivery_cost = 0
        self.delivery_status = ""

    def calculate_total_cost(self):
        self.total_delivery_cost = (self.base_fee * self.distance) + self.surcharge

    def classify_delivery_status(self):
        if self.total_delivery_cost < 100000:
            self.delivery_status = "Đơn hàng Tiêu chuẩn (Nội thành)"
        elif self.total_delivery_cost < 300000:
            self.delivery_status = "Đơn hàng Cận tỉnh"
        elif self.total_delivery_cost < 600000:
            self.delivery_status = "Đơn hàng Đường dài (Cần giám sát)"
        else:
            self.delivery_status = "Đơn hàng Đặc biệt (Ưu tiên cao - Rủi ro cao)"

class OrderManager:
    def __init__(self):
        self.orders: list[DeliveryOrder] = []

    def show_all_orders(self):
        if not self.orders:
            print("Hệ thống chưa có vận đơn nào")
            return
        print(f"{"Mã Đơn":<8} | {"Tên người nhận":<15} | {"Cước nền":<15} | "
              f"{"Khoảng cách (km)":<18} | {"Phụ phí":<10} | {"Tổng chi phí":<15} | {"Trạng thái đơn":<15}")
        for order in self.orders:
            print(f"{order.order_id:<8} | {order.receiver_name:<15} | {order.base_fee:<15} | "
              f"{order.distance:<18} | {order.surcharge:<10} | {order.total_delivery_cost:<15} | {order.delivery_status:<15}")

    def add_order(self):
        while True:
            order_id = input("Nhập mã đơn: ")
            if not order_id:
                print("Không được để trống!")
                continue
            for order in self.orders:
                if order_id == order.order_id:
                    print("Không được trùng!")
                    break
            else: break

        while True:
            receiver_name = input("Nhập tên người nhận: ")
            if not receiver_name:
                print("Không được để trống!")
                continue
            break

        while True:
            try:
                base_fee = float(input("Nhập cước nền: "))
                if not base_fee :
                    print("Không được để trống!")
                    continue
                if base_fee <= 0:
                    print("Dữ liệu không hợp lệ")
                break
            except ValueError:
                print("Dữ liệu không hợp lệ")

        while True:
            try:
                distance = int(input("Nhập khoảng cách (km): "))
                if not distance:
                    print("Không được để trống!")
                    continue
                if distance < 1 or distance > 5000:
                    print("Dữ liệu không hợp lệ")
                break
            except ValueError:
                print("Dữ liệu không hợp lệ")

        while True:
            try:
                surcharge = float(input("Nhập phụ phí: "))
                if not surcharge:
                    print("Không được để trống!")
                    continue
                if surcharge <= 0:
                    print("Dữ liệu không hợp lệ")
                break
            except ValueError:
                print("Dữ liệu không hợp lệ")

        order = DeliveryOrder(order_id, receiver_name, base_fee, distance, surcharge)
        order.calculate_total_cost()
        order.classify_delivery_status()
        self.orders.append(order)

    def update_order(self):
        if not self.orders:
            print("Hệ thống chưa có vận đơn nào")
            return
        order_id = input("Nhập mã cần sửa: ")
        for order in self.orders:
            if order_id == order.order_id:
                while True:
                    try:
                        base_fee = float(input("Nhập cước nền: "))
                        if not base_fee :
                            print("Không được để trống!")
                            continue
                        if base_fee <= 0:
                            print("Dữ liệu không hợp lệ")
                        break
                    except ValueError:
                        print("Dữ liệu không hợp lệ")
                        continue

                while True:
                    try:
                        distance = int(input("Nhập khoảng cách (km): "))
                        if not distance:
                            print("Không được để trống!")
                            continue
                        if distance <= 0:
                            print("Dữ liệu không hợp lệ")
                        break
                    except ValueError:
                        print("Dữ liệu không hợp lệ")
                        continue

                while True:
                    try:
                        surcharge = float(input("Nhập phụ phí: "))
                        if not surcharge:
                            print("Không được để trống!")
                            continue
                        if surcharge < 1 or surcharge > 5000:
                            print("Dữ liệu không hợp lệ")
                        break
                    except ValueError:
                        print("Dữ liệu không hợp lệ")
                        continue
                
                order = DeliveryOrder()
                order.base_fee = base_fee
                order.distance = distance
                order.surcharge = surcharge
                order.calculate_total_cost()
                order.classify_delivery_status()
            break
        else:
            print("Không tìm thấy vận đơn phù hợp")
        
    def delete_order(self):
        if not self.orders:
            print("Hệ thống chưa có vận đơn nào")
            return
        order_id = input("Nhập mã muốn xóa: ")
        for order in self.orders:
            if order_id == order.order_id:
                del order
            break
        else:
            print("Không tìm thấy vận đơn phù hợp")
        
    def search_by_receiver(self):
        if not self.orders:
            print("Hệ thống chưa có vận đơn nào")
            return
        receiver_name = input("Nhập tên người nhận cần tìm: ")
        print(f"{"Mã Đơn":<10} | {"Tên người nhận":<20} | {"Cước nền":<20} | "
              f"{"Khoảng cách (km)":<20} | {"Phụ phí":<20} | {"Tổng chi phí":<20} | {"Trạng thái đơn":<20}")
        for order in self.orders:
            if receiver_name.lower() == order.receiver_name.lower():
                print(f"{order.order_id:<10} | {order.receiver_name:<20} | {order.base_fee:<20} | "
                    f"{order.distance:<20} | {order.surcharge:<20} | {order.total_delivery_cost:<20} | {order.delivery_status:<20}")
            break
        else:
            print("Không tìm thấy vận đơn phù hợp")

def main():
    manager = OrderManager()
    manager.orders = [
        DeliveryOrder("OR001", "Anh Duy", 50000, 2, 0),
        DeliveryOrder("OR002", "Anh Duy", 50000, 5, 5000),
    ]
    for order in manager.orders:
        order.calculate_total_cost()
        order.classify_delivery_status()
    while True:
        print("""
================ MENU ================
1. Hiển thị danh sách vận đơn trong hệ thống
2. Nhập vận đơn mới
3. Cập nhật thông tin vận đơn
4. Xóa vận đơn khỏi hệ thống
5. Tìm kiếm vận đơn theo tên người nhận
6. Thoát
=====================================""")
        choice = input("Nhập lựa chọn của bạn: ")
        match choice:
            case "1":
                manager.show_all_orders()

            case "2":
                manager.add_order()

            case "3":
                manager.update_order()

            case "4":
                manager.delete_order()

            case "5":
                manager.search_by_receiver()

            case "6":
                print("Cảm ơn bạn đã sử dụng hệ thống quản lý vận đơn!")
                break

            case _:
                print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()