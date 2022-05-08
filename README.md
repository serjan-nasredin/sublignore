# Sublime Text pattern exclusion file

<div align="center">
    <figure>
        <img type="image/png"
            src="https://raw.githubusercontent.com/snxx-lppxx/sublignore/master/screenshots/dark-theme.png" alt="Dark Theme"/>
        <figcaption>Sublime Ignore highlight in dark theme</figcaption>
    </figure>
    <figure>
        <img type="image/png"
            src="https://raw.githubusercontent.com/snxx-lppxx/sublignore/master/screenshots/light-theme.png" alt="Light Theme"/>
        <figcaption>Sublime Ignore highlight in light theme</figcaption>
    </figure>
</div>

<details>
    <summary>Preferences.sublime-settings</summary>

```json
"folder_exclude_patterns": [
    ".svn",
    ".git",
    ".hg",
    "CVS",
    ".Trash",
    ".Trash-*"
]
```

```json
"file_exclude_patterns": [
    "*.pyc",
    "*.pyo",
    "*.exe",
    "*.dll",
    "*.obj",
    "*.o",
    "*.a",
    "*.lib",
    "*.so",
    "*.dylib",
    "*.ncb",
    "*.sdf",
    "*.suo",
    "*.pdb",
    "*.idb",
    ".DS_Store",
    ".directory",
    "desktop.ini",
    "*.class",
    "*.psd",
    "*.db",
    "*.sublime-workspace"
]
```

```json
"binary_file_patterns": [
    "*.jpg",
    "*.jpeg",
    "*.png",
    "*.gif",
    "*.ttf",
    "*.tga",
    "*.dds",
    "*.ico",
    "*.eot",
    "*.pdf",
    "*.swf",
    "*.jar",
    "*.zip"
]
```

```json
"index_exclude_gitignore": true
```

```json
"index_exclude_patterns": [
    "*.log"
]
```

```json
"ignored_packages": [
    "Vintage"
]
```

</details>
