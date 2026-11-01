# Facts — What's inside a USB flash drive? (ep. 9)

| Claim | Source |
|---|---|
| Inside a USB stick: connector, mass-storage controller chip, NAND flash memory chip, crystal oscillator ("a tiny clock"), often an LED | https://usbmemorydirect.com/blog/whats-inside-usb-flash-drive-components |
| Flash memory = billions of cells (multi-gigabyte chips, ≥1 bit per cell) | https://en.wikipedia.org/wiki/Flash_memory |
| Each cell has a floating gate insulated all around by an oxide layer (silicon dioxide ≈ glass), electrons stay trapped there | https://en.wikipedia.org/wiki/Flash_memory ; https://www.halbleiter.org/en/digital-technology/flash-cell/ |
| Writing: a high voltage makes electrons tunnel through the oxide into the floating gate (Fowler–Nordheim tunnelling / hot-electron injection) | https://en.wikipedia.org/wiki/Flash_memory |
| NAND: erased cells read as 1, programming (adding charge) sets them to 0 | https://en.wikipedia.org/wiki/Flash_memory |
| Non-volatile: data kept for years without power (datasheets: 10–20+ years; worn cells less) | https://en.wikipedia.org/wiki/Flash_memory |
| "The silicon oxide in a cell degrades with every erase operation"; finite program/erase cycles | https://en.wikipedia.org/wiki/Flash_memory |
| Controller spreads writes over all blocks = wear leveling | https://en.wikipedia.org/wiki/Flash_memory |
| Invented by Fujio Masuoka at Toshiba (~1980); colleague Shōji Ariizumi suggested "flash" because erasing (a whole block at once) reminded him of a camera flash | https://en.wikipedia.org/wiki/Flash_memory ; https://petapixel.com/2017/07/13/know-flash-memory-named-camera-flash/ |
