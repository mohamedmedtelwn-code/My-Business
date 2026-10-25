# Cloud ids (rewritten whenever they change)

Runner session (receives every scheduled message; created 2026-10-25 with the
repository as its source and `main` as its outcome branch; git identity
"Venture Studio"): `session_01PzBeX8zGkWK1VKZA5RpADm`

Scheduled tasks on the owner's Claude account, all firing into the runner
session (Qatar time):

| Task | Cron | Trigger id |
|------|------|------------|
| Research cycle (Mon, Thu 05:46) | `CRON_TZ=Asia/Qatar 46 5 * * 1,4` | `trig_013ZTp7Z24m6SxaEvDS3JiJA` |
| Planning pass (daily 06:47) | `CRON_TZ=Asia/Qatar 47 6 * * *` | `trig_01GzErQG9gYmHhLNAXW1SshJ` |
| Preparation pass (daily 08:14) | `CRON_TZ=Asia/Qatar 14 8 * * *` | `trig_019qfB1cDz2xW4aHHHnf76pQ` |
| Management nightly (daily 21:42) | `CRON_TZ=Asia/Qatar 42 21 * * *` | `trig_01E3X6DX3EJgh3drNDJQAyjF` |
| Management weekly (Fri 17:43) | `CRON_TZ=Asia/Qatar 43 17 * * 5` | `trig_019awiyNSeqwP8KADwtWQVQ4` |

First verified run through the runner: Management nightly, 2026-10-25 21:42
Qatar time, commit 5ba826f on main, live dashboard refreshed, push
notification sent. The five fresh-session tasks created earlier the same day
(they could not push) were deleted.

Work tasks (one per live business) are added here when Preparation launches a
business; they fire into the same runner session.
