# Minimal iOS Gyp Builder

It just happens that I want to get rid of Xcode `.pbxproj` file hell. Thus I try to use GYP as my development
workflow. This is the POC project.

# Usage

Install GYP

```
brew tap jonmorehouse/tap
brew install gyp
make gyp
```

Generating XCodeProj

```
gyp hello-ios.gyp --depth .
```

# LICENSING

Copyright (C) 2015 YKode

Everyone is permitted to copy and distribute verbatim or modified
copies of this license document, and changing it is allowed as long
as the name is changed.

DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

0. You just DO WHAT THE FUCK YOU WANT TO.
