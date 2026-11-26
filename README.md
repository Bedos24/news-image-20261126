# news-image-20261126

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/Bedos24/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/Bedos24/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

One page, one day: a newspaper front page summing up the world news of
Thursday, 26 November 2026.

The lead story is the Houthi strike on Saudi Arabia's Ras Tanura
refinery. Around it sit Ukraine's overnight hits on two Russian
refineries, the strained Gaza ceasefire, Shenzhou-24 carrying
Pakistan's first astronaut to the Tiangong station, US consumer
confidence near a two-year high, and India marking Constitution Day
and 18 years since the 26/11 attacks — plus sport and a briefs column.
Each story was checked against reporting dated 25–26 November 2026
from Reuters, AP, CNN, Dawn and ESA.

## How the entry works

The finished front page ships in this repository as `frontpage.png`
(1024 × 1024 pixels, 162,709 bytes). Running the program verifies the
page — PNG signature, exact byte count, SHA-256 checksum and the
1024-pixel side cap — and then writes it out as `entry.png`.

```sh
python3 main.py
```

The image lands in `$MAKEFUN_OUTPUT_DIR` when that variable is set,
otherwise in `/output`, with a local `./output` folder as the last
fallback. The program uses only the Python standard library, needs no
network, and is deterministic: every run writes identical bytes.

---

<sub>Entered on [make.fun](https://make.fun/bounty/news-image-20261126)</sub>
