# Facts — What's inside an iPhone? (long-form 001)

Checked on 2026-10-25. Every number in the script is listed here with its source.

| Chapter | Claim | Source |
|---|---|---|
| intro | iPhone 18 Pro starts at $1,199 (Pro Max $1,299, +$100 vs last year) | https://www.macrumors.com/2026/09/09/iphone-18-pro-iphone-duo-new-c2-modem/ ; https://www.tomsguide.com/phones/iphones/iphone-18-pro-and-iphone-18-pro-max-are-official-heres-what-you-need-to-know |
| c01 | Pentalobe = five rounded lobes, no centre pin; on iPhone since the iPhone 4 | https://www.eweek.com/mobile/apple-iphone-4-uses-evil-tamper-proof-screws-ifixit/ |
| c01 | iPhone 18 Pro is front-entry: major repairs go through the display; rear glass only gives access to the wireless charging coil; pentalobe screwdriver needed | https://www.igeeksblog.com/iphone-18-pro-ifixit-teardown-battery-variable-aperture/ ; https://hothardware.com/news/iphone-18-pro-teardown-brilliant-upgrades-costly-repair-traps |
| c01 | iFixit heated the screen ~70–72 °C; the plastic display frame cracked on 3 of the 4 phones opened | https://www.igeeksblog.com/iphone-18-pro-ifixit-teardown-battery-variable-aperture/ |
| c02 | A20 Pro, 2 nm, made by TSMC | https://www.tomsguide.com/phones/iphones/iphone-18-pro-and-iphone-18-pro-max-are-official-heres-what-you-need-to-know ; https://hothardware.com/news/iphone-18-pro-teardown-brilliant-upgrades-costly-repair-traps |
| c02 | Apple's first custom-designed CPU core: A6 (iPhone 5, 2012) | https://www.anandtech.com/show/6292 |
| c02 | Phone chip market Q1 2025: MediaTek 36 %, Qualcomm 26 %, Apple 17 % | https://www.channelnews.com.au/mediatek-again-tops-smartphone-soc-market/ (Counterpoint) |
| c02 | C2 modem + N1 wireless chip are Apple-made; US iPhone 18 Pro Max still uses Qualcomm's Snapdragon X80 modem | https://www.igeeksblog.com/iphone-18-pro-ifixit-teardown-battery-variable-aperture/ ; https://www.macrumors.com/2026/09/09/iphone-18-pro-iphone-duo-new-c2-modem/ |
| c03 | Stacked ("sandwich") logic board since iPhone X (2017): two boards soldered on top of each other with a spacer board; ~70 % of the footprint (≈30 % less) | https://appleinsider.com/articles/17/11/03/dual-batteries-layered-logic-boards-revealed-in-iphone-x-teardown |
| c03 | iPhone 18 Pro: NAND storage now inside the sandwich, A20 Pro on the outside against the vapor chamber; storage repair needs the layers separated | https://www.igeeksblog.com/iphone-18-pro-ifixit-teardown-battery-variable-aperture/ |
| c04 | Face ID: dot projector >30,000 IR dots, flood illuminator, IR camera, 3D map; 1 in 1,000,000 (Touch ID 1 in 50,000); twins/siblings are an exception (Apple) | https://en.wikipedia.org/wiki/Face_ID |
| c04 | iPhone 18 Pro: IR camera under the display, every other row of pixels removed above it | https://9to5mac.com/2026/09/20/ifixit-tears-down-iphone-18-pro-explores-variable-aperture-finds-concerning-repair-issue/ |
| c04 | Most Android face unlock is 2D (selfie camera, no depth/IR); Which? test: 133 of 208 phones fooled by a printed photo; Which? recommends fingerprint | https://www.bgr.com/2258891/difference-between-apple-id-android-face-unlock-explained/ |
| c05 | iPhone 18 Pro battery 4,288 mAh (eSIM model) | https://www.igeeksblog.com/iphone-18-pro-ifixit-teardown-battery-variable-aperture/ |
| c05 | OnePlus 15: 7,300 mAh | https://www.androidauthority.com/oneplus-15-battery-size-3608565/ |
| c05 | Tom's Guide test: iPhone 17 Pro Max (5,088 mAh) 17 h 54; Galaxy S26 Ultra (5,000 mAh) 16 h 10; OnePlus 15 25 h 13 | https://www.tomsguide.com/phones/samsung-phones/samsung-galaxy-s26-ultra-battery-life-tested-heres-how-it-stacks-up-to-iphone-17-pro-max-and-more |
| c05 | Electrically releasable battery adhesive: releases in ~90 s at 12 V (18 Pro) | https://www.igeeksblog.com/iphone-18-pro-ifixit-teardown-battery-variable-aperture/ |
| c06 | iPhone 7 home button is solid-state, the click is simulated by the Taptic Engine | https://www.phonearena.com/news/Here-is-one-likely-reason-why-Apple-removed-the-physical-Home-button-in-the-iPhone-7_id85374 |
| c06 | ERM (spinning off-centre weight) typical of old/cheap phones, LRA moves a mass along one axis, crisper | https://www.androidpolice.com/2020/10/20/a-lot-more-goes-into-good-smartphone-haptics-than-youd-think/ ; https://ti.com/lit/SLOA194 |
| c07 | iPhone 17 Pro: first iPhone vapor chamber, deionized water sealed inside, laser-welded into the aluminium chassis | https://www.apple.com/newsroom/2025/09/apple-unveils-iphone-17-pro-and-iphone-17-pro-max ; https://www.channelnews.com.au/vapour-chamber-cooling-belatedly-embraced-by-apple/ |
| c07 | iPhone 18 Pro: vapor chamber with 3× the surface area, Apple claims 40 % more sustained performance | https://www.tomsguide.com/phones/iphones/iphone-18-pro-and-iphone-18-pro-max-are-official-heres-what-you-need-to-know |
| c07 | ASUS ROG Phone (2018) had a 3D vapor-chamber cooling system | https://betanews.com/article/asus-rog-phone/ |
| c08 | iPhone 18 Pro OLED panels from Samsung Display and LG Display | https://en.tempo.co/read/2103447/iphone-18-pro-series-to-use-oled-panels-from-samsung-and-lg |
| c08 | Lightning: iPhone 5, 2012; EU Parliament approved USB-C rules on 4 Oct 2022; iPhone 15 (2023) first USB-C iPhone | https://en.wikipedia.org/wiki/Lightning_(connector) |
| c09 | Parts and Service History: battery, display, logic board, front & rear cameras tracked (iPhone 12+); "Unknown" part → notification at first unlock and again 5 days later; genuine parts calibrated with data on Apple's servers | https://support.apple.com/en-us/HT212878 |
| c10 | Counterpoint: iPhone 17 Pro Max 256 GB bill of materials ≈ $410 | https://www.phonearena.com/news/apple-iphone-18-pro-max-big-price-hike-less-profitable-than-17-pro-max_id181745 |
| c10 | iPhone 17 Pro Max launch price $1,199 (18 Pro Max $1,299 = +$100) | https://www.tomsguide.com/phones/iphones/iphone-18-pro-and-iphone-18-pro-max-are-official-heres-what-you-need-to-know |
| c10 | TrendForce: iPhone 18 Pro BOM ≈ +38 % vs 17 Pro, driven by memory prices | https://notebookcheck.net/TrendForce-says-iPhone-18-Pro-s-bill-of-materials-cost-rises-almost-40-as-memory-prices-surge.1364498.0.html |
| c11 | iPhone Duo = Apple's first foldable (teaser) | https://www.macrumors.com/2026/09/09/iphone-18-pro-iphone-duo-new-c2-modem/ |
| c05 | eSIM-only models (US etc.) get the bigger cells; physical-SIM models have smaller batteries | https://www.igeeksblog.com/iphone-18-pro-ifixit-teardown-battery-variable-aperture/ |
| c07 | iPhone 18 Pro main camera: variable aperture, six blades ~1 mm at the tip, driven by electromagnets, f/1.48–f/4.0, widest ≈ 7.3× more light; a stuck aperture = whole camera replaced; one blade flew out during iFixit's teardown | https://www.igeeksblog.com/iphone-18-pro-ifixit-teardown-battery-variable-aperture/ ; https://9to5mac.com/2026/09/20/ifixit-tears-down-iphone-18-pro-explores-variable-aperture-finds-concerning-repair-issue/ |
| c07 | Galaxy S9 (2018) had a dual aperture f/1.5 / f/2.4 | https://bgr.com/2268324/android-phones-with-variable-aperture-cameras-before-iphone-18-pro/ |
