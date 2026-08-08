#!/usr/bin/env bash
# Runs timer_4.py with its sound cues routed into a virtual PipeWire mic
# ("Discord Mic Mix") so Discord hears them, mixed with your real mic so
# you can still talk. In Discord: Settings > Voice & Video > Input Device
# -> "Discord Mic Mix (Source)".
set -euo pipefail

MIC_SOURCE="alsa_input.usb-Logitech_Logitech_USB_Microphone-00.mono-fallback"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON="/home/drake/Documents/github/Free-time-coding/.venv/bin/python3"

cleanup() {
    [[ -n "${MIC_FEED_PID:-}" ]] && kill "$MIC_FEED_PID" 2>/dev/null || true
    [[ -n "${SINK_PID:-}" ]] && kill "$SINK_PID" 2>/dev/null || true
}
trap cleanup EXIT

pw-loopback -n discord_mic -m '[FL FR]' \
    --capture-props='media.class=Audio/Sink node.name=discord_mic node.description="Discord Mic Mix"' \
    --playback-props='media.class=Audio/Source node.name=discord_mic_source node.description="Discord Mic Mix (Source)"' &
SINK_PID=$!
sleep 1

pw-loopback -n discord_mic_feed -C "$MIC_SOURCE" -P discord_mic &
MIC_FEED_PID=$!
sleep 1

"$PYTHON" "$SCRIPT_DIR/timer_4.py" &
TIMER_PID=$!
sleep 1.5

# Route the timer's own audio output into the virtual sink too, alongside
# its default speaker output, so the cues reach Discord AND stay audible
# locally. Matched by this process's PID (not by the ambiguous "python3"
# node name) since QMediaPlayer opens one stream node per sound file, and
# other python3 processes may be running audio at the same time.
for node_id in $(pw-dump | jq -r --argjson pid "$TIMER_PID" \
        '.[] | select(.type=="PipeWire:Interface:Node") | select(.info.props["application.process.id"]==$pid) | .id'); do
    for ch in FL FR; do
        src_port=$(pw-dump | jq -r --argjson nid "$node_id" \
            '.[] | select(.type=="PipeWire:Interface:Port") | select(.info.direction=="output") | select(.info.props["node.id"]==$nid) | select(.info.props["port.name"]=="output_'"$ch"'") | .id')
        dst_port=$(pw-dump | jq -r \
            '.[] | select(.type=="PipeWire:Interface:Port") | select(.info.props["port.alias"]=="discord_mic:playback_'"$ch"'") | .id')
        [[ -n "$src_port" && -n "$dst_port" ]] && pw-link "$src_port" "$dst_port" 2>/dev/null || true
    done
done

wait "$TIMER_PID"
