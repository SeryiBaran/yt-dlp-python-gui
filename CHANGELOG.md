# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog],
and this project adheres to [Semantic Versioning] and [Conventional Commits].

## [1.3.1] - 2025-05-29

### Fixed

- Fix links color in About window

### Changed

- Cool urls log

## [1.3.0] - 2025-05-29

### Added

- [UV](https://docs.astral.sh/uv/) as package manager
- Experimental cancel button
- Errors list

### Changed

- Improve ui

## [1.2.2] - 2025-05-29

### Changed

- Bump yt-dlp from `2025.1.26` to `2025.4.30`

## [1.2.1] - 2025-02-14

### Changed

- Bump yt-dlp from `2024.12.13` to `2025.1.26`

### Added

- Add urls saving to ./yt-dlp-python-gui__URL_HISTORY.txt

## [1.2.0] - 2024-12-25

### Fixed

- Force download H264 codec (because AV1 doesn't play on NTV Plus TV's)

## [1.1.6] - 2024-12-22

### Changed

- Bump yt-dlp
- Added normal default big_ui mode

## [1.1.5] - 2024-10-15

### Changed

- Bump yt-dlp

## [1.1.4] - 2024-07-13

### Changed

- Bump yt-dlp

## [1.1.3] - 2024-04-20

### Added

- Added button to paste link to textarea

### Changed

- Improved design

## [1.1.2] - 2024-04-08

### Changed

- Update yt-dlp version

## [1.1.1] - 2024-03-13

### Fixed

- Continue download if error

## [1.1.0] - 2024-03-04

### Added

- checkbox for mp3 only downloading

## [1.0.6] - 2024-02-22

### Added

- dark theme with pyqtdarktheme

## [1.0.5] - 2024-02-20

### Added

- add ffmpeg information in "About program"

## [1.0.4] - 2024-02-20

### Added

- compact ui (big ui not removed)
- normal mp4 downloading if ffmpeg installed

### Fixed

- set openExternalLinks in about window links to `True`

## [1.0.3] - 2024-02-19

### Added

- settings saving to `yt-dlp-python-gui.ini` in folder where exe located
- window "About program"

## [1.0.2] - 2024-02-17

### Added

- version number at bottom of ui

### Changed

- ui font size slightly reduced (from 16 to 14)

## [1.0.1] - 2024-02-17

### Changed

- add 1080 video size

### Fixed

- set big ui checkbox font size
- add normal filenames sanitization (now forbidden characters is replaced by `_`, not unicode symbols)

## [1.0.0] - 2024-01-16

- initial release

<!-- Links -->
[keep a changelog]: https://keepachangelog.com/en/1.0.0/
[semantic versioning]: https://semver.org/spec/v2.0.0.html
[conventional commits]: https://www.conventionalcommits.org/en/v1.0.0/
