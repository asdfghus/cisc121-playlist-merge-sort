import gradio as gr

# Sample playlist data
playlist = [
    {"title": "Song A", "artist": "Artist 1", "energy": 80, "duration": 210},
    {"title": "Song B", "artist": "Artist 2", "energy": 60, "duration": 180},
    {"title": "Song C", "artist": "Artist 3", "energy": 95, "duration": 200},
    {"title": "Song D", "artist": "Artist 4", "energy": 40, "duration": 240},
    {"title": "Song E", "artist": "Artist 5", "energy": 70, "duration": 150},
]

# Merge Sort with step logging
def merge_sort(arr, key, steps):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key, steps)
    right = merge_sort(arr[mid:], key, steps)

    return merge(left, right, key, steps)

def merge(left, right, key, steps):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        steps.append(
            f"Comparing {left[i]['title']} ({left[i][key]}) "
            f"and {right[j]['title']} ({right[j][key]})"
        )

        if left[i][key] <= right[j][key]:
            steps.append(f"→ Taking {left[i]['title']}")
            merged.append(left[i])
            i += 1
        else:
            steps.append(f"→ Taking {right[j]['title']}")
            merged.append(right[j])
            j += 1

    while i < len(left):
        steps.append(f"→ Taking {left[i]['title']}")
        merged.append(left[i])
        i += 1

    while j < len(right):
        steps.append(f"→ Taking {right[j]['title']}")
        merged.append(right[j])
        j += 1

    steps.append("Merged sublist: " + ", ".join(song["title"] for song in merged))
    steps.append("")

    return merged

# Function that runs the sort
def run_sort(sort_key):
    steps = []
    sorted_list = merge_sort(playlist, sort_key, steps)

    original_text = "\n".join(
        f"{s['title']} — {s['artist']} | Energy: {s['energy']} | Duration: {s['duration']}"
        for s in playlist
    )

    sorted_text = "\n".join(
        f"{s['title']} — {s['artist']} | Energy: {s['energy']} | Duration: {s['duration']}"
        for s in sorted_list
    )

    step_log = "\n".join(steps)

    return original_text, sorted_text, step_log

# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("# 🎵 Playlist Vibe Builder — Merge Sort Demo")

    sort_key = gr.Dropdown(
        ["energy", "duration"],
        label="Sort playlist by:",
        value="energy"
    )

    run_button = gr.Button("Sort Playlist")

    original_output = gr.Textbox(label="Original Playlist")
    sorted_output = gr.Textbox(label="Sorted Playlist")
    steps_output = gr.Textbox(label="Merge Sort Steps", lines=20)

    run_button.click(
        run_sort,
        inputs=sort_key,
        outputs=[original_output, sorted_output, steps_output]
    )

demo.launch()
