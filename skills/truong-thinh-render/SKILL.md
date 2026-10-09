---
name: truong-thinh-render
description: Render ảnh phối cảnh 3D thô từ SketchUp hoặc phần mềm tương tự thành ảnh chân thật cho Trường Thịnh; giữ thiết kế, đồng bộ vật liệu và ánh sáng giữa nhiều góc của một dự án, kiểm định nghiêm và sửa lỗi có giới hạn. Dùng khi người dùng gọi Render đồng bộ Trường Thịnh, yêu cầu render nhiều góc thống nhất hoặc chuyển bản vẽ thô thành ảnh thực tế. Không dùng cho video, tái dựng mặt bằng 2D hay thiết kế lại.
---

# Render đồng bộ Trường Thịnh

Thực hiện trực tiếp trong ChatGPT bằng công cụ tạo/chỉnh ảnh được cung cấp. Đọc skill imagegen hiện có trước lượt tạo đầu tiên. Không phụ thuộc Google Flow, không tự mở Flow. Không hứa khóa hình học hoặc vật liệu tuyệt đối; đây là ảnh mô phỏng cần đối soát.

## 1. Chuẩn hóa đầu vào

- Tiếp nhận JPG/PNG/WEBP phối cảnh thô của cùng một công trình. Không nhận .skp như ảnh, không suy ra kích thước kỹ thuật từ phối cảnh.
- Xem từng ảnh, gắn mã G01, G02… theo thứ tự nguồn. Ghi hướng nhìn, vị trí vật thể và đặc điểm nhận dạng; chọn góc rõ nhất làm ứng viên chuẩn. Không tự chuyển góc máy.
- Tìm file được nêu trong ngữ cảnh/nguồn lưu trữ được phép trước khi yêu cầu gửi lại. Đường dẫn thiếu không có nghĩa là đã xem ảnh. Chỉ hỏi gửi lại nếu không tìm thấy ảnh thực tế.
- Lập bảng chung: bộ phận/bề mặt | vật liệu | màu/hoàn thiện | chi tiết phải giữ. Thêm kịch bản ánh sáng, nội dung bảng hiệu và yêu cầu bảo toàn. Dùng thông tin người dùng đã chốt, không hỏi lại.
- Nếu thiếu vật liệu của bộ phận quan trọng, hỏi gọn trước khi tạo. Với màu chưa chốt, đề xuất giả định ghi rõ và chỉ áp dụng khi đã được người dùng chấp thuận. Không tự chọn vật liệu sang trọng.
- Nếu là bản vẽ 2D, giải thích phạm vi và yêu cầu phối cảnh xuất từ mô hình hoặc chuyển sang quy trình khác; không dựng 3D tùy tiện.

## Chọn ánh sáng trước khi render

Khi bắt đầu dự án hoặc khi người dùng yêu cầu đổi ánh sáng, đưa danh sách đánh số sau để người dùng chọn; không tự tạo ảnh trước khi có lựa chọn hoặc chỉ định đủ rõ. Cho trả lời bằng số hoặc mô tả riêng:

1. **Ban ngày dịu** — ánh sáng tự nhiên khuếch tán, đều, bóng mềm; dễ đối chiếu vật liệu.
2. **Ban ngày sáng trong, nắng nhẹ** — trong trẻo, một ít hoa nắng; tránh bóng gắt và cháy sáng.
3. **Chiều ấm / hoàng hôn** — ánh sáng vàng dịu, cảm giác ấm; giữ màu vật liệu có thể nhận biết.
4. **Nội thất trung tính** — dùng hệ đèn hiện hữu, sắc sáng trung tính khoảng 4000K; không thêm thiết bị.
5. **Nội thất ấm** — dùng hệ đèn hiện hữu, sắc sáng ấm khoảng 3000K; không thêm thiết bị.
6. **Ban đêm** — bối cảnh tối, dùng đèn hiện hữu và ánh sáng môi trường hợp lý; không tự chế đèn.
7. **Theo ảnh tham khảo** — yêu cầu ảnh tham khảo thực tế rồi phân tích thời điểm, độ mềm, màu và hướng nguồn sáng.
8. **Tùy chỉnh** — nhận mô tả riêng của người dùng.

Các nhiệt độ màu là định hướng mô phỏng, không phải số đo hay cam kết vật lý. Nếu người dùng đã chỉ định/duyệt ánh sáng đủ rõ trong phiên đang làm, giữ lựa chọn và không hỏi lại chỉ vì gọi skill. Không áp ánh sáng của dự án cũ cho dự án mới. Nếu yêu cầu "cho list tôi chọn", luôn hiển thị danh sách và chờ chọn, chưa render.

Nếu chọn chế độ đèn nhưng ảnh nguồn không cho thấy hệ đèn hoặc người dùng muốn thêm đèn, hỏi một câu gọn về vị trí/loại đèn trước khi tạo; không phát sinh đèn mới chỉ vì chọn preset. Với nắng nhẹ/hoàng hôn, không thêm cửa hay ô mở để có nắng. Nếu không đủ cơ sở xác định hướng sáng, hỏi hoặc dùng ánh sáng môi trường mềm, ghi rõ giả định.

Ghi lựa chọn thành một cấu hình chung: mã/tên kịch bản, thời điểm, độ mềm, sắc sáng, hướng sáng theo không gian nếu xác định được, thiết bị hiện hữu và điều cấm. Dùng cùng cấu hình cho mọi góc; trái/phải trên ảnh có thể đổi theo camera, không ép hướng sáng màn hình giống nhau. Kiểm tra không cháy sáng, không ám màu quá mức, không mất chi tiết kính/kim loại và không đổi màu vật liệu ngoài tác động ánh sáng.

Đổi lựa chọn thì giữ ảnh đã duyệt thành phiên bản trước, cập nhật brief và kiểm tra lại các góc; không ghi đè bộ ảnh cũ. Chỉ cập nhật skill không phải yêu cầu đổi ánh sáng của bộ ảnh đã duyệt.

## 2. Khóa brief dùng chung

Ghi một phiên bản brief với bảng vật liệu và ánh sáng. Tách vật liệu người dùng chỉ định khỏi màu placeholder trong SketchUp. Ưu tiên:
1. Chỉ định vật liệu/màu mới nhất của người dùng.
2. Hình học, góc máy, số lượng và bố cục trong ảnh nguồn của chính góc đang làm.
3. Ảnh chuẩn đã duyệt: chỉ tham khảo diện mạo vật liệu và ánh sáng.
4. Moodboard: chỉ bộ phận được người dùng cho phép.

Khi các nguồn xung đột, tuân theo đúng vai trò. Ví dụ: nan trắng trong ảnh thô vẫn phải thành sắt đen nếu brief yêu cầu; không thay tiết diện/số lượng nan. Không sao chép góc máy ảnh chuẩn sang góc xiên.

Đọc [references/render-contract.md](references/render-contract.md) để soạn prompt và kiểm định. Không áp vật liệu Dừa Cửu Long vào công trình khác; đó chỉ là ví dụ lỗi đã gặp.

## 3. Render và duyệt góc chuẩn

- Tạo một ứng viên chuẩn từ ảnh nguồn, bảng vật liệu và ánh sáng chung. Nêu vai trò từng ảnh theo đúng thứ tự truyền vào công cụ. Dùng đường dẫn tham chiếu đã xem hoặc số ảnh hội thoại nhỏ nhất bao gồm đủ nguồn; không khai báo ảnh chưa được đưa vào công cụ.
- Giữ hình dáng, tỷ lệ, camera, số lượng tầng kệ, vách/cửa và chữ. Không thêm người, hàng hóa, cây, logo hoặc đèn nếu chưa yêu cầu.
- Xem kết quả trực tiếp; đối chiếu từng hàng vật liệu và hình học với ảnh thô. Không kết luận đạt chỉ dựa vào prompt hoặc thông báo thành công của công cụ.
- Nếu có lỗi quan trọng, ghi rõ lỗi rồi sửa đúng vùng/bộ phận bằng công cụ chỉnh ảnh; nhắc toàn bộ ràng buộc chung để tránh sửa kính thành gỗ hoặc làm đổi ánh sáng.
- Tối đa hai lượt tự sửa mỗi góc trong một vòng. Sau hai lượt vẫn sai: dừng góc đó, báo CHƯA ĐẠT, đề xuất ảnh xuất rõ hơn/chú thích bộ phận hoặc render từ phần mềm 3D. Không lặp vô hạn hoặc giấu sai lệch.
- Chỉ dùng làm chuẩn sau khi kiểm định nội bộ đạt và người dùng duyệt chính ứng viên đó. Duyệt trước đây vẫn hợp lệ nếu ảnh/brief không đổi. Trong khi chờ duyệt, chuẩn bị prompt góc còn lại; không tự lấy ảnh có lỗi làm chuẩn.

## 4. Render các góc còn lại

- Tạo tuần tự, mỗi góc dùng ảnh thô riêng làm nguồn hình học; thêm ứng viên chuẩn đã duyệt chỉ cho vật liệu/ánh sáng.
- Soạn mô tả camera cụ thể từ ảnh nguồn (xuồng gần/xa, vị trí vách/cầu thang/tủ, phần bị cắt) để giảm lỗi kéo về camera chính diện.
- Chỉ định cùng vật liệu, sắc gỗ, màu kim loại và kịch bản ánh sáng. Cho phép phản xạ/bóng đổ đổi theo góc nhìn thực tế, không ép ảnh có bóng giống hệt nhau.
- Nếu góc mới lộ bộ phận chưa có vật liệu, hỏi bổ sung rồi cập nhật brief; kiểm tra lại các góc bị ảnh hưởng.
- Đổi brief hoặc sửa ảnh chuẩn thì đánh dấu kết quả liên quan CẦN KIỂM TRA LẠI; không coi phê duyệt cũ là nghiệm thu mới. Giữ phiên bản trước, không tự ghi đè.

## 5. Sếp khó tính kiểm định và giao ảnh

Chấm riêng từng góc: camera/bố cục; hình khối/số lượng; từng vật liệu; ánh sáng; chữ/logo. Dùng trạng thái ĐẠT / CHƯA ĐẠT / KHÔNG ĐỦ CƠ SỞ. Không đánh dấu ĐẠT cho phần khuất hoặc chưa nhìn rõ.

Lỗi chặn nghiệm thu: sai bộ phận/vật liệu/màu, đổi góc nhìn, thêm/bớt vật thể, đổi kết cấu hoặc sai chữ quan trọng. Sai ánh sáng rõ giữa các góc cũng chặn nghiệm thu đồng nhất. Nêu sai lệch còn lại kể cả ảnh nhìn đẹp.

Giao ảnh và bảng đánh giá ngắn; phân biệt kiểm định nội bộ với người dùng duyệt. Ảnh do công cụ imagegen trả về được hiển thị/lưu theo cơ chế của công cụ, không tạo bản sao chỉ để giao. Nếu tạo báo cáo/checkpoint khác, lưu bằng cơ chế file bền vững hiện có. Không dùng đường dẫn scratch làm nguồn dài hạn.

Chỉ nói 4K khi biết kích thước thật đạt mục tiêu. Không gọi nội suy kích thước là tăng chi tiết AI. Nếu không đọc được pixel, ghi chưa xác định. Không hứa ảnh AI dùng làm bản vẽ sản xuất chính xác.

Khi tiếp tục phiên khác, đọc brief/ảnh chuẩn hiện tại từ nguồn đã lưu; không đoán từ trí nhớ. Chỉ tạo render khi người dùng yêu cầu thực hiện render; việc tạo hoặc kiểm tra skill không tự cho phép chạy lượt tạo ảnh.
