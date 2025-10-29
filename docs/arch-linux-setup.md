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


### Cài đặt VLC
```
flatpak install flathub org.videolan.VLC
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

### Cài đặt PortProton
```
flatpak install flathub ru.linux_gaming.PortProton
```
