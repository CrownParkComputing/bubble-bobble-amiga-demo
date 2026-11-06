# Bubble Bobble — native Amiga demo

A native 68020/AGA/Paula conversion for A1200 with 2 MB Chip + 8 MB Fast RAM.
This public demo contains the first **five ordinary rounds**, arranged as a
short 1×5 scrolling map, and a **five-minute active-play limit** per new game.
The executable contains five ordinary room layouts; rooms 6–100 are absent.
Complete round 5 or run out of demo time to finish and enter qualifying scores.
Intro, menus and pause do not spend the clock. Restarting a level preserves it;
starting a new game refills it. The remaining time is shown during play.

Includes simultaneous 1P/2P co-op, original-colour graphics, enemy drops and
collectibles, music selection, FPS toggle, pause/restart and persistent scores.
Arcade reconstruction is still in progress; this is a demo, not a claim that
all original arcade behavior has been reproduced.

## Play on an Amiga

Copy `BubbleBobbleDemo` to your Amiga and run, from that directory:

```
WHDLoad SLAVE=BubbleBobble.slave NOMMU CACHE
```

Needs AGA, a 68020 or newer,2MB Chip/8MB Fast, WHDLoad and your own original
A1200 Kickstart 40.068 with its WHDLoad relocation file. The package does not
include original ROM sets, Kickstart images or AmigaOS boot files.

## Play in Amiberry

Requires Python 3 and Amiberry with its WHDBoot files installed. Run:

```
python3 launch.py --cpu 020
```

The launcher finds locally installed
WHDBoot and Kickstart files and creates a local boot under `.local/`.
Use `--kickstart /path/to/kick40068.A1200`, `--whdboot /path/to/WHDBoot`,
or `--emulator /path/to/amiberry` when needed. Nothing is downloaded.

Two portable configurations are included:

- 020: stock 14.18758 MHz 68020, A1200, 2 MB Chip/8 MB Fast, no JIT.
- 040: 25 MHz 68040, A4000 AGA, 2 MB Chip/8 MB Fast, no JIT. Use `--cpu 040`
  and, if needed, `--host-rom /path/to/kick40068.A4000`.

Do not mount the full game's data over the demo; its shortened map and timer
are built into its separate executable.

## Controls

| Action | Player 1 | Player 2 |
| --- | --- | --- |
| Move | Left/Right | A/D |
| Blow bubble | Z or Left Alt | F |
| Jump | X or Left Shift | G |
| Start/join | 1 | 2 |
| Credit | 5 | 6 |

Both pads use D-pad movement, A for bubbles/select, B for jump/back, Back for
credits, Start to start/join or pause an active player. Menu: D-pad/arrows,
A/Return selects, B goes back. F1/Escape pauses, R restarts the level, Tab/F10
switches FPS. Title offers 1 Player, 2 Players Co-op, Round, Options, High Scores
and Quit. Options includes soundtrack mode/track and sound effects.

The top ten entries accept three initials. Scores and settings use a separate
`demo-scores.dat`, with CRC and backup recovery.

## Credits and package

Original game and artwork: Taito. Amiga music: David Whittaker, sourced from
[the requested Zophar collection](https://www.zophar.net/music/amiga/bubble-bobble).
Music is preconverted signed 8-bit PCM, including the recordings' supplied fades;
it is not a native tracker replay. Full private source/assets and recovery data
are kept separately. Included component notices are under `BubbleBobbleDemo/Licenses`;
those licenses do not grant ownership of the original game or soundtrack.

See `demo-manifest.json` for limits and file hashes, and `validation/` for the
focused timer/map checks and isolated emulator verification.

Primary controller: physical Amiga port2; port1 defaults to mouse. Replace the
mouse with a second pad only for Player2. Automatic input switching is disabled.
