# Steam DepotDownloader GUI using tkinter
This is a basic GUI for [DepotDownloader](https://github.com/SteamRE/DepotDownloader) written in Python using tkinter library.

## Installation

Download executable in [Releases](https://github.com/52554d41/sddtk/releases) and move to DepotDownloader installation folder. The program will not work outside of DepotDownloader installation folder!

## Usage
Enter values and click "Download" to start. To download anonymously, leave username empty.
The program currently supports Windows and Linux, but only Windows has been tested and working.

## Support
If you encounter a problem, or would like to propose a change, open an issue and describe your setup, reproduction of the problem, proposal, etc...

## Why not just use SteamDepotDownloaderGUI?

[SteamDepotDownloaderGUI](https://github.com/mmvanheusden/SteamDepotDownloaderGUI) handles your account password in the app and passes it over to DepotDownloader, which has [potential security implications](https://github.com/SteamRE/DepotDownloader/issues/343). To address this sddtk uses interactive password option of DepotDownloader. There's also the matter of personal preference, with SteamDepotDownloaderGUI being an Electron app, which has its own pros and cons. In the end, it's up to you to use whichever you like.