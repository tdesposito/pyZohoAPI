# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [v0.10.0](https://github.com/tdesposito/pyZohoAPI/releases/tag/v0.10.0) - 2022-01-17

<small>[Compare with v0.9.1](https://github.com/tdesposito/pyZohoAPI/compare/v0.9.1...v0.10.0)</small>

### Added
- Added automatic decimal.decimal usage in zohoobjects ([d786e40](https://github.com/tdesposito/pyZohoAPI/commit/d786e4005ea888295989d58d73d4198d9e689997) by Todd Esposito).
- Add decimal.decimal note to docs ([45694f7](https://github.com/tdesposito/pyZohoAPI/commit/45694f7eac56bff2cb739b2336c5aeac1faf6bf4) by Todd Esposito).

### Fixed
- Fix typo ([93645ee](https://github.com/tdesposito/pyZohoAPI/commit/93645ee805fe5eedf1a1a8cb9ced0d3939fc4ccc) by Todd Esposito).
- Fixed parameter name in __init__.py ([99c02c9](https://github.com/tdesposito/pyZohoAPI/commit/99c02c93a4576815800436cf67eef0b89cc1697c) by Shubham Agawane).


## [v0.9.1](https://github.com/tdesposito/pyZohoAPI/releases/tag/v0.9.1) - 2021-09-30

<small>[Compare with v0.9.0](https://github.com/tdesposito/pyZohoAPI/compare/v0.9.0...v0.9.1)</small>

### Changed
- Changelog ([776354a](https://github.com/tdesposito/pyZohoAPI/commit/776354a49e330ef8cefbd610c69ab211408ffeb6) by Todd Esposito).

### Fixed
- Fix shipmentorder key ([a52891f](https://github.com/tdesposito/pyZohoAPI/commit/a52891f2866a03f53e67b9056a9f2ee0310a9a63) by Todd Esposito).
- Fix classifiers to include 3.9 ([e8449d7](https://github.com/tdesposito/pyZohoAPI/commit/e8449d760780346f8d352a7ff4949643a7848bab) by Todd Esposito).


## [v0.9.0](https://github.com/tdesposito/pyZohoAPI/releases/tag/v0.9.0) - 2021-09-30

<small>[Compare with v0.7.1](https://github.com/tdesposito/pyZohoAPI/compare/v0.7.1...v0.9.0)</small>

### Added
- Add logging to core ([3a0cb29](https://github.com/tdesposito/pyZohoAPI/commit/3a0cb2938e557c98fd3e33931b8df645fcb9359e) by Todd Esposito).
- Add hasdeliver(), apply to shipmentorder ([4686e24](https://github.com/tdesposito/pyZohoAPI/commit/4686e245651d74991bc306812cd4eea5e8462ed7) by Todd Esposito).
- Add custom fields to contacts ([d0f47ed](https://github.com/tdesposito/pyZohoAPI/commit/d0f47ed1daae94f9eb5149a71b47180089a92131) by Todd Esposito).
- Add brand type ([1d085a4](https://github.com/tdesposito/pyZohoAPI/commit/1d085a45ef274faca6a08d82e770f662ed54ae3b) by Todd Esposito).

### Fixed
- Fix: allow first() to filter ([e69451a](https://github.com/tdesposito/pyZohoAPI/commit/e69451aa7636a66b25649d093b086c50b10a775b) by Todd Esposito).


## [v0.7.1](https://github.com/tdesposito/pyZohoAPI/releases/tag/v0.7.1) - 2021-06-08

<small>[Compare with v0.7.0](https://github.com/tdesposito/pyZohoAPI/compare/v0.7.0...v0.7.1)</small>

### Fixed
- Fix: missed removal of _req_fields reference after refactor ([f80e2c0](https://github.com/tdesposito/pyZohoAPI/commit/f80e2c0540f920aebb47c96eb86c26c76ddd0cea) by Todd Esposito).


## [v0.7.0](https://github.com/tdesposito/pyZohoAPI/releases/tag/v0.7.0) - 2021-05-30

<small>[Compare with v0.6.0](https://github.com/tdesposito/pyZohoAPI/compare/v0.6.0...v0.7.0)</small>

### Added
- Add: warehouse type ([18c3530](https://github.com/tdesposito/pyZohoAPI/commit/18c3530e6d48fcdc11b761fb22506c51e59f449a) by Todd Esposito).
- Add: tax (and related) types ([4705a96](https://github.com/tdesposito/pyZohoAPI/commit/4705a96996494c9ebb64d10d458b32150b38e6ef) by Todd Esposito).
- Add: salesreturn type -- untested/incomplete ([d69da72](https://github.com/tdesposito/pyZohoAPI/commit/d69da722f8093583a0374cbd955d439c5df9bf0a) by Todd Esposito).
- Add: retainerinvoice type -- untested/incomplete ([a98f3d7](https://github.com/tdesposito/pyZohoAPI/commit/a98f3d76fb5bee189e95be5fdc809d47f2a401f3) by Todd Esposito).
- Add: purchasereceive type ([fbb6038](https://github.com/tdesposito/pyZohoAPI/commit/fbb603832c0f5783a547c90da3e91d6b8823530e) by Todd Esposito).
- Add: pricelist type ([4aa6cf1](https://github.com/tdesposito/pyZohoAPI/commit/4aa6cf1269f10e4e5e41a12086c40d988df42a24) by Todd Esposito).
- Add: currency type ([23c2a05](https://github.com/tdesposito/pyZohoAPI/commit/23c2a0581699412c29c2fd476024e581bc0c9980) by Todd Esposito).
- Add: transferorder type ([d38199e](https://github.com/tdesposito/pyZohoAPI/commit/d38199e51c5ae135f9d209f18928a4fe815bd53a) by Todd Esposito).
- Add: itemadjustment type ([2851bb0](https://github.com/tdesposito/pyZohoAPI/commit/2851bb0968424086dae57f63411f6cabfe244441) by Todd Esposito).

### Fixed
- Fix: allow non-computed plural response keys ([ba11b8c](https://github.com/tdesposito/pyZohoAPI/commit/ba11b8cc67c208085077015d6db84d076820e616) by Todd Esposito).
- Fix: include request url in response panel in the test-server ([9db661a](https://github.com/tdesposito/pyZohoAPI/commit/9db661a124eee85ee68f4786f239c03ab6f2fd81) by Todd Esposito).
- Fix: clarify and make object factory params more flexible ([f3d3093](https://github.com/tdesposito/pyZohoAPI/commit/f3d3093237f3143768af7785575e08c156eae908) by Todd Esposito).


## [v0.6.0](https://github.com/tdesposito/pyZohoAPI/releases/tag/v0.6.0) - 2021-05-26

<small>[Compare with v0.5.0](https://github.com/tdesposito/pyZohoAPI/compare/v0.5.0...v0.6.0)</small>

### Added
- Add makebundle() function for compositeitem object ([c8bbf95](https://github.com/tdesposito/pyZohoAPI/commit/c8bbf952259880771ca8c3f01f3c4408549d0203) by Todd Esposito).
- Add "salesperson" object ([9f397d2](https://github.com/tdesposito/pyZohoAPI/commit/9f397d297237bb92591840eb5c8023f170c50cc1) by Todd Esposito).

### Fixed
- Fix issue with test server url quoting "type" params ([265cef1](https://github.com/tdesposito/pyZohoAPI/commit/265cef1fe273713e42169af5759f9023d8a6ea88) by Todd Esposito).
- Fix published debug-code! yikes! ([18be5b8](https://github.com/tdesposito/pyZohoAPI/commit/18be5b8fd622c855d77e05582385dd3040e8435a) by Todd Esposito).
- Fix behavior on extending a list-of when paging ([65d564e](https://github.com/tdesposito/pyZohoAPI/commit/65d564eb75917b01038021dc627b59a717d50c71) by Todd Esposito).

### Removed
- Remove superfluous file ([e2694b9](https://github.com/tdesposito/pyZohoAPI/commit/e2694b959d14a51f6bbd8c68dafca652389db5f4) by Todd Esposito).


## [v0.5.0](https://github.com/tdesposito/pyZohoAPI/releases/tag/v0.5.0) - 2021-03-13

<small>[Compare with v0.4.1](https://github.com/tdesposito/pyZohoAPI/compare/v0.4.1...v0.5.0)</small>

### Added
- Add lots of documentation ([8c2afd6](https://github.com/tdesposito/pyZohoAPI/commit/8c2afd6e26230b97da9b38363bef6746a6249bea) by Todd Esposito).
- Add setcustomfield ([53de008](https://github.com/tdesposito/pyZohoAPI/commit/53de0085348e66efd047f59d1f91f44842aa16a4) by Todd Esposito).


## [v0.4.1](https://github.com/tdesposito/pyZohoAPI/releases/tag/v0.4.1) - 2021-03-03

<small>[Compare with v0.4.0](https://github.com/tdesposito/pyZohoAPI/compare/v0.4.0...v0.4.1)</small>

### Fixed
- Fix retry around an unexpectedly invalid access_token ([c70df33](https://github.com/tdesposito/pyZohoAPI/commit/c70df33607a1c491f456d0c9508a600e8a4bfc1d) by Todd Esposito).


## [v0.4.0](https://github.com/tdesposito/pyZohoAPI/releases/tag/v0.4.0) - 2021-03-01

<small>[Compare with v0.3.0](https://github.com/tdesposito/pyZohoAPI/compare/v0.3.0...v0.4.0)</small>

### Added
- Add intercall_delay ([0e2a5fa](https://github.com/tdesposito/pyZohoAPI/commit/0e2a5fa6618531add2f53daacc454c7ccce2b690) by Todd D. Esposito).

### Fixed
- Fix possible access token expiry problem ([ba6db9e](https://github.com/tdesposito/pyZohoAPI/commit/ba6db9e33758a30295ec3fc54bf830f2f89a0dcf) by Todd Esposito).


## [v0.3.0](https://github.com/tdesposito/pyZohoAPI/releases/tag/v0.3.0) - 2021-02-27

<small>[Compare with v0.2.6](https://github.com/tdesposito/pyZohoAPI/compare/v0.2.6...v0.3.0)</small>

### Added
- Add getimage() and deleteimage() ([62f0bbf](https://github.com/tdesposito/pyZohoAPI/commit/62f0bbf62e081b4b0e507d3676bb05e876bb2d4a) by Todd Esposito).

### Fixed
- Fix bumptrack config to include pyproject.toml ([610f6ec](https://github.com/tdesposito/pyZohoAPI/commit/610f6ece02b1b5ac283741eaad3b4af0f26e7d51) by Todd Esposito).
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


