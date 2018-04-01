killall -q wallpaperchanger

# Wait until the processes have been shut down
while pgrep -x wallpaperchanger >/dev/null; do sleep 1; done

wallpaperchager ~/Pictures/Wallpapers ~/.config/wall.png 300
