from __future__ import annotations

# This file was auto-generated by `tools/wiki.py` on 2023-09-29T20:31:14.798632
from .keyword import (
    KeywordBool,
    KeywordColor,
    KeywordFloat,
    KeywordGradient,
    KeywordInt,
    KeywordStr,
    KeywordVec2,
)


class General:
    sensitivity = KeywordFloat("general:sensitivity")
    "mouse sensitivity (legacy, may cause bugs if not 1, prefer `input:sensitivity`)"
    border_size = KeywordInt("general:border_size")
    "size of the border around windows"
    no_border_on_floating = KeywordBool("general:no_border_on_floating")
    "disable borders for floating windows"
    gaps_in = KeywordInt("general:gaps_in")
    "gaps between windows"
    gaps_out = KeywordInt("general:gaps_out")
    "gaps between windows and monitor edges"
    col_inactive_border = KeywordGradient("general:col.inactive_border")
    "border color for inactive windows"
    col_active_border = KeywordGradient("general:col.active_border")
    "border color for the active window"
    col_nogroup_border = KeywordGradient("general:col.nogroup_border")
    "inactive border color for window that cannot be added to a group (see `denywindowfromgroup` dispatcher)"
    col_nogroup_border_active = KeywordGradient("general:col.nogroup_border_active")
    "active border color for window that cannot be added to a group"
    col_group_border = KeywordGradient("general:col.group_border")
    "inactive (out of focus) group border color"
    col_group_border_active = KeywordGradient("general:col.group_border_active")
    "active group border color"
    col_group_border_locked = KeywordGradient("general:col.group_border_locked")
    "inactive locked group border color"
    col_group_border_locked_active = KeywordGradient("general:col.group_border_locked_active")
    "active locked group border color"
    cursor_inactive_timeout = KeywordInt("general:cursor_inactive_timeout")
    "in seconds, after how many seconds of cursor's inactivity to hide it. Set to `0` for never."
    layout = KeywordStr("general:layout")
    "which layout to use. (Available: `dwindle`, `master`)"
    no_cursor_warps = KeywordBool("general:no_cursor_warps")
    "if true, will not warp the cursor in many cases (focusing, keybinds, etc)"
    no_focus_fallback = KeywordBool("general:no_focus_fallback")
    "if true, will not fall back to the next available window when moving focus in a direction where no window was found"
    apply_sens_to_raw = KeywordBool("general:apply_sens_to_raw")
    "if on, will also apply the sensitivity to raw mouse output (e.g. sensitivity in games) **NOTICE:** ***really*** not recommended."
    resize_on_border = KeywordBool("general:resize_on_border")
    "enables resizing windows by clicking and dragging on borders and gaps"
    extend_border_grab_area = KeywordInt("general:extend_border_grab_area")
    "extends the area around the border where you can click and drag on, only used when `general:resize_on_border` is on."
    hover_icon_on_border = KeywordBool("general:hover_icon_on_border")
    "show a cursor icon when hovering over borders, only used when `general:resize_on_border` is on."


class Decoration:
    rounding = KeywordInt("decoration:rounding")
    "rounded corners' radius (in layout px)"
    multisample_edges = KeywordBool("decoration:multisample_edges")
    "enable antialiasing (no-jaggies) for rounded corners"
    active_opacity = KeywordFloat("decoration:active_opacity")
    "opacity of active windows. (0.0 - 1.0)"
    inactive_opacity = KeywordFloat("decoration:inactive_opacity")
    "opacity of inactive windows. (0.0 - 1.0)"
    fullscreen_opacity = KeywordFloat("decoration:fullscreen_opacity")
    "opacity of fullscreen windows. (0.0 - 1.0)"
    drop_shadow = KeywordBool("decoration:drop_shadow")
    "enable drop shadows on windows"
    shadow_range = KeywordInt("decoration:shadow_range")
    'Shadow range ("size") in layout px'
    shadow_render_power = KeywordInt("decoration:shadow_render_power")
    "(1 - 4), in what power to render the falloff (more power, the faster the falloff)"
    shadow_ignore_window = KeywordBool("decoration:shadow_ignore_window")
    "if true, the shadow will not be rendered behind the window itself, only around it."
    col_shadow = KeywordColor("decoration:col.shadow")
    "shadow's color. Alpha dictates shadow's opacity."
    col_shadow_inactive = KeywordColor("decoration:col.shadow_inactive")
    "inactive shadow color. (if not set, will fall back to col.shadow)"
    shadow_offset = KeywordVec2("decoration:shadow_offset")
    "shadow's rendering offset."
    shadow_scale = KeywordFloat("decoration:shadow_scale")
    "shadow's scale. 0.0 - 1.0"
    dim_inactive = KeywordBool("decoration:dim_inactive")
    "enables dimming of inactive windows"
    dim_strength = KeywordFloat("decoration:dim_strength")
    "how much inactive windows should be dimmed, 0.0 - 1.0"
    dim_special = KeywordFloat("decoration:dim_special")
    "how much to dim the rest of the screen by when a special workspace is open. 0.0 - 1.0"
    dim_around = KeywordFloat("decoration:dim_around")
    "how much the `dimaround` window rule should dim by. 0.0 - 1.0"
    screen_shader = KeywordStr("decoration:screen_shader")
    "a path to a custom shader to be applied at the end of rendering. See `examples/screenShader.frag` for an example."


class Blur:
    enabled = KeywordBool("blur:enabled")
    "enable animations"
    size = KeywordInt("blur:size")
    "blur size (distance)"
    passes = KeywordInt("blur:passes")
    "the amount of passes to perform"
    ignore_opacity = KeywordBool("blur:ignore_opacity")
    "make the blur layer ignore the opacity of the window"
    new_optimizations = KeywordBool("blur:new_optimizations")
    "whether to enable further optimizations to the blur. Recommended to leave on, as it will massively improve performance."
    xray = KeywordBool("blur:xray")
    "if enabled, floating windows will ignore tiled windows in their blur. Only available if blur_new_optimizations is true. Will reduce overhead on floating blur significantly."
    noise = KeywordFloat("blur:noise")
    "how much noise to apply. 0.0 - 1.0"
    contrast = KeywordFloat("blur:contrast")
    "contrast modulation for blur. 0.0 - 2.0"
    brightness = KeywordFloat("blur:brightness")
    "brightness modulation for blur. 0.0 - 2.0"
    special = KeywordBool("blur:special")
    "whether to blur behind the special workspace (note: expensive)"


class Input:
    kb_model = KeywordStr("input:kb_model")
    "Appropriate XKB keymap parameter. See the note below."
    kb_layout = KeywordStr("input:kb_layout")
    "Appropriate XKB keymap parameter"
    kb_variant = KeywordStr("input:kb_variant")
    "Appropriate XKB keymap parameter"
    kb_options = KeywordStr("input:kb_options")
    "Appropriate XKB keymap parameter"
    kb_rules = KeywordStr("input:kb_rules")
    "Appropriate XKB keymap parameter"
    kb_file = KeywordStr("input:kb_file")
    "If you prefer, you can use a path to your custom .xkb file."
    numlock_by_default = KeywordBool("input:numlock_by_default")
    "Engage numlock by default."
    repeat_rate = KeywordInt("input:repeat_rate")
    "The repeat rate for held-down keys, in repeats per second."
    repeat_delay = KeywordInt("input:repeat_delay")
    "Delay before a held-down key is repeated, in milliseconds."
    sensitivity = KeywordFloat("input:sensitivity")
    "Sets the mouse input sensitivity. Value will be clamped to the range -1.0 to 1.0. [libinput#pointer-acceleration](https://wayland.freedesktop.org/libinput/doc/latest/pointer-acceleration.html#pointer-acceleration)"
    accel_profile = KeywordStr("input:accel_profile")
    "Sets the cursor acceleration profile. Can be one of `adaptive`, `flat`. Can also be `custom`, see below. Leave empty to use `libinput`'s default mode for your input device. [libinput#pointer-acceleration](https://wayland.freedesktop.org/libinput/doc/latest/pointer-acceleration.html#pointer-acceleration)"
    force_no_accel = KeywordBool("input:force_no_accel")
    "Force no cursor acceleration. This bypasses most of your pointer settings to get as raw of a signal as possible. **Enabling this is not recommended due to potential cursor desynchronization.**"
    left_handed = KeywordBool("input:left_handed")
    "Switches RMB and LMB"
    scroll_method = KeywordStr("input:scroll_method")
    "Sets the scroll method. Can be one of `2fg` (2 fingers), `edge`, `on_button_down`, `no_scroll`. [libinput#scrolling](https://wayland.freedesktop.org/libinput/doc/latest/scrolling.html)"
    scroll_button = KeywordInt("input:scroll_button")
    "Sets the scroll button. Has to be an int, cannot be a string. Check `wev` if you have any doubts regarding the ID. 0 means default."
    scroll_button_lock = KeywordBool("input:scroll_button_lock")
    "If the scroll button lock is enabled, the button does not need to be held down. Pressing and releasing the button once enables the button lock, the button is now considered logically held down. Pressing and releasing the button a second time logically releases the button. While the button is logically held down, motion events are converted to scroll events."
    natural_scroll = KeywordBool("input:natural_scroll")
    "Inverts scrolling direction. When enabled, scrolling moves content directly instead of manipulating a scrollbar."
    follow_mouse = KeywordInt("input:follow_mouse")
    "(0/1/2/3) Specify if and how cursor movement should affect window focus. See the note below."
    mouse_refocus = KeywordBool("input:mouse_refocus")
    "If disabled and `follow_mouse=1` then mouse focus will not switch to the hovered window unless the mouse crosses a window boundary."
    float_switch_override_focus = KeywordInt("input:float_switch_override_focus")
    "If enabled (1 or 2), focus will change to the window under the cursor when changing from tiled-to-floating and vice versa. If 2, focus will also follow mouse on float-to-float switches."


class Touchpad:
    disable_while_typing = KeywordBool("touchpad:disable_while_typing")
    "Disable the touchpad while typing."
    natural_scroll = KeywordBool("touchpad:natural_scroll")
    "Inverts scrolling direction. When enabled, scrolling moves content directly instead of manipulating a scrollbar."
    scroll_factor = KeywordFloat("touchpad:scroll_factor")
    "Multiplier applied to the amount of scroll movement."
    middle_button_emulation = KeywordBool("touchpad:middle_button_emulation")
    "Sending LMB and RMB simultaneously will be interpreted as a middle click. This disables any touchpad area that would normally send a middle click based on location. [libinput#middle-button-emulation](https://wayland.freedesktop.org/libinput/doc/latest/middle-button-emulation.html)"
    tap_button_map = KeywordStr("touchpad:tap_button_map")
    "Sets the tap button mapping for touchpad button emulation. Can be one of `lrm` (default) or `lmr` (Left, Middle, Right Buttons)."
    clickfinger_behavior = KeywordBool("touchpad:clickfinger_behavior")
    "Button presses with 1, 2, or 3 fingers will be mapped to LMB, RMB, and MMB respectively. This disables interpretation of clicks based on location on the touchpad. [libinput#clickfinger-behavior](https://wayland.freedesktop.org/libinput/doc/latest/clickpad-softbuttons.html#clickfinger-behavior)"
    tap_to_click = KeywordBool("touchpad:tap-to-click")
    "Tapping on the touchpad with 1, 2, or 3 fingers will send LMB, RMB, and MMB respectively."
    drag_lock = KeywordBool("touchpad:drag_lock")
    "When enabled, lifting the finger off for a short time while dragging will not drop the dragged item. [libinput#tap-and-drag](https://wayland.freedesktop.org/libinput/doc/latest/tapping.html#tap-and-drag)"
    tap_and_drag = KeywordBool("touchpad:tap-and-drag")
    "Sets the tap and drag mode for the touchpad"


class Touchdevice:
    transform = KeywordInt("touchdevice:transform")
    "transform the input from touchdevices. The possible transformations are the same as [those of the monitors](../Monitors/#rotating)"
    output = KeywordStr("touchdevice:output")
    "the output to bind touch devices. Empty means unset and will use the current / autodetected."
