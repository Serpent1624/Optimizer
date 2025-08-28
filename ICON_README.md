# Icon Instructions for Windows Optimizer

To add a custom icon to your executable:

## Option 1: Use Existing System Icon
The build scripts will automatically use `icon.ico` if it exists in the same directory.

## Option 2: Create Your Own Icon
1. Use an online icon converter: https://favicon.io/favicon-converter/
2. Or use tools like:
   - GIMP (free)
   - Photoshop
   - Online converters

## Option 3: Use System Icons
Extract icons from Windows system files:
```batch
# Extract from shell32.dll (folder icon)
rundll32.exe shell32.dll,Control_RunDLL

# Or use PowerShell to extract icons
```

## Recommended Icon Specifications
- Format: ICO (icon file)
- Size: 256x256 pixels (recommended)
- Include multiple sizes: 16x16, 32x32, 48x48, 256x256
- Background: Transparent or solid color

## Adding Icon to Build
Once you have `icon.ico` in the project folder, the build scripts will automatically include it.

## Default Behavior
If no icon.ico is found, the executable will use the default Python icon.
