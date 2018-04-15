killall -q wallpaperchanger

# Wait until the processes have been shut down
while pgrep -x wallpaperchanger >/dev/null; do sleep 1; done

wallpaperchanger ~/Pictures/desktop/ ~/.config/wall.png 300 85
