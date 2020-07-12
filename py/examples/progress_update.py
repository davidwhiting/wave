# Form / Progress / Updating
# Update a progress bar's completion status periodically.
# ---
import time

from telesync import site, ui

page = site['/demo']

page['example'] = ui.form_card(
    box='1 1 4 -1',
    items=[
        ui.progress(label='Basic Progress'),
    ]
)
page.sync()

for i in range(1, 11):
    time.sleep(1)
    page['example'].items = [
        ui.progress(label='Basic Progress', caption=f'{i * 10}% complete', value=i / 10),
    ]

    # This will work, too:
    # page['example'].items[0].progress.value = i/10

    page.sync()
