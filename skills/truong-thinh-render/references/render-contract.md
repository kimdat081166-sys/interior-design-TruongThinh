# Hợp đồng render và kiểm định

## Mẫu prompt

Điền từ ảnh đã xem và brief, không giữ placeholder. Viết tiếng Anh nếu phù hợp công cụ.

TASK: Photorealistic architectural render of THIS raw 3D perspective, preserving its design.
INPUT ROLES: Image 1 = current raw source, sole authority for camera, geometry, layout, quantity and proportions. Image 2, if supplied = approved render, appearance/material/lighting reference only. Other supplied images = explicitly named material references only. Never transfer camera/layout from appearance references.
CURRENT CAMERA: [describe observed near/far objects, left/right placement and crop].
AUTHORITATIVE MATERIAL TABLE: [each object -> material -> color/finish -> preservation constraints]. This table overrides placeholder colors in the raw sketch and conflicting appearance references. Apply each material only to its named component, across every visible instance.
PRESERVE: [observed fixed features, shelf tiers, slat spacing/section/count, cabinets, signage]. Do not redesign, round off or rebuild objects. Keep existing text and logo shapes; no new content.
LIGHTING: [shared time, light softness, color tone]; plausible viewpoint-dependent reflections/shadows. Keep existing fixtures only.
PROHIBITIONS: Do not substitute materials, transfer camera, add/remove furnishings, people, merchandise, plants, vehicles or fixtures. [derive specific prohibitions from this project's table].

For a correction, explicitly label the current result and raw source according to the actual input order. State a narrow change, preserve all unrequested features and repeat the material table. Include the approved appearance reference only when actually supplied and useful.

## Bảng kiểm thủ công

| Tiêu chí | Kiểm tra |
|---|---|
| Camera | Góc xiên/chính diện, vật gần/xa, trái/phải, phần cắt có khớp nguồn? |
| Hình học | Số vật thể, tầng kệ, tiết diện/khoảng cách nan, cấu trúc xuồng/tủ có giữ? |
| Vật liệu | Đối chiếu TỪNG bộ phận trong bảng, không đánh giá cả ảnh chung chung. |
| Ánh sáng | Cùng thời điểm, nhiệt độ màu, độ mềm; không thêm đèn; bóng hợp lý theo góc. |
| Chữ/logo | Giữ đúng nội dung, màu và bố cục; chữ không rõ phải báo. |
| Xuất ảnh | Kích thước thật nếu biết, phiên bản và trạng thái kiểm định rõ. |

## Case Dừa Cửu Long: chỉ đọc làm ví dụ

- Thân xuồng: MDF vân gỗ; nâu tự nhiên là màu tạm đã duyệt riêng case này.
- Cánh buồm/tầng kệ: kính trong. Không lan vân gỗ từ thân lên buồm.
- Vách lam: sắt sơn đen mờ, giữ hình học của nguồn dù placeholder màu trắng.
- Tủ kính: khung nhôm, kính trong; bạc là màu tạm duyệt riêng case này; giữ chân/bệ.
- Ánh sáng ban ngày. Bảng hiệu nền vàng chữ xanh; giữ sàn/tường/trần theo nguồn.
- Lỗi từng gặp: góc xiên bị kéo thành chính diện; buồm kính thành gỗ; lam đen thành trắng; tủ nhôm thành gỗ; độ sáng/sắc gỗ lệch; xuồng bị làm tròn/đổi kết cấu.

Đây là các lỗi cần kiểm tra, không phải vật liệu mặc định cho mọi dự án. Kính thường có cạnh/phản xạ nhưng không được trở thành tấm đặc. Màu trắng của một cột/trụ khác không có nghĩa toàn bộ vật thể đó là lam sắt; xác định đúng bộ phận từ nguồn, hỏi nếu mơ hồ.
