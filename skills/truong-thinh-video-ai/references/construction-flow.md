# Ảnh trạng thái và prompt thi công

## Ảnh trung gian

Xem ảnh hoàn thiện, lập danh sách phần giữ nguyên và lớp có thể tháo bỏ. Dùng từng ảnh mốc riêng làm frame; không tạo montage/contact sheet làm ảnh đầu/cuối video. Gắn lại ảnh hoàn thiện làm chuẩn ở mỗi lần sửa để hạn chế lệch tích lũy. Không suy đoán dầm, khung chịu lực hay hệ kỹ thuật khuất.

Mẫu prompt sửa ảnh; thay STATE và CHANGES bằng quan sát từ ảnh thật:

```text
Edit the supplied completed-project image into this installation stage: [STATE].
Keep the exact camera position, perspective, framing, room proportions,
existing walls, floor, ceiling, openings and lighting.
Change only these visible installation elements: [CHANGES].
Preserve every element that belongs to this stage in its final aligned position.
No people, workers, faces, hands, human silhouettes, human shadows or human reflections.
No floating parts, suspended tools, invented openings, dimensions or structural changes.
Photorealistic materials; consistent exposure and white balance with the supplied final image.
Do not invent text or logos. Preserve only supplied, stage-appropriate branding.
```

Không dùng ảnh hoàn thiện nguyên bản có người làm end frame cho clip thi công; chuẩn bị bản sạch người mà giữ đúng thiết kế. Giữ nguyên bản nguồn riêng. Xem và sửa ảnh trạng thái trước khi nối động tác.

## Khóa thợ

Tạo hồ sơ riêng trước khi viết chuỗi prompt. Nếu chưa có chỉ định, chọn một nhóm nhỏ đủ cho công đoạn, ghi rõ đây là nhân vật mô phỏng; không nhận là thợ thật của doanh nghiệp. Có thể tạo ảnh tham chiếu thợ riêng khi được yêu cầu và công cụ hỗ trợ; không đưa thợ vào ảnh trung gian.

Khóa các trường: ID, tuổi tương đối, khuôn mặt/da/tóc, chiều cao tương đối/vóc dáng, áo/quần/giày/bảo hộ, dụng cụ, vai trò, hướng vào/ra cảnh. Nếu có ảnh tham chiếu, chỉ mô tả chi tiết nhìn thấy và ưu tiên đúng ảnh ấy.

Ví dụ hồ sơ hai thợ, chỉ dùng sau khi chọn cho tác vụ; không áp hai người vào mọi công trình:

Với video Trường Thịnh, giữ đúng đồng phục chung đã khóa trong SKILL.md cho cả hai thợ và qua nhiều video. Phân biệt thợ bằng khuôn mặt, vóc dáng và vai trò; không dùng màu áo khác để phân biệt.

```text
WORKER LOCK — use these same two simulated installers throughout this sequence.
Installer A: adult man, approximately 35, medium build, slightly taller than B,
square face, medium skin tone, short straight black hair, clean-shaven.
Plain navy-blue short-sleeve polo shirt, dark charcoal work trousers, black safety shoes,
grey protective gloves and clear safety glasses.
Installer B: adult man, approximately 28, slim build, narrow face, medium skin tone,
short straight black hair, clean-shaven.
Plain navy-blue short-sleeve polo shirt, dark charcoal work trousers, black safety shoes,
grey protective gloves and clear safety glasses.
Clothing has no generated writing or logos.
Use this exact uniform colour and style across all shots and all Truong Thinh videos.
Keep their individual faces, proportions, hair, clothing colours and roles unchanged.
Use the separate supplied worker references if supported; the room-state images contain no workers.
No extra workers, duplicate bodies, identity swaps or wardrobe changes.
```

Nếu công đoạn cần bảo hộ khác, xác định trước cảnh và nêu rõ chuyển đổi hợp lý; không để model tự đổi toàn bộ trang phục.

## Timeline 8 hoặc 10 giây

Các mốc sau là dự kiến để thiết kế, không phải khả năng Flow được bảo đảm:

| Clip | Vào cảnh | Thao tác | Ra cảnh | Giữ trạng thái cuối |
|---|---|---|---|---|
| 8 giây | 0–1 | 1–6 | 6–7 | 7–8 |
| 10 giây | 0–1 | 1–8 | 8–9 | 9–10 |

Tăng tốc thao tác như time-lapse nhưng giữ thứ tự, tiếp xúc tay/vật và hướng mang cấu kiện. Chia cảnh khi cần nhiều bước hơn ngân sách. Không cố lắp cả công trình trong 8 giây. Dùng 10 giây chỉ khi cấu hình thực tế hỗ trợ; chuyển về 8 giây bằng rút công đoạn, không chỉ đổi con số trong prompt.

## Prompt thi công đầy đủ

Mỗi prompt phải độc lập; dán nguyên văn WORKER LOCK vào vị trí tương ứng và điền mọi trường. Khung cho 10 giây:

```text
Create one 10-second accelerated installation shot at [CONFIRMED ASPECT RATIO].
Use the supplied [START IMAGE ID] as the exact starting state and
[END IMAGE ID] as the target ending state wherever this mode supports both frames.
Match the original architecture, camera position, perspective, lighting and materials.
Locked-off camera; no cut, no pan and no lens change during installation.

[PASTE THE COMPLETE LOCKED WORKER DESCRIPTIONS HERE.]

0–1s: the room starts empty of people. The installers enter from [VISIBLE ACCESS],
carrying [PARTS/TOOLS] at a plausible scale.
1–4s: A [ACTION 1], while B [SUPPORTING ACTION].
4–6s: [ACTION 2 WITH VISIBLE HAND-TO-PART CONTACT].
6–8s: [ACTION 3 / ALIGNMENT AND FINAL CHECK].
8–9s: both remove their tools and leave through the same access.
9–10s: hold the finished installation stage, matching the end reference, with no people.
Parts remain physically supported. Nothing floats, teleports or assembles by itself.
No hand/object penetration, added structures, changed materials or extra workers.

Branding: use only the supplied [LOGO FILE] if [CONFIRMED LOGO PLACEMENT] is included.
Preserve its exact symbol, lettering, colours and proportions.
Do not invent any other logo, watermark or writing.
[AUDIO PLAN: restrained handling/drill sounds; music treatment; exact Vietnamese voice if any.]
No generated subtitles or phone numbers; these will be added accurately in editing.
```

Nếu chế độ chỉ nhận một ảnh, nêu rõ cấu hình đó và mô tả đích theo ảnh đã xem; không hứa đã gắn end frame. Nếu không có lối vào trong khung, chọn mép ngoài khung hợp lý, không tạo thêm cửa.

## Tự kiểm tra prompt

- Ảnh đầu/cuối cùng kiến trúc và không có người?
- Hồ sơ thợ có đủ và lặp đúng nguyên văn ở tất cả cảnh?
- Vào → mang/đỡ → lắp → kiểm tra → ra có đủ thời gian?
- Mỗi động tác có tác động cụ thể, phù hợp cấu kiện trong ảnh?
- Trạng thái cuối sạch người, đúng ảnh mốc, có khoảng giữ?
- Logo dùng file gốc, không tự sinh; audio có kế hoạch rõ?
