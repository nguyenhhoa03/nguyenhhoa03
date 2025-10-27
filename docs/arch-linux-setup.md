# Cấu hình Arch Linux lúc cài đặt

## Cài đặt gói

### Fix `Remote Desktop`
```
gsettings set org.gnome.mutter.wayland xwayland-disable-extension "['Xtest']"
```

### Setup Flathub
```
sudo pacman -Syu flatpak
```

### Cài đặt `Chromium`
```
flatpak install flathub org.chromium.Chromium
```
### Cài đặt `chrome extensions`
- [MYNT: Material You New Tab](https://chromewebstore.google.com/detail/mynt-material-you-new-tab/jjpokbgpiljgndebfoljdeihhkpcpfgl)
- [Save image as Type](https://chromewebstore.google.com/detail/save-image-as-type/gabfmnliflodkdafenbcpjdlppllnemd)
- [uBlock Origin Lite](https://chromewebstore.google.com/detail/ublock-origin-lite/ddkjiahejlhfcafbddmgiahcphecmpfh)
- [VNK - Vietnamese Input Method](https://chromewebstore.google.com/detail/vnk-vietnamese-input-meth/hoelaaippkdglnlbonkfjmlcoendcoce)
- [ZaDark – Zalo Dark Mode](https://chromewebstore.google.com/detail/zadark-%E2%80%93-zalo-dark-mode/llfhpkkeljlgnjgkholeppfnepmjppob)

### Cài đặt `Firefox extensions`
- [uBlock Origin](https://addons.mozilla.org/en-US/firefox/addon/ublock-origin/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=search)

### Cài đặt `Lutris` và `Protonplus`
```
sudo pacman -S lutris
yay -S protonplus
```

### Cài đặt VLC
```
flatpak install flathub org.videolan.VLC
```

### Xử lý file desktop
```
sudo tee -a /usr/share/applications/net.lutris.Lutris.desktop > /dev/null <<'EOF'
Hidden=true
NoDisplay=true
EOF

sudo tee -a /usr/share/applications/com.vysp3r.ProtonPlus.desktop > /dev/null <<'EOF'
Hidden=true
NoDisplay=true
EOF
```

### Cài đặt Authenticator
```
flatpak install flathub com.belmoussaoui.Authenticator
```

### Cài đặt Proton VPN
```
flatpak install flathub com.protonvpn.www
```

### Cài đặt Extension Manager
```
flatpak install flathub com.mattjakeman.ExtensionManager
```

## Cài đặt snapshot

### Cài Snapper & service
```
sudo pacman -S snapper snap-pac
```

### Tạo cấu hình
```
sudo snapper -c root create-config /
```

### Cấu hình snapshot
```
sudo nano /etc/snapper/configs/root
```

Sửa `TIMELINE_CREATE="no"` thành `TIMELINE_CREATE="yes"`

Ví dụ 
```
TIMELINE_CREATE="yes"          # bật tạo snapshot định kỳ (timeline)
TIMELINE_CLEANUP="yes"         # bật tự dọn snapshot cũ
TIMELINE_MIN_AGE="1800"        # thời gian tối thiểu giữa 2 snapshot (giây) = 30 phút
TIMELINE_LIMIT_HOURLY="10"     # giới hạn snapshot theo giờ
TIMELINE_LIMIT_DAILY="7"       # giới hạn snapshot theo ngày
TIMELINE_LIMIT_WEEKLY="0"      # giới hạn snapshot theo tuần
TIMELINE_LIMIT_MONTHLY="0"     # giới hạn snapshot theo tháng
TIMELINE_LIMIT_YEARLY="0"      # giới hạn snapshot theo năm
```

### Kích hoạt service
```
sudo systemctl enable --now snapper-timeline.timer
sudo systemctl enable --now snapper-cleanup.timer
```
