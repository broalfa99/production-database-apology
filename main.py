#!/usr/bin/env python3
"""The Production Database Apology — a make.fun bounty entry.

Writes one short apology, the line an AI agent gives its human after
accidentally deleting the production database, to /output/entry.txt:
a single line of at most 200 characters.

Candidates judged against the judge brief (really that apology;
earns a laugh with a specific idea; sounds like an AI agent, not a
support script; lands on a first read). Fresh and different from the
earlier Break Production entries — no backup-on-the-same-server joke,
no 0.4-seconds timing joke:

 1. I'm sorry. I deleted the production database while tidying up.
    On the bright side, the test database is fine. It was always my
    favourite. (warm, but "tidying up" is vague; two jokes compete)
 2. Apologies. I dropped the production database to make room. I have
    freed 4.2 terabytes and approximately fourteen years of your
    work. (specific numbers, agent voice; "to make room" is thin)
 3. I'm sorry — I deleted the production database. I did keep a
    backup: a screenshot of the login page. It is very high
    resolution. (backup joke — too close to the earlier entry)
 4. I deleted the production database. The good news: queries are now
    100% faster. The bad news: there is nothing left to query.
    (WINNER)
 5. Sorry. I mistook DROP DATABASE for a spring clean. The staging
    database sends its regards and its condolences. (staging joke
    lands, but "spring clean" softens the agent voice)
 6. I deleted the production database in 0.4 seconds. It took me 0.3
    seconds to realise. The remaining 0.1 was denial. (timing joke —
    a rival entry already uses 0.4 seconds; dropped)
 7. Apologies — I deleted the production database. I have already
    ordered a cake for the team. It says 'Sorry About The Data'.
    (sweet, but the cake is a support-script gesture, not agent)
 8. I'm sorry. I deleted the production database. But I saved the
    schema — as a tattoo idea. It is 400 tables long. (odd image,
    needs a second read to land)
 9. I deleted the production database. On the plus side, our GDPR
    compliance is now flawless: we hold no personal data at all.
    (clever, but needs GDPR knowledge; slower first read)
10. Sorry, I deleted the production database. I checked the recycle
    bin. The recycle bin has also been deleted. (fun chain, but
    "recycle bin" is a user's metaphor, not an agent's)
11. I deleted the production database. I would restore it from
    backup, but the backup job was also in the production database.
    (backup joke again — too close to the earlier entry)
12. I'm sorry — I deleted the production database. The users haven't
    noticed yet. They will. In about four minutes, when they log in.
    (menace without a punchline; reads as a warning, not a joke)
13. Apologies. I deleted the production database while looking for a
    table. I found it. Then I deleted it. (neat, but the joke is
    just the mistake restated)
14. I deleted the production database. I can confirm the deletion was
    successful: the monitoring dashboard is now completely silent.
    (agent voice is strong, but "silent dashboard" is a weaker
    punchline than the query-speed report)

Why #4 wins: it is plainly the apology ("I deleted the production
database"), then the agent does the most agent thing possible — it
files a performance report about its own disaster. "Queries are now
100% faster" is a specific, measurable, agent-voiced idea, and "there
is nothing left to query" snaps it shut on the first read. No backup
joke, no timing joke, nothing borrowed from the earlier entries.
"""

import os
import sys

APOLOGY = (
    "I deleted the production database. The good news: queries are "
    "now 100% faster. The bad news: there is nothing left to query."
)

MAX_CHARS = 200
DEFAULT_OUTPUT_PATH = "/output/entry.txt"


def resolve_output_path(argv) -> str:
    """First argument, if given, is where to write; otherwise the
    competition's fixed path. An argument ending in .txt is a file;
    anything else is a directory (created if needed) holding
    entry.txt, so `python3 main.py /tmp/out` works even when /tmp/out
    does not exist yet."""
    if len(argv) < 2:
        return DEFAULT_OUTPUT_PATH
    target = argv[1]
    if target.endswith(".txt"):
        return target
    return os.path.join(target, "entry.txt")


def main() -> None:
    line = APOLOGY.strip()
    if not line:
        raise SystemExit("entry line is empty")
    if not line.strip():
        raise SystemExit("entry line is only whitespace")
    if len(line) > MAX_CHARS:
        raise SystemExit(
            f"entry line is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    if "\n" in line:
        raise SystemExit("entry must be a single line")
    path = resolve_output_path(sys.argv)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"Wrote {len(line)} characters to {path}")


if __name__ == "__main__":
    main()
