---
name: truong-thinh-video-ai
description: Tạo video marketing Trường Thịnh từ ảnh hoàn thiện bằng ChatGPT và Google Flow. Dùng khi cần tạo ảnh trung gian xây dựng/lắp đặt không có người, viết prompt Flow tiếng Anh cho clip 8 hoặc 10 giây, giữ thợ nhất quán, làm intro với @me, gắn logo được cung cấp, chọn nhạc và voice phù hợp, rồi ghép clip với outro thành MP4; cũng hỗ trợ cắt video, phụ đề và CTA.
---

# Video AI Trường Thịnh

## Mục tiêu và nguồn lực

Thực hiện hai bước: (1) ảnh hoàn thiện → ảnh trung gian → prompt Flow và intro; (2) clip Flow → ghép với outro → video marketing. Định tuyến nội dung qua Project 8, prompt qua Project 4 khi đang làm vai trò điều phối; giao bản bàn giao đủ để project thực hiện, không chỉ trả lời tên project.

Giao tiếp ngắn bằng tiếng Việt. Viết prompt Flow bằng tiếng Anh, giữ lời thoại tiếng Việt nguyên văn. Ưu tiên Flow người dùng đã có, một phương án tốt, ít lần tạo lại và không thêm thuê bao. Dùng tỷ lệ đã chốt hoặc tỷ lệ tư liệu; chỉ mặc định 9:16 khi chưa có chỉ định. Phân biệt token ChatGPT với credit Flow; không báo tiết kiệm bằng số khi chưa đo.

Đọc [quy trình và công cụ](references/workflow.md) khi sản xuất/dựng video; [ảnh trung gian và thợ](references/construction-flow.md) khi tạo các trạng thái hoặc prompt thi công; [intro/outro](references/intro-outro-flow.md) khi có người dẫn. Dùng [brief/checkpoint](assets/video-brief.md) để lưu quyết định gọn.

Khi người dùng yêu cầu dạng video thi công mẫu, đọc [mẫu tua nhanh lắp đặt theo lớp](references/layered-installation-reference.md). Ưu tiên chuyển đổi công trình liên tục bằng thao tác thợ, camera cố định và đoạn cuối sạch người để khoe thành phẩm. Không thay dạng này bằng slideshow, zoom ảnh hoặc chỉ ghép clip ngắn đã bỏ công đoạn quan trọng. Giữ tỷ lệ tác vụ đã chốt; không đổi sang 9:16 chỉ vì video mẫu là dọc.

## 1. Nhận và khóa tư liệu

- Xem trực tiếp ảnh hoàn thiện trước khi phân tích hoặc viết prompt theo ảnh. Đọc phiên bản hiện hành của file được chỉ định. Không nhận đã xem/nghe clip nếu chưa kiểm tra được.
- Xác định ảnh hoàn thiện, logo gốc, ảnh nhân vật cho `@me`, tỷ lệ và outro muốn dùng. Tìm tư liệu đã xác nhận trước khi yêu cầu gửi lại; chỉ hỏi phần thiếu chặn thao tác tiếp theo và tiếp tục phần độc lập.
- Khóa kiến trúc, góc máy, tỷ lệ, vật liệu nhìn thấy, vị trí cấu kiện và các chi tiết phải giữ. Không bịa kích thước, mở thêm cửa, đổi thiết kế hay suy đoán kết cấu bị che như dữ kiện thật.
- Dùng logo người dùng cung cấp cho tác vụ. Chỉ dùng `assets/truong-thinh-logo.png` làm logo Trường Thịnh mặc định nếu không có bản thay thế; xem file trước khi dùng. Giữ thương hiệu khách khi làm cho khách.
- Hiểu `@me` là ký hiệu người dùng yêu cầu có trong prompt để chỉ định ảnh cá nhân, không phải lệnh/khả năng avatar được xác nhận của Flow. Ghi rõ phải gắn ảnh người dẫn tham chiếu; không coi ký hiệu là một ảnh đã tải lên.

## 2. Bước 1 — Tạo ảnh trung gian và gói prompt

### Ảnh trạng thái

Lấy ảnh hoàn thiện làm mốc cuối. Suy ngược các lớp lắp đặt nhìn thấy để chọn số trạng thái cần thiết: hiện trạng trống → phần nền/khung nếu phù hợp → lắp cấu kiện → hoàn thiện. Không bắt mọi công trình phải có đủ bốn ảnh.

Tạo ảnh trung gian thật khi có công cụ tạo/sửa ảnh; không thay bằng danh sách ý tưởng rồi nhận đã tạo. Dùng công cụ image generation theo hướng dẫn môi trường, gắn đúng ảnh tham chiếu và xem kết quả. Nếu đang chỉ điều phối hoặc công cụ chưa khả dụng, giao prompt ảnh và báo rõ trạng thái chờ ảnh.

**Không có người trong bất kỳ ảnh trung gian nào:** không thợ, bóng người, tay/chân hay hình phản chiếu người. Giữ góc máy, khung hình, kiến trúc và ánh sáng ổn định. Mỗi ảnh phải thể hiện một trạng thái công trình hợp lý, cấu kiện đã đặt đứng yên; không vật lơ lửng. Đối chiếu từng ảnh với ảnh hoàn thiện, sửa ảnh sai trước khi viết chuyển động. Giữ ảnh hồ sơ thợ riêng, không trộn vào ảnh trạng thái.

### Hồ sơ thợ và chuyển động

**Khóa đồng phục giữa nhiều video Trường Thịnh, không chỉ giữa các cảnh.** Dùng cùng chuẩn hiện đã chốt: áo polo xanh navy trơn, quần công tác tối màu, giày bảo hộ đen; giữ màu, kiểu áo và kiểu quần cho cả thợ nam/nữ trong mọi công trình. Không lấy màu áo trong video mẫu làm chuẩn mới. Lặp nguyên văn mô tả đồng phục trong từng prompt và ghi chuẩn vào checkpoint để video sau kế thừa. Thay găng/kính/bảo hộ theo công đoạn khi cần, không tự đổi đồng phục. Chỉ đổi chuẩn khi người dùng yêu cầu; ghi rõ thay đổi áp dụng cho một video hay toàn bộ chuỗi.

Giữ quy cách logo xuyên nhiều video: chỉ file logo Trường Thịnh gốc, cùng vị trí/tỷ lệ đã duyệt. Khi tác vụ đã chọn áo trơn vì Flow sinh logo sai, tiếp tục áo trơn trong prompt; chèn logo gốc ở bước dựng nếu phù hợp. Không tự quay lại sinh logo trên áo ở video sau hoặc nhận logo overlay cố định là logo đã bám áo. Đối với video cho thương hiệu khách, dùng chuẩn riêng được xác nhận, không áp đồng phục Trường Thịnh.

Chốt một hồ sơ thợ cho toàn video: số người, mã A/B, khuôn mặt, tuổi tương đối, vóc dáng, tóc, màu và kiểu áo/quần, giày, bảo hộ, dụng cụ đặc trưng và vai trò. Dùng ảnh thợ tham chiếu riêng nếu chế độ đang dùng hỗ trợ. Lặp nguyên văn hồ sơ đã khóa trong mỗi prompt; không chỉ ghi “workers” hoặc “same as before”. Giữ số lượng, diện mạo và đồ bảo hộ nhất quán theo công đoạn; không tự thay thợ, đổi áo hay thêm người. Không suy diễn quốc tịch/giọng theo ảnh.

Cho thợ đi vào từ vị trí ngoài khung đã chọn, mang dụng cụ/cấu kiện, thao tác có tiếp xúc, rồi rời khung trước ảnh mốc cuối không người. Giữ vai trò nối tiếp: người mang cấu kiện tiếp tục giữ/lắp cấu kiện ấy. Tránh người hiện đột ngột, vật tự bay/tự mọc, đổi vật liệu và tay xuyên đồ vật. Không hứa mô tả bảo đảm tuyệt đối nhân vật nhất quán; kiểm tra clip.

### Thời lượng, logo và âm thanh

- Chọn 8 giây cho một nhóm thao tác chính; chọn 10 giây cho hai đến ba nhóm ngắn có liên hệ khi tài khoản/chế độ hỗ trợ. Nếu không đủ thời gian để vào cảnh, thao tác và ra cảnh, tách clip thay vì nhồi động tác.
- Ghi các khoảng giây trong từng prompt, chừa khoảng cuối để xem thành phẩm và nối ảnh mốc. Các mốc là dự kiến đến khi kiểm tra clip/audio.
- Kiểm tra lựa chọn thực tế của Flow trước khi chạy. Không mặc định 10 giây luôn khả dụng; nếu thiếu, chuyển thành clip 8 giây với ít động tác hơn hoặc chia công đoạn, báo cấu hình thực tế. Không tự dùng extend trả phí.
- Yêu cầu dùng đúng logo file gốc; gắn làm tham chiếu khi cần logo trong cảnh. Không để Flow tự sáng tạo biểu tượng/chữ. Nếu logo bị lỗi, dùng clip đạt yêu cầu và chèn logo gốc ở bước dựng.
- Thiết kế nhạc hấp dẫn theo chủ đề: hook vào sớm, nhịp rõ ở cảnh lắp đặt, điểm nhấn khi hoàn thiện. Yêu cầu voice tự nhiên, rõ, phù hợp người dẫn và nhất quán; không mặc định vùng miền. Hạ nhạc khi có lời nói, giữ tiếng thao tác vừa đủ.
- Ưu tiên voice/tiếng thao tác ở clip Flow và một bản nhạc xuyên suốt khi dựng để tránh đổi nhạc mỗi cảnh. Khi yêu cầu nhạc trong Flow, mô tả mood/nhịp và để nhạc thấp dưới voice. Không ghi “no music” nếu người dùng yêu cầu nhạc trong clip.

Giao một bảng cảnh gọn có: mã cảnh, ảnh đầu/cuối, nhóm động tác, 8/10 giây và lý do, voice/âm thanh. Giao prompt độc lập cho mỗi cảnh gồm ảnh tham chiếu, hồ sơ thợ hoặc `@me`, timeline, camera, logo, lời thoại/âm thanh và ràng buộc. Điền hết chỗ trống; không bắt người dùng ghép/sửa nhiều đoạn prompt. Không dùng prompt mẫu chưa nhìn ảnh làm prompt cuối.

## 3. Intro và outro

Tạo intro với `@me`, ảnh tham chiếu thật, một câu hook gắn đúng công trình, cử chỉ tự nhiên và logo chuẩn. Mặc định 8 giây, kết thúc lời trước giây 7; nếu không vừa thì rút lời hoặc dùng 10 giây khi hỗ trợ. Giữ voice, diện mạo, trang phục và mood giữa intro/outro.

Dùng outro đã chọn nếu clip đạt yêu cầu. Chỉ tạo outro mới khi thiếu hoặc được yêu cầu. Dùng CTA Trường Thịnh và hotline đã xác nhận **0913 131 050** cho video của Trường Thịnh; không áp số này cho thương hiệu khách. Chèn hotline/phụ đề chính xác khi dựng. Không tự bịa ưu đãi, giá, chất liệu, bảo hành hoặc kết quả thi công.

## 4. Chạy Flow theo khả năng và ngân sách

Xác minh connector là Google Flow/Veo và hỗ trợ thao tác cần thiết. Không đồng nhất Wispr Flow, Google Drive hoặc API Veo với thuê bao Flow. Dùng browser khi người dùng yêu cầu thao tác Flow và môi trường cho phép; không tự dò phiên đăng nhập.

Nếu chưa có kết nối, vẫn hoàn thành ảnh, storyboard và prompt; nhận clip tải về để dựng. Không nhận đã render trên Flow khi mới giao prompt. Kiểm tra model, audio, thời lượng và credit thực tế trước thao tác tốn credit. Ưu tiên một đầu ra mỗi lần, thử một cảnh trước và chỉ tạo lại cảnh lỗi. Không mua gói/credit, gọi API trả phí hoặc thêm dịch vụ ngoài phạm vi. Không yêu cầu duyệt lại việc đã được cho phép.

## 5. Bước 2 — Dựng video marketing

Ghép **intro → thi công/lắp đặt → khoe thành phẩm → outro**. Cắt phần thừa, nối theo nhịp nhạc, giữ audio gốc và lời thoại. Tránh lặp dài các ảnh mốc giữa clip. Ưu tiên cắt thẳng rõ động tác; chỉ dùng chuyển cảnh khi có mục đích.

Nếu có FFmpeg/ffprobe, dùng `scripts/assemble_video.py` để trim/ghép/giữ audio/chèn SRT; đọc schema trước khi chạy. Script hiện chỉ ghép và phụ đề: thực hiện overlay logo, CTA và mix/duck nhạc bằng công cụ dựng hoặc FFmpeg riêng, rồi kiểm tra kết quả. Không nói script đã làm các tính năng chưa có.

Chèn file logo gốc, phụ đề có dấu, CTA đã chốt. Dùng nhạc từ nguồn phù hợp được phép dùng; không tự chọn bản nhạc không có nguồn. Nếu clip đã có nhạc lẫn voice, tránh chồng thêm nhạc; điều chỉnh mix thực tế. Không tự crop mất kiến trúc hoặc đổi tỷ lệ đã chốt.

Căn phụ đề theo audio thật; không nhận timestamp phỏng đoán là đã đồng bộ. Nếu không nghe được, báo giới hạn và không nhận đã kiểm tra voice.

## 6. Kiểm tra và giao

Kiểm tra hình tại các mốc đầu/giữa/cuối, độ nhất quán thợ, trình tự thao tác, kiến trúc, vật liệu và thành phẩm. Kiểm tra logo/chữ/hotline, tiếng Việt, voice, môi, nhạc không lấn lời, khoảng im lặng ngoài ý muốn, khung hình và thời lượng. Phân biệt video mô phỏng quy trình với tư liệu thi công thật khi viết caption.

Giao MP4 thật sau khi dựng, hoặc ảnh + prompt với trạng thái chờ clip; không trình bày kế hoạch là video hoàn chỉnh. Lưu deliverable theo quy tắc môi trường. Ghi checkpoint gọn theo mẫu, chỉ sửa phần ảnh hưởng khi có phản hồi.
