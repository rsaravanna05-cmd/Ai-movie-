# 🚀 Release Guide - AI Movie Studio

## Creating a Release

Follow these steps to create and release a new version of AI Movie Studio with APK builds.

### Step 1: Update Version

Update version numbers in these files:

```bash
# config.py
APP_VERSION = "1.1.0"

# buildozer.spec
version = 1.1.0

# .github/workflows/release-apk.yml
# AI Movie Studio v1.1.0
```

### Step 2: Commit Changes

```bash
git add .
git commit -m "Release v1.1.0: Add new features"
```

### Step 3: Create Git Tag

```bash
# Create annotated tag
git tag -a v1.1.0 -m "Version 1.1.0 Release"

# Push tag to GitHub
git push origin v1.1.0
```

### Step 4: GitHub Actions Builds APK

Once you push the tag:

1. Go to your repository
2. Click on "Actions" tab
3. Watch the "Build and Release APK" workflow
4. Wait for the build to complete (~30-45 minutes)

### Step 5: Download APK

After the workflow completes:

1. Click on "Releases" in your GitHub repository
2. Find the release with your tag version
3. Download the APK files:
   - `aimovie-1.1.0.apk` (Release build)
   - `aimovie-1.1.0-debug.apk` (Debug build)

---

## Release Checklist

- [ ] Update version numbers
- [ ] Update CHANGELOG.md
- [ ] Test the application locally
- [ ] Commit changes
- [ ] Create git tag (format: v1.x.x)
- [ ] Push tag to GitHub
- [ ] Wait for GitHub Actions workflow
- [ ] Verify APK files in Releases
- [ ] Test APK on Android device
- [ ] Announce release

---

## Downloading APK on Android

### Method 1: Direct Download

1. Open GitHub Releases page on your Android device
2. Click APK file to download
3. Open file manager and install

### Method 2: QR Code

Generate QR code for release URL:

```
https://github.com/rsaravanna05-cmd/Ai-movie-/releases/download/v1.1.0/aimovie-1.1.0.apk
```

### Method 3: ADB

```bash
# Download APK
wget https://github.com/rsaravanna05-cmd/Ai-movie-/releases/download/v1.1.0/aimovie-1.1.0.apk

# Install via ADB
adb install aimovie-1.1.0.apk
```

---

## Troubleshooting Build Issues

### Build Timeout

- GitHub Actions has 6-hour limit
- APK builds typically take 30-45 minutes
- If timeout, reduce app size or optimize dependencies

### Build Failure

Check workflow logs:
1. Go to Actions tab
2. Click on failed workflow
3. Scroll down to see error messages
4. Common issues:
   - Missing Java/Android SDK
   - Invalid buildozer.spec
   - Missing dependencies

### APK Installation Issues

```bash
# Clear app cache
adb shell pm clear org.aimovie

# Uninstall and reinstall
adb uninstall org.aimovie
adb install aimovie-1.1.0.apk
```

---

## Distribution Channels

### GitHub Releases

✅ Best for: Development versions, bleeding edge builds
```
https://github.com/rsaravanna05-cmd/Ai-movie-/releases
```

### Google Play Store

📱 Best for: Stable releases, wider audience
1. Create Google Play Developer account
2. Upload signed APK
3. Fill app store listing
4. Submit for review

### F-Droid

🔐 Best for: Open source, privacy-focused users
1. Submit repository
2. Maintain reproducible builds
3. Community reviews

---

## Version Numbering

Follow Semantic Versioning (MAJOR.MINOR.PATCH):

- **v1.0.0** - First stable release
- **v1.1.0** - Minor feature addition
- **v1.1.1** - Bug fix
- **v2.0.0** - Major changes

---

## Release Notes Template

```markdown
# AI Movie Studio v1.1.0

## 🎉 New Features
- Feature 1
- Feature 2

## 🐛 Bug Fixes
- Fixed issue #123
- Fixed issue #124

## 📈 Improvements
- Performance improvement
- Better Tamil font support

## 📱 Download
- [aimovie-1.1.0.apk](https://github.com/rsaravanna05-cmd/Ai-movie-/releases/download/v1.1.0/aimovie-1.1.0.apk)
- [aimovie-1.1.0-debug.apk](https://github.com/rsaravanna05-cmd/Ai-movie-/releases/download/v1.1.0/aimovie-1.1.0-debug.apk)

## 🙏 Thanks
Thanks to all contributors!
```

---

## GitHub Releases API

### Create Release Programmatically

```bash
curl -X POST https://api.github.com/repos/rsaravanna05-cmd/Ai-movie-/releases \
  -H "Authorization: token YOUR_GITHUB_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "tag_name": "v1.1.0",
    "name": "AI Movie Studio v1.1.0",
    "body": "Release notes here",
    "draft": false,
    "prerelease": false
  }'
```

### Upload Asset to Release

```bash
curl -X POST https://uploads.github.com/repos/rsaravanna05-cmd/Ai-movie-/releases/{release_id}/assets \
  -H "Authorization: token YOUR_GITHUB_TOKEN" \
  -H "Content-Type: application/octet-stream" \
  --data-binary @aimovie-1.1.0.apk
```

---

## Quick Release Commands

```bash
#!/bin/bash

# Complete release workflow
VERSION="1.1.0"

# 1. Update files
sed -i "s/APP_VERSION = .*/APP_VERSION = \"$VERSION\"/" config.py
sed -i "s/version = .*/version = $VERSION/" buildozer.spec

# 2. Commit
git add .
git commit -m "Release v$VERSION"

# 3. Create tag and push
git tag -a v$VERSION -m "Version $VERSION"
git push origin main
git push origin v$VERSION

echo "✅ Release v$VERSION initiated! Check GitHub Actions for build progress."
```

---

## Support

- 📧 Email: support@aimovie.com
- 🐛 Report bugs: https://github.com/rsaravanna05-cmd/Ai-movie-/issues
- 💬 Discussions: https://github.com/rsaravanna05-cmd/Ai-movie-/discussions

---

## Changelog Format

Create `CHANGELOG.md` in your repository:

```markdown
# Changelog

All notable changes to this project will be documented in this file.

## [1.1.0] - 2026-08-28

### Added
- New feature A
- New feature B

### Changed
- Improved performance

### Fixed
- Bug fix 1
- Bug fix 2

## [1.0.0] - 2026-08-15

### Added
- Initial release
```

---

**Happy Releasing! 🚀**
