# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [v0.3.0](https://github.com/tdesposito/pyZohoAPI/releases/tag/v0.3.0) - 2021-02-27

<small>[Compare with v0.2.6](https://github.com/tdesposito/pyZohoAPI/compare/v0.2.6...v0.3.0)</small>

### Added
- Add getimage() and deleteimage() ([62f0bbf](https://github.com/tdesposito/pyZohoAPI/commit/62f0bbf62e081b4b0e507d3676bb05e876bb2d4a) by Todd Esposito).

### Fixed
- Fix testdata references in test-shell ([cf9e851](https://github.com/tdesposito/pyZohoAPI/commit/cf9e851bfd6ab481f7f8f6c564f8abb2690aaf60) by Todd Esposito).


## [v0.2.6](https://github.com/tdesposito/pyZohoAPI/releases/tag/v0.2.6) - 2021-02-26

<small>[Compare with v0.2.0](https://github.com/tdesposito/pyZohoAPI/compare/v0.2.0...v0.2.6)</small>

### Added
- Add test for confirm() ([dab9453](https://github.com/tdesposito/pyZohoAPI/commit/dab9453eb26d336516119e7a46bf14d053abc428) by Todd Esposito).
- Add test for number property ([5c6e670](https://github.com/tdesposito/pyZohoAPI/commit/5c6e670eb331501a4c9e832fd87fcb7c7e3d0997) by Todd Esposito).
- Add test for maprelatedlist() ([7528621](https://github.com/tdesposito/pyZohoAPI/commit/752862120900c9a5ba095fd6ec405164a04d1085) by Todd Esposito).
- Add changelog ([8d3e6da](https://github.com/tdesposito/pyZohoAPI/commit/8d3e6da2474fc5d780c482263c3cccaf88d3e2f0) by Todd Esposito).
- Add pypi badges ([aa2d593](https://github.com/tdesposito/pyZohoAPI/commit/aa2d593c28c3d64a128eedebcf10f777714aef95) by Todd Esposito).

### Changed
- Changed confirm() (et al) to return true/false ([4173407](https://github.com/tdesposito/pyZohoAPI/commit/41734079837e9fa90abfddc32da490d06ae81ed3) by Todd Esposito).

### Fixed
- Fix typo ([809c25c](https://github.com/tdesposito/pyZohoAPI/commit/809c25cb2635fe3d581e6c7c7cdcf9d4451a7d55) by Todd Esposito).
- Fix number prop for after-delete() ([ddc5567](https://github.com/tdesposito/pyZohoAPI/commit/ddc5567982f07c235ebff3a253b04264bc4d96cd) by Todd Esposito).

### Removed
- Remove parameter position markers for 3.6-compatibility ([1a09f04](https://github.com/tdesposito/pyZohoAPI/commit/1a09f04ac6769f093615b70f1dd528be2c641669) by Todd Esposito).
- Remove obsoleted file ([934ead7](https://github.com/tdesposito/pyZohoAPI/commit/934ead766a55623c642c3da5a8827486e60e2b2d) by Todd Esposito).


## [v0.2.0](https://github.com/tdesposito/pyZohoAPI/releases/tag/v0.2.0) - 2021-02-25

<small>[Compare with first commit](https://github.com/tdesposito/pyZohoAPI/compare/4617c8f940003a6cc57dc94b8e42b1feab851d11...v0.2.0)</small>

### Added
- Add install-from-source section ([e2515fd](https://github.com/tdesposito/pyZohoAPI/commit/e2515fddaea03e63bb48150c61fe4631c6c2869c) by Todd Esposito).
- Add books to test shell ([c620d87](https://github.com/tdesposito/pyZohoAPI/commit/c620d87f5c9a6975835df793e341fdf259425c0a) by Todd Esposito).
- Add confirm(), void() to sos ([72752d2](https://github.com/tdesposito/pyZohoAPI/commit/72752d27970ad1184a02eff4d641754b4f346348) by Todd Esposito).
- Add docs for more better exceptions; more xrefs. ([440bd88](https://github.com/tdesposito/pyZohoAPI/commit/440bd8845448f63839e2bf04d748590b5b099d9c) by Todd Esposito).
- Add extra path params to test server ([07a5580](https://github.com/tdesposito/pyZohoAPI/commit/07a5580efe1d35cc43ad781739037dd405ac4c8a) by Todd Esposito).
- Add query params to test server ([c761f13](https://github.com/tdesposito/pyZohoAPI/commit/c761f13b82f099d120247e1856794741ad42896a) by Todd Esposito).
- Add start of interactive testing server ([be99df4](https://github.com/tdesposito/pyZohoAPI/commit/be99df4241b066443a0724b29e7408b7daf06246) by Todd Esposito).
- Add maprelatedlist, fix bug in iterrelatedlist ([6c73730](https://github.com/tdesposito/pyZohoAPI/commit/6c737306bedeec9c7f6a0879101e51d920dd560a) by Todd Esposito).
- Add issue templates ([460a5b3](https://github.com/tdesposito/pyZohoAPI/commit/460a5b35324e6ca2a13882c4e64c8399b1f741f1) by Todd D. Esposito).
- Add version to readme ([895e2ba](https://github.com/tdesposito/pyZohoAPI/commit/895e2bad171ac6e2defde006cae4cae59ecdf6e4) by Todd Esposito).
- Add rtd link and badge ([b407232](https://github.com/tdesposito/pyZohoAPI/commit/b4072322b3410ee191546255d984ffa99c782000) by Todd Esposito).
- Add docs and some mixins. ([0eaeb98](https://github.com/tdesposito/pyZohoAPI/commit/0eaeb981d0974d2710ba5868e8c11a1b335ab3a0) by Todd Esposito).

### Fixed
- Fix typo test-shell ([61ddc5d](https://github.com/tdesposito/pyZohoAPI/commit/61ddc5d45dad6918c848d018817ba32a6b329dbe) by Todd Esposito).
- Fix bug in first() with failed search ([199b4bf](https://github.com/tdesposito/pyZohoAPI/commit/199b4bfad81ad208347ee94e36b7997cf7a606c0) by Todd Esposito).
- Fix scroll on response text in test server ([50736cb](https://github.com/tdesposito/pyZohoAPI/commit/50736cb7b4e7c11f2650f82e29f1275530fe32a2) by Todd Esposito).
- Fix getrelated bug ([f232830](https://github.com/tdesposito/pyZohoAPI/commit/f232830bdae2812b60be1310c173dbd8215a15bf) by Todd Esposito).
- Fix response-not-json in do_request ([c52269e](https://github.com/tdesposito/pyZohoAPI/commit/c52269edd8f283a6eff502ec4d4d2c7acddd233a) by Todd Esposito).
- Fix first() error on non-loaded list ([cf6c296](https://github.com/tdesposito/pyZohoAPI/commit/cf6c2969082b163358764fd617cf78ffc01725c2) by Todd Esposito).
- Fix paging error ([b3407dc](https://github.com/tdesposito/pyZohoAPI/commit/b3407dcf07e148dbf603f84f23d326ce645a5fa2) by Todd Esposito).

### Removed
- Remove dotted - obsolete ([bfa2d5b](https://github.com/tdesposito/pyZohoAPI/commit/bfa2d5b7ef89c7da48d1f453017e2ee6825fe544) by Todd Esposito).


