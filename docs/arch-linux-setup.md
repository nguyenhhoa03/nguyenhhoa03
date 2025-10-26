# Cấu hình Arch Linux lúc cài đặt

Fix `Remote Desktop`
```
gsettings set org.gnome.mutter.wayland xwayland-disable-extension "['Xtest']"
```

Setup Flathub
```
sudo pacman -Syu flatpak
```

Cài đặt `Chromium`
```
flatpak install flathub org.chromium.Chromium
```

Cài đặt `Lutris` và `Protonplus`
```
sudo pacman -S lutris
yay -S protonplus
```

Cài đặt VLC
```
flatpak install flathub org.videolan.VLC
```

Xử lý file desktop
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

Cài đặt Authenticator
```
flatpak install flathub com.belmoussaoui.Authenticator
```
