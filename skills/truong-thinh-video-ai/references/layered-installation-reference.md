# Mẫu tua nhanh lắp đặt theo lớp

## Nguồn và giới hạn quan sát

Mẫu người dùng chọn là video tua nhanh lắp vách TV, dài khoảng 10 giây, 576×1024, 30 fps. Đã xem các khung đầu, giữa và cuối trong lần chuẩn hóa mẫu; chưa nghe/xác nhận nhạc hoặc voice. Không mô tả nội dung audio như dữ kiện. Bản skill chỉ lưu mô tả hành vi, không kèm video nguồn hoặc mã file cá nhân. Khi cần xem lại mẫu, tìm tư liệu người dùng đã chỉ định; không dựa vào đường scratch để tái sử dụng lâu dài.

Mẫu là vách TV: đầu clip đã có một tấm ốp đá, tiếp đến thêm các tấm ốp; thợ lắp nan/trang trí đứng và tủ trưng bày bên phải, kệ thấp, TV và đồ trang trí; cuối clip bật sáng và sạch người. Quan sát có 2–3 thợ, không nhận mẫu đã đạt yêu cầu khóa số người hoặc logo. Dùng nhịp và cấu trúc thị giác làm tham chiếu, không sao chép logo, watermark hay thiết kế của thương hiệu trong mẫu.

## Hành vi cần tái tạo

- Giữ một góc máy cho toàn cảnh thi công. Cho trạng thái công trình tiến triển ngay đầu clip; không để thợ đứng hoặc đi lại lâu.
- Suy ngược từ ảnh hoàn thiện của tác vụ mới, xác định các lớp nhìn thấy và thứ tự lắp có lý. Ví dụ vách TV: tấm ốp → nan/tủ → kệ → TV/đồ trang trí. Ví dụ bếp: hệ tủ dưới → mặt đá → thiết bị/kệ → trang trí. Không áp một trình tự cố định cho mọi phòng.
- Chọn 2–3 nhóm thao tác chính cho 10 giây. Gộp việc căn chỉnh/kiểm tra vào nhóm chính. Khi nhiều lớp khó thể hiện, chia thành các clip 8/10 giây nối bằng ảnh mốc; không hứa lắp mọi công đoạn chỉ trong một clip.
- Thể hiện người mang, giữ, đặt, căn chỉnh cấu kiện với tiếp xúc tay rõ. Cho người hoặc cấu kiện che khuất vùng lắp trong lúc thao tác; không dùng che khuất để chấp nhận vật tự mọc, sai hình học hay thiết kế biến đổi.
- Tua nhanh đều, cho phép motion blur nhẹ ở thợ và dụng cụ, giữ công trình ổn định. Không cắt nhanh che mất sự tiến triển.
- Thu dụng cụ và cho mọi người rời cảnh trước mốc cuối; giữ thành phẩm 1–2 giây, dùng ánh sáng hoàn thiện làm điểm nhấn khi phù hợp ảnh gốc.

## Ảnh trung gian và nhân vật

Chuẩn bị ảnh trạng thái riêng, không người, cùng góc máy và kiến trúc. Chọn số ảnh đủ để khóa các lớp quan trọng; không đặt thợ sẵn vào các ảnh đầu/cuối. Không đưa contact sheet vào Flow như một frame.

Lặp nguyên văn hồ sơ từng thợ trong các prompt, khóa số người, vai trò, khuôn mặt, tóc, vóc dáng, trang phục và hướng vào/ra. Nếu tác vụ yêu cầu thợ Việt Nam, ghi rõ Vietnamese adults; không suy đoán quốc tịch từ khuôn mặt trong mẫu. Chọn bảo hộ theo thao tác; không sao chép việc đi chân trần của mẫu.

Giữ `@me` cho nhân vật người dùng chỉ định trong intro. Không tự đổi người dùng thành nữ; nếu thêm nhân vật nữ, định nghĩa riêng và ghi rõ vai trò. Không ép người dẫn vào cảnh tua nhanh nếu gây che công trình hoặc tăng khó giữ nhân vật.

Đồng phục là chuẩn thương hiệu dùng qua nhiều video, không chỉ hồ sơ một cảnh. Giữ áo polo navy trơn, quần công tác tối màu, giày bảo hộ đen theo chuẩn hiện đã chọn. Không sao chép áo xanh royal blue hay chữ của đội trong video mẫu. Dán nguyên văn khối sau vào mỗi prompt thi công Trường Thịnh, bổ sung hồ sơ từng người riêng:

```text
SERIES-WIDE UNIFORM LOCK:
Every Truong Thinh installer wears the same plain navy-blue short-sleeve
polo shirt, dark charcoal work trousers and black safety shoes.
Keep this exact uniform color and style across all shots and all videos
in this series, including both male and female crew members.
No generated logos, letters, badges or decorative graphics on clothing.
Task-specific gloves or eye protection may change only as explicitly specified.
```

## Logo và audio

Dùng logo gốc của tác vụ, giữ biểu tượng/chữ/màu/tỷ lệ. Không yêu cầu Flow tự vẽ nhãn hiệu trong mẫu. Nếu sinh logo trên áo lỗi, chọn đồng phục trơn rồi chèn logo gốc ở vị trí cố định trong bước dựng; logo trên áo chuyển động cần tracking/biến dạng phù hợp, không hứa overlay tĩnh sẽ bám áo. Giữ lựa chọn đồng phục trơn khi người dùng đã chốt cho tác vụ hiện tại, trừ khi họ đổi yêu cầu.

Lập kế hoạch nhạc riêng vì chưa xác nhận audio mẫu: nhịp rõ dưới tua nhanh, điểm nhấn khi bật đèn/khoe thành phẩm, giảm nhạc khi intro/outro có thoại. Dùng nguồn nhạc được phép hoặc yêu cầu tạo nhạc theo mood; không nhận đã tái tạo nhạc mẫu. Cảnh thi công không cần voice nếu đã có intro/outro; thêm khi giúp kể chuyện mà không lấn tiếng thao tác.

## Ngôn ngữ prompt chuyển động

Điền cấu kiện, hồ sơ thợ và ảnh mốc đã xem vào prompt độc lập; đoạn sau chỉ là hướng dẫn viết, không giao nguyên văn như prompt cuối:

```text
One continuous locked-off construction timelapse. Show the installation
progressing through clearly readable physical stages, from the supplied
starting state to the exact finished reference. The specified installers
carry and position each component, keep visible hand-to-part contact, align
it and secure it before progressing to the next stage. Accelerated but
coherent movement; mild motion blur on the workers, stable room geometry.
Complete the final cleanup and have everyone leave before the last second.
Hold the finished installation without people. Match the final reference;
no additional shelves, structures, invented branding or floating parts.
```

## Duyệt trước khi ghép

Kiểm tra sự tiến triển ở ít nhất đầu/giữa/cuối và mỗi chuyển lớp. Loại/sửa cảnh có công trình đổi hình, số thợ thay đổi, logo sai hoặc công đoạn chính mất. Không cắt bỏ công đoạn để giấu lỗi rồi gọi là cùng dạng mẫu. Giữ đủ lắp đặt và đoạn khoe thành phẩm trước outro. Chỉ thêm chuyển động máy quay ở đoạn khoe riêng khi được chọn; không thay cảnh thi công bằng chuyển động trên ảnh tĩnh.
