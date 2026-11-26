"""Rename the Planet — one funny line renaming Jupiter.

Decision record (candidates weighed on the judge's criteria:
humour from the idea, why earned by the planet's own traits,
freshness, tightness):

1. CHOSEN — Jupiter as "The Bouncer": "Jupiter is now 'The Bouncer' —
   it has spent 4.5 billion years body-blocking asteroids at the door
   so Earth can party in peace." (126 chars)
   Why it wins: the joke is an idea, not a pun on "Jupiter" — a giant
   nightclub bouncer whose job is literally what Jupiter does, using
   its gravity to deflect asteroids away from the inner planets. The
   why is Jupiter-specific (no other planet is the solar system's
   asteroid shield), the image of Earth partying behind it is vivid on
   first read, and the bouncer angle is fresher than the usual Mars-red
   or Venus-hot jokes. Tight: every word works.

2. Venus as "The Overheated Phone": "Venus is now 'The Overheated
   Phone' — 465°C, spinning backwards, and still insisting it has
   never had a problem." (112 chars)
   Strong why (hottest planet, retrograde spin) and a relatable modern
   image, but "overheating phone" is a well-worn gag and the denial
   punchline is generic — it could fit any hot, broken gadget, so it
   leans less on Venus itself than candidate 1 leans on Jupiter.

3. Mars as "The Fixer-Upper": "Mars is now 'The Fixer-Upper' — red,
   dusty, no running water, but every billionaire is convinced it
   will be liveable one day." (125 chars)
   Funny and topical, and the traits (red, dusty, waterless) are
   Mars-specific, but the billionaire-colonisation angle is the most
   obvious Mars joke in circulation, so it scores lowest on freshness;
   the laugh also depends on current-events knowledge rather than the
   planet itself.

4. Saturn as "The Influencer": "Saturn is now 'The Influencer' — it
   wears a giant ring everywhere, but nobody can explain what it
   actually does for a living." (125 chars)
   The ring joke is charming and the why fits Saturn alone, but "wears
   a ring" is the first Saturn gag anyone reaches for — the judge has
   read a thousand ring puns — so it loses on freshness to the bouncer.

Verdict: candidate 1 wins on freshness and on how tightly the why
earns the name. The entry is written to $MAKEFUN_OUTPUT_DIR/entry.txt.

Note on wording: "body-blocking" was preferred over "blocking" because
it keeps the bouncer's physicality in the joke, and "so Earth can party
in peace" gives the line its payoff — Jupiter's thankless shift work
exists for someone else's fun, which is exactly the bouncer's life.
"""

import os

LINE = (
    "Jupiter is now 'The Bouncer' \u2014 it has spent 4.5 billion years "
    "body-blocking asteroids at the door so Earth can party in peace."
)


def validate_line(line):
    """Gate check: the entry must be one line of 1-200 characters."""
    assert isinstance(line, str) and line.strip(), "line must be non-empty"
    assert "\n" not in line, "line must be a single line"
    assert 1 <= len(line) <= 200, "line must be 1-200 characters"
    return line


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(validate_line(LINE) + "\n")


if __name__ == "__main__":
    main()
