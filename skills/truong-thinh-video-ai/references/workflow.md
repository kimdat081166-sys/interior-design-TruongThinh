# Sản xuất và dựng video

## Hai bước

| Bước | Thực hiện | Đầu ra |
|---|---|---|
| 1 | Xem ảnh hoàn thiện, tạo ảnh trung gian không người, khóa thợ, chia động tác, viết prompt Flow và intro @me | Ảnh mốc thật + bảng cảnh + prompt tiếng Anh độc lập |
| 2 | Nhận clip Flow, ghép intro/thi công/thành phẩm/outro, xử lý logo/voice/nhạc/phụ đề/CTA | MP4 đã kiểm tra + checkpoint |

Phân biệt trạng thái đã tạo ảnh, đã viết prompt, chờ clip và đã dựng. Hoàn thành phần được phép làm; không tự tiêu credit khi người dùng chỉ yêu cầu prompt.

## Flow và chi phí

Xác minh công cụ và cấu hình thực tế trước khi tạo: model, hỗ trợ ảnh đầu/cuối/character reference, audio, tỷ lệ, thời lượng 8/10 giây và số đầu ra. Chọn model đáp ứng tác vụ với chi phí thấp phù hợp; không cố định tên model hoặc giá credit. Chạy một cảnh trước, chỉ tạo lại phần lỗi.

Không đồng nhất Wispr Flow, Google Drive hay API Veo với thuê bao Google Flow. Nếu chỉ có prompt, giao prompt hoàn chỉnh và nhận clip; chỉ dùng browser khi có ý định thao tác Flow được phép. Không báo đã kết nối/render nếu chưa làm.

Khi cần cập nhật thông số, kiểm tra hướng dẫn chính thức:

- https://support.google.com/flow/answer/16526234?hl=en
- https://support.google.com/flow/answer/16353333?hl=en
- https://support.google.com/flow/answer/16353334?hl=en
- https://ffmpeg.org/ffmpeg-filters.html

## Ghép clip bằng script có sẵn

Đọc đầu `scripts/assemble_video.py` và xác minh FFmpeg/ffprobe tồn tại. Dùng đường dẫn shell được trích dẫn đúng; không nội suy prompt, token hoặc tên file vào mã shell. Script chạy qua subprocess với danh sách đối số, không gọi AI API.

Ví dụ plan, thay file nguồn bằng clip thật đã kiểm tra và bỏ subtitles nếu chưa có SRT căn đúng:

```json
{
  "width": 1080,
  "height": 1920,
  "clips": [
    {"path": "intro.mp4", "start": 0, "duration": 8},
    {"path": "installation-01.mp4", "start": 0, "duration": 10},
    {"path": "outro.mp4", "start": 0, "duration": 8}
  ],
  "subtitles": "timed.srt"
}
```

Chạy `python3 scripts/assemble_video.py plan.json merged.mp4`. File nguồn resolve theo thư mục plan. Output không được tồn tại. Đổi width/height theo tỷ lệ đã chốt; không mặc định crop clip ngang thành dọc.

Script hỗ trợ trim, ghép cắt thẳng, fit toàn khung có viền, 30 fps, H.264/AAC, giữ audio và burn-in SRT. Clip không audio được thêm silence để ghép ổn định. Script không overlay logo, mix nhạc, làm CTA, phiên âm hoặc lip-sync.

## Hoàn thiện ngoài script

Thực hiện bằng FFmpeg hoặc công cụ dựng sẵn có; đọc khả năng thực tế thay vì nhận đã làm:

1. Chèn logo file gốc bằng overlay; giữ tỷ lệ và khoảng an toàn, tránh che công trình/gương mặt. Khi logo sai nằm trong cảnh, chỉnh vùng lỗi hoặc chọn bản sạch phù hợp, không đặt thêm một logo rồi bỏ nguyên logo giả.
2. Thêm một nhạc nền xuyên suốt từ nguồn phù hợp; cắt/loop đến thời lượng thật, có fade đầu/cuối. Giảm nhạc dưới voice bằng automation hoặc sidechain khi phù hợp. Nếu audio gốc đã trộn nhạc/voice, nghe trước để tránh chồng nhạc và làm hỏng tiếng nói.
3. Thêm CTA/phụ đề có dấu bằng font hỗ trợ tiếng Việt và file text/SRT UTF-8; không nhúng chữ trực tiếp vào lệnh shell không an toàn. Căn phụ đề theo audio thật.
4. Nghe ở đoạn có voice và điểm nối; kiểm tra tiếng không mất, không clipping, không im lặng do ghép sai. Giữ câu nói trọn vẹn.
5. Xem khung đầu/giữa/cuối mỗi cảnh; kiểm tra nhân vật, trạng thái cuối, logo và hotline. Dùng ffprobe xác minh kích thước, thời lượng và có stream audio.

Không nhận bản dựng có nhạc/CTA/logo nếu thao tác đó chưa thực hiện. Nếu thiếu nguồn nhạc hoặc không nghe được, nêu đúng giới hạn và vẫn hoàn thành các phần độc lập.

## Bàn giao

Giao MP4 đã dựng và lưu theo quy tắc môi trường. Nếu chưa có clip Flow, giao ảnh mốc + prompt với trạng thái chờ clip. Viết caption theo nội dung thật; gọi đúng “mô phỏng quy trình” nếu cảnh là AI, không nhận là ghi hình thi công thực tế.
