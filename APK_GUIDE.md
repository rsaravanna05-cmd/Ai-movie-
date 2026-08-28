# 📱 AI Movie Studio - APK Download & Installation Guide

## Building APK for Android

This guide helps you create an Android APK for the AI Movie Studio app using Python and Kivy framework.

### Prerequisites

- Python 3.8+
- Java Development Kit (JDK) 8 or higher
- Android SDK
- Buildozer (for building APK)

### Installation Steps

#### 1. Install Required Tools

```bash
# Install Buildozer
pip install buildozer

# Install Cython
pip install Cython==0.29.32

# Install dependencies
pip install -r requirements.txt
pip install kivy pillow
```

#### 2. Create buildozer.spec

```bash
buildozer android create
```

This creates a `buildozer.spec` file. Edit it:

```ini
[app]
title = AI Movie Studio
package.name = aimovie
package.domain = org.aimovie
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0
requirements = python3,kivy,opencv,numpy,requests
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,CAMERA
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
```

#### 3. Build APK

```bash
# Debug APK (for testing)
buildozer android debug

# Release APK (for production)
buildozer android release
```

The APK will be generated in: `bin/aimovie-1.0.0-debug.apk`

### Download Links

#### Pre-built APK Releases

Visit the [GitHub Releases](https://github.com/rsaravanna05-cmd/Ai-movie-/releases) page to download pre-built APKs:

- **Latest Release**: [Download v1.0.0](https://github.com/rsaravanna05-cmd/Ai-movie-/releases/download/v1.0.0/aimovie-1.0.0.apk)
- **Debug Build**: [Download Debug APK](https://github.com/rsaravanna05-cmd/Ai-movie-/releases/download/v1.0.0/aimovie-1.0.0-debug.apk)

### Installation on Android Device

#### Method 1: USB Transfer

```bash
# Connect Android device via USB
adb devices  # Verify connection

# Transfer APK
adb push bin/aimovie-1.0.0-debug.apk /sdcard/Download/

# Install
adb install /sdcard/Download/aimovie-1.0.0-debug.apk
```

#### Method 2: Direct Installation

1. Download APK file on your Android device
2. Open File Manager
3. Navigate to Downloads folder
4. Tap the APK file
5. Grant necessary permissions
6. Tap "Install"

#### Method 3: Scan QR Code

Scan the QR code below to download directly:

```
[QR Code will be generated]
```

### Features in APK

✅ Upload video/audio files  
✅ Write Tamil scripts  
✅ Generate movies  
✅ Download generated videos  
✅ Real-time status tracking  
✅ Offline script writing  
✅ Media gallery integration  

### System Requirements

- **Android Version**: 5.0 (API 21) or higher
- **Storage**: Minimum 500MB free space
- **RAM**: Minimum 2GB
- **Internet**: Required for movie generation

### Troubleshooting

#### APK Installation Issues

**Error: "App not installed"**
```bash
# Clear cache and retry
adb shell pm clear org.aimovie
adb install bin/aimovie-1.0.0-debug.apk
```

**Error: "Insufficient storage"**
- Free up at least 500MB on your device
- Move files to SD card if available

#### Build Issues

**"buildozer: command not found"**
```bash
pip install --upgrade buildozer
```

**"Java not found"**
```bash
# Set JAVA_HOME
export JAVA_HOME=/path/to/jdk
export PATH=$JAVA_HOME/bin:$PATH
```

### API Configuration for APK

Create `android_config.json`:

```json
{
  "api_url": "https://your-server.com:5000",
  "api_timeout": 600,
  "max_file_size": 500000000,
  "language": "tamil"
}
```

Place it in: `AI Movie Studio > Settings > Server Configuration`

### Building Custom APK

#### Step 1: Modify app.py for mobile

```python
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from upload_script import UploadManager

class AIMovieApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        btn = Button(text='Upload Script')
        btn.bind(on_press=self.upload_video)
        layout.add_widget(btn)
        return layout
    
    def upload_video(self, instance):
        manager = UploadManager()
        # Upload logic here
        pass

if __name__ == '__main__':
    AIMovieApp().run()
```

#### Step 2: Update buildozer.spec

```bash
buildozer android debug
```

#### Step 3: Sign Release APK

```bash
# Create keystore
keytool -genkey -v -keystore aimovie.keystore \
  -keyalg RSA -keysize 2048 -validity 10000 \
  -alias aimovie_key

# Sign APK
jarsigner -verbose -sigalg SHA256withRSA \
  -digestalg SHA-256 -keystore aimovie.keystore \
  bin/aimovie-1.0.0-release.apk aimovie_key

# Verify
jarsigner -verify -verbose -certs \
  bin/aimovie-1.0.0-release.apk
```

### Distribution

#### Google Play Store

1. Create Google Play Developer account
2. Sign APK with release keystore
3. Upload APK to Play Console
4. Fill app details and store listing
5. Submit for review

#### Direct Download

Host APK on GitHub Releases or your server:

```html
<!-- Example HTML -->
<a href="https://github.com/rsaravanna05-cmd/Ai-movie-/releases/download/v1.0.0/aimovie-1.0.0.apk">
  📱 Download AI Movie Studio APK
</a>
```

### Performance Tips

- Limit video resolution to 720p for mobile
- Use H.264 codec for better compatibility
- Compress audio to 128kbps
- Clear app cache regularly

### Support

For issues or questions:
- 📧 Email: support@aimovie.com
- 🐛 GitHub Issues: [Open Issue](https://github.com/rsaravanna05-cmd/Ai-movie-/issues)
- 💬 Discussions: [Join Discord](https://discord.gg/aimovie)

---

**Happy Movie Making on Mobile! 🎬📱**
