# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog],
and this project adheres to [Semantic Versioning] and [Conventional Commits].

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
