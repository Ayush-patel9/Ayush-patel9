"""Render the contribution calendar visible on the public GitHub profile."""

import argparse
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request, urlopen

CALENDAR_URL = "https://github.com/users/Ayush-patel9/contributions"
COLORS = ("#36312e", "#664232", "#a45c3d", "#dc8252", "#ffb681")
OUTPUT = Path(__file__).resolve().parents[1] / "assets/profile/activity.svg"


class Calendar(HTMLParser):
    def __init__(self):
        super().__init__()
        self.days = {}
        self.summary = []
        self.reading_summary = False

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag == "h2" and attrs.get("id") == "js-contribution-activity-description":
            self.reading_summary = True
        if tag == "td" and "ContributionCalendar-day" in attrs.get("class", "").split():
            if "data-date" in attrs and "data-level" in attrs:
                day = date.fromisoformat(attrs["data-date"])
                self.days[day] = int(attrs["data-level"])

    def handle_data(self, data):
        if self.reading_summary:
            self.summary.append(data)

    def handle_endtag(self, tag):
        if tag == "h2":
            self.reading_summary = False


def render(html):
    calendar = Calendar()
    calendar.feed(html)
    days = sorted(calendar.days)
    summary = " ".join(" ".join(calendar.summary).split())
    count = summary.partition(" ")[0]

    if (
        len(days) not in (365, 366)
        or (days[-1] - days[0]).days != len(days) - 1
        or not count.replace(",", "").isdigit()
        or any(not 0 <= level < len(COLORS) for level in calendar.days.values())
    ):
        raise ValueError("GitHub did not return a complete public contribution calendar")

    start_weekday = (days[0].weekday() + 1) % 7
    svg = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 864 208" role="img" aria-labelledby="title">',
        f'<title id="title">{count} GitHub contributions in the past year</title>',
        '<rect x="1" y="1" width="862" height="206" rx="15" fill="#171716" stroke="#58493f" stroke-width="2"/>',
        '<g font-family="ui-monospace, SFMono-Regular, monospace">',
        f'<text x="42" y="37" fill="#fff5e8" font-size="21" font-weight="bold">{count} contributions</text>',
        '<text x="822" y="36" fill="#ccbbab" font-size="14" text-anchor="end">Past year</text>',
    ]
    last_label_x = -100
    for index, day in enumerate(days):
        week, weekday = divmod(index + start_weekday, 7)
        x = 42 + week * 14
        y = 70 + weekday * 14
        if (index == 0 or day.day == 1) and x - last_label_x >= 38:
            svg.append(f'<text x="{x}" y="61" fill="#ccbbab" font-size="12">{day:%b}</text>')
            last_label_x = x
        color = COLORS[calendar.days[day]]
        svg.append(f'<rect x="{x}" y="{y}" width="11" height="11" rx="2" fill="{color}"/>')

    svg.extend([
        '<text x="42" y="186" fill="#ccbbab" font-size="13">Activity through ' + days[-1].isoformat() + '</text>',
        '<text x="694" y="186" fill="#ccbbab" font-size="13">Less</text>',
    ])
    for index, color in enumerate(COLORS):
        svg.append(f'<rect x="{733 + index * 14}" y="176" width="11" height="11" rx="2" fill="{color}"/>')
    svg.extend([
        '<text x="808" y="186" fill="#ccbbab" font-size="13">More</text>',
        '</g>',
        '</svg>',
    ])
    return "\n".join(svg) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--html", type=Path, help="Use a saved copy of the public calendar")
    args = parser.parse_args()
    if args.html:
        html = args.html.read_text(encoding="utf-8")
    else:
        request = Request(CALENDAR_URL, headers={"User-Agent": "Ayush-patel9-profile-calendar"})
        with urlopen(request, timeout=30) as response:
            html = response.read().decode("utf-8")
    OUTPUT.write_text(render(html), encoding="utf-8")


if __name__ == "__main__":
    main()
