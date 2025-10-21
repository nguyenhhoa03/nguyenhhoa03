# Khắc phục lỗi pop-up khi vuốt 4 ngón trên GNOME 46

Trong GNOME 46, một số người dùng gặp phải pop-up lạ khi **vuốt 4 ngón tay sang trái hoặc phải**. Nguyên nhân chủ yếu là do **XWayland**.

![Pop-up lỗi khi vuốt 4 ngón](https://preview.redd.it/remote-desktop-pop-up-on-four-finger-swipe-left-or-right-v0-oj1c1w0a9wcd1.png?width=640&crop=smart&auto=webp&s=b063e3c2a2e66d56abf0acdb9e101dc74d90cb45)

## Cách khắc phục

 Sử dụng **Terminal**

Chạy trực tiếp lệnh sau trong terminal:

```bash
gsettings set org.gnome.mutter.wayland xwayland-disable-extension "['Xtest']"
```

Sau đó đăng xuất và đăng nhập lại.

