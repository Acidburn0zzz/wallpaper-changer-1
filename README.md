# Wallpaper Changer
Just a python script to change my wallpapers with my configs.
## Installations
Download and extract the repo
```bash
git clone https://github.com/GitOffMyLAN/wallpaper-changer.git && cd wallpaper-changer && bash install.sh
```
You will need to add these commands to your i3wm config (please install https://github.com/derf/feh feh)
```bash
exec_always --no-startup-id feh --bg-scale ~/.config/wall.png
exec_always --no-startup-id wallpaperchanger ~/Pictures/Wallpapers ~/.config/wall.png 300
```
This will make your wallpaper change on reset every 5 minutes (you can change the config file and the wallpaper file to your liking)
 ```bash
exec_always --no-startup-id wal -g -c -i ~/.config/wall.png -a 70
```
You could also add this to change your terminals color scheme to your wall paper (please install https://github.com/dylanaraps/pywal pywal)
