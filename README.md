# Ursina For Mobile  
### The New Era of Ursina Gaming on Android

[![GitHub issues](https://img.shields.io/github/issues/ShivamKR12/UrsinaForMobile)](https://github.com/ShivamKR12/UrsinaForMobile/issues)
[![GitHub forks](https://img.shields.io/github/forks/ShivamKR12/UrsinaForMobile)](https://github.com/ShivamKR12/UrsinaForMobile/network)
[![GitHub stars](https://img.shields.io/github/stars/ShivamKR12/UrsinaForMobile)](https://github.com/ShivamKR12/UrsinaForMobile/stargazers)
[![License](https://img.shields.io/github/license/ShivamKR12/UrsinaForMobile)](LICENSE)

## Overview

Ever wanted to export your Ursina game to Android? Now you can!  
**Ursina For Mobile** brings the power of the Ursina engine to Android devices, letting you port your desktop game to mobile with ease.

> **Note:**  
> Currently, only Android is supported. iOS is not supported due to Panda3D limitations and testing constraints (i.e., lack of macOS/iOS hardware).

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running Your Game](#running-your-game)
- [Documentation](#documentation)
- [Community and Support](#community-and-support)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)
- [License](#license)

---

## Features

- **Android Support:** Export and run your Ursina games on Android devices.
- **Seamless Integration:** Follow detailed instructions and scripts for porting.
- **Modern Toolchain:** Uses Python 3.13, OpenJDK 21, and up-to-date dependencies.
- **Community Driven:** Join discussions and report issues to help evolve the project.

---

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:
- [Python 3.13](https://www.python.org/downloads/release/python-313/)
- [Ursina Engine](https://github.com/pokepetter/ursina)
- **Android SDK & Build Tools** (for packaging)
- [OpenJDK 21](https://jdk.java.net/21/)
- **ADB** (for device communication)

### Installation

1. **Clone the Repository:**  
   ```bash
   git clone https://github.com/ShivamKR12/UrsinaForMobile.git
   cd UrsinaForMobile
   ```

2. **Environment Setup:**  
   - No extensive setup is required on your main machine—special wheels and dependencies will be managed during the build process for Android.
   - Make sure you have Python 3.13 and OpenJDK 21 configured in your PATH.

---

### Running Your Game

Follow the detailed steps in our [documentation](https://github.com/ShivamKR12/UrsinaForMobile/tree/main/New-Docs) to:
- Configure your Android project.
- Package your Ursina game for Android.
- Troubleshoot common issues.

---

## Documentation

For full details on how to port your game for Android, please visit our [comprehensive documentation](https://github.com/ShivamKR12/UrsinaForMobile/tree/main/New-Docs). The docs include:
- Step-by-step setup instructions.
- Environment configuration.
- Build and deployment procedures.
- Troubleshooting and FAQs.

---

## Community and Support

If you encounter any issues or need help:
- **Issues:** Report bugs or feature requests by opening an [issue](https://github.com/ShivamKR12/UrsinaForMobile/issues).
- **Discussions:** Join our [discussions](https://github.com/ShivamKR12/UrsinaForMobile/discussions) for community support.
- **Discord:** For real-time help, join the [Ursina Engine Discord](https://discord.com/invite/ydXfhyb).

---

## Contributing

Contributions are welcome! Get involved by:
1. **Forking the repository.**
2. **Creating a new branch:**  
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Committing your changes** with clear, concise messages.
4. **Pushing your branch** and opening a pull request.

For more details, see our [Contributing Guide](https://github.com/ShivamKR12/UrsinaForMobile/blob/main/New-Docs/06_Contributing.md).

---

## Acknowledgments

Special thanks to:
- **pokepetter** – for creating the Ursina Engine.
- **Panda3D Developers** – for their continuous support and development of Panda3D.
- **The Community** – for testing and contributing to this project.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
